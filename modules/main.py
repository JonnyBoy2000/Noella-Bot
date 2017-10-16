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

##########################################
############## Help Command ##############
##########################################

    @bot.command(pass_context = True, aliases=['h'])
    async def help(ctx):
        embed = discord.Embed(title=f"Command List for {bot.user.name}!", colour = embed_color, description=f"Prefix for {ctx.guild}: **{bot_prefix}**\nIf a command is not working, or something goes wrong?\nUse the this command `{bot_prefix}ctdev [question/feedback]`!\n**Don't include the example brackets when using the commands!**⠀\n⠀")
        embed.set_thumbnail(url = bot.user.avatar_url)
        embed.add_field(name="Core Commands", value=f"{bot_prefix}h or {bot_prefix}help \n{bot_prefix}invite \n{bot_prefix}ls or {bot_prefix}listservers \n{bot_prefix}si or {bot_prefix}serverinfo \n{bot_prefix}about \n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", inline=True)
        embed.add_field(name="⠀", value=f"To get help and commands per PM \nTo get a PM with the Bot Invite \nTo get a list of server with {bot.user.name} \nTo see server information \nTo see information about {bot.user.name} \n", inline=True)
        embed.add_field(name="Kawaii Commands", value=f"{bot_prefix}hug [@mention]⠀\n{bot_prefix}poke [@mention]⠀\n{bot_prefix}wave [@mention]⠀\n{bot_prefix}hide [@mention]⠀\n{bot_prefix}blush⠀\n{bot_prefix}shine⠀\n{bot_prefix}happy \n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", inline=True)
        embed.add_field(name="⠀", value=f"To hug {bot.user.name} or someone else! \nTo poke {bot.user.name} or someone else! \nTo wave at {bot.user.name} or someone else! \nTo hide for {bot.user.name} or someone else! \nTo express that you're blushing! \nTo express you're shining! \nTo express you're happy! \n", inline=True)
        embed.add_field(name="Fun Commands", value=f"{bot_prefix}8ball [question]⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", inline=True)
        embed.add_field(name="⠀", value="Ask all you want, to the holy 8Ball!\n", inline=True)
        embed.add_field(name="Voice Commands", value=f"{bot_prefix}connect⠀\n{bot_prefix}disconnect \n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", inline=True)
        embed.add_field(name="⠀", value=f"Connect {bot.user.name} [voice-channel]\nDisconnect {bot.user.name} [voice-channel]\n", inline=True)
        embed.add_field(name="Administrator Commands", value=f"{bot_prefix}sr [@mention] [rolename]\n{bot_prefix}rr [@mention] [rolename] \n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", inline=True)
        embed.add_field(name="⠀", value="Give/set a role to someone!\nRemove a role from someone!\n", inline=True)
        await ctx.author.send(embed = embed),

        embed = discord.Embed(description = f"**{ctx.author.name}**, a personal message with all my commands is on the way!", color = embed_color_succes)
        message = await ctx.send(embed = embed)
        await ctx.message.delete()
        await message.edit(delete_after = message_delete_time)

#################################################
############## Contact Dev Command ##############
#################################################

    @bot.command(pass_context = True)
    async def ctdev(ctx, *, pmessage : str = None):
        invite = await ctx.channel.create_invite(max_uses = 1, xkcd = True)
        dev = bot.get_user(bot_owner)

        if pmessage == None:
            embed = discord.Embed(description = f"**{ctx.author.name}**, my developers need to know something right? Type a feedback!", color = embed_color_attention)
            message = await ctx.send(embed = embed)
            await ctx.message.delete()
            await message.edit(delete_after = 15)

        else:
            embed = discord.Embed(title = f"Invite to {ctx.guild} discord server!", colour = embed_color, url = f"{invite.url}", description = f"**Feedback:** {pmessage}")
            embed.set_thumbnail(url = f"{ctx.author.avatar_url}")
            embed.set_author(name = f"{ctx.author.name} sent:", icon_url = f"{ctx.author.avatar_url}")
            await dev.send(embed = embed)
            embed = discord.Embed(description = f"I have PMed **{dev.name}#{dev.discriminator}** with your feedback! Thank you for your help!", color = embed_color_succes)
            message = await ctx.send(embed = embed)
            await ctx.message.delete()
            await message.edit(delete_after = message_delete_time)

#################################################

### Prefix Command ###
    @bot.command(no_pm = True, aliases = ['p'])
    async def prefix(ctx):

        embed = discord.Embed(description = f"**{ctx.author.name}**, the prefix to use **{bot.user.name}** is: `{bot_prefix}`", color = embed_color)
        message = await ctx.send(embed = embed)
        await ctx.message.delete()
        await message.edit(delete_after = message_delete_time)

    @bot.event
    async def on_message(message):
        if message.content.startswith('prefix'):
            embed = discord.Embed(description = f"**{message.author.name}**, the prefix to use **{bot.user.name}** is: `{bot_prefix}`", color = embed_color)
            await message.channel.send(embed = embed)
            await message.delete()
        await bot.process_commands(message)

### Ping/Latency Command ###
    @bot.command(no_pm = True, aliases = ['ping'])
    async def latency(ctx):
        pingms = "{}".format(int(bot.latency * 1000))
        pings = "{}".format(int(bot.latency * 1))
        message = await ctx.send("Ping - Calculating some shit in the background... beep beep...")
        await asyncio.sleep(3)
        await message.edit(content = f"Pong! - My latency is **{pings}**s | **{pingms}**ms")
        await message.edit(delete_after = message_delete_time)
        await ctx.message.delete()

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(bot_token)
