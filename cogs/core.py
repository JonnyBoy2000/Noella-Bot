#########################################
############# Core Commands #############
#########################################

from config import *
from discord.ext import commands
from collections import Counter
from .utils import checks, formats, db
from collections import OrderedDict, deque, Counter

#from .utils import checks, db

import logging
import time
import discord
import asyncio
import datetime
import traceback
import copy
import unicodedata
import inspect
import psutil
import os, datetime

log = logging.getLogger(__name__)

#########################################

class Core:
    def __init__(self, bot):
        self.bot = bot
        self.initialtime = time.time()
        self.process = psutil.Process()

### Invite Bot Link Command ###
    @commands.guild_only()
    @commands.command(aliases = ['inv'])
    async def invite(self, ctx):
        embed = discord.Embed(title = f"**Invite {self.bot.user.name} to your server!**", description = f"You want to invite **{self.bot.user.name}** to your server?\nThen you can use this link to invite her!\n\n[Click here to invite **{self.bot.user.name}**](https://discordapp.com/oauth2/authorize?client_id=357852849029513216&scope=bot&permissions=527952983)\n[Click here to visit **{self.bot.user.name}'s** website](https://goo.gl/2FCCPw)\n[Click here to join **{self.bot.user.name}'s** Dev Discord]({dev_discord})", color = embed_color)
        embed.set_thumbnail(url = self.bot.user.avatar_url)
        await ctx.send(embed = embed)

    @commands.guild_only()
    @commands.command(pass_context = True)
    async def ctdev(self, ctx, *, pmessage : str = None):
        invite = await ctx.channel.create_invite(max_uses = 1, xkcd = True)
        dev = self.bot.get_user(self.bot.owner_id)

        if pmessage == None:
            embed = discord.Embed(description = f"**{ctx.author.name}**, my developers need to know something right? Type a feedback!", color = embed_color_attention)
            message = await ctx.send(embed = embed)
            await message.edit(delete_after = 15)

        else:
            embed = discord.Embed(title = f"Invite to {ctx.guild} discord server!", colour = embed_color, url = f"{invite.url}", description = f"**Feedback:** {pmessage}")
            embed.set_thumbnail(url = f"{ctx.author.avatar_url}")
            embed.set_author(name = f"{ctx.author.name} sent:", icon_url = f"{ctx.author.avatar_url}")
            await dev.send(embed = embed)
            embed = discord.Embed(description = f"I have PMed **{dev.name}#{dev.discriminator}** with your feedback! Thank you for your help!", color = embed_color_succes)
            await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Core(bot))
