########################################
############# Stats Module #############
########################################

from extra.config import *
from discord.ext import commands
from collections import Counter
from utils import checks, formats, db
from utils.paginator import HelpPaginator, CannotPaginate
from collections import OrderedDict, deque, Counter

#from .utils import checks, db

import utils.checks
import utils.db
import logging
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

class Stats:
    def __init__(self, bot):
        self.bot = bot
        self.initialtime = time.time()
        self.process = psutil.Process()

    def getuptime(self):
        seconds = int(time.time() - self.initialtime)
        minutes = 0
        hours = 0
        days = 0

        if seconds > 86399:
            days = int(seconds/86400)
            seconds = seconds % 86400
        if seconds > 3599:
            hours = int(seconds/3600)
            seconds = seconds % 3600
        if seconds > 59:
            minutes = int(seconds/60)
            seconds = seconds % 60

        return "{d}d {h}h {m}m {s}s".format(d=days, h=hours, m=minutes, s=seconds)

    @commands.command(rest_is_raw = True, hidden = True)
    async def uptime(self, ctx, *, content):
        await ctx.send(self.getuptime())
        await ctx.message.delete()

#########################################

### About This Bot Command ###
    @commands.command()
    async def about(self, ctx):
        """Tells you information about the bot itself."""
        cmd = r'git show -s HEAD~3..HEAD --format="[{}](https://github.com/exunious/Noella-Bot/commit/%H) %s (%cr)"'
        if os.name == 'posix':
            cmd = cmd.format(r'\`%h\`')
        else:
            cmd = cmd.format(r'`%h`')

        revision = os.popen(cmd).read().strip()
        embed = discord.Embed(description='⠀\n**Latest Changes**\n' + revision + '\n⠀')
        embed.set_thumbnail(url = self.bot.user.avatar_url)
        embed.title = 'Official Bot Server Invite'
        embed.url = dev_discord
        embed.colour = embed_color

        owner = self.bot.get_user(bot_owner)
        embed.set_author(name=str(owner), icon_url=owner.avatar_url)

        # statistics
        total_members = sum(1 for _ in self.bot.get_all_members())
        total_online = len({m.id for m in self.bot.get_all_members() if m.status is discord.Status.online})
        total_unique = len(self.bot.users)

        voice_channels = []
        text_channels = []
        for guild in self.bot.guilds:
            voice_channels.extend(guild.voice_channels)
            text_channels.extend(guild.text_channels)

        text = len(text_channels)
        voice = len(voice_channels)

        embed.add_field(name='Members in Guilds', value=f'Total Users: **{total_members}**\nTotal Unique: **{total_unique}**\nTotal Online: **{total_online}**')
        embed.add_field(name='Channels in Guilds', value=f'Total Channels: **{text + voice}**\nText Channels: **{text}**\nVoice Channels: **{voice}**')

        memory_usage = self.process.memory_full_info().uss / 1024**2
        cpu_usage = self.process.cpu_percent() / psutil.cpu_count()
        embed.add_field(name='Process', value=f'{memory_usage:.2f} MiB\n{cpu_usage:.2f}% CPU')


        embed.add_field(name='Active in Guilds', value = len(self.bot.guilds))
        #embed.add_field(name='Commands Run', value=sum(self.bot.command_stats.values()))
        embed.add_field(name='Uptime', value=(self.getuptime()))
        embed.set_footer(text='writen in discord.py', icon_url='http://i.imgur.com/5BFecvA.png')
        message = await ctx.send(embed=embed)
        await ctx.message.delete()
        await message.edit(delete_after = message_delete_time + 15)

### Server Information Command ###
    @commands.command(no_pm = True, aliases=['si'])
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

        message = await ctx.send(embed = embed)
        await ctx.message.delete()
        await message.edit(delete_after = message_delete_time + 15)

### List Servers Command ###
    @commands.command(aliases = ['ls'])
    async def listservers(self, ctx, number : int = 10):

        e = discord.Embed(colour = embed_color)
        if number > 50:
            number = 50
        if number < 1:
            await ctx.channel.send('Oookay - look!  No servers!  Just like you wanted!')
            return
        i = 1
        for guild in self.bot.guilds:
            if i > number:
                break
            tmembers = guild.member_count
            vchannels = guild.voice_channels
            tchannels = guild.text_channels
            omembers = sum(m.status is discord.Status.online for m in guild.members)
            e.add_field(name = guild.name, value = f"Server Owner: **{guild.owner.name}#{guild.owner.discriminator}**\nOnline Members: **{omembers}** - Total Members: **{tmembers}**\nText Channels: **"+ str(len(tchannels)) +"** - Voice Channels: **"+ str(len(vchannels)) +"**", inline = False)
            i += 1
        message = await ctx.channel.send(embed = e)
        await ctx.message.delete()
        await message.edit(delete_after = message_delete_time + 15)

### User information Command ###
    @commands.group(invoke_without_command=True, aliases =  ['info', 'uinfo', 'user'])
    async def userinfo(self, ctx, *, member: discord.Member = None):

        if member is None:
            member = ctx.author

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
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(Stats(bot))
