import discord
from discord.ext import commands
import os
import sys
import random

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

#TXT FILES
#MOODS
with open(os.path.join(sys.path[0], "moods.txt"), "r", encoding='utf8') as txt1:
    moods = []
    for line in txt1:
        moods.append(line)

#EDBALL FUNCTIONALITY
@bot.command(brief='Ask the mysterious Edball a question...', description='Usage: -edball <question>')
async def edball(ctx, question):
    with open(os.path.join(sys.path[0], "8ball.txt"), "r", encoding='utf8') as txt3:
        eight = []
        for line in txt3:
            eight.append(line)

    if question != None:
        await ctx.send(random.choice(eight))

#POSITIVITY
@bot.command(brief='Get some positivity from Ed!', description='Usage: -positivity')
async def positivity(ctx):
    with open(os.path.join(sys.path[0], "positive.txt"), "r", encoding='utf8') as txt:
        positive = []
        for line in txt:
            positive.append(line)

    await ctx.send(random.choice(positive))

#NEGATIVITY
@bot.command(brief='Get some random negativity from Ed!', description='Usage: -negativity')
async def negativity(ctx):
    with open(os.path.join(sys.path[0], "negativity.txt"), "r", encoding='utf8') as txt4:
        negative = []
        for line in txt4:
            negative.append(line)

    await ctx.send(random.choice(negative))

#COIN FLIP
@bot.command(brief='Get Ed to flip a coin!', description='Usage: -coinflip')
async def coinflip(ctx):
    coin = random.randint(1,2)
    if coin == 1:
        await ctx.send("Heads!")
    else:
        await ctx.send("Tails!")

#ROCK PAPER SCISSORS
@bot.command(brief='Play Rock Paper Scissors with Ed!', description='Usage: -rps <choice>')
async def rps(ctx, play):
    choices = ['rock', 'paper', 'scissors']
    bot_choice = random.choice(choices)
    if play == bot_choice:
        await ctx.send(f"We both chose {play}. It's a tie!")
    elif play == "rock":
        if bot_choice == "scissors":
            await ctx.send(f"I chose {bot_choice}... you win!")
        else:
            await ctx.send(f"You chose {play}... I chose {bot_choice}... I win!")
    elif play == "scissors":
        if bot_choice == "paper":
            await ctx.send(f"You chose {play}... I chose {bot_choice}... you win!")
        else:
            await ctx.send(f"You chose {play}... I chose {bot_choice}... I win!")
            leaderboard += 1
    elif play == "paper":
        if bot_choice == "rock":
            await ctx.send(f"You chose {play}... I chose {bot_choice}... you win!")
        else:
            await ctx.send(f"You chose {play}... I chose {bot_choice}... I win!")

#THE SILVER CASE
@bot.command(brief='Spread the beginnings of Kill The Past...', description='Usage: -tsc')
async def tsc(ctx):
    await ctx.send('You mean the debut title from world-renowned developer SUDA51, available in English for the first time as of 2016?\n<https://store.steampowered.com/app/476650/The_Silver_Case/>')

#HIGURASHI
@bot.command(brief='Spread the beginnings of Hinamizawa...', description='Usage: -higurashi')
async def higurashi(ctx):
    await ctx.send('You mean Higurashi When They Cry the hit murder mystery visual novel series written and produced by Ryukishi07?\n<https://store.steampowered.com/app/310360/Higurashi_When_They_Cry_Hou__Ch1_Onikakushi/>')

#FEELING
@bot.command(brief="Ask Ed how he's feeling!", description='Usage: -feeling')
async def feeling(ctx):
    await ctx.send(random.choice(moods))


#id thing
with open(os.path.join(sys.path[0], "token.txt"), "r", encoding='utf8') as f:
    TOKEN = f.readline()

bot.run(TOKEN)