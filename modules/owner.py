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
				total_servers = len(self.bot.guilds)

				embed = discord.Embed(description = f"**{ctx.author.name}** my **Now Streaming** was succesfully changed! [Default Messages]", color = embed_color)
				message = await ctx.send(embed = embed)
				await message.edit(delete_after = message_delete_time)

				games = [f"Need Help? Use {bot_prefix}help", f"{total_members} users | {total_servers} guilds", f"Wanna invite {self.bot.user.name}? Use: {bot_prefix}invite", f"Give us feedback? Use: {bot_prefix}ctdev [message]"]
				current_number = 0
				while True:
					if current_number == len(games):
						current_number = 0
					await self.bot.change_presence(game=discord.Game(name = games[current_number], url = "https://twitch.tv/MikamiTenshii", type = 1), status = current_status)
					await asyncio.sleep(20)
					current_number += 1

			else:
				await self.bot.change_presence(game=discord.Game(name = game, url = "https://twitch.tv/MikamiTenshii", type = 1), status = current_status)
				embed = discord.Embed(description = f"**{ctx.author.name}** my **Now Streaming** was succesfully changed!", color = embed_color)
				message = await ctx.send(embed = embed)
				await ctx.message.delete()
				await message.edit(delete_after = message_delete_time)

		else:
			raise commands.NotOwner()


	@commands.guild_only()
	@commands.command()
	async def updateavatar(self, ctx):

		if ctx.message.author.id == bot_owner:
			avatar_rb = open(f"modules/data/images/new_avatar.png", "rb")
			try:
				await ctx.bot.user.edit(avatar = avatar_rb.read())
			except Exception as e:
				await ctx.send(e)
			else:
				await ctx.send('Avatar set.')
		else:
			raise commands.NotOwner()

def setup(bot):
    bot.add_cog(Owner(bot))
