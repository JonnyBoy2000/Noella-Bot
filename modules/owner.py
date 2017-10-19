########################################
############ Owner Commands ############
########################################

import discord
import os
import sys
from discord.ext import commands
from extra.config import *

class Owner:
	def __init__(self, bot):
		self.bot = bot

	@commands.guild_only()
	@commands.command(name = 'shutdown', aliases = ['sd'])
	async def shutdown(self, ctx):
		send_log = self.bot.get_channel(log_channel)
		time_log = dt.utcnow().__format__('%H:%M:%S')
		if ctx.author.id == bot_owner:
			embed = discord.Embed(description = "**"+ ctx.author.name +"** byebye!", color = embed_color_succes)
			await ctx.send(embed = embed)
			await send_log.send(f"[{time_log}] - **{self.bot.user.name}** has been shut down by **{ctx.author.name}**")
			await self.bot.logout()
		else:
			raise commands.NotOwner()

	@commands.guild_only()
	@commands.command(name = 'restart', aliases = ['rs'])
	async def restart(self, ctx):
		send_log = self.bot.get_channel(log_channel)
		time_log = dt.utcnow().__format__('%H:%M:%S')
		if ctx.author.id == bot_owner:
			embed = discord.Embed(description = "**"+ ctx.author.name +"**, see you soon!", color = embed_color_succes)
			await ctx.send(embed = embed)
			await send_log.send(f"[{time_log}] - **{self.bot.user.name}** has been restarted by **{ctx.author.name}**")
			os.execve(sys.executable, ['python'] + sys.argv, os.environ)
		else:
			raise commands.NotOwner()


### Load Module Command ###
	@commands.guild_only()
	@commands.command(name = 'modload', aliases = ['ml'])
	async def modload(self, ctx, *, extension_name : str = None):
		send_log = self.bot.get_channel(log_channel)
		time_log = dt.utcnow().__format__('%H:%M:%S')
		if ctx.author.id == bot_owner and extension_name is not None:
			try:
				self.bot.load_extension(extension_name)
				embed = discord.Embed(description = "**"+ ctx.author.name +" **the module** {} **was successfully loaded.".format(extension_name), color = embed_color_succes)
				message = await ctx.send(embed = embed)
				await send_log.send(f"[{time_log}] - **{ctx.author.name}** successfully loaded the module **{extension_name}**")
				await ctx.message.delete()
				await message.edit(delete_after = message_delete_time)
			except (AttributeError, ImportError) as e:
				embed = discord.Embed(description = "**"+ ctx.author.name +" {}:** *{}*".format(type(e).__name__, str(e)), color = embed_color_error)
				message = await ctx.send(embed = embed)
				await ctx.message.delete()
				await message.edit(delete_after = message_delete_time)

		elif extension_name == None:
			embed = discord.Embed(description = "**"+ ctx.author.name +"** you need to tell me what to load!", color = embed_color_attention)
			message = await ctx.send(embed = embed)
			await ctx.message.delete()
			await message.edit(delete_after = message_delete_time)

		elif ctx.author.id is not bot_owner:
			raise commands.NotOwner()
		else:
			pass

### Unload Module Command ###
	@commands.guild_only()
	@commands.command(name = 'modunload', aliases = ['mu'])
	async def modunload(self, ctx, *, extension_name : str = None):
		send_log = self.bot.get_channel(log_channel)
		time_log = dt.utcnow().__format__('%H:%M:%S')
		if ctx.author.id == bot_owner and extension_name is not None:
			try:
				self.bot.unload_extension(extension_name)
				embed = discord.Embed(description = "**"+ ctx.author.name +" **the module** {} **was successfully unloaded.".format(extension_name), color = embed_color_succes)
				message = await ctx.send(embed = embed)
				await send_log.send(f"[{time_log}] - **{ctx.author.name}** successfully unloaded the module **{extension_name}**")
				await ctx.message.delete()
				await message.edit(delete_after = message_delete_time)
			except (AttributeError, ImportError) as e:
				embed = discord.Embed(description = "**"+ ctx.author.name +" {}:** *{}*".format(type(e).__name__, str(e)), color = embed_color_error)
				message = await ctx.send(embed = embed)
				await ctx.message.delete()
				await message.edit(delete_after = message_delete_time)

		elif extension_name == None:
			embed = discord.Embed(description = "**"+ ctx.author.name +"** you need to tell me what to unload!", color = embed_color_attention)
			message = await ctx.send(embed = embed)
			await ctx.message.delete()
			await message.edit(delete_after = message_delete_time)

		elif ctx.author.id is not bot_owner:
			raise commands.NotOwner()
		else:
			pass

### Reload Module Command ###
	@commands.guild_only()
	@commands.command(name = 'modreload', aliases = ['mr'])
	async def modreload(self, ctx, *, extension_name : str = None):
		send_log = self.bot.get_channel(log_channel)
		time_log = dt.utcnow().__format__('%H:%M:%S')
		if ctx.author.id == bot_owner and extension_name is not None:
			try:
				self.bot.unload_extension(extension_name)
				self.bot.load_extension(extension_name)
				embed = discord.Embed(description = "**"+ ctx.author.name +" **the module** {} **was successfully reloaded.".format(extension_name), color = embed_color_succes)
				message = await ctx.send(embed = embed)
				await send_log.send(f"[{time_log}] - **{ctx.author.name}** successfully reloaded the module **{extension_name}**")
				await ctx.message.delete()
				await message.edit(delete_after = message_delete_time)
			except (AttributeError, ImportError) as e:
				embed = discord.Embed(description = "**"+ ctx.author.name +" {}:** *{}*".format(type(e).__name__, str(e)), color = embed_color_error)
				message = await ctx.send(embed = embed)
				await ctx.message.delete()
				await message.edit(delete_after = message_delete_time)

		elif extension_name == None:
			embed = discord.Embed(description = "**"+ ctx.author.name +"** you need to tell me what to reload!", color = embed_color_attention)
			message = await ctx.send(embed = embed)
			await ctx.message.delete()
			await message.edit(delete_after = message_delete_time)

		elif ctx.author.id is not bot_owner:
			raise commands.NotOwner()
		else:
			pass

#########################################

	@commands.guild_only()
	@commands.command(name = 'setgame', pass_context=True, aliases = ['sg'])
	async def setgame(self, ctx, *, game = None):

		server = ctx.guild
		current_status = ctx.me.status if server is not None else None

		if ctx.message.author.id == bot_owner:
			await self.bot.change_presence(game=discord.Game(name=game),status=current_status)
			embed = discord.Embed(description = "**"+ctx.author.name +"** my **Now Playing** was succesfully changed!", color = embed_color)
			message = await ctx.send(embed = embed)
			await ctx.message.delete()
			await message.edit(delete_after = message_delete_time)

		else:
			raise commands.NotOwner()

	@commands.guild_only()
	@commands.command(name = 'setstream', aliases = ['ss'])
	async def setstream(self, ctx, *, game = None):

		server = ctx.guild
		current_status = ctx.me.status if server is not None else None

		if ctx.message.author.id == bot_owner:
			if game == "default":
				total_members = sum(1 for _ in self.bot.get_all_members())
				await self.bot.change_presence(game=discord.Game(name = f"{bot_prefix}help | {total_members} users!", url = "https://twitch.tv/MikamiTenshii", type = 1), status = current_status)
				embed = discord.Embed(description = f"**{ctx.author.name}** my **Now Streaming** was succesfully changed! to **{bot_prefix}help | {total_members} users!** ", color = embed_color)
				message = await ctx.send(embed = embed)
				await ctx.message.delete()
				await message.edit(delete_after = message_delete_time)

			else:
				await self.bot.change_presence(game=discord.Game(name = game, url = "https://twitch.tv/MikamiTenshii", type = 1), status = current_status)
				embed = discord.Embed(description = f"**{ctx.author.name}** my **Now Streaming** was succesfully changed!", color = embed_color)
				message = await ctx.send(embed = embed)
				await ctx.message.delete()
				await message.edit(delete_after = message_delete_time)

		else:
			raise commands.NotOwner()

def setup(bot):
    bot.add_cog(Owner(bot))
