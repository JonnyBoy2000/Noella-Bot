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
    @commands.command(pass_context = True, no_pm = True)
    async def hug(self, ctx, *, member : discord.Member = None):

        author = ctx.author
        if not member:
            member = self.bot.user

        choice = random.choice(hugs)
        embed = discord.Embed(description = f"**{member.name}** you got hugged by **{author.name}**", color = embed_color)
        embed.set_image(url = f"{choice}")
        await ctx.send(embed = embed)
        await ctx.message.delete()

#poke command (-poke [@mention])
    @commands.command(pass_context = True, no_pm = True)
    async def poke(self, ctx, *, member : discord.Member = None):

        author = ctx.author
        if not member:
            member = self.bot.user

        choice = random.choice(pokes)
        embed = discord.Embed(description = f"**{member.name}** you got poked by **{author.name}**", color = embed_color)
        embed.set_image(url = f"{choice}")
        await ctx.send(embed = embed)
        await ctx.message.delete()

#wave command (-wave [@mention])
    @commands.command(pass_context = True, no_pm = True)
    async def wave(self, ctx, *, member : discord.Member = None):

        author = ctx.author
        if not member:
            member = self.bot.user

        embed = discord.Embed(description = f"**{author.name}** waves at you **{member.name}**", color = embed_color)
        embed.set_image(url = "https://i.imgur.com/w5kTICt.gif")
        await ctx.send(embed = embed)
        await ctx.message.delete()

#hide command (-hide [@mention])
    @commands.command(pass_context = True, no_pm = True)
    async def hide(self, ctx, *, member : discord.Member = None):

        author = ctx.author
        if not member:
            member = self.bot.user

        embed = discord.Embed(description = f"**{author.name}** is hiding for **{member.name}**", color = embed_color)
        embed.set_image(url = "https://i.imgur.com/BZQwbid.gif")
        await ctx.send(embed = embed)
        await ctx.message.delete()

#blush command (-blush)
    @commands.command(pass_context = True, no_pm = True)
    async def blush(self, ctx):

        embed = discord.Embed(description = f"**{ctx.author.name}** is blushing!", color = embed_color)
        embed.set_image(url = "https://i.imgur.com/DGhgJ1R.gif")
        await ctx.send(embed = embed)
        await ctx.message.delete()

#shine command (-shine)
    @commands.command(pass_context = True, no_pm = True)
    async def shine(self, ctx):

        embed = discord.Embed(description = f"**{ctx.author.name}** is shining!", color = embed_color)
        embed.set_image(url = "https://i.imgur.com/VUuoZfa.gif")
        await ctx.send(embed = embed)
        await ctx.message.delete()

#happy command (-happy)
    @commands.command(pass_context = True, no_pm = True)
    async def happy(self, ctx):

        embed = discord.Embed(description = f"**{ctx.author.name}** is super happy!", color = embed_color)
        embed.set_image(url = "https://i.imgur.com/4xSrwsj.gif")
        await ctx.send(embed = embed)
        await ctx.message.delete()

#Not Kawaii but still really needed!
#dab command (-dab)
    @commands.command(pass_context = True, no_pm = True)
    async def dab(self, ctx):

        choice = random.choice(dabs)
        embed = discord.Embed(description = f"**{ctx.author.name}** is dabbing!", color = embed_color)
        embed.set_image(url = f"{choice}")
        await ctx.send(embed = embed)
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(Kawaii(bot))
