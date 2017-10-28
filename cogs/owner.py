########################################
############ Owner Commands ############
########################################

import discord
import os
import sys
from discord.ext import commands
from config import *

class Owner:
	def __init__(self, bot):
		self.bot = bot


	@commands.guild_only()
	@commands.command(name = 'setgame', pass_context=True, aliases = ['sg'])
	async def setgame(self, ctx, *, game = None):

		server = ctx.guild
		current_status = ctx.me.status if server is not None else None

		if ctx.message.author.id == self.bot.owner_id:
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

		bot_prefix = ">"
		server = ctx.guild
		current_status = ctx.me.status if server is not None else None

		if ctx.message.author.id == self.bot.owner_id:
			if game == "default":

				embed = discord.Embed(description = f"**{ctx.author.name}** my **Now Streaming** was succesfully changed! [Default Messages]", color = embed_color)
				message = await ctx.send(embed = embed)
				await message.edit(delete_after = message_delete_time)

				games = [f"Need Help? Use {bot_prefix}help", f"{sum(1 for _ in self.bot.get_all_members())} users | {len(self.bot.guilds)} guilds", f"Wanna invite {self.bot.user.name}? Use: {bot_prefix}invite", f"Give us feedback? Use: {bot_prefix}ctdev [message]", f"{self.bot.user.name} has a website: goo.gl/2FCCPw"]
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

		if ctx.message.author.id == self.bot.owner_id:
			avatar_rb = open(f"cogs/data/images/new_avatar.png", "rb")
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
