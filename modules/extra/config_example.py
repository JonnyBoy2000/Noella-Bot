#######################################
############# Config File #############
#######################################

from discord.ext import commands
from collections import Counter
from utils import checks, formats
from utils.paginator import HelpPaginator, CannotPaginate
from collections import OrderedDict, deque, Counter
from datetime import datetime as dt

#from .utils import checks, db

import openweathermapy.core as owm
import utils.checks
import utils.db
import utils.formats
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

bot_token = "************************" #Bot Token
bot_owner = ******************** #Bot Owner ID
log_channel = ***************** #Log Channel ID
postgresql = 'postgresql://***:****@******'
dev_discord = "https://discord.gg/EVfHKKn"

### API Key's ###
youtube_api = '****************'
openweathermap_api = '***************'

startup_extensions = ["owner", "admin", "core", "stats", "polls", "kawaii", "fun"]
bot_prefix = ">" #Default Prefix
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
