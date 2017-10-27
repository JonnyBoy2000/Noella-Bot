##########################################
############ Utility Commands ############
##########################################

import discord
import random
from discord.ext import commands
from .musicutils.paginator import Pages
from config import *

class Utility():
	def __init__(self, bot):
		self.bot = bot

### Ping/Latency Command ###
	@commands.guild_only()
	@commands.command(aliases = ['ping'])
	async def latency(self, ctx):
		pingms = "{}".format(int(self.bot.latency * 1000))
		pings = "{}".format(int(self.bot.latency * 1))
		message = await ctx.send("Ping - Calculating some shit in the background... beep beep...")
		await asyncio.sleep(3)
		await message.edit(content = f"Pong! - My latency is **{pings}**s | **{pingms}**ms")

### Server Information Command ###
	@commands.guild_only()
	@commands.command(aliases=['si'])
	async def serverinfo(self, ctx):
		vchannels = ctx.guild.voice_channels
		tchannels = ctx.guild.text_channels
		tmembers = ctx.guild.member_count
		omembers = sum(m.status is discord.Status.online for m in ctx.guild.members)
		time = str(ctx.guild.created_at); time = time.split(' '); time= time[0];
		roles = [x.name for x in ctx.guild.role_hierarchy]
		role_length = len(roles)
		roles = ', '.join(roles);

		if str(ctx.guild.verification_level) == "none":
			verification_text = "Protection: **None**\n*No further protection!*"
		elif str(ctx.guild.verification_level) == "low":
			verification_text = "Protection: **Low**\n*Verified Email*"
		elif str(ctx.guild.verification_level) == "medium":
			verification_text = "Protection: **Medium**\n*Registered for 5 Minutes*"
		elif str(ctx.guild.verification_level) == "high":
			verification_text = "Protection: **High**\n*Member for 10 Minutes*"
		elif str(ctx.guild.verification_level) == "extreme":
			verification_text = "Protection: **Extreme**\n*Verified Phone Number*"
		else:
			verification_text = "Protection: **N/A**\n*Cant find any protection*"

		embed = discord.Embed(colour = embed_color)
		if ctx.guild.icon_url:
			embed.set_thumbnail(url = ctx.guild.icon_url)
		else:
			embed.set_thumbnail(url = "https://cdn.discordapp.com/embed/avatars/0.png")
		embed.set_author(name = "Server Information", icon_url = "http://icons.iconarchive.com/icons/graphicloads/100-flat/128/information-icon.png")
		embed.add_field(name="Server Name:", value = str(ctx.guild), inline=True)
		embed.add_field(name="Server ID:", value = str(ctx.guild.id), inline=True)
		embed.add_field(name="Server Owner:", value = str(ctx.guild.owner), inline=True)
		embed.add_field(name="Server Owner ID:", value = ctx.guild.owner.id, inline=True)
		embed.add_field(name="Member Count:", value = f'Members Online: **{omembers}**\nMembers Total: **{tmembers}**', inline=True)
		embed.add_field(name="Channels Count:", value = "Text Channels: **"+ str(len(tchannels)) +"** \nVoice Channels: **"+ str(len(vchannels)) +"**", inline=True)
		embed.add_field(name="Verification Level:", value = f"{verification_text}", inline=True)
		embed.add_field(name="AFK Channel & Time:", value = f"Channel: **{ctx.guild.afk_channel}**\n" "Time: **{} minutes**".format(int(ctx.guild.afk_timeout / 60)), inline=True)
		embed.add_field(name="Server Region:", value = '%s'%str(ctx.guild.region), inline=True)
		embed.add_field(name="Server Roles:", value = '%s'%str(role_length), inline=True)
		embed.set_footer(text ='Server Created: %s'%time);

		await ctx.send(embed = embed)

### List Servers Command ###
	@commands.guild_only()
	@commands.command(aliases = ['ls'])
	async def listservers(self, ctx):
		for guild in self.bot.guilds:
			guilds = [f"**{guild.name}** \nServer Owner: **{guild.owner.name}#{guild.owner.discriminator}**\nOnline Members: **{sum(m.status is discord.Status.online for m in guild.members)}** - Total Members: **{guild.member_count}**\nText Channels: **{str(len(guild.text_channels))}** - Voice Channels: **{str(len(guild.voice_channels))}**\n" for guild in self.bot.guilds]
		try:
			p = Pages(ctx, entries=guilds, per_page=5)
			p.embed.colour = embed_color
			await p.paginate()
		except Exception as e:
			await ctx.send(e)

def setup(bot):
    bot.add_cog(Utility(bot))
