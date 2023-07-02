'''
可以複製todolist的架構, 但請記得更改class & function的名稱
這個檔案的名字也可以改
'''
import discord
from discord.ext import commands
import json 
from core import Cog_Extension
import random

intents = discord.Intents.default()
intents.message_content = True

class GuessNumber(Cog_Extension):

    def init(self, bot):
        self.target_number = None
        self.max_guesses = 5
        self.guess_time = 0
        self.todo = []
        self.bot = bot

    @commands.command()
    async def play(self, ctx):
        # 指令一：
        await ctx.send("start")
        await ctx.send("歡迎來到猜數字遊戲！")
        await ctx.send("請猜數字範圍")
        self.guess_time = 0

    @commands.command()
    async def value(self, ctx, minNum, maxNum):
        # 指令二：
        min_num = int(minNum)
        max_num = int(maxNum)
        self.target_number = random.randint(min_num, max_num)
        await ctx.send(f"數字範圍為 {min_num}~{max_num}")

    @commands.command()
    async def GuessNumber(self, ctx, guess):

        guess = int(guess)
        self.guess_time = self.guess_time + 1
        if guess > self.target_number:
            await ctx.send("太大了！")
            await ctx.send("請繼續在猜一個數")
        elif guess < self.target_number:
            await ctx.send("太小了！")
            await ctx.send("請繼續在猜一個數")
        else:
            await ctx.send("恭喜！你猜對了")
            self.guess_time = 0
        if self.guess_time == self.max_guesses:
            await ctx.send(f"很可惜，你未能猜對。正確答案是 {self.target_number}")

async def setup(bot):
    await bot.add_cog(GuessNumber(bot))

