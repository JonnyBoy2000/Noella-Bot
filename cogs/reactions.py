###################################
############ Reactions ############
###################################

import discord
import random
from cogs.data.reactionsdata import *
from discord.ext import commands

class Reactions():
	def __init__(self, bot):
		self.bot = bot

	@commands.cooldown(1, 30, commands.BucketType.user)
	async def on_message(self, message):
		if "❤" in message.content or "♥" in message.content:
			choice = random.choice(hearts)
			try:
				await message.channel.send(choice)
			except discord.Forbidden:
				pass


def setup(bot):
    bot.add_cog(Reactions(bot))
