import discord
import random
from discord.ext import commands

class Fun:
    def __init__(self, bot):
        self.bot = bot
        
    responses = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely",
                 "You may rely on it", "As I see it, yes", "Most likely", "Outlook good",
                 "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later",
                 "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
                 "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good",
                 "Very doubtful"]

    @commands.command(aliases='8ball')
    async def eightball(self, ctx, question:str):
        num = random.randint(0, 20)
        response = responses[num]
        em = discord.Embed(color=discord.Color(value=0xff0000))
        em.title = question
        em.description = response
        await ctx.send(embed=em)
