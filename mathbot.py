#Mathbot
#Author: Everett Yee

import discord
#print(discord.__version__)
from discord.ext import commands

bot = commands.Bot(command_prefix='$', description="A bot that does simple math calculations and shortcuts.")

@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print('-----')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send("The answer is: ")
    await ctx.send(a+b)

@bot.command()
async def percentof(ctx, a: float, b: float):
    await ctx.send("The answer is: ")
    await ctx.send((a*b)/100)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Mathbot", description="A bot that does simple math calculations and shortcuts.", color=0xeee657)
    # give users a link to invite this bot to their server
    embed.add_field(name="Invite", value="[Invite link(paste this in your browser)](OAuth2 link goes here)")

    await ctx.send(embed=embed)

bot.remove_command("help")
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Mathbot", description="List of commands are:", color=0xeee657)

    embed.add_field(name="$add X Y", value="Returns the addition of **X** and **Y**", inline=False)
    embed.add_field(name="$percentof X Y", value="Returns **X** percent of **Y**", inline=False)
    embed.add_field(name="$info", value="Displays information about Mathbot", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

bot.run("Bot secret token goes here")
