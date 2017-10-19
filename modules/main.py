import discord
from datetime import datetime as dt
import time
import asyncio
from discord.ext import commands
from extra.config import *

bot = commands.Bot(command_prefix=bot_prefix)
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Logged in as {}".format(bot.user.name))
    print("Servers: {}".format(len(bot.guilds)))
    print("Prefix: {}".format(bot_prefix))
    print("ID: {}".format(bot.user.id))
    print('------')
    global log_send
    send_log = bot.get_channel(log_channel)
    time_log = dt.utcnow().__format__('%H:%M:%S')
    await send_log.send(f"[{time_log}] - **{bot.user.name}** is online now!")

#################################################
############## Contact Dev Command ##############
#################################################

    @commands.guild_only()
    @bot.command(pass_context = True)
    async def ctdev(ctx, *, pmessage : str = None):
        invite = await ctx.channel.create_invite(max_uses = 1, xkcd = True)
        dev = bot.get_user(bot_owner)

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

#################################################

### Prefix Command ###
    @commands.guild_only()
    @bot.command(no_pm = True, aliases = ['p'])
    async def prefix(ctx):

        embed = discord.Embed(description = f"**{ctx.author.name}**, the prefix to use **{bot.user.name}** is: `{bot_prefix}`", color = embed_color)
        message = await ctx.send(embed = embed)
        await message.edit(delete_after = message_delete_time)

    @bot.event
    async def on_message(message):
        if message.content.startswith('prefix'):
            embed = discord.Embed(description = f"**{message.author.name}**, the prefix to use **{bot.user.name}** is: `{bot_prefix}`", color = embed_color)
            await message.channel.send(embed = embed)
        await bot.process_commands(message)

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(bot_token)
