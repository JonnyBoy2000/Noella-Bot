#######################################
############# Config File #############
#######################################

from discord.ext import commands
from collections import Counter
from utils import checks, formats
from collections import OrderedDict, deque, Counter
from datetime import datetime as dt

#from .utils import checks, db

import openweathermapy.core as owm
import cogs.utils.checks
import cogs.utils.db
import cogs.utils.formats
import time
import logging
import aiohttp
import discord
import sys
import asyncio
import datetime
import traceback
import copy
import unicodedata
import inspect
import os
import json

#######################################

bot_token = "MzcwNzEzNzMwNjE2MzkzNzI4.DMrFlw.m9t6ROynEio96Wjg_ODIeKeZCRA" #Bot Token
bot_owner = 139191103625625600 #Bot Owner ID
bot_version = "3.63" #Bot Version
log_channel = 367584507240382464 #Log Channel ID
postgresql = 'postgresql://mikami:Not-4-You@localhost/noella'
dev_discord = "https://discord.gg/EVfHKKn"

### API Key's ###
youtube_api = 'AIzaSyAPvJZpOkrwaxdWH27KlbceDRQwiqYUWoY'
openweathermap_api = 'f34d56c8ac5418a799698caf7e80f243'

startup_extensions = ["extra.errorhandler", "help", "music", "utility", "owner", "admin", "core", "polls", "kawaii", "fun"]
bot_prefix = "n." #Default Prefix
mute_role = "Server Mute"

embed_color = 13454262 #Default Embed Color
embed_color_succes = 65280 #Default SuccesEmbed Color
embed_color_error = 13434880 #Default ErrorEmbed Color
embed_color_attention = 16776960 #Default AttentionEmbed Color

message_delete_time = 15 #Default Message Delete Time

#######################################

def setup(bot):
    bot.add_cog(Config(bot))
### "extra.errorhandler", ###
