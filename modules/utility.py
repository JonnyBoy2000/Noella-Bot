##########################################
############ Utility Commands ############
##########################################

import discord
import random
from discord.ext import commands
from utils.paginator import Pages
from extra.config import *

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
		await ctx.send(embed=e)

	@commands.guild_only()
	@commands.command(no_pm = True, hidden = True, aliases = ['perms'])
	async def permissions(self, ctx, member: discord.Member = None, channel: discord.TextChannel = None):
		channel = channel or ctx.channel
		if member is None:
			member = ctx.author
		await self.say_permissions(ctx, member, channel)

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

### User information Command ###
	@commands.guild_only()
	@commands.group(invoke_without_command = True, aliases =  ['info', 'uinfo', 'user'])
	async def userinfo(self, ctx, *, member: discord.Member = None):

		if member is None:
			member = ctx.author

		if member.game is None or member.game.url is None:
			if str(member.status) == "online":
				status_colour = embed_color_succes
				status_name = "Online"
			elif str(member.status) == "idle":
				status_colour = embed_color_attention
				status_name = "Away / Idle"
			elif str(member.status) == "dnd":
				status_colour = embed_color_error
				status_name = "Do Not Disturb"
			elif str(member.status) == "offline" or str(member.status) == "invisible":
				status_colour = 0x000000
				status_name = "Offline"
			else:
				status_colour = member.colour
				status_name = "N/A"
		else:
			status_colour = 0x593695
			status_name = "Streaming"

		e = discord.Embed(description = f"**Nickname**: {member.nick}", colour = status_colour)
		roles = [role.name.replace('@', '@\u200b') for role in member.roles]
		shared = sum(1 for m in self.bot.get_all_members() if m.id == member.id)
		voice = member.voice

		highrole = member.top_role.name
		if highrole == "@everyone":
			role = "N/A"

		if member.avatar_url[54:].startswith('a_'):
			avi = 'https://cdn.discordapp.com/avatars/' + member.avatar_url[35:-10]
		else:
			avi = member.avatar_url

		if avi:
			e.set_thumbnail(url = avi)
			e.set_author(name = str(member), icon_url = avi)
		else:
			e.set_thumbnail(url = member.default_avatar_url)
			e.set_author(name = str(member), icon_url = member.default_avatar_url)

		e.set_footer(text = 'Member since').timestamp = member.joined_at
		e.add_field(name = 'User ID', value = member.id)
		e.add_field(name = 'Servers', value = f'{shared} shared')
		#e.add_field(name = 'Voice', value = voice)
		e.add_field(name = 'Client Status', value = status_name)

		if member.game is None:
			e.add_field(name = 'Doing:', value = "Completely nothing!")
		elif member.game.url is None:
			e.add_field(name = 'Playing:', value = f"{member.game}")
		else:
			e.add_field(name = 'Streaming:', value = f"[{member.game}]({member.game.url})")

		e.add_field(name = 'Created at', value = member.created_at.__format__('%d. %B %Y\n%H:%M:%S'))
		e.add_field(name='Highest Role', value = highrole)
		e.add_field(name = 'Roles', value = ' **|** '.join(roles) if len(roles) < 15 else f'{len(roles)} roles')

		await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(Utility(bot))
