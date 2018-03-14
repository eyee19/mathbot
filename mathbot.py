#Mathbot
#Author: Everett Yee
#v2.7

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

#Angular conversion
@bot.command() #convert radians to degrees
async def degree(ctx, x: float):
    if (x <= 0):
        await ctx.send(ctx.message.author.mention + " Error: input cannot be 0 or less than 0.")
    else:
        await ctx.send(ctx.message.author.mention + " the answer is:")
        await ctx.send(math.degrees(x))

@bot.command() #convert degrees to radians
async def radian(ctx, x: float):
    if (x <= 0):
        await ctx.send(ctx.message.author.mention + " Error: input cannot be 0 or less than 0.")
    else:
        await ctx.send(ctx.message.author.mention + " the answer is:")
        await ctx.send(math.radians(x))

#Time and distance
@bot.command() #calculate MPH given feet per second
async def mph(ctx, x: float):
    if (x <= 0):
        await ctx.send(ctx.message.author.mention + " Error: input less than 0.")
    else:
        await ctx.send(ctx.message.author.mention + " the answer (in miles per hour) is:")
        await ctx.send(x*(2/3))

#Cool shortcuts
@bot.command()
async def percentof(ctx, a: float, b: float):
    if (a < 0):
        await ctx.send(ctx.message.author.mention + " Error: cannot have a negative percentage.")
    else:
        await ctx.send(ctx.message.author.mention + " the answer is:")
        await ctx.send((a*b)/100)

#Decision trees
@bot.command()
async def sEntropy(ctx, y: int, n: int): #Starting entropy for a binary variable (yes/no)
    if (y == 0 and n == 0):
        await ctx.send(ctx.message.author.mention + " Starting entropy is 0.")
    elif (y < 0 or n < 0):
        await ctx.send(ctx.message.author.mention + " Error: input cannot be negative.")
    else:
        await ctx.send(ctx.message.author.mention + " the starting entropy is:")
        total = y + n
        yes = -1*(y/total)*math.log((y/total),2)
        no = (n/total)*math.log((n/total),2)
        await ctx.send(yes-no)

#Information gain
@bot.command() #for one category of an attribute, given yes/no for the starting node, and yes/no for the category of the attribute
async def infoGain(ctx, y: int, n: int, y1: int, n1: int):
    if (y < 0 or n < 0 or y1 < 0 or n1 < 0):
        await ctx.send(ctx.message.author.mention + " Error: input cannot be negative.")
    else:
        await ctx.send(ctx.message.author.mention + " the information gain for this attribute category is:")
        total = y + n
        total1 = y1 + n1
        yes1 = -1*(y1/total1) * math.log((y1/total1),2)
        no1 = (n1/total1) * math.log((n1/total1),2)
        entropy = yes1 - no1
        infoGain = (total1/total) * entropy
        await ctx.send(infoGain)

#Data communications/networking formulas
@bot.command()
async def nyquist(ctx, bandwidth: int, signal: int): #Nyquist, for a noiseless channel given bandwidth in hertz and signal level
    if (bandwidth < 0 or signal < 0):
        await ctx.send(ctx.message.author.mention + " Error: input cannot be negative.")
    else:
        await ctx.send(ctx.message.author.mention + " the maximum data rate (in bits/second) is:")
        mdr = (2*bandwidth)*(math.log(signal,2))
        await ctx.send(mdr)

@bot.command()
async def shannon(ctx, bandwidth: int, noise: float): #Shannon, given bandwidth H and signal to noise ratio S/N
    if (bandwidth < 0 or noise < 0):
        await ctx.send(ctx.message.author.mention + " Error: input cannot be negative.")
    else:
        await ctx.send(ctx.message.author.mention + " the maximum data rate (in bits/second) is:")
        left = noise / 10.0
        sn = 10**left
        mdr = (bandwidth) * (math.log(1+sn,2))
        await ctx.send(mdr)

#Info
@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Mathbot", description="A bot that does simple math calculations and shortcuts.", color=0xeee657)
    # give users a link to invite this bot to their server
    embed.add_field(name="Invite", value="[Invite link(paste this in your browser)](https://discordapp.com/api/oauth2/authorize?client_id=417040473316786186&permissions=2048&scope=bot)")
    await ctx.send(embed=embed)

bot.remove_command("help")
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Mathbot", description="List of sections are:", color=0xeee657)

    embed.add_field(name="$basic", value="Basic math (+,-,*,/)", inline=False)
    embed.add_field(name="$foil", value="First, outer, inner, last", inline=False)
    embed.add_field(name="$power", value="Power, factorials, exponents", inline=False)
    embed.add_field(name="$pytha", value="Pythagorean theorem", inline=False)
    embed.add_field(name="$area", value="Area formulas", inline=False)
    embed.add_field(name="$peri", value="Perimeter formulas", inline=False)
    embed.add_field(name="$volume", value="Volume formulas", inline=False)
    embed.add_field(name="$angular", value="Angular conversions", inline=False)
    embed.add_field(name="$tAndD", value="Time and distance", inline=False)
    embed.add_field(name="$shortcut", value="Cool shortcuts", inline=False)
    embed.add_field(name="$tree", value="Decision trees", inline=False)
    embed.add_field(name="$network", value="Data communications/networking", inline=False)
    #Miscellaneous
    embed.add_field(name="$info", value="Displays information about Mathbot", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def basic(ctx):
    embed = discord.Embed(title="Basic math", description="Syntax: $function <parameters>", color=0xeee657)
    #Basic math
    embed.add_field(name="$add X Y", value="Returns the addition of **X** and **Y**", inline=False)
    embed.add_field(name="$minus X Y", value="Returns **X** subtracted by **Y**", inline=False)
    embed.add_field(name="$mult X Y", value="Returns **X** multiplied by **Y**", inline=False)
    embed.add_field(name="$div X Y", value="Returns **X** divided by **Y**", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def foil(ctx):
    embed = discord.Embed(title="FOIL method", description="Syntax: $function <parameters>", color=0xeee657)
    #FOIL
    embed.add_field(name="$plusplus A B C D", value="FOIL method on (**A** + **B**)(**C** + **D**) \n**Float/Whole Numbers Only**", inline=False)
    embed.add_field(name="$plusminus A B C D", value="FOIL method on (**A** + **B**)(**C** - **D**) \n**Float/Whole Numbers Only**", inline=False)
    embed.add_field(name="$minusminus A B C D", value="FOIL method on (**A** - **B**)(**C** - **D**) \n**Float/Whole Numbers Only**", inline=False)
    embed.add_field(name="$minusplus A B C D", value="FOIL method on (**A** - **B**)(**C** + **D**) \n**Float/Whole Numbers Only**", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def power(ctx):
    embed = discord.Embed(title="Square root, factorials, exponents", description="Syntax: $function <parameters>", color=0xeee657)
    #Square root, Exponents, Factorials
    embed.add_field(name="$sqrt X", value="Returns the square root of **X**", inline=False)
    embed.add_field(name="$exp X Y", value="Returns **X** to the power of **Y**", inline=False)
    embed.add_field(name="$fact X", value="Returns the factorial of **X**", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def pytha(ctx):
    embed = discord.Embed(title="Pythagorean theorem", description="Syntax: $function <parameters>", color=0xeee657)
    #Pythagorean theorem
    embed.add_field(name="$pyAB A B", value="Returns the length of hypotenuse C given length of side **A** and **B**", inline=False)
    embed.add_field(name="$pyAC A C", value="Returns the length of side B given length of side **A** and hypotenuse **C**", inline=False)
    embed.add_field(name="$pyBC B C", value="Returns the length of side A given length of side **B** and hypotenuse **C**", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def area(ctx):
    embed = discord.Embed(title="Area formulas", description="Syntax: $function <parameters>", color=0xeee657)
    #Area
    embed.add_field(name="$areaRightTri B H", value="Returns the area of a right triangle given base **B** and height **H**", inline=False)
    embed.add_field(name="$areaTri A B C", value="Returns the area of a triangle given side lengths **A**, **B**, and **C**", inline=False)
    embed.add_field(name="$areaTrap H B1 B2", value="Returns the area of a trapezoid given height **H** and length of base one **B1** and base two **B2**", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def peri(ctx):
    embed = discord.Embed(title="Perimeter formulas", description="Syntax: $function <parameters>", color=0xeee657)
    #Perimeter
    embed.add_field(name="$periCircle R", value="Returns the perimeter length of a circle given radius **R**", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def volume(ctx):
    embed = discord.Embed(title="Volume formulas", description="Syntax: $function <parameters>", color=0xeee657)
    #Volume
    embed.add_field(name="$volSphere R", value="Returns the volume of a sphere given radius **R**", inline=False)
    embed.add_field(name="$volCyl R H", value="Returns the volume of a cylinder given radius **R** and height **H**", inline=False)
    embed.add_field(name="$volCone R H", value="Returns the volume of a cone given radius **R** and height **H**", inline=False)
    embed.add_field(name="$volPyra BL BW H", value="Returns the volume of a pyramid given base length **BL**, base width **BW**, and height **H**", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def angular(ctx):
    embed = discord.Embed(title="Angular conversion", description="Syntax: $function <parameters>", color=0xeee657)
    #Angular conversion
    embed.add_field(name="$degree X", value="Converts **X** radians to degrees", inline=False)
    embed.add_field(name="$radian X", value="Converts **X** degrees to radians", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def tAndD(ctx):
    embed = discord.Embed(title="Time and distance", description="Syntax: $function <parameters>", color=0xeee657)
    #Time and distance
    embed.add_field(name="$mph X", value="Returns miles per hour given **X** feet per second", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def shortcut(ctx):
    embed = discord.Embed(title="Cool shortcuts", description="Syntax: $function <parameters>", color=0xeee657)
    #Cool shortcuts
    embed.add_field(name="$percentof X Y", value="Returns **X** percent of **Y**", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def tree(ctx):
    embed = discord.Embed(title="Decision trees", description="Syntax: $function <parameters>", color=0xeee657)
    #Decision trees
    embed.add_field(name="$sEntropy Y N", value="Returns the starting entropy given **Y** number of Yes and **N** number of No", inline=False)
    embed.add_field(name="$infoGain Y N Y1 N1", value="Returns the information gain for a specific category in an attribute given **Y** number of Yes (from starting node) and **N** number of No (from starting node), and given **Y1** number of Yes (from category) and **N1** number of No (from category)", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def network(ctx):
    embed = discord.Embed(title="Data communications/networking", description="Syntax: $function <parameters>", color=0xeee657)
    #Nyquist
    embed.add_field(name="$nyquist H V", value="Returns maximum data rate in bits/second given bandwidth **H** in hertz and signal level **V**", inline=False)
    #Shannon
    embed.add_field(name="$shannon H N", value="Returns maximum data rate in bits/second given bandwidth **H** in hertz and noise ratio **N**", inline=False)
    await ctx.send(embed=embed)

bot.run("NDE3MDQwNDczMzE2Nzg2MTg2.DXc0Pw.rtggjKy6O0fxb2UVFLMnYlsorY8")
