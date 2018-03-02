#Mathbot
#Author: Everett Yee
#v1.4

import discord
import math
print(discord.__version__)
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix='$', description="A bot that does simple math calculations and shortcuts.")

@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print('-----')

#Basic math
@bot.command()
async def add(ctx, a: float, b: float):
    await ctx.send(ctx.message.author.mention + " the answer is:")
    await ctx.send(a+b)

@bot.command()
async def minus(ctx, a: float, b: float):
    await ctx.send(ctx.message.author.mention + " the answer is:")
    await ctx.send(a-b)

@bot.command()
async def mult(ctx, a: float, b: float):
    await ctx.send(ctx.message.author.mention + " the answer is:")
    await ctx.send(a*b)

@bot.command()
async def div(ctx, a: float, b: float):
    await ctx.send(ctx.message.author.mention + " the answer is:")
    await ctx.send(a/b)

#FOIL method, (++) (+-) (--) (-+), only for whole numbers, not binomials
@bot.command()
async def plusplus(ctx, a: float, b: float, c: float, d: float):
    await ctx.send(ctx.message.author.mention + " the answer is:")
    await ctx.send((a*c)+(a*d)+(b*c)+(b*d))

@bot.command()
async def plusminus(ctx, a: float, b: float, c: float, d: float):
    await ctx.send(ctx.message.author.mention + " the answer is:")
    await ctx.send((a*c)-(a*d)+(b*c)-(b*d))

@bot.command()
async def minusminus(ctx, a: float, b: float, c: float, d: float):
    await ctx.send(ctx.message.author.mention + " the answer is:")
    await ctx.send((a*c)-(a*d)-(b*c)+(b*d))

@bot.command()
async def minusplus(ctx, a: float, b: float, c: float, d: float):
    await ctx.send(ctx.message.author.mention + " the answer is:")
    await ctx.send((a*c)+(a*d)-(b*c)-(b*d))

#Square root
@bot.command()
async def sqrt(ctx, a: float):
    await ctx.send(ctx.message.author.mention + " the answer is:")
    await ctx.send(math.sqrt(a))

#Exponents
@bot.command()
async def exp(ctx, a: float, b: float):
    await ctx.send(ctx.message.author.mention + " the answer is:")
    await ctx.send(a**b)

#Cool shortcuts
@bot.command()
async def percentof(ctx, a: float, b: float):
    await ctx.send(ctx.message.author.mention + " the answer is:")
    await ctx.send((a*b)/100)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Mathbot", description="A bot that does simple math calculations and shortcuts.", color=0xeee657)
    # give users a link to invite this bot to their server
    embed.add_field(name="Invite", value="[Invite link(paste this in your browser)](https://discordapp.com/api/oauth2/authorize?client_id=417040473316786186&permissions=2048&scope=bot)")
    await ctx.send(embed=embed)

bot.remove_command("help")
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Mathbot", description="Syntax: $function <parameters> \nList of commands are:", color=0xeee657)

    embed.add_field(name="$add X Y", value="Returns the addition of **X** and **Y**", inline=False)
    embed.add_field(name="$minus X Y", value="Returns **X** subtracted by **Y**", inline=False)
    embed.add_field(name="$mult X Y", value="Returns **X** multiplied by **Y**", inline=False)
    embed.add_field(name="$div X Y", value="Returns **X** divided by **Y**", inline=False)

    embed.add_field(name="$sqrt X", value="Returns the square root of **X**", inline=False)
    embed.add_field(name="$exp X Y", value="Returns **X** to the power of **Y**", inline=False)

    embed.add_field(name="$plusplus A B C D", value="FOIL method on (**A** + **B**)(**C** + **D**) \n**Float/Whole Numbers Only**", inline=False)
    embed.add_field(name="$plusminus A B C D", value="FOIL method on (**A** + **B**)(**C** - **D**) \n**Float/Whole Numbers Only**", inline=False)
    embed.add_field(name="$minusminus A B C D", value="FOIL method on (**A** - **B**)(**C** - **D**) \n**Float/Whole Numbers Only**", inline=False)
    embed.add_field(name="$minusplus A B C D", value="FOIL method on (**A** - **B**)(**C** + **D**) \n**Float/Whole Numbers Only**", inline=False)

    embed.add_field(name="$percentof X Y", value="Returns **X** percent of **Y**", inline=False)
    embed.add_field(name="$info", value="Displays information about Mathbot", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

bot.run("NDE3MDQwNDczMzE2Nzg2MTg2.DXc0Pw.rtggjKy6O0fxb2UVFLMnYlsorY8")
