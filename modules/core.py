#########################################
############# Core Commands #############
#########################################

from extra.config import *
from discord.ext import commands
from collections import Counter
from utils import checks, formats, db
from utils.paginator import HelpPaginator, CannotPaginate
from collections import OrderedDict, deque, Counter

#from .utils import checks, db

import utils.checks
import utils.db
import logging
import discord
import asyncio
import datetime
import traceback
import copy
import unicodedata
import inspect
import psutil
import os, datetime

log = logging.getLogger(__name__)

#########################################

class Core:
    def __init__(self, bot):
        self.bot = bot
        self.process = psutil.Process()

    @commands.command(rest_is_raw = True, hidden = True, aliases = ['say'])
    @commands.is_owner()
    async def echo(self, ctx, *, content):
        await ctx.send(content)
        await ctx.message.delete()

### Permissions Command ###
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
        message = await ctx.send(embed=e)
        await ctx.message.delete()
        await message.edit(delete_after = message_delete_time + 15)

    @commands.command(no_pm = True, hidden = True, aliases = ['perm'])
    @commands.guild_only()
    async def permissions(self, ctx, member: discord.Member = None, channel: discord.TextChannel = None):
        channel = channel or ctx.channel
        if member is None:
            member = ctx.author
        await self.say_permissions(ctx, member, channel)

### Invite Bot Link Command ###
    @commands.command(no_pm = True, hidden = True, aliases = ['inv'])
    async def invite(self, ctx):
        embed = discord.Embed(title = f"**Invite {self.bot.user.name} to your server!**", description = f"You want to invite **Noëlla** to your server?\nThen you can use this link to invite him!\n\n[Click here to invite **{self.bot.user.name}**](https://discordapp.com/oauth2/authorize?client_id=357852849029513216&scope=bot&permissions=527952983)\n[Click here to join **{self.bot.user.name}'s** Dev Discord]({dev_discord})", color = embed_color)
        embed.set_thumbnail(url = self.bot.user.avatar_url)
        message = await ctx.send(embed = embed)
        await ctx.message.delete()
        await message.edit(delete_after = message_delete_time)

### Character Information Checker ###
    @commands.command(no_pm = True, hidden = True, aliases = ['char'])
    async def charinfo(self, ctx, *, characters: str):
        if len(characters) > 25:
            return await ctx.send(f'Too many characters ({len(characters)}/25)')

        def to_string(c):
            digit = f'{ord(c):x}'
            name = unicodedata.name(c, 'Name not found.')
            return f'`\\U{digit:>08}`: {name} - {c} \N{EM DASH} <http://www.fileformat.info/info/unicode/char/{digit}>'

        await ctx.send('\n'.join(map(to_string, characters)))

def setup(bot):
    bot.add_cog(Core(bot))
