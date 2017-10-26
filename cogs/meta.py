from discord.ext import commands
from .utils import checks, formats
from .utils.paginator import HelpPaginator, CannotPaginate
import discord
from collections import OrderedDict, deque, Counter
import os, datetime
import asyncio
import copy
import unicodedata
import inspect
from config import embed_color, embed_color_succes, embed_color_error

class Prefix(commands.Converter):
    async def convert(self, ctx, argument):
        user_id = ctx.bot.user.id
        if argument.startswith((f'<@{user_id}>', f'<@!{user_id}>')):
            raise commands.BadArgument('That is a reserved prefix already in use.')
        return argument

class Meta:
    """Commands for utilities related to Discord or the Bot itself."""

    def __init__(self, bot):
        self.bot = bot
        bot.remove_command('help')

    async def __error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(error)

    @commands.group(name='prefix', invoke_without_command=True)
    async def prefix(self, ctx):
        """Manages the server's custom prefixes.

        If called without a subcommand, this will list the currently set
        prefixes.
        """

        prefixes = self.bot.get_guild_prefixes(ctx.guild)

        # we want to remove prefix #2, because it's the 2nd form of the mention
        # and to the end user, this would end up making them confused why the
        # mention is there twice
        del prefixes[1]

        e = discord.Embed(title=f'Prefixes for {str(ctx.guild)}', colour=discord.Colour.blurple())
        e.set_footer(text=f'{len(prefixes)} prefixes')
        e.description = '\n'.join(f'{index}. {elem}' for index, elem in enumerate(prefixes, 1))
        await ctx.send(embed=e)

    @prefix.command(name='add', ignore_extra=False)
    @checks.is_mod()
    async def prefix_add(self, ctx, prefix: Prefix):
        """Appends a prefix to the list of custom prefixes.

        Previously set prefixes are not overridden.

        To have a word prefix, you should quote it and end it with
        a space, e.g. "hello " to set the prefix to "hello ". This
        is because Discord removes spaces when sending messages so
        the spaces are not preserved.

        Multi-word prefixes must be quoted also.

        You must have Manage Server permission to use this command.
        """

        current_prefixes = self.bot.get_raw_guild_prefixes(ctx.guild.id)
        current_prefixes.append(prefix)
        try:
            await self.bot.set_guild_prefixes(ctx.guild, current_prefixes)
        except Exception as e:
            embed = discord.Embed(title = f"**Prefix Not Added**", description = f"**{ctx.author.name}**, nothing went wrong!\n{e}", color = embed_color_error)
            return await ctx.send(embed = embed)
        else:
            embed = discord.Embed(title = f"**Prefix Added**", description = f"**{ctx.author.name}**, successfully added: `{prefix}` to the prefixes", color = embed_color_succes)
            await ctx.send(embed = embed)

    @prefix_add.error
    async def prefix_add_error(self, ctx, error):
        if isinstance(error, commands.TooManyArguments):
            embed = discord.Embed(title = f"**Prefix Not Added**", description = f"**{ctx.author.name}**, You've given too many prefixes. \nEither quote it or only do it one by one.", color = embed_color_error)
            await ctx.send(embed = embed)

    @prefix.command(name='remove', aliases=['delete'], ignore_extra=False)
    @checks.is_mod()
    async def prefix_remove(self, ctx, prefix: Prefix):
        """Removes a prefix from the list of custom prefixes.

        This is the inverse of the 'prefix add' command. You can
        use this to remove prefixes from the default set as well.

        You must have Manage Server permission to use this command.
        """

        current_prefixes = self.bot.get_raw_guild_prefixes(ctx.guild.id)

        try:
            current_prefixes.remove(prefix)
        except ValueError:
            embed = discord.Embed(title = f"**Prefix Not Removed**", description = f"**{ctx.author.name}**, I do not have this prefix registered.", color = embed_color_error)
            return await ctx.send(embed = embed)
        try:
            await self.bot.set_guild_prefixes(ctx.guild, current_prefixes)
        except Exception as e:
            embed = discord.Embed(title = f"**Prefix Not Removed**", description = f"**{ctx.author.name}**, nothing went wrong!\n{e}", color = embed_color_error)
            return await ctx.send(embed = embed)
        else:
            embed = discord.Embed(title = f"**Prefix Removed**", description = f"**{ctx.author.name}**, successfully removed: `{prefix}` from the prefixes", color = embed_color_succes)
            await ctx.send(embed = embed)

    @prefix.command(name='clear')
    @checks.is_mod()
    async def prefix_clear(self, ctx):
        """Removes all custom prefixes.

        After this, the bot will listen to only mention prefixes.

        You must have Manage Server permission to use this command.
        """

        await self.bot.set_guild_prefixes(ctx.guild, [])
        embed = discord.Embed(title = f"**Prefix Removed**", description = f"**{ctx.author.name}**, successfully removed all custom prefixes.\nDefault prefix is `@{self.bot.user.name}#{self.bot.user.discriminator}`", color = embed_color_succes)
        await ctx.send(embed = embed)

    @commands.command(name='shutdown', hidden=True)
    @commands.is_owner()
    async def _shutdown(self, ctx):
        """Quits the bot."""
        embed = discord.Embed(title = f"**Shutdown**", description = f"**{ctx.author.name}**, {self.bot.user.name} is successfully shutted down!", color = embed_color_succes)
        await ctx.send(embed = embed)
        await self.bot.logout()

    async def say_permissions(self, ctx, member, channel):
        permissions = channel.permissions_for(member)
        e = discord.Embed(colour=member.colour)
        allowed, denied = [], []
        for name, value in permissions:
            name = name.replace('_', ' ').replace('guild', 'server').title()
            if value:
                allowed.append(name)
            else:
                denied.append(name)

        e.add_field(name='Allowed', value='\n'.join(allowed))
        e.add_field(name='Denied', value='\n'.join(denied))
        await ctx.send(embed=e)

    @commands.command()
    @commands.guild_only()
    async def permissions(self, ctx, member: discord.Member = None, channel: discord.TextChannel = None):
        """Shows a member's permissions in a specific channel.

        If no channel is given then it uses the current one.

        You cannot use this in private messages. If no member is given then
        the info returned will be yours.
        """
        channel = channel or ctx.channel
        if member is None:
            member = ctx.author

        await self.say_permissions(ctx, member, channel)

    @commands.command()
    @commands.guild_only()
    @checks.admin_or_permissions(manage_roles=True)
    async def botpermissions(self, ctx, *, channel: discord.TextChannel = None):
        """Shows the bot's permissions in a specific channel.

        If no channel is given then it uses the current one.

        This is a good way of checking if the bot has the permissions needed
        to execute the commands it wants to execute.

        To execute this command you must have Manage Roles permission.
        You cannot use this in private messages.
        """
        channel = channel or ctx.channel
        member = ctx.guild.me
        await self.say_permissions(ctx, member, channel)

    @commands.command(rest_is_raw=True, hidden=True)
    @commands.is_owner()
    async def echo(self, ctx, *, content):
        await ctx.send(content)

def setup(bot):
    bot.add_cog(Meta(bot))
