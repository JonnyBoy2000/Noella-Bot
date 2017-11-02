######################################
############ Fun Commands ############
######################################

import discord
import random
from discord.ext import commands
from config import *
from cogs.data.eightballdata import answers
from cogs.data.fortunedata import fortunes
import openweathermapy.core as owm

class Fun():
	def __init__(self, bot):
		self.bot = bot

	@commands.guild_only()
	@commands.command(no_pm = True, aliases=['8ball'])
	async def eightball(self, ctx, *, question : str = None):

		if question == None:
			embed = discord.Embed(description = f"**{ctx.author.name}** you first need to ask me something! Duhh", color = embed_color_attention)
			await ctx.send(embed=embed)

		elif not question.endswith("?"):
			embed = discord.Embed(description = f"**{ctx.author.name}**, that doesn't look like a question!", color = embed_color_attention)
			await ctx.send(embed=embed)

		else:
			result = answers
			choice = random.choice(result)
			embed = discord.Embed(colour = embed_color)
			embed.set_thumbnail(url = ctx.author.avatar_url)
			embed.add_field(name=f"**{ctx.author.name}** asks:", inline=False, value=f"{question}")
			embed.add_field(name="**Holy 8ball** answers:", inline=False, value=f"{choice}")
			await ctx.send(embed=embed)

#########################################

	@commands.guild_only()
	@commands.command(no_pm = True, aliases = ['fort'])
	async def fortune(self, ctx, *, member : discord.Member = None):

		author = ctx.author
		if not member:
			member = author

		choice = random.choice(fortunes)
		embed = discord.Embed(colour = embed_color)
		embed.add_field(name = f":crystal_ball:⠀|⠀{member.name}:", value = f"⠀\n{choice}", inline = False)
		await ctx.send(embed=embed)

#########################################

	@commands.guild_only()
	@commands.command(no_pm = True, aliases = ['hub'])
	async def discordhub(self, ctx, *, member : discord.Member = None):

		author = ctx.author
		if not member:
			member = author

		embed = discord.Embed(title="Click here to visit *%s* profile!"%member.name, colour = embed_color, url="https://discordhub.com/profile/%s"%member.id, description="DiscordHub aims to provide a centralized platform for Discord\nby providing features such as user accounts and a public server list.")
		embed.set_thumbnail(url="https://cdn.discordapp.com/embed/avatars/4.png")
		embed.set_author(name="%s Profile!"%member.name, icon_url="https://cdn.discordapp.com/embed/avatars/4.png")
		await ctx.send(embed=embed)

#########################################

	@commands.guild_only()
	@commands.command(no_pm = True, aliases = ['pfp'])
	async def avatar(self, ctx, *, member : discord.Member = None):
		author = ctx.author

		if not member:
			member = author

		if member.avatar:
#			if member.avatar_url[54:].startswith('a_'):
#				avi = 'https://cdn.discordapp.com/avatars/' + member.avatar_url[35:-10]
#			else:
			avi = member.avatar_url
			embed = discord.Embed(description = f"**{member.name}'s** avatar!\n[Click to open {member.name}'s avatar!]({member.avatar_url})", color = embed_color)
			embed.set_image(url = f"{avi}")
			await ctx.send(embed = embed)
		else:
			embed = discord.Embed(description = f"**{member.name}** has no avatar!\n", color = embed_color)
			embed.set_image(url = "https://i.imgur.com/lkeELEJ.png")
			await ctx.send(embed = embed)

#########################################

	@commands.guild_only()
	@commands.command(no_pm = True, aliases = ['gicon'])
	async def guildicon(self, ctx):
		guild = ctx.guild

		if guild.icon_url:
			embed = discord.Embed(description = f"**{guild.name}'s** guild icon!\n[Click to open {guild.name}'s guild icon!]({guild.icon_url})", color = embed_color)
			embed.set_image(url = f"{guild.icon_url}")
			await ctx.send(embed = embed)
		else:
			embed = discord.Embed(description = f"**{guild.name}** has no icon!\n", color = embed_color)
			embed.set_image(url = "https://i.imgur.com/lkeELEJ.png")
			await ctx.send(embed = embed)

#########################################

	@commands.guild_only()
	@commands.command(no_pm = True, aliases = ['uid'])
	async def userid(self, ctx, member : discord.Member = None):
		author = ctx.author
		if not member:
			member = author

		embed = discord.Embed(description = f"`{member.id}`", color = embed_color)
		embed.set_author(name = f"{member.name}", icon_url = f"{member.avatar_url}")
		await ctx.send(embed = embed)

#########################################

	@commands.guild_only()
	@commands.command(no_pm = True, aliases=['osu'])
	async def osustats(self, ctx, *, osuplayer : str = None):

		if osuplayer == None:
			embed = discord.Embed(description = "**"+ ctx.author.name +"** you need to tell me a username!", color = embed_color)
			await ctx.send(embed = embed)

		else:
			#embed.set_thumbnail(url = ctx.author.avatar_url)
			embed = discord.Embed(color = embed_color)
			embed.set_author(name = f"{osuplayer}'s Stats", url = f"https://osu.ppy.sh/u/{osuplayer}", icon_url = "https://s.ppy.sh/images/head-logo.png")
			embed.set_footer(text = "Images provided by lemmmy.pw/osusig")
			embed.set_image(url = f"http://lemmmy.pw/osusig/sig.php?colour=hexff66aa&uname={osuplayer}&pp=1&countryrank&flagshadow&flagstroke&opaqueavatar&avatarrounding=5&onlineindicator=undefined&xpbar&xpbarhex")
			await ctx.send(embed = embed)

#########################################

	@commands.guild_only()
	@commands.command(no_pm = True)
	async def virus(self, ctx, *, member : discord.Member = None):

		author = ctx.author
		if not member:
			member = ctx.guild

		message = await ctx.send(f"[⠀▓▓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀] / discord-virus.exe Packing files..")
		await asyncio.sleep(1)
		await message.edit(content = f"[⠀▓▓▓▓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀] / discord-virus.exe Packing files..")
		await asyncio.sleep(1)
		await message.edit(content = f"[⠀▓▓▓▓▓▓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀] / discord-virus.exe Packing files..")
		await asyncio.sleep(2)
		await message.edit(content = f"[⠀▓▓▓▓▓▓▓▓▓▓▓▓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀] / discord-virus.exe Packing files..")
		await asyncio.sleep(1)
		await message.edit(content = f"[⠀▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓⠀⠀⠀⠀] / discord-virus.exe Packing files..")
		await asyncio.sleep(1)
		await message.edit(content = f"[⠀▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓⠀] / discord-virus.exe Packing files..")
		await asyncio.sleep(0.50)
		await message.edit(content = f"Injecting virus.")
		await asyncio.sleep(0.50)
		await message.edit(content = f"Injecting virus..")
		await asyncio.sleep(0.50)
		await message.edit(content = f"Injecting virus...")
		await asyncio.sleep(0.50)
		await message.edit(content = f"Injecting virus....")
		await asyncio.sleep(0.50)
		await message.edit(content = f"Injecting virus.")
		await asyncio.sleep(0.50)
		await message.edit(content = f"Injecting virus..")
		await asyncio.sleep(0.50)
		await message.edit(content = f"Injecting virus...")
		await asyncio.sleep(0.50)
		await message.edit(content = f"Injecting virus....")
		await asyncio.sleep(0.50)
		await message.edit(content = f"Injecting virus.")
		await asyncio.sleep(0.50)
		await message.edit(content = f"Injecting virus..")
		await asyncio.sleep(2)
		await message.edit(content = f"**Successfully** Injected __discord-virus.exe__ into **{member.name}**")

#########################################

	@commands.guild_only()
	@commands.command(no_pm = True)
	async def weather(self, ctx, *, city : str = None):
		if city is None:
			embed = discord.Embed(description = f"**{ctx.author.name}**, 'nothing' has no weather! That was an easy weather forecast! :rofl: ", color = embed_color_attention)
			message = await ctx.send(embed = embed)
			await message.edit(delete_after = message_delete_time)
			return
		else:
			settings = {"APPID":f"{openweathermap_api}", "units": "metric"}
			data = owm.get_current(f'{city}', **settings)
			cityname_raw = data.get_many(['name'])
			country_raw = data.get_many(['sys.country'])
			temperature_raw = data.get_many(['main.temp'])
			humidity_raw = data.get_many(['main.humidity'])
			windspeed_raw = data.get_dict(['wind.speed'])

			cityname = f"{cityname_raw}".replace("('", '').replace("',)", '')
			country = f"{country_raw}".replace("('", '').replace("',)", '')
			temperature = f"{temperature_raw}".replace("(", '').replace(",)", '')
			humidity = f"{humidity_raw}".replace("(", '').replace(",)", '')
			windspeed = f"{windspeed_raw}".replace("{'wind", "").replace(".speed': ", "").replace("}", "")

			embed = discord.Embed(title = f"Weather for **{cityname}**, **{country}**", colour = embed_color)
			embed.add_field(name = "⠀", value = "Temperature: \nHumidity: \nWindspeed: \n", inline = True)
			embed.add_field(name = "⠀", value = f"**{temperature}°C** \n**{humidity}%** \n**{windspeed} m/s** \n", inline = True)
			embed.set_footer(text = "Powered by OpenWeatherMap")
			embed.set_thumbnail(url = "http://www.iconsfind.com/wp-content/uploads/2015/11/20151125_565508763073c.png")
			await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Fun(bot))
