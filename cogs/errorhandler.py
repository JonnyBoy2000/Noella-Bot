###########################################
############## Error Handler ##############
###########################################

import discord
from config import embed_color, embed_color_succes, embed_color_error
from discord.ext import commands

class ErrorHandler:
	def __init__(self, bot):
		self.bot = bot

	async def on_command_error(self, ctx, error):
			if isinstance (error, commands.CommandNotFound):
				pass

			elif isinstance (error, commands.MissingPermissions):
				embed = discord.Embed(color = embed_color_error)
				embed.add_field(name = "Oops, something went wrong!", value = f"**{ctx.author.name}**, you're sooo not allowed to do this!", inline = False)
				await ctx.send(embed = embed)

			elif isinstance(error, commands.NotOwner):
				embed = discord.Embed(description = "**"+ ctx.author.name +"**, you think you're my boss?", color =embed_color_error)
				await ctx.send(embed = embed)

			try:
				await ctx.message.delete()
			except:
				pass

				if isinstance (error, commands.BotMissingPermissions):
					pass

def setup(bot):
	bot.add_cog(ErrorHandler(bot))
