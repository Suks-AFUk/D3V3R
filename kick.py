import discord
from discord.ext import commands

@bot.command()
async def kick(ctx, user: discord.Member, *, reason= "No reason"):
    if commands.has_permissions(kick_members=True):
        await user.kick(reason=reason)
        embed = discord.Embed(color=discord.Color.red(), title="", description="")
        embed.add_field(name="Kicked:", value=f"""
The user **{user}** has been kicked.
Reason = **{reason}**.
id = **{user.id}**
""", inline=True)
        embed.add_field(name="Este usuario se puede volver a unir, pero si se le kickea 2 veces mas, se le baneara", value="")
        await ctx.reply(embed=embed)
