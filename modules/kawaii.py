#########################################
############ Kawaii Commands ############
#########################################

import discord
import random
from data.kawaii import *
from extra.config import *
from discord.ext import commands

class Kawaii():
    def __init__(self, bot):
        self.bot = bot

#hug command (-hug [@mention])
    @commands.guild_only()
    @commands.command()
    async def hug(self, ctx, *, member : discord.Member = None):

        author = ctx.author
        if not member:
            member = self.bot.user

        choice = random.choice(hugs)
        embed = discord.Embed(description = f"**{member.name}** you got hugged by **{author.name}**", color = embed_color)
        embed.set_image(url = f"{choice}")
        await ctx.send(embed = embed)

#poke command (-poke [@mention])
    @commands.guild_only()
    @commands.command()
    async def poke(self, ctx, *, member : discord.Member = None):

        author = ctx.author
        if not member:
            member = self.bot.user

        choice = random.choice(pokes)
        embed = discord.Embed(description = f"**{member.name}** you got poked by **{author.name}**", color = embed_color)
        embed.set_image(url = f"{choice}")
        await ctx.send(embed = embed)

#wave command (-wave [@mention])
    @commands.guild_only()
    @commands.command()
    async def wave(self, ctx, *, member : discord.Member = None):

        author = ctx.author
        if not member:
            member = self.bot.user

        embed = discord.Embed(description = f"**{author.name}** waves at you **{member.name}**", color = embed_color)
        embed.set_image(url = "https://i.imgur.com/w5kTICt.gif")
        await ctx.send(embed = embed)

#hide command (-hide [@mention])
    @commands.guild_only()
    @commands.command()
    async def hide(self, ctx, *, member : discord.Member = None):

        author = ctx.author
        if not member:
            member = self.bot.user

        embed = discord.Embed(description = f"**{author.name}** is hiding for **{member.name}**", color = embed_color)
        embed.set_image(url = "https://i.imgur.com/BZQwbid.gif")
        await ctx.send(embed = embed)

#pat command (-pat [@mention])
    @commands.guild_only()
    @commands.command()
    async def pat(self, ctx, *, member : discord.Member = None):

        author = ctx.author
        if not member:
            member = self.bot.user

        choice = random.choice(pats)
        embed = discord.Embed(description = f"**{member.name}** you got a pat from **{author.name}**", color = embed_color)
        embed.set_image(url = f"{choice}")
        await ctx.send(embed = embed)

#hit command (-hit [@mention])
    @commands.guild_only()
    @commands.command()
    async def hit(self, ctx, *, member : discord.Member = None):

        author = ctx.author
        if not member:
            member = self.bot.user

        choice = random.choice(hits)
        embed = discord.Embed(description = f"**{member.name}** you got hitted by **{author.name}**", color = embed_color)
        embed.set_image(url = f"{choice}")
        await ctx.send(embed = embed)

#blush command (-blush)
    @commands.guild_only()
    @commands.command()
    async def blush(self, ctx):

        embed = discord.Embed(description = f"**{ctx.author.name}** is blushing!", color = embed_color)
        embed.set_image(url = "https://i.imgur.com/DGhgJ1R.gif")
        await ctx.send(embed = embed)

#shine command (-shine)
    @commands.guild_only()
    @commands.command()
    async def shine(self, ctx):

        choice = random.choice(shines)
        embed = discord.Embed(description = f"**{ctx.author.name}** is shining!", color = embed_color)
        embed.set_image(url = f"{choice}")
        await ctx.send(embed = embed)

#happy command (-happy)
    @commands.guild_only()
    @commands.command()
    async def happy(self, ctx):

        embed = discord.Embed(description = f"**{ctx.author.name}** is super happy!", color = embed_color)
        embed.set_image(url = "https://i.imgur.com/4xSrwsj.gif")
        await ctx.send(embed = embed)

#sad command (-sad)
    @commands.guild_only()
    @commands.command()
    async def sad(self, ctx):

        choice = random.choice(sad)
        embed = discord.Embed(description = f"**{ctx.author.name}** is really sad!", color = embed_color)
        embed.set_image(url = f"{choice}")
        await ctx.send(embed = embed)

#dancing command (-dance)
    @commands.guild_only()
    @commands.command()
    async def dance(self, ctx):

        choice = random.choice(dancing)
        embed = discord.Embed(description = f"**{ctx.author.name}** is cheerfully dancing!", color = embed_color)
        embed.set_image(url = f"{choice}")
        await ctx.send(embed = embed)

#Not Kawaii but still really needed!
#dab command (-dab)
    @commands.guild_only()
    @commands.command()
    async def dab(self, ctx):

        choice = random.choice(dabs)
        embed = discord.Embed(description = f"**{ctx.author.name}** is dabbing!", color = embed_color)
        embed.set_image(url = f"{choice}")
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Kawaii(bot))
