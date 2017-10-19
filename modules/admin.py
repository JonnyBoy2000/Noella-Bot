########################################
############ Admin Commands ############
########################################

import discord
import asyncio
import random
import utils.checks
from discord.ext import commands
from extra.config import *

class Admin():
	def __init__(self, bot):
		self.bot = bot

########################################
############ Role  Commands ############
########################################

	@commands.guild_only()
	@commands.command(aliases = ['rr'])
	async def removerole(self, ctx, user : discord.Member, *, role):
			if ctx.author.guild_permissions.manage_roles:
				await user.remove_roles(discord.utils.get(ctx.message.guild.roles, name=role))
				embed = discord.Embed(title = "Remove Role!", description = "**" + ctx.author.name + "** succesfully removed a role from **{}**".format(user), color = embed_color_succes)
				embed.add_field(name="Removed Role: ", value = "{}".format(role))
				await ctx.send(embed = embed)
			else:
				raise commands.MissingPermissions(["Manage Roles"])

	@commands.guild_only()
	@commands.command(aliases = ['sr'])
	async def setrole(self, ctx, user : discord.Member, *, role):
			if ctx.author.guild_permissions.manage_roles:
				await user.add_roles(discord.utils.get(ctx.message.guild.roles, name=role))
				embed = discord.Embed(title = "Set Role!", description = "**" + ctx.author.name + "** succesfully set a role to **{}**".format(user), color = embed_color_succes)
				embed.add_field(name="Set Role: ", value = "{}".format(role))
				await ctx.send(embed = embed)
			else:
				raise commands.MissingPermissions(["Manage Roles"])

########################################
############ Mute  Commands ############
########################################

	@commands.guild_only()
	@commands.command(aliases = ['mute'])
	async def muteuser(self, ctx, *, user : discord.Member):
			if ctx.author.guild_permissions.administrator:
				overwrite = discord.PermissionOverwrite()
				overwrite.send_messages = False
				await ctx.channel.set_permissions(user, overwrite = overwrite)
				await ctx.send(f"Muted  {user.mention}")
			else:
				raise commands.MissingPermissions(["Administrator"])

	@commands.guild_only()
	@commands.command(aliases = ['unmute'])
	async def unmuteuser(self, ctx, *, user : discord.Member):
			if ctx.author.guild_permissions.administrator:
				overwrite = discord.PermissionOverwrite()
				overwrite.send_messages = True
				await ctx.channel.set_permissions(user, overwrite = overwrite)
				await ctx.send("Unmuted %s"%user.mention)
			else:
				raise commands.MissingPermissions(["Administrator"])

########################################

	@commands.guild_only()
	@commands.command()
	async def cleanup(self, ctx, limit: int = 250):
		prefixes = tuple(ctx.bot.command_prefix(ctx.bot, ctx.message))

		def check(m):
			return m.author == ctx.me or m.content.startswith(prefixes)

		deleted = await ctx.purge(limit=limit, check=check)
		await ctx.send(f'Cleaned up {len(deleted)} messages.')

	@commands.guild_only()
	@commands.command(aliases=['nick'])
	async def nickname(self, ctx, *, txt = None):
		if ctx.author.guild_permissions.change_nickname:
			await ctx.message.delete()
			await ctx.message.author.edit(nick = txt)
			await ctx.send(f"Changed nickname to: `{txt}`")
		else:
			raise commands.MissingPermissions(["ChangeNickname"])

def setup(bot):
    bot.add_cog(Admin(bot))
