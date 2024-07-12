import discord
from discord.ext import commands

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason= "No reason",):
    try:
        await user.ban(reason=reason)
        embed = discord.Embed(color=discord.Color.red(), title="", description="")
        embed.add_field(name="Banned:", value=f"""
The user **{user}** has been banned.
Reason = **{reason}**
id = **{user.id}**
""", inline=True)
        await ctx.reply(embed=embed)
    except:
            embed = discord.Embed(color=discord.Color.red(), title="", description="")
            embed.add_field(name="Banned:", value=f"""
Error 
""", inline=True)
            await ctx.reply(embed=embed)
