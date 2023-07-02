import discord
from discord.ext import commands
import json 
from core import Cog_Extension
import urllib
import random



class Wordle(Cog_Extension):
    # Initialization 
    def __init__(self, bot):
        #========== start ==========

        self.bot = bot
        self.guess = 0
        # 紀錄猜的次數
        self.word_list = []

        wordleURL = "https://gist.githubusercontent.com/cfreshman/d97dbe7004522f7bc52ed2a6e22e2c04/raw/633058e11743065ad2822e1d2e6505682a01a9e6/wordle-nyt-words-14855.txt"
        # wordleURL--> 儲存網址

        url = urllib.request.urlopen(wordleURL)

        word_data = url.read().decode('utf-8')        
        # 網頁的原始碼以decode("utf-8")解碼
        # 用 read 的方式讀網址的內容
        # 讀取後的內容存在word_data中
        

        self.word_list = word_data.split('\n')
        # 以換行的方式切割

        #========== end ==========
        
        '''
        要在init function 中載入單字庫

        Hint:
        1. 好像有import urllib
        2. data.json中有貼上url了
        '''
    
    @commands.command()
    async def Play(self, ctx):
        #========== start ==========

        self.default_answer = random.choice(self.word_list)
        await ctx.send("隨機選一個單字為答案了")

        #========== end ==========
        '''
        TODO 
        要在爬好的單字庫中, 隨機挑選一個單字做為預設的答案
        '''
    

    
    @commands.command()
    async def Ask(self, ctx, ans):

        '''
        ans 是使用者傳入的猜測答案

        TODO
        1. 沒有play直接ask : 請先輸入 Play 指令
        2. 不是5個字的單字 : 請輸入5個字母的單字
        3. 不是單字的英文組合(不在單字庫中) : 這好像不是個單字
        4. 答對 : 恭喜答對!!!
        5. 猜太多次了 : 真可惜, 答案是{answer}
        '''
        self.guess += 1
        response = ""
        
        if not hasattr(self, 'default_answer'): 
            # 檢查設定 default_answer了嗎
            await ctx.send("請先輸入 Play 指令")
            # 若還未有 default_answer 則代表尚未輸入Play指令，所以告訴他先輸入Play

        if len(ans) != 5:
            await ctx.send("請輸入5個字母的單字") 

        if ans.lower() not in self.word_list:
            await ctx.send("這好像不是個單字")
            # 如果傳的單字並不在 self.word_list 裡面，就告訴他這好像不是個單字


        if ans.lower() == self.default_answer:
            await ctx.send("恭喜答對!!!")
            # 如果完全和 self.default_answer 一樣，傳"恭喜答對!!!"
        
        else:
        # 輸入符合要求時    
            for i in range(5):
            # 開始對輸入進行比對    
                if ans[i] == self.default_answer[i]:
                    response += ans[i].upper()
                    # 相同位置的字母相同-->大寫且加到 response
                    

                elif ans[i] in self.default_answer:
                    response += ans[i].lower()
                    # 位置不同-->小寫且加到 response

                else:
                    response += "#"
                    # 都不是
            await ctx.send(response)
            if(self.guess >= 6):
                await ctx.send(f"真可惜, 答案是{self.default_answer}")
                # 猜超過6次時，直接傳送答案

        #========== end ==========    
        

async def setup(bot):
    await bot.add_cog(Wordle(bot))