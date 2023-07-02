'''
可以複製todolist的架構, 但請記得更改class & function的名稱
這個檔案的名字也可以改
'''

import discord
from discord.ext import commands
import json
from core import Cog_Extension

class Cookies(Cog_Extension):
    def __init__(self, bot):
        self.buycookies = []
        # 用來記錄買餅乾的資訊
        self.bot = bot

    @commands.command()
    async def buycookies(self, ctx):
        await ctx.send("要買餅乾嗎？(yes/no)")
        # 當輸入"$buycookies"開始後，先詢問是否要買餅乾，並提示輸入內容

        try:
            msg = await ctx.bot.wait_for('message', timeout=30)
            # 給30秒的時間回覆
            if msg.content == 'yes':
            # 若回傳"是"，則接著問口味 數量...etc.
                await ctx.send("要甚麼口味？有牛奶、起司、藍藻和紫菜")
                flavor = await ctx.bot.wait_for('message', timeout=30)

                if flavor.content in ['牛奶', '起司', '藍藻', '紫菜']:
                # 判斷傳的口味是否是有提供的    
                    await ctx.send("要幾包呢？(一到四包)")
                    quantity = await ctx.bot.wait_for('message', timeout=30)
                    # 若提供了有效的口味，則詢問數量

                    if 1 <= int(quantity.content) <= 4:
                        total_price = int(quantity.content) * 5
                        # 以一包五元計算總金額
                        await ctx.send(f"總共是 {total_price} 元")
                        # 回傳總金額

                    else:
                        await ctx.send("請提供有效的數量（一到四包）")
                        # 若回傳數量不在1~4包之間，則傳送這則訊息，提示可購買數量
                else:
                    await ctx.send("請提供有效的口味（牛奶、起司、藍藻或紫菜）")
                    # 若回傳口味為提供，則傳送這則訊息，提示有提供的口味
            else:
                await ctx.send("下次需要時可以再來買")
                # 若在詢問"buycookies"時回傳"否"，則傳下次需要時可以再來買
        except TimeoutError:
            await ctx.send("操作超時，再試一次")
            # 當操作超時，告訴他操作超時，再試一次

async def setup(bot):
    await bot.add_cog(Cookies(bot))
