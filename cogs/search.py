import discord
import random
import datetime
import urllib.parse
from discord.ext import commands
from config import *

BASE_URL_WIKIPEDIA_API = "https://en.wikipedia.org/w/api.php?{0}"

class Search():
	def __init__(self, bot):
		self.bot = bot

	@commands.guild_only()
	@commands.command(aliases=["wikipedia"])
	async def wiki(self, ctx, *, query: str):
		params = urllib.parse.urlencode({"action": "opensearch", "search": query})
		url = BASE_URL_WIKIPEDIA_API.format(params)
		async with ctx.bot.session.get(url) as response:
			if response.status == 200:
				data = await response.json()
				if not data[1]:
					await ctx.send("Hmm looks like there is nothing there!")
					return
				embed = discord.Embed(colour = embed_color)
				for index in range(0, min(2, len(data[1]))):
					description = f"{data[3][index]}\n{data[2][index]}"
					embed.add_field(name = data[1][index], value = description, inline = False)
				await ctx.send(embed = embed)
			else:
				message = "Couldn't reach Wikipedia. x.x"
				await ctx.send(message)

def setup(bot):
    bot.add_cog(Search(bot))
