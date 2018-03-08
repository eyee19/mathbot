#Mathbot
#Author: Everett Yee
#v2.1

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
    if (b == 0):
        await ctx.send(ctx.message.author.mention + " Error: cannot divide by 0.")
    else:
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
    if (a < 0):
        await ctx.send(ctx.message.author.mention + " Error: input cannot less than 0.")
    else:
        await ctx.send(ctx.message.author.mention + " the answer is:")
        await ctx.send(math.sqrt(a))

#Exponents
@bot.command()
async def exp(ctx, a: float, b: float):
    await ctx.send(ctx.message.author.mention + " the answer is:")
    await ctx.send(a**b)

#Factorials
@bot.command()
async def fact(ctx, x: int):
    if (x < 1):
        await ctx.send(ctx.message.author.mention + " Error: factorial function only accepts inputs of 1 or more.")
    else:
        await ctx.send(ctx.message.author.mention + " the factorial is:")
        await ctx.send(math.factorial(x))

#Pythagorean theorem
@bot.command()
async def pyAB(ctx, a: float, b: float): #given the two sides
    await ctx.send(ctx.message.author.mention + " the side length of C is:")
    await ctx.send(math.sqrt((a**2) + (b**2)))

@bot.command()
async def pyAC(ctx, a: float, c: float): #given shorter side and hypotenuse
    await ctx.send(ctx.message.author.mention + " the side length of B is:")
    await ctx.send(math.sqrt((c**2) - (a**2)))

@bot.command()
async def pyBC(ctx, b: float, c: float): #given longer side and hypotenuse
    await ctx.send(ctx.message.author.mention + " the side length of A is:")
    await ctx.send(math.sqrt((c**2) - (b**2)))

#Area
@bot.command() #area of right triangle given base and height
async def areaRightTri(ctx, b: float, h: float):
    if (b < 1 or h < 1):
        await ctx.send(ctx.message.author.mention + " Error: base or height cannot be negative number or is less than 1.")
    else:
        await ctx.send(ctx.message.author.mention + " the area is:")
        await ctx.send(0.5*(b*h))

@bot.command() #area of a triangle given lengths of each sides
async def areaTri(ctx, a: float, b: float, c: float):
    if (a + b <= c or a + c <= b or b + c <= a):
        await ctx.send(ctx.message.author.mention + " Error: triangle inequality rule. Sum of any two sides must be greater than the length of the third side.")
    else:
        await ctx.send(ctx.message.author.mention + " the area is:")
        s = (a + b + c)/2 #semiperimeter
        await ctx.send(math.sqrt(s*(s-a)*(s-b)*(s-c)))

@bot.command() #area of a trapezoid given height and base 1 and base 2
async def areaTrap(ctx, h: float, b1: float, b2: float):
    if (h <= 0 or b1 <= 0 or b2 <= 0):
        await ctx.send(ctx.message.author.mention + " Error: height, base 1, or base 2 cannot be 0.")
    else:
        await ctx.send(ctx.message.author.mention + " the area is:")
        await ctx.send(((b1 + b2)/2)*h)

#Perimeter
@bot.command() #perimeter of a circle given the radius
async def periCircle(ctx, r: float):
    if (r <= 0):
        await ctx.send(ctx.message.author.mention + " Error: radius cannot be 0 or less than 0.")
    else:
        await ctx.send(ctx.message.author.mention + " the perimeter is:")
        await ctx.send(2*(math.pi)*r)

#Volume
@bot.command() #volume of a sphere given the radius
async def volSphere(ctx, r: float):
    if (r <= 0):
        await ctx.send(ctx.message.author.mention + " Error: radius cannot be 0 or less than 0.")
    else:
        await ctx.send(ctx.message.author.mention + " the volume is:")
        await ctx.send((4/3)*math.pi*(r**3))

@bot.command() #volume of a cylinder given radius and height
async def volCyl(ctx, r: float, h: float):
    if (r <= 0 or h <= 0):
        await ctx.send(ctx.message.author.mention + " Error: radius or height cannot be 0 or less than 0.")
    else:
        await ctx.send(ctx.message.author.mention + " the volume is:")
        await ctx.send(math.pi*(r**2)*h)

@bot.command() #volume of a cone given radius and height
async def volCone(ctx, r: float, h: float):
    if (r <= 0 or h <= 0):
        await ctx.send(ctx.message.author.mention + " Error: radius or height cannot be 0 or less than 0.")
    else:
        await ctx.send(ctx.message.author.mention + " the volume is:")
        await ctx.send((math.pi*(r**2)*h)/3)

@bot.command() #volume of a pyramid given base length, base width, and height
async def volPyra(ctx, bl: float, bw: float, h: float):
    if (bl <= 0 or bw <= 0 or h <= 0):
        await ctx.send(ctx.message.author.mention + " Error: base or height length cannot be 0 or less than 0.")
    else:
        await ctx.send(ctx.message.author.mention + " the volume is:")
        await ctx.send((bl*bw*h)/3)

#Cool shortcuts
@bot.command()
async def percentof(ctx, a: float, b: float):
    if (a < 0):
        await ctx.send(ctx.message.author.mention + " Error: cannot have a negative percentage.")
    else:
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
    #Basic math
    embed.add_field(name="$add X Y", value="Returns the addition of **X** and **Y**", inline=False)
    embed.add_field(name="$minus X Y", value="Returns **X** subtracted by **Y**", inline=False)
    embed.add_field(name="$mult X Y", value="Returns **X** multiplied by **Y**", inline=False)
    embed.add_field(name="$div X Y", value="Returns **X** divided by **Y**", inline=False)
    #FOIL
    embed.add_field(name="$plusplus A B C D", value="FOIL method on (**A** + **B**)(**C** + **D**) \n**Float/Whole Numbers Only**", inline=False)
    embed.add_field(name="$plusminus A B C D", value="FOIL method on (**A** + **B**)(**C** - **D**) \n**Float/Whole Numbers Only**", inline=False)
    embed.add_field(name="$minusminus A B C D", value="FOIL method on (**A** - **B**)(**C** - **D**) \n**Float/Whole Numbers Only**", inline=False)
    embed.add_field(name="$minusplus A B C D", value="FOIL method on (**A** - **B**)(**C** + **D**) \n**Float/Whole Numbers Only**", inline=False)
    #Square root, Exponents, Factorials
    embed.add_field(name="$sqrt X", value="Returns the square root of **X**", inline=False)
    embed.add_field(name="$exp X Y", value="Returns **X** to the power of **Y**", inline=False)
    embed.add_field(name="$fact X", value="Returns the factorial of **X**", inline=False)
    #Pythagorean theorem
    embed.add_field(name="$pyAB A B", value="Returns the length of hypotenuse C given length of side **A** and **B**", inline=False)
    embed.add_field(name="$pyAC A C", value="Returns the length of side B given length of side **A** and hypotenuse **C**", inline=False)
    embed.add_field(name="$pyBC B C", value="Returns the length of side A given length of side **B** and hypotenuse **C**", inline=False)
    #Area
    embed.add_field(name="$areaRightTri B H", value="Returns the area of a right triangle given base **B** and height **H**", inline=False)
    embed.add_field(name="$areaTri A B C", value="Returns the area of a triangle given side lengths **A**, **B**, and **C**", inline=False)
    embed.add_field(name="$areaTrap H B1 B2", value="Returns the area of a trapezoid given height **H** and length of base one **B1** and base two **B2**", inline=False)
    #Perimeter
    embed.add_field(name="$periCircle R", value="Returns the perimeter length of a circle given radius **R**", inline=False)
    #Volume
    embed.add_field(name="$volSphere R", value="Returns the volume of a sphere given radius **R**", inline=False)
    embed.add_field(name="$volCyl R H", value="Returns the volume of a cylinder given radius **R** and height **H**", inline=False)
    embed.add_field(name="$volCone R H", value="Returns the volume of a cone given radius **R** and height **H**", inline=False)
    embed.add_field(name="$volPyra BL BW H", value="Returns the volume of a pyramid given base length **BL**, base width **BW**, and height **H**", inline=False)
    #Cool shortcuts
    embed.add_field(name="$percentof X Y", value="Returns **X** percent of **Y**", inline=False)
    #Miscellaneous
    embed.add_field(name="$info", value="Displays information about Mathbot", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

bot.run("NDE3MDQwNDczMzE2Nzg2MTg2.DXc0Pw.rtggjKy6O0fxb2UVFLMnYlsorY8")
