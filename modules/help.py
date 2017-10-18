######################################
############ Help Command ############
######################################

import discord
import random
from discord.ext import commands
from extra.config import *

class Help():
	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context = True, aliases=['h'])
	async def help(self, ctx, *, inputs : str = None):

		### Core Help Inputs ###
		if inputs == "help" or inputs == "h":
			embed = discord.Embed(title = "Help - Command", description = f"To request a personal message with information.\nTo request information about a specific command.", colour = embed_color)
			embed.add_field(name = "Basic Usage: ", value = f"`{bot_prefix}help` or `{bot_prefix}h`", inline = False)
			embed.add_field(name = "Other Usage: ", value = f"`{bot_prefix}help [command]` or `{bot_prefix}h [command]`", inline = False)
			embed.set_footer(text = "Do not use the example brackets when using the commands!")
			await ctx.send(embed = embed)

		elif inputs == "invite":
			embed = discord.Embed(title = "Invite - Command", description = f"Request for an invite to {self.bot.user.name} developers Discord\nAnd get an invite link to invite {self.bot.user.name} to your own Discord", colour = embed_color)
			embed.add_field(name = "Basic Usage: ", value = f"`{bot_prefix}invite`", inline = False)
			embed.set_footer(text = "Do not use the example brackets when using the commands!")
			await ctx.send(embed = embed)

		elif inputs == "ctdev":
			embed = discord.Embed(title = "Contact Developers - Command", description = f"Sent the developers of {self.bot.user.name} feedback or questions.", colour = embed_color)
			embed.add_field(name = "Basic Usage: ", value = f"`{bot_prefix}ctdev [message]`", inline = False)
			embed.set_footer(text = "Do not use the example brackets when using the commands!")
			await ctx.send(embed = embed)

		elif inputs == "prefix":
			embed = discord.Embed(title = "Prefix - Command", description = f"Request for the prefix of {self.bot.user.name} on your current server.", colour = embed_color)
			embed.add_field(name = "Basic Usage: ", value = f"`{bot_prefix}prefix` or `prefix`", inline = False)
			embed.set_footer(text = "Do not use the example brackets when using the commands!")
			await ctx.send(embed = embed)

		elif inputs == "si" or inputs == "serverinfo":
			embed = discord.Embed(title = "Server Information - Command", description = f"Request for information about the current server.", colour = embed_color)
			embed.add_field(name = "Basic Usage: ", value = f"`{bot_prefix}si` or `{bot_prefix}serverinfo`", inline = False)
			embed.set_footer(text = "Do not use the example brackets when using the commands!")
			await ctx.send(embed = embed)

		elif inputs == "ls" or inputs == "listservers":
			embed = discord.Embed(title = "List Servers - Command", description = f"Request for a list where {self.bot.user.name} is active in.", colour = embed_color)
			embed.add_field(name = "Basic Usage: ", value = f"`{bot_prefix}ls` or `{bot_prefix}listservers`", inline = False)
			embed.set_footer(text = "Do not use the example brackets when using the commands!")
			await ctx.send(embed = embed)

		elif inputs == "info" or inputs == "uinfo" or inputs == "userinfo" or inputs == "user":
			embed = discord.Embed(title = "User Information - Command", description = f"Request for information about yourself or someone else.", colour = embed_color)
			embed.add_field(name = "Basic Usage: ", value = f"`{bot_prefix}info`, `{bot_prefix}user`, `{bot_prefix}uinfo` or `{bot_prefix}userinfo`", inline = False)
			embed.add_field(name = "Other Usage: ", value = f"`{bot_prefix}info [person]`, `{bot_prefix}user [person]`, `{bot_prefix}uinfo [person]` or `{bot_prefix}userinfo [person]`", inline = False)
			embed.set_footer(text = "Do not use the example brackets when using the commands!")
			await ctx.send(embed = embed)

		elif inputs == "about":
			embed = discord.Embed(title = "Bot Information - Command", description = f"Request for information about {self.bot.user.name}.", colour = embed_color)
			embed.add_field(name = "Basic Usage: ", value = f"`{bot_prefix}about`", inline = False)
			embed.set_footer(text = "Do not use the example brackets when using the commands!")
			await ctx.send(embed = embed)

		elif inputs == "ping" or inputs == "latency":
			embed = discord.Embed(title = "Latency - Command", description = f"Request for latency of {self.bot.user.name} to the Discord server.", colour = embed_color)
			embed.add_field(name = "Basic Usage: ", value = f"`{bot_prefix}ping` or `{bot_prefix}latency`", inline = False)
			embed.set_footer(text = "Do not use the example brackets when using the commands!")
			await ctx.send(embed = embed)

		elif inputs == "permissions" or inputs == "perms":
			embed = discord.Embed(title = "Permissions - Command", description = f"Request for information about your or others permissions in a channel.", colour = embed_color)
			embed.add_field(name = "Basic Usage: ", value = f"`{bot_prefix}permissions` or `{bot_prefix}perms`", inline = False)
			embed.add_field(name = "Other Usage: ", value = f"`{bot_prefix}permissions [person]` or `{bot_prefix}perms [person]`", inline = False)
			embed.add_field(name = "Another Usage: ", value = f"`{bot_prefix}permissions [person] [channel]` or `{bot_prefix}perms [person] [channel]`", inline = False)
			embed.set_footer(text = "Do not use the example brackets when using the commands!")
			await ctx.send(embed = embed)

		### Fun Help Inputs ###
		elif inputs == "poll":
			embed = discord.Embed(title = "Poll - Command", description = f"Make a poll where people can vote on with reactions.", colour = embed_color)
			embed.add_field(name = "Basic Usage: ", value = f"`{bot_prefix}poll [\"question\"] [\"answer1\"] [\"answer2\"] [\"answer3\"]`", inline = False)
			embed.add_field(name = "Important: ", value = f"The question and answers **must** be within **double quotes**! (up to 20 answers)", inline = False)
			embed.set_footer(text = "Do not use the example brackets when using the commands!")
			await ctx.send(embed = embed)

		elif inputs == "eightball" or inputs == "8ball":
			embed = discord.Embed(title = "Eightball - Command", description = f"Ask the 8ball something.", colour = embed_color)
			embed.add_field(name = "Basic Usage: ", value = f"`{bot_prefix}eightball [question]` or `{bot_prefix}8ball [question]`", inline = False)
			embed.set_footer(text = "Do not use the example brackets when using the commands!")
			await ctx.send(embed = embed)

		elif inputs == "discordhub" or inputs == "hub":
			embed = discord.Embed(title = "DiscordHub - Command", description = f"Request for an URL of your or another DiscordHub profile.", colour = embed_color)
			embed.add_field(name = "Basic Usage: ", value = f"`{bot_prefix}discordhub` or `{bot_prefix}hub`", inline = False)
			embed.add_field(name = "Other Usage: ", value = f"`{bot_prefix}discordhub [person]` or `{bot_prefix}hub [person]`", inline = False)
			embed.set_footer(text = "Do not use the example brackets when using the commands!")
			await ctx.send(embed = embed)

		elif inputs == "osustats" or inputs == "osu":
			embed = discord.Embed(title = "Osu!Stats - Command", description = f"Show your osu! stats or that from someone else.", colour = embed_color)
			embed.add_field(name = "Basic Usage: ", value = f"`{bot_prefix}osustats` or `{bot_prefix}osu`", inline = False)
			embed.add_field(name = "Other Usage: ", value = f"`{bot_prefix}osustats [person]` or `{bot_prefix}osu [person]`", inline = False)
			embed.set_footer(text = "Do not use the example brackets when using the commands!")
			await ctx.send(embed = embed)

		elif inputs == "avatar" or inputs == "pfp":
			embed = discord.Embed(title = "Avatar - Command", description = f"Request for an URL of your avatar or that from someone else.", colour = embed_color)
			embed.add_field(name = "Basic Usage: ", value = f"`{bot_prefix}avatar` or `{bot_prefix}pfp`", inline = False)
			embed.add_field(name = "Other Usage: ", value = f"`{bot_prefix}avatar [person]` or `{bot_prefix}pfp [person]`", inline = False)
			embed.set_footer(text = "Do not use the example brackets when using the commands!")
			await ctx.send(embed = embed)

		elif inputs == "weather":
			embed = discord.Embed(title = "Weather - Command", description = f"Request for weather forcast on your location.", colour = embed_color)
			embed.add_field(name = "Basic Usage: ", value = f"`{bot_prefix}weather [location name]`", inline = False)
			embed.set_footer(text = "Do not use the example brackets when using the commands!")
			await ctx.send(embed = embed)

		elif inputs == "virus":
			embed = discord.Embed(title = "Virus - Command", description = f"Inject a fake virus into someone or the server.", colour = embed_color)
			embed.add_field(name = "Basic Usage: ", value = f"`{bot_prefix}virus`", inline = False)
			embed.add_field(name = "Other Usage: ", value = f"`{bot_prefix}virus [person]`", inline = False)
			embed.set_footer(text = "Do not use the example brackets when using the commands!")
			await ctx.send(embed = embed)

		### Music Help Inputs ###
		elif inputs == "join":
			embed = discord.Embed(title = "Join - Command", description = f"Make {self.bot.user.name} join a given voice-channel.", colour = embed_color)
			embed.add_field(name = "Basic Usage: ", value = f"`{bot_prefix}join [channel name]`", inline = False)
			embed.add_field(name = "Important: ", value = f"**This feature is still in development, do not expect much from it!**", inline = False)
			embed.set_footer(text = "Do not use the example brackets when using the commands!")
			await ctx.send(embed = embed)

		elif inputs == "play" or inputs == "yt" or inputs == "sc":
			embed = discord.Embed(title = "Play - Command", description = f"Make {self.bot.user.name} play music by a given URL from YouTube or SoundCloud.", colour = embed_color)
			embed.add_field(name = "Basic Usage: ", value = f"`{bot_prefix}play [url]`, `{bot_prefix}yt [url]` or `{bot_prefix}sc [url]`", inline = False)
			embed.add_field(name = "Important: ", value = f"**This feature is still in development, do not expect much from it!**", inline = False)
			embed.set_footer(text = "Do not use the example brackets when using the commands!")
			await ctx.send(embed = embed)

		elif inputs == "volume" or inputs == "vol":
			embed = discord.Embed(title = "Volume - Command", description = f"Change the volume of {self.bot.user.name} when playing music.", colour = embed_color)
			embed.add_field(name = "Basic Usage: ", value = f"`{bot_prefix}volume [amount (1 - 100)]`, `{bot_prefix}vol [amount (1 - 100)]`", inline = False)
			embed.add_field(name = "Important: ", value = f"**This feature is still in development, do not expect much from it!**", inline = False)
			embed.set_footer(text = "Do not use the example brackets when using the commands!")
			await ctx.send(embed = embed)

		elif inputs == "stop" or inputs == "quit":
			embed = discord.Embed(title = "Stop - Command", description = f"Stop current playing song and disconnects {self.bot.user.name} from the voice-channel.", colour = embed_color)
			embed.add_field(name = "Basic Usage: ", value = f"`{bot_prefix}stop`, `{bot_prefix}quit`", inline = False)
			embed.add_field(name = "Important: ", value = f"**This feature is still in development, do not expect much from it!**", inline = False)
			embed.set_footer(text = "Do not use the example brackets when using the commands!")
			await ctx.send(embed = embed)

		### Kawaii Help Inputs ###
		elif inputs == "hug":
			embed = discord.Embed(title = "Hug - Kawaii Command", description = f"Hug someone or hug {self.bot.user.name}.", colour = embed_color)
			embed.add_field(name = "Basic Usage: ", value = f"`{bot_prefix}hug`", inline = False)
			embed.add_field(name = "Other Usage: ", value = f"`{bot_prefix}hug [person]`", inline = False)
			embed.set_footer(text = "Do not use the example brackets when using the commands!")
			await ctx.send(embed = embed)

		elif inputs == "poke":
			embed = discord.Embed(title = "Poke - Kawaii Command", description = f"Poke someone or poke {self.bot.user.name}.", colour = embed_color)
			embed.add_field(name = "Basic Usage: ", value = f"`{bot_prefix}poke`", inline = False)
			embed.add_field(name = "Other Usage: ", value = f"`{bot_prefix}poke [person]`", inline = False)
			embed.set_footer(text = "Do not use the example brackets when using the commands!")
			await ctx.send(embed = embed)

		elif inputs == "wave":
			embed = discord.Embed(title = "Wave - Kawaii Command", description = f"Wave at someone or to {self.bot.user.name}.", colour = embed_color)
			embed.add_field(name = "Basic Usage: ", value = f"`{bot_prefix}wave`", inline = False)
			embed.add_field(name = "Other Usage: ", value = f"`{bot_prefix}wave [person]`", inline = False)
			embed.set_footer(text = "Do not use the example brackets when using the commands!")
			await ctx.send(embed = embed)

		elif inputs == "hide":
			embed = discord.Embed(title = "Hide - Kawaii Command", description = f"Hide for someone or for {self.bot.user.name}.", colour = embed_color)
			embed.add_field(name = "Basic Usage: ", value = f"`{bot_prefix}hide`", inline = False)
			embed.add_field(name = "Other Usage: ", value = f"`{bot_prefix}hide [person]`", inline = False)
			embed.set_footer(text = "Do not use the example brackets when using the commands!")
			await ctx.send(embed = embed)

		elif inputs == "blush":
			embed = discord.Embed(title = "Blush - Kawaii Command", description = f"Express that you're blushing.", colour = embed_color)
			embed.add_field(name = "Basic Usage: ", value = f"`{bot_prefix}blush`", inline = False)
			embed.set_footer(text = "Do not use the example brackets when using the commands!")
			await ctx.send(embed = embed)

		elif inputs == "shine":
			embed = discord.Embed(title = "Shine - Kawaii Command", description = f"Express that you're shining.", colour = embed_color)
			embed.add_field(name = "Basic Usage: ", value = f"`{bot_prefix}shine`", inline = False)
			embed.set_footer(text = "Do not use the example brackets when using the commands!")
			await ctx.send(embed = embed)

		elif inputs == "happy":
			embed = discord.Embed(title = "Happy - Kawaii Command", description = f"Express that you're happy.", colour = embed_color)
			embed.add_field(name = "Basic Usage: ", value = f"`{bot_prefix}happy`", inline = False)
			embed.set_footer(text = "Do not use the example brackets when using the commands!")
			await ctx.send(embed = embed)

		elif inputs == "dab":
			embed = discord.Embed(title = "Dab - Kawaii Command", description = f"Dab, dab, dab and more dabs!", colour = embed_color)
			embed.add_field(name = "Basic Usage: ", value = f"`{bot_prefix}dab`", inline = False)
			embed.set_footer(text = "Do not use the example brackets when using the commands!")
			await ctx.send(embed = embed)

		else:
			embed = discord.Embed(title=f"Command List for {self.bot.user.name}!", colour = embed_color, description=f"Prefix for {ctx.guild}: **{bot_prefix}**\nIf a command is not working, or something goes wrong?\nUse the this command `{bot_prefix}ctdev [question/feedback]`!\nTo get more information about a command: `>help [command]`\n⠀")
			embed.set_thumbnail(url = self.bot.user.avatar_url)
			embed.add_field(name="Core Commands", value=f"``{bot_prefix}help`` **|** ``{bot_prefix}ctdev`` **|** ``{bot_prefix}invite`` **|** ``{bot_prefix}about``", inline = False)
			embed.add_field(name="Kawaii Commands", value=f"``{bot_prefix}hug`` **|** ``{bot_prefix}poke`` **|** ``{bot_prefix}wave`` **|** ``{bot_prefix}hide`` **|** ``{bot_prefix}blush`` **|** ``{bot_prefix}shine`` **|** ``{bot_prefix}happy`` **|** ``{bot_prefix}dab``", inline = False)
			embed.add_field(name="Fun Commands", value=f"``{bot_prefix}8ball`` **|** ``{bot_prefix}poll`` **|** ``{bot_prefix}hub`` **|** ``{bot_prefix}osu`` **|** ``{bot_prefix}avatar`` **|** ``{bot_prefix}weather`` **|** ``{bot_prefix}virus``", inline = False)
			embed.add_field(name="Music/Voice Commands", value=f"``{bot_prefix}join`` **|** ``{bot_prefix}play`` **|** ``{bot_prefix}volume`` **|** ``{bot_prefix}stop``", inline=True)
			embed.add_field(name="Utility Commands", value=f"``{bot_prefix}ping`` **|** ``{bot_prefix}permissions`` **|** ``{bot_prefix}userinfo`` **|** ``{bot_prefix}serverinfo`` **|** ``{bot_prefix}listservers`` **|** ``{bot_prefix}uptime``", inline=True)
			embed.add_field(name="Administrative Commands", value=f"``{bot_prefix}setrole`` **|** ``{bot_prefix}removerole`` **|** ``{bot_prefix}mute`` **|** ``{bot_prefix}unmute`` **|** ``{bot_prefix}nickname``", inline=True)
			embed.set_footer(text = "Do not use the example brackets when using the commands!")
			#await ctx.author.send(embed = embed),

			#embed = discord.Embed(description = f"**{ctx.author.name}**, a pm with all my commands is on the way!\nUse `{bot_prefix}h [command]` for more information about specific commands!", color = embed_color_succes)
			await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Help(bot))
