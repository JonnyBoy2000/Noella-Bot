######################################
############ Fun Commands ############
######################################

import discord
import random
from discord.ext import commands
from extra.config import *
import openweathermapy.core as owm

class Fun():
	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context = True, no_pm = True, aliases=['8ball'])
	async def eightball(self, ctx, *, question : str = None):

		if question == None:
			embed = discord.Embed(description = f"**{ctx.author.name}** you first need to ask me something! Duhh", color = embed_color_attention)
			await ctx.send(embed=embed)
			await ctx.message.delete()

		elif not question.endswith("?"):
			embed = discord.Embed(description = f"**{ctx.author.name}**, that doesn't look like a question!", color = embed_color_attention)
			await ctx.send(embed=embed)
			await ctx.message.delete()

		else:
			result = ["Neko", "Loli", "Kitsune"]
			choice = random.choice(result)
			embed = discord.Embed(colour = embed_color)
			embed.set_thumbnail(url = ctx.author.avatar_url)
			embed.add_field(name=f"**{ctx.author.name}** asks:", inline=False, value=f"{question}")
			embed.add_field(name="**Holy 8ball** answers:", inline=False, value=f"{choice}")
			await ctx.send(embed=embed)
			await ctx.message.delete()

#########################################

	@commands.command(pass_context = True, no_pm = True, aliases = ['hub'])
	async def discordhub(self, ctx, *, member : discord.Member = None):

		author = ctx.author
		if not member:
			member = author

		embed = discord.Embed(title="Click here to visit *%s* profile!"%member.name, colour = embed_color, url="https://discordhub.com/profile/%s"%member.id, description="DiscordHub aims to provide a centralized platform for Discord\nby providing features such as user accounts and a public server list.")
		embed.set_thumbnail(url="https://cdn.discordapp.com/embed/avatars/4.png")
		embed.set_author(name="%s Profile!"%member.name, icon_url="https://cdn.discordapp.com/embed/avatars/4.png")
		await ctx.send(embed=embed)
		await ctx.message.delete()

#########################################

	@commands.command(pass_context=True)
	async def avatar(self, ctx, *, member : discord.Member = None):
		author = ctx.author

		if not member:
			member = author

		if member.avatar_url[54:].startswith('a_'):
			avi = 'https://cdn.discordapp.com/avatars/' + member.avatar_url[35:-10]
		else:
			avi = member.avatar_url

		embed = discord.Embed(description = f"**{member.name}'s** avatar!\n[Click to open {member.name}'s avatar!]({member.avatar_url})", color = embed_color)
		embed.set_image(url = f"{avi}")
		await ctx.send(embed = embed)
		await ctx.message.delete()

#########################################

	@commands.command(no_pm = True, aliases=['osu'])
	async def osustats(self, ctx, *, osuplayer : str = None):

		if osuplayer == None:
			embed = discord.Embed(description = "**"+ ctx.author.name +"** you need to tell me a username!", color = embed_color)
			await ctx.send(embed = embed)
			await ctx.message.delete()

		else:
			#embed.set_thumbnail(url = ctx.author.avatar_url)
			embed = discord.Embed(color = embed_color)
			embed.set_author(name = f"{osuplayer}'s Stats", url = f"https://osu.ppy.sh/u/{osuplayer}", icon_url = "https://s.ppy.sh/images/head-logo.png")
			embed.set_footer(text = "Images provided by lemmmy.pw/osusig")
			embed.set_image(url = f"http://lemmmy.pw/osusig/sig.php?colour=hexff66aa&uname={osuplayer}&pp=1&countryrank&flagshadow&flagstroke&opaqueavatar&avatarrounding=5&onlineindicator=undefined&xpbar&xpbarhex")
			await ctx.send(embed = embed)
			await ctx.message.delete()

#########################################

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
		await message.edit(delete_after = message_delete_time)
		await ctx.message.delete()

#########################################

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
			cityname = data.get_many(['name'])
			country = data.get_many(['sys.country'])
			coordinates = data.get_many(['coord.lon', 'coord.lat'])
			temprature = data.get_many(['main.temp'])
			tempminmax = data.get_many(['main.temp_min', 'main.temp_max'])
			humidity = data.get_many(['main.humidity'])
			windspeed = data.get_dict(['wind.speed'])

			sunrise_raw = data.get_many(['sys.sunrise'])
			sunrise_convert = f"{sunrise_raw}".replace('(', '').replace(',)', '')
			sunrise = time.strftime("%H:%M", time.gmtime(int(sunrise_convert)))

			sunset_raw = data.get_many(['sys.sunset'])
			sunset_convert = f"{sunset_raw}".replace('(', '').replace(',)', '')
			sunset = time.strftime("%H:%M", time.gmtime(int(sunset_convert)))

			embed = discord.Embed(colour = embed_color)
			embed.add_field(name = ":earth_africa: Location", value = f"{cityname}, {country}".replace("('", '').replace("',)", ''), inline = True)
			embed.add_field(name = ":straight_ruler: Coordinates", value = f"{coordinates}".replace('(', '').replace(')', ''), inline = True)
			embed.add_field(name = ":sweat: Humidity", value = f"{humidity}%".replace('(', '').replace(',)', ''), inline = True)
			embed.add_field(name = ":dash: Wind speed", value = f"{windspeed} m/s".replace("{'wind", "").replace(".speed':", "").replace("}", ""), inline = True)
			embed.add_field(name = ":thermometer: Temperature", value = f"{temprature}°C".replace('(', '').replace(',)', ''), inline = True)
			embed.add_field(name = ":high_brightness: Min/Max", value = f"{tempminmax}°C".replace('(', '').replace(', ', '°C - ').replace(')', ''), inline = True)
			embed.add_field(name = ":sunrise_over_mountains: Sunrise", value = f"{sunrise} UTC", inline = True)
			embed.add_field(name = ":city_sunset: Sunset", value = f"{sunset} UTC", inline = True)
			embed.set_thumbnail(url = "http://www.iconsfind.com/wp-content/uploads/2015/11/20151125_565508763073c.png")
			await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Fun(bot))
