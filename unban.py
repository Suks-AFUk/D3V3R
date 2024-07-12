import discord
from discord.ext import commands

@bot.command()
async def unban(ctx, user: discord.User, reason= "No reason"):
    guild = ctx.guild
    mbed = discord.Embed(
         color=discord.Color.green(),
         title = "Unbanned:",
         description= f"{user} has succesfully been UNBANED"
         )
    mbed.add_field(name="",value=f"""
id = **{user.id}**
""", inline=True)     
    
    if commands.has_permissions(ban_members=True):
         await ctx.send(embed = mbed)
         await guild.unban(user=user)
