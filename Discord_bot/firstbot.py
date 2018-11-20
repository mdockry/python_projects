import discord
from discord.ext import commands
import random

TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("...{} is online...".format(client.user.name))

@client.command()
async def number_generation(ctx):
    number = random.randint(1, 101)
    await ctx.send(number)

@client.command()
async def copy_cat(ctx, *args):
    await ctx.send(" ".join(args))

@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return
    if message.content.startswith('.guess'):
        await message.channel.send("I'm thinking of a number between 1-20 - can you guess it?")

        guesses = 0
        number = random.randint(1, 20)
        while guesses < 5:
            guess = await client.wait_for('message', check=None, timeout=None)

            if int(guess.content) == number:
                await message.channel.send("You are right!")
                break
            elif int(guess.content) > number:
                guesses = guesses + 1
                await message.channel.send("You're guess is to high")
                continue
            elif int(guess.content) < number:
                guesses = guesses + 1
                await message.channel.send("Your guess is to low")
                continue

        if (guess.content) != number:
            await message.channel.send("The number was {}".format(number))

    await client.process_commands(message)


client.run(TOKEN)
