#######################################
############# Config File #############
#######################################

from discord.ext import commands
from collections import Counter
from collections import OrderedDict, deque, Counter
from datetime import datetime as dt

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

bot_version = "3.63" #Bot Version
dev_discord = "https://discord.gg/EVfHKKn"

client_id   = '357852849029513216' # your bot's client ID
token = 'MzU3ODUyODQ5MDI5NTEzMjE2.DNMy-Q.37xJjs-r-oWI6rH660g1ntkjDmI' # your bot's token
postgresql = 'postgresql://noella:Not-4-You@localhost/noella' # your postgresql info from above

carbon_key = '' # your bot's key on carbon's site
bots_key = '' # your key on bots.discord.pw
challonge_api_key = '...' # for tournament cog
openweathermap_api = 'f34d56c8ac5418a799698caf7e80f243'
youtube_api = 'AIzaSyAPvJZpOkrwaxdWH27KlbceDRQwiqYUWoY'

embed_color = 13454262 #Default Embed Color
embed_color_succes = 65280 #Default SuccesEmbed Color
embed_color_error = 13434880 #Default ErrorEmbed Color
embed_color_attention = 16776960 #Default AttentionEmbed Color
message_delete_time = 15 #Default Message Delete Time
