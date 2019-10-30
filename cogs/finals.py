# -*- coding: UTF-8 -*-

import discord
from discord.ext import commands
from oauth2client.service_account import ServiceAccountCredentials


def is_owner():
    def predicate(ctx):
        if ctx.author.id == 222147236728012800:
            return True
        else:
            return False
    return commands.check(predicate)





class Finals:
    """OWLETBot Match Embed Poster"""

    def __init__(self, bot):
        print("Finals Cog Deprecated.")
        self.bot = bot

    @commands.command(name='finalsEmbeds')
    @is_owner()
    async def finals_embeds(self, num):
        
        return await ctx.send("Function deprecated.")

        
# def setup(bot):
    # bot.add_cog(Finals(bot))
    # asyncio.get_event_loop().create_task(Finals(bot).match_embed_updater())
