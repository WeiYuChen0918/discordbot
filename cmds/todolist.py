import discord
from discord.ext import commands
import json 
from core import Cog_Extension

class TodoList(Cog_Extension):
    # Initialization 
    def __init__(self, bot):
        self.todo = []
        #========== start ==========

        self.bot = bot

        #========== end ==========

        '''
        todo 是一個 list 變數
        你可以在各個function中對self.todo做操作
        來當作模擬todolist

        你可能需要用到的function 
        list : append, remove, sort
        ctx.send(str)

        '''
        
        
    # Add todolist 
    # item 是要增加的待辨事項
    @commands.command()
    async def AddTodoList(self, ctx, item):
        #========== start ==========

        self.todo.append(item)
        await ctx.send(f"新增代辦事項:{item}了~")

        # 用 append 將新代辦事項加入

        #========== end ==========
    

    # Remove todolist
    # item 是要移除的待辨事項
    @commands.command()
    async def RemoveTodoList(self, ctx, item):
        #========== start ==========
        if item in self.todo:
            self.todo.remove(item)
            await ctx.send(f"移除代辦事項:{item}了")
        else:
            await ctx.send(f"清單中找不到:{item}")

        # 用 remove 刪除項目
        # 若刪除的 item 在事項中--->傳刪除某 item 了
        # 若刪除的 item 未在清單中-->傳清單中找不到 item

        #========== end ==========     

    # Sort todolist
    @commands.command()
    async def SortTodoList(self, ctx):
        #========== start ==========

        self.todo.sort()
        # 將代辦事項清單 self.todo 進行排列
        sortedlist = "\n".join(self.todo) 
        # 將 self.todo 列表中的所有元素換行接起來
        await ctx.send(f"已排序:\n{sortedlist}")
        # 回傳"已排序"和排序後的內容

        #========== end ==========

    # Clear todolist
    @commands.command()
    async def ClearTodoList(self, ctx):
       #========== start ==========

        self.todo.clear()
        # 用clear的方式清除所有代辦事項
        await ctx.send("已清除")
        # 回傳"已清除"

       #========== end ==========

async def setup(bot):
    await bot.add_cog(TodoList(bot))