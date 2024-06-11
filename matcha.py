from unicodedata import category
import discord
import random 
from discord.ext import commands
from typing import Optional

from discord.utils import MISSING
import requests
import utils 
 
guildid = 706403459661955104 #706403459661955104 build a boat, 706403459661955104 = matcha shop
bot = commands.Bot(command_prefix=',', intents=discord.Intents.all())
channel = 1249031124873642005 #1243213659883311206 build a boat, 1248794448943386685 = matcha queue

@bot.event
async def on_ready():
    print("All oiled up for you daddy <3 UwU")

class vee(discord.ui.View):
    def __init__(self):
        super().__init__()

        # Adds the dropdown to our view object.
        self.add_item(OrderDropdown())

    async def summonDC(self, interaction:discord.Interaction, choice1):
        self.children[0].disabled= True
        self.add_item(DCview())
        await interaction.message.edit(view=self)
        await interaction.response.defer()

    async def NitroBasic(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(NitroBasic())

    async def NitroBoostm(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(NitroBoostm())

    async def NitroBoosty(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(NitroBoosty())

    async def AA(self, interaction:discord.Interaction, choice):
        self.children[0].disabled= True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(AA())

    async def SM(self, interaction:discord.Interaction, choice):
        self.children[0].disabled= True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(SM())
    
    async def Minecraft(self, interaction:discord.Interaction, choice2):
        self.ORDER1 = choice2
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(Minecraft())

    async def Netflix(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(Netflix())

    async def Sonyliv(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(Sonyliv())

    async def Crunchyroll(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(Crunchyroll())

    async def spotify(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(Spotify())

    async def youtube(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(Youtube())

    async def Prime(self, interaction:discord.Interaction, choice2):
        self.ORDER1 = choice2
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(Prime())

    async def SBINSTA(self, interaction:discord.Interaction, choice2):
        self.ORDER1 = choice2
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(SBINSTA())

    async def SBYT(self, interaction:discord.Interaction, choice2):
        self.ORDER1 = choice2
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(SBYT())

    async def SBTIKTOK(self, interaction:discord.Interaction, choice2):
        self.ORDER1 = choice2
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(SBTIKTOK())

    async def SBTWITCH(self, interaction:discord.Interaction, choice2):
        self.ORDER1 = choice2
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(SBTWITCH())

    async def SBTWITTER(self, interaction:discord.Interaction, choice2):
        self.ORDER1 = choice2
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(SBTWITTER())

    async def SBTELEGRAM(self, interaction:discord.Interaction, choice2):
        self.ORDER1 = choice2
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(SBTELEGRAM())

    async def Robux(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(Robux())

    async def Vbucks(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(Vbucks())

    async def SG(self, interaction:discord.Interaction, choice2):
        self.children[0].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(SG())

    async def PDmod(self, interaction:discord.Interaction, choice2):
        self.children[0].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(PDmod())

    async def OTHER(self, interaction:discord.Interaction, choice2):
        self.ORDER2 = choice2
        self.children[0].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(OTHER())

    async def ServerBoosts(self, interaction:discord.Interaction, choice2):
        self.children[0].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(ServerBoost())

    async def summonTV(self, interaction:discord.Interaction, choice1):
        self.children[0].disabled= True
        self.add_item(TVview())
        await interaction.message.edit(view=self)
        await interaction.response.defer() 

    async def summonGC(self, interaction:discord.Interaction, choice1):
        self.children[0].disabled= True
        self.add_item(GCview())
        await interaction.message.edit(view=self)
        await interaction.response.defer()

    async def summonSB(self, interaction:discord.Interaction, choice1):
        self.children[0].disabled= True
        self.add_item(SBview())
        await interaction.message.edit(view=self)
        await interaction.response.defer() 

    async def ESM(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled= True
        await interaction.message.edit(view=self)
        self.stop()

class sec(discord.ui.View):
    def __init__(self):
        super().__init__()

        # Adds the dropdown to our view object.
        self.add_item(OrderDropdown())

    async def summonDC(self, interaction:discord.Interaction, choice1):
        self.children[0].disabled= True
        self.add_item(DCview())
        await interaction.message.edit(view=self)
        await interaction.response.defer()

    async def NitroBasic(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(NitroBasic())

    async def NitroBoostm(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(NitroBoostm())

    async def NitroBoosty(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(NitroBoosty())

    async def AA(self, interaction:discord.Interaction, choice):
        self.children[0].disabled= True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(AA())

    async def SM(self, interaction:discord.Interaction, choice):
        self.children[0].disabled= True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(SM())
    
    async def Minecraft(self, interaction:discord.Interaction, choice2):
        self.ORDER1 = choice2
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(Minecraft())

    async def Netflix(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(Netflix())

    async def Sonyliv(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(Sonyliv())

    async def Crunchyroll(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(Crunchyroll())

    async def spotify(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(Spotify())

    async def youtube(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(Youtube())

    async def Prime(self, interaction:discord.Interaction, choice2):
        self.ORDER1 = choice2
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(Prime())

    async def SBINSTA(self, interaction:discord.Interaction, choice2):
        self.ORDER1 = choice2
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(SBINSTA())

    async def SBYT(self, interaction:discord.Interaction, choice2):
        self.ORDER1 = choice2
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(SBYT())

    async def SBTIKTOK(self, interaction:discord.Interaction, choice2):
        self.ORDER1 = choice2
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(SBTIKTOK())

    async def SBTWITCH(self, interaction:discord.Interaction, choice2):
        self.ORDER1 = choice2
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(SBTWITCH())

    async def SBTWITTER(self, interaction:discord.Interaction, choice2):
        self.ORDER1 = choice2
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(SBTWITTER())

    async def SBTELEGRAM(self, interaction:discord.Interaction, choice2):
        self.ORDER1 = choice2
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(SBTELEGRAM())

    async def Robux(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(Robux())

    async def Vbucks(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(Vbucks())

    async def SG(self, interaction:discord.Interaction, choice2):
        self.children[0].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(SG())

    async def PDmod(self, interaction:discord.Interaction, choice2):
        self.children[0].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(PDmod())

    async def OTHER(self, interaction:discord.Interaction, choice2):
        self.ORDER2 = choice2
        self.children[0].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(OTHER())

    async def ServerBoosts(self, interaction:discord.Interaction, choice2):
        self.children[0].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(ServerBoost())

    async def summonTV(self, interaction:discord.Interaction, choice1):
        self.children[0].disabled= True
        self.add_item(TVview())
        await interaction.message.edit(view=self)
        await interaction.response.defer() 

    async def summonGC(self, interaction:discord.Interaction, choice1):
        self.children[0].disabled= True
        self.add_item(GCview())
        await interaction.message.edit(view=self)
        await interaction.response.defer()

    async def summonSB(self, interaction:discord.Interaction, choice1):
        self.children[0].disabled= True
        self.add_item(SBview())
        await interaction.message.edit(view=self)
        await interaction.response.defer() 

    async def ESM(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled= True
        await interaction.message.edit(view=self)
        self.stop()

class AA(discord.ui.Modal, title = "Order placement"):  #reworked

    Age = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How old do you want the account to be?",
        required=True,
        placeholder="We offer accounts from 2022 and from 2020 to 2016")

    Qty = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How many accounts??",
        required=True,
        placeholder="Two, for me and my friend....."
    )

    Pmt = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How would you like to pay?",
        required=True,
        placeholder="Paypal Balance, Crypto, UPI......"
    )

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=(f"Would like to buy Aged Account <a:m_kerohi:1221301733658198046>"),
            color=discord.Color.green()
        )
        embed.set_author(name=interaction.user)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Account Age:** {self.Age.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Number of accounts:** {self.Qty.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Payment Via:** {self.Pmt.value}", value=(f''), inline=False)
        embed.set_footer(text="✅- Confirm ❌- Cancel ")
        await interaction.response.send_message(embed=embed)

class SM(discord.ui.Modal, title = "Server Members"):   #reworked

    Status = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Botted or real members?",
        required=True,
        placeholder="Botted but always online, or real via paid invites...."
    )

    Qty = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How many members?",
        required=True,
        placeholder="200"
    )

    Pmt = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How would you like to pay?",
        required=True,
        placeholder="Paypal Balance, Crypto, UPI......"
    )

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=(f"Would like to buy Server members <a:excla:1221291701616775330>"),
            color=discord.Color.green()
        )
        embed.set_author(name=interaction.user)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Member status:** {self.Status.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Number of members:** {self.Qty.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Payment Via:** {self.Pmt.value}", value=(f''), inline=False)
        embed.set_footer(text="✅- Confirm ❌- Cancel")
        await interaction.response.send_message(embed=embed)
    
class SG(discord.ui.Modal, title = "Steam game"):  #reworked

    Game = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Which steam game would you like to purchase?",
        required=True,
        placeholder="We have most offline steam games, as well as GTA online"
    )

    Copies = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How many copies would you like?",
        required=True,
        placeholder="Two, one for me and my friend"
    )

    Pmt = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How would you like to pay?",
        required=True,
        placeholder="Paypal Balance, Crypto, UPI......"
    )

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=(f"Would like to buy Steam game <a:excla:1221291701616775330>"),
            color=discord.Color.green()
        )
        embed.set_author(name=interaction.user)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Game name:** {self.Game.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Copies:** {self.Copies.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Payment Via:** {self.Pmt.value}", value=(f''), inline=False)
        embed.set_footer(text="✅- Confirm ❌- Cancel")
        await interaction.response.send_message(embed=embed)

class Robux(discord.ui.Modal, title = "Creds"):  #reworked

    Qty = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How many would you like to purchase?",
        required=True,
        placeholder="Enter number of creds...."
    )

    Pmt = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How would you like to pay?",
        required=True,
        placeholder="Paypal Balance, Crypto, UPI......"
    )

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=(f"Would like to buy Robux <a:excla:1221291701616775330>"),
            color=discord.Color.green()
        )
        embed.set_author(name=interaction.user)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Quantity:** {self.Qty.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Payment Via:** {self.Pmt.value}", value=(f''), inline=False)
        embed.set_footer(text="✅- Confirm ❌- Cancel")
        await interaction.response.send_message(embed=embed)

class Vbucks(discord.ui.Modal, title = "Creds"):  #reworked

    Qty = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How many would you like to purchase?",
        required=True,
        placeholder="Enter number of creds...."
    )

    Pmt = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How would you like to pay?",
        required=True,
        placeholder="Paypal Balance, Crypto, UPI......"
    )

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=(f"Would like to buy Vbucks <a:excla:1221291701616775330>"),
            color=discord.Color.green()
        )
        embed.set_author(name=interaction.user)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Quantity:** {self.Qty.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Payment Via:** {self.Pmt.value}", value=(f''), inline=False)
        embed.set_footer(text="✅- Confirm ❌- Cancel")
        await interaction.response.send_message(embed=embed)

class Minecraft(discord.ui.Modal, title = "Order placement"): #reworked

    Qty = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How many accounts would you like to buy?",
        required=True,
        placeholder="Two, for me and my friend....."
    )

    Pmt = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How would you like to pay?",
        required=True,
        placeholder="Paypal Balance, Crypto, UPI......"
    )

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=(f"Would like to buy Minecraft Account <a:excla:1221291701616775330>"),
            color=discord.Color.green()
        )
        embed.set_author(name=interaction.user)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Quantity:** {self.Qty.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Payment Via:** {self.Pmt.value}", value=(f''), inline=False)
        embed.set_footer(text="✅- Confirm ❌- Cancel")
        await interaction.response.send_message(embed=embed)

class PDmod(discord.ui.Modal, title = 'Profile decoration'):#reworked

    PD = discord.ui.TextInput(
        style=discord.TextStyle.long,
        label="Which decoration would you like to buy?",
        required=True,
        max_length=500,
        placeholder="We have Feelin' Retro, Pirates, Galaxy, Lofi Vibes, Anime, Elements, Cyberpunk, Fantasy, Springtoons, and Arcade!"
    )

    Qty = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="What Quantity?",
        required=True,
        placeholder="Two, for me and my friend....."
    )

    Pmt = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How would you like to pay?",
        required=True,
        placeholder="Paypal Balance, Crypto, UPI......"
    )

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=(f"Would like to buy Profile Deco <a:excla:1221291701616775330>"),
            color=discord.Color.green()
        )
        embed.set_author(name=f"{interaction.user}")
        embed.add_field(name=f"<a:m_greenstar:123008378719297566> **Decoration:** {self.PD.value}", value=(f" "), inline= False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Quantity:** {self.Qty.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Payment Via:** {self.Pmt.value}", value=(f''), inline=False)
        embed.set_footer(text="✅- Confirm ❌- Cancel")
        await interaction.response.send_message(embed=embed)

class NitroBasic(discord.ui.Modal, title = "Order placement"):#reworked

    Qty = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="What Quantity?",
        required=True,
        placeholder="Two, for me and my friend....."
    )

    Pmt = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How would you like to pay?",
        required=True,
        placeholder="Paypal Balance, Crypto, UPI......"
    )

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=(f"Would like to buy Nitro Basic  <a:nitro_basic:1231178872649945148>"),
            color=discord.Color.green()
        )
        embed.set_author(name=interaction.user)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Quantity:** {self.Qty.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Payment Via:** {self.Pmt.value}", value=(f''), inline=False)
        embed.set_footer(text="✅- Confirm ❌- Cancel")
        await interaction.response.send_message(embed=embed)

class NitroBoostm(discord.ui.Modal, title = "Order placement"):#reworked

    Qty = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="What Quantity?",
        required=True,
        placeholder="Two, for me and my friend....."
    )

    Pmt = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How would you like to pay?",
        required=True,
        placeholder="Paypal Balance, Crypto, UPI......"
    )

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=(f"Would like to buy Nitro Boost (monthly)  <a:Nitro:1231178853742022677>"),
            color=discord.Color.green()
        )
        embed.set_author(name=interaction.user)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Quantity:** {self.Qty.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Payment Via:** {self.Pmt.value}", value=(f''), inline=False)
        embed.set_footer(text="✅- Confirm ❌- Cancel")
        await interaction.response.send_message(embed=embed)

class NitroBoosty(discord.ui.Modal, title = "Order placement"):#reworked

    Qty = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="What Quantity?",
        required=True,
        placeholder="Two, for me and my friend....."
    )

    Pmt = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How would you like to pay?",
        required=True,
        placeholder="Paypal Balance, Crypto, UPI......"
    )

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=(f"Would like to buy Nitro Boost (yearly)  <a:Nitro:1231178853742022677>"),
            color=discord.Color.green()
        )
        embed.set_author(name=interaction.user)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Quantity:** {self.Qty.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Payment Via:** {self.Pmt.value}", value=(f''), inline=False)
        embed.set_footer(text="✅- Confirm ❌- Cancel")
        await interaction.response.send_message(embed=embed)

class ServerBoost(discord.ui.Modal, title = "Order placement"):#reworked

    Duration = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Num of months",
        required=True,
        placeholder="Available packs = 1m / 3m"
    )

    Quantity = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Number of boosts",
        required=True,
        placeholder="Available packs = 4x / 8x / 14x"
    )

    Pmt = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How would you like to pay?",
        required=True,
        placeholder="Paypal Balance, Crypto, UPI......"
    )

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=(f"Would like to buy Server boosting <a:excla:1221291701616775330>"),
            color=discord.Color.green()
        )
        embed.set_author(name=interaction.user)

        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Numeber of Months:** {self.Duration.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Number of Boosts:** {self.Quantity.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Payment Via:** {self.Pmt.value}", value=(f''), inline=False)
        embed.set_footer(text="✅- Confirm ❌- Cancel")
        await interaction.response.send_message(embed=embed)

class Netflix(discord.ui.Modal, title = "Order placement"):#reworked


    Dur = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Which package? 1m/ 3m/ 6m/ 1y available!",
        required=True,
        placeholder="Enter package...."
    )

    Qty = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="What Quantity?",
        required=True,
        placeholder="Two, for me and my friend....."
    )

    Pmt = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How would you like to pay?",
        required=True,
        placeholder="Paypal Balance, Crypto, UPI......"
    )

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=(f"Would like to buy Netflix <a:excla:1221291701616775330>"),
            color=discord.Color.green()
        )
        embed.set_author(name=interaction.user)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Duration** {self.Dur.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Quantity:** {self.Qty.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Payment Via:** {self.Pmt.value}", value=(f''), inline=False)
        embed.set_footer(text="✅- Confirm ❌- Cancel")
        await interaction.response.send_message(embed=embed)

class Youtube(discord.ui.Modal, title = "Order placement"):#reworked


    Dur = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Which package? 2m/ 6m/ 1y available!",
        required=True,
        placeholder="Enter package...."
    )

    Qty = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="What Quantity?",
        required=True,
        placeholder="Two, for me and my friend....."
    )

    Pmt = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How would you like to pay?",
        required=True,
        placeholder="Paypal Balance, Crypto, UPI......"
    )

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=(f"Would like to buy Youtube Premium <a:excla:1221291701616775330>"),
            color=discord.Color.green()
        )
        embed.set_author(name=interaction.user)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Package Duration:** {self.Dur.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Quantity:** {self.Qty.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Payment Via:** {self.Pmt.value}", value=(f''), inline=False)
        embed.set_footer(text="✅- Confirm ❌- Cancel")
        await interaction.response.send_message(embed=embed)

class Spotify(discord.ui.Modal, title = "Order placement"):#reworked

    Dur = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Which package? 2m/ 6m/ 1y available!",
        required=True,
        placeholder="Enter package...."
    )

    Qty = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="What Quantity?",
        required=True,
        placeholder="Two, for me and my friend....."
    )

    Pmt = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How would you like to pay?",
        required=True,
        placeholder="Paypal Balance, Crypto, UPI......"
    )

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=(f"Would like to buy Spotify Premium <a:excla:1221291701616775330>"),
            color=discord.Color.green()
        )
        embed.set_author(name=interaction.user)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Package Duration:** {self.Dur.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Quantity:** {self.Qty.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Payment Via:** {self.Pmt.value}", value=(f''), inline=False)
        embed.set_footer(text="✅- Confirm ❌- Cancel")
        await interaction.response.send_message(embed=embed)

class Sonyliv(discord.ui.Modal, title = "Order placement"):#reworked


    Dur = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Which package? 1m/ 1y available!",
        required=True,
        placeholder="Enter package...."
    )

    Qty = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="What Quantity?",
        required=True,
        placeholder="Two, for me and my friend....."
    )

    Pmt = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How would you like to pay?",
        required=True,
        placeholder="Paypal Balance, Crypto, UPI......"
    )

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=(f"Would like to buy Sonyliv <a:excla:1221291701616775330>"),
            color=discord.Color.green()
        )
        embed.set_author(name=interaction.user)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Package Duration:** {self.Dur.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Quantity:** {self.Qty.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Payment Via:** {self.Pmt.value}", value=(f''), inline=False)
        embed.set_footer(text="✅- Confirm ❌- Cancel")
        await interaction.response.send_message(embed=embed)

class Crunchyroll(discord.ui.Modal, title = "Order placement"):#reworked


    Dur = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Which package? 1m/ 1y available!",
        required=True,
        placeholder="Enter package...."
    )

    Qty = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="What Quantity?",
        required=True,
        placeholder="Two, for me and my friend....."
    )

    Pmt = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How would you like to pay?",
        required=True,
        placeholder="Paypal Balance, Crypto, UPI......"
    )

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=(f"Would like to buy Crunchyroll <a:excla:1221291701616775330>"),
            color=discord.Color.green()
        )
        embed.set_author(name=interaction.user)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Package Duration:** {self.Dur.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Quantity:** {self.Qty.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Payment Via:** {self.Pmt.value}", value=(f''), inline=False)
        embed.set_footer(text="✅- Confirm ❌- Cancel")
        await interaction.response.send_message(embed=embed)

class Prime(discord.ui.Modal, title = "Order placement"):#reworked


    Dur = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Which package? 6m/ 1y available!",
        required=True,
        placeholder="Enter package...."
    )

    Qty = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="What Quantity?",
        required=True,
        placeholder="Two, for me and my friend....."
    )

    Pmt = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How would you like to pay?",
        required=True,
        placeholder="Paypal Balance, Crypto, UPI......"
    )

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=(f"Would like to buy Prime <a:excla:1221291701616775330>"),
            color=discord.Color.green()
        )
        embed.set_author(name=interaction.user)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Package Duration:** {self.Dur.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Quantity:** {self.Qty.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Payment Via:** {self.Pmt.value}", value=(f''), inline=False)
        embed.set_footer(text="✅- Confirm ❌- Cancel")
        await interaction.response.send_message(embed=embed)

class SBINSTA(discord.ui.Modal, title = "Order placement"):#reworked


    Followers = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How many followers? (optional)",
        required=False,
        placeholder="Available packs = 1k, 2.5k, 5k, 10k or 20k"
    )

    Likes = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How many likes? (optional) ",
        required=False,
        placeholder="Available packs = 1k, 5k, 10k, 20k, 50k, 100k"
    )

    Pmt = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How would you like to pay?",
        required=True,
        placeholder="Paypal Balance, Crypto, UPI......"
    )

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=(f"Would like to buy Insta boost <a:excla:1221291701616775330>"),
            color=discord.Color.green()
        )
        embed.set_author(name=interaction.user)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Followers:** {self.Followers.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Likes:** {self.Likes.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Payment Via:** {self.Pmt.value}", value=(f''), inline=False)
        embed.set_footer(text="✅- Confirm ❌- Cancel")
        await interaction.response.send_message(embed=embed)

class SBYT(discord.ui.Modal, title = "Order placement"):#reworked

    Subscribers = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How many followers? (optional)",
        required=False,
        placeholder="Available packs = 500, 1k, 2.5k, 5k, 10k"
    )

    Views = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How many Views? (optional) ",
        required=False,
        placeholder="Available packs = 1k, 5k, 7,5k, 20k"
    )

    Pmt = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How would you like to pay?",
        required=True,
        placeholder="Paypal Balance, Crypto, UPI......"
    )

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=(f"Would like to buy Youtube boost <a:excla:1221291701616775330>"),
            color=discord.Color.green()
        )
        embed.set_author(name=interaction.user)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Subscribers:** {self.Subscribers.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Views:** {self.Views.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Payment Via:** {self.Pmt.value}", value=(f''), inline=False)
        embed.set_footer(text="✅- Confirm ❌- Cancel")
        await interaction.response.send_message(embed=embed)

class SBTIKTOK(discord.ui.Modal, title = "Order placement"):#reworked

    
    Followers = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How many followers? (optional)",
        required=False,
        placeholder="Available packs = 500, 1k, 2.5k, 5k, 10k"
    )

    Views = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How many Views? (optional) ",
        required=False,
        placeholder="Available packs = 1k, 5k, 7,5k, 20k"
    )

    Likes = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How many Likes (optional) ",
        required=False,
        placeholder="Available packs = 1k, 5k, 7,5k, 20k"
    )


    Pmt = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How would you like to pay?",
        required=True,
        placeholder="Paypal Balance, Crypto, UPI......"
    )

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=(f"Would like to buy Tiktok boost <a:excla:1221291701616775330>"),
            color=discord.Color.green()
        )
        embed.set_author(name=interaction.user)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Followers:** {self.Followers.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Likes:** {self.Likes.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Views:** {self.Views.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Payment Via:** {self.Pmt.value}", value=(f''), inline=False)
        embed.set_footer(text="✅- Confirm ❌- Cancel")
        await interaction.response.send_message(embed=embed)

class SBTWITTER(discord.ui.Modal, title = "Order placement"):#reworked

    Followers = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How many followers? (optional)",
        required=False,
        placeholder="Available packs = 500, 1k, 2k, 5k, 10k"
    )

    Likes = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How many likes? (optional) ",
        required=False,
        placeholder="Available packs = 1k, 2.5k, 7.5k, 15k, 50k,"
    )

    Retweet = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How many Retweets? (optional) ",
        required=False,
        placeholder="Available packs = 1k, 2k, 3k, 4k, 5k"
    )

    Pmt = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How would you like to pay?",
        required=True,
        placeholder="Paypal Balance, Crypto, UPI......"
    )

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=(f"Would like to buy Twitter boost <a:excla:1221291701616775330>"),
            color=discord.Color.green()
        )
        embed.set_author(name=interaction.user)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Followers:** {self.Followers.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Likes:** {self.Likes.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Retweets:** {self.Retweet.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Payment Via:** {self.Pmt.value}", value=(f''), inline=False)
        embed.set_footer(text="✅- Confirm ❌- Cancel")
        await interaction.response.send_message(embed=embed)

class SBTWITCH(discord.ui.Modal, title = "Order placement"):#reworked


    Followers = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How many followers?",
        required=True,
        placeholder="Available packs = 1k, 2k, 3k, 4k, 5k"
    )

    Pmt = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How would you like to pay?",
        required=True,
        placeholder="Paypal Balance, Crypto, UPI......"
    )

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=(f"Would like to buy Twitch boost <a:excla:1221291701616775330>"),
            color=discord.Color.green()
        )
        embed.set_author(name=interaction.user)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Followers:** {self.Followers.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Payment Via:** {self.Pmt.value}", value=(f''), inline=False)
        embed.set_footer(text="✅- Confirm ❌- Cancel")
        embed.set_footer(text="✅- Confirm ❌- Cancel")
        await interaction.response.send_message(embed=embed)

class SBTELEGRAM(discord.ui.Modal, title = "Order placement"):#reworked

    Members = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How many members? (optional)",
        required=False,
        placeholder="Available packs = 500, 1k, 2k, 5k, 10k"
    )

    Views = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How many Views? (optional)",
        required=False,
        placeholder="Available packs = 1k, 10k, 100k, 1,000,000 , 10,000,000"
    )

    Pmt = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How would you like to pay?",
        required=True,
        placeholder="Paypal Balance, Crypto, UPI......"
    )

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=(f"Would like to buy Telegram boost <a:excla:1221291701616775330>"),
            color=discord.Color.green()
        )
        embed.set_author(name=interaction.user)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Members:** {self.Members.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Views:** {self.Views.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Payment Via:** {self.Pmt.value}", value=(f''), inline=False)
        embed.set_footer(text="✅- Confirm ❌- Cancel")
        await interaction.response.send_message(embed=embed)

class OTHER(discord.ui.Modal, title = "Order placement"):#reworked

    Name = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="What are you looking for?",
        required=True,
        placeholder="Short description with name"
    )

    Description = discord.ui.TextInput(
        style=discord.TextStyle.long,
        max_length=500,
        label="Elaborate a little if necessary",
        required=False,
        placeholder="Optional, Enter specifics (duration, views etc) here"
    )

    Pmt = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How would you like to pay?",
        required=True,
        placeholder="Paypal Balance, Crypto, UPI......"
    )

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=(f"Would like to place a custom order <a:excla:1221291701616775330>"),
            color=discord.Color.green()
        )
        embed.set_author(name=interaction.user)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Name of product:** {self.Name.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Descrption:** {self.Description.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Payment Via:** {self.Pmt.value}", value=(f''), inline=False)
        embed.set_footer(text="✅- Confirm ❌- Cancel")
        await interaction.response.send_message(embed=embed)

class GCview(discord.ui.Select): #resolved
    def __init__(self):
        options = [
            discord.SelectOption(label='Robux', emoji='<:m_robux:1231178907865317417>', value='Robux'),
            discord.SelectOption(label='Vbucks', emoji='<:vbucks:1239621148036038749>', value='Vbucks')
        ]
        super().__init__(options=options, placeholder="Buy game creds at a heavy discount!", max_values=1, min_values=1)
    
    async def callback(self, interaction:discord.Interaction):
        if self.values[0] == 'Robux':
            await self.view.Robux(interaction,self.values) # custom game credits modal
        elif self.values[0] == 'Vbucks':
            await self.view.Vbucks(interaction,self.values) # same
        await self.view.ESM(interaction,self.values)

class GAMview(discord.ui.Select): #not in function rn
    def __init__(self):
        options = [
            discord.SelectOption(label='Minecraft(java) account!', value='Minecraft acc'),
            discord.SelectOption(label='Steam Games!', value='Steam game')
        ]
        super().__init__(options=options, placeholder="Buy a game or account at heavy discount!", max_values=1, min_values=1)
    
    async def callback(self, interaction:discord.Interaction):
        if self.values[0] == 'Minecraft acc':
            await self.view.QtyPay(interaction,self.values)
        elif self.values[0] == 'Steam game':
            await self.view.SG(interaction,self.values)
        await self.view.ESM(interaction,self.values)

class TVview(discord.ui.Select): #resolved
    def __init__(self):
        options = [
            discord.SelectOption(label='Netflix', emoji='<:77927netflixblack:1239509363568414740>', value='Netflx'),
            discord.SelectOption(label='Spotify Premium', emoji='<:35773spotify:1239509347076411464>', value='Spotify premium'),
            discord.SelectOption(label='Youtube Premium', emoji='<:12899youtube:1239509336334667806>', value='Youtube premium'),
            discord.SelectOption(label='Sony Liv', emoji='<:sony:1239601618379341826>', value='Sony liv'),
            discord.SelectOption(label='Minecraft', emoji='<:Minecraft:906531805639872512>', value='Minecraft'),
            discord.SelectOption(label='Crunchyroll', emoji='<a:C_animevibe:921257006105493585>', value='Crunchyroll'),
            discord.SelectOption(label='Prime Video', emoji='<:26439amazonprime:1239509341900374067>', value='Prime Video')  
        ]
        super().__init__(options=options, placeholder="What subscription?", max_values=1, min_values=1)
    
    async def callback(self, interaction:discord.Interaction):
        if self.values[0] == 'Netflx':
            await self.view.Netflix(interaction,self.values)
        elif self.values[0] == 'Spotify premium':
            await self.view.spotify(interaction,self.values)
        elif self.values[0] == 'Youtube premium':
            await self.view.youtube(interaction,self.values)
        elif self.values[0] == 'Sony liv':
            await self.view.Sonyliv(interaction,self.values)
        elif self.values[0] == 'Minecraft':
            await self.view.Minecraft(interaction,self.values)
        elif self.values[0] == 'Crunchyroll':
            await self.view.Crunchyroll(interaction,self.values)
        elif self.values[0] == 'Prime Video':
            await self.view.Prime(interaction,self.values)
        await self.view.ESM(interaction,self.values)

class SBview(discord.ui.Select): #resolved
    def __init__(self):
        options = [
            discord.SelectOption(label='Instagram',emoji='<:98820instagram:1239509369192714291>', value='Instagram boost'),
            discord.SelectOption(label='Youtube',emoji='<:12899youtube:1239509336334667806>', value='Youtube boost'),
            discord.SelectOption(label='Tiktok',emoji='<:45751tiktok:1239509352100925510>', value='Tiktok boost'),
            discord.SelectOption(label='Twitter',emoji='<:12994twitter:1239509338532479068>', value='Twitter boost'),
            discord.SelectOption(label='Twitch',emoji='<:77281twitch:1239509360871215154>', value='Twitch boost'),
            discord.SelectOption(label='Telegram',emoji='<:47647telegram:1239509358052769812>', value='Telegram Boost')
        ]
        super().__init__(options=options, placeholder="Which social boost?", max_values=1, min_values=1)
    
    async def callback(self, interaction:discord.Interaction):
        if self.values[0] == 'Instagram boost':
            await self.view.SBINSTA(interaction,self.values)
        elif self.values[0] == 'Youtube boost':
            await self.view.SBYT(interaction,self.values)
        elif self.values[0] == 'Tiktok boost':
            await self.view.SBTIKTOK(interaction,self.values)
        elif self.values[0] == 'Twitter boost':
            await self.view.SBTWITTER(interaction,self.values)
        elif self.values[0] == 'Twitch boost':
            await self.view.SBTWITCH(interaction,self.values)
        elif self.values[0] == 'Telegram Boost':
            await self.view.SBTELEGRAM(interaction,self.values)
        await self.view.ESM(interaction,self.values)

class DCview(discord.ui.Select):    #resolved
    def __init__(self):
        options = [
            discord.SelectOption(label='Nitro basic!', emoji='<a:nitro_basic:1231178872649945148>', value='Nitro basic'),
            discord.SelectOption(label='Nitro Boost! (monthly)', emoji='<a:Nitro:1231178853742022677>', value='Nitro boost (m)'),
            discord.SelectOption(label='Nitro Boost! (yearly)', emoji='<a:Nitro:1231178853742022677>', value='Nitro boost (y)')
        ]
        super().__init__(options=options, placeholder="Which Nitro subscription would you like?", max_values=1, min_values=1)
    
    async def callback(self, interaction:discord.Interaction):
        DCORDER = self.values[0]
        if self.values[0] == 'Nitro basic':
            await self.view.NitroBasic(interaction,self.values)
        elif self.values[0] == 'Nitro boost (m)':
            await self.view.NitroBoostm(interaction,self.values)
        elif self.values[0] == 'Nitro boost (y)':
            await self.view.NitroBoosty(interaction,self.values)

class OrderDropdown(discord.ui.Select):#reworked
    def __init__(self):
        options = [
            discord.SelectOption(label='Nitro', description='Buy Nitro at discounted rates!' , emoji='<a:Nitro:1231178853742022677>', value='Nitro'),
            discord.SelectOption(label='Profile Decor', description='Buy Profile Decorations at a discount!' , emoji='<:Discord:787321652345438228>', value='ProfileDecor'),
            discord.SelectOption(label='Server boosts', description='Buy Server Boosts at a discount!' , emoji='<a:Server_Boosts:867777823468027924>', value='ServerBoosts'),
            discord.SelectOption(label='Subscriptions', description='Choose one of our various video and audio streaming services!', emoji='<:77927netflixblack:1239509363568414740>', value='Subscription'),
            discord.SelectOption(label='Game Credits', description="Buy in game currency at discounted rates!", emoji='<:m_robux:1231178907865317417>', value='GameCredits'),
            discord.SelectOption(label='Steam Games', description="Buy steam games at discounted rates!", emoji='<:47647steam:1239509355255169106>', value='SteamGames'),
            discord.SelectOption(label='Aged Accounts', description='Buy old accounts from upto 2016 at a discount!' , emoji='<:DiscordLogoOld:866085733587353620>', value='AgedAccounts'),
            discord.SelectOption(label='Social Boosts', description='Choose one of our various Social media boosting services1', emoji='<:98820instagram:1239509369192714291>', value='SocialBoosts'),
            discord.SelectOption(label='Server Members', description='Buy active or inactive server members for cheap!' , emoji='<:members:1239545776951132252>', value='ServerMembers'),
            discord.SelectOption(label='Other', description="Select this if your order isnt on our list!", emoji='<:m_toroconfused:1233396013360877639>', value='Other')
     ]
        super().__init__(options=options, placeholder='Which would you like to purchase?', max_values=1, min_values=1)

    async def callback(self, interaction : discord.Interaction):
        if self.values[0] == 'Nitro':
            await self.view.summonDC(interaction,self.values)
        elif self.values[0] == 'ProfileDecor':
            await self.view.PDmod(interaction,self.values)
        elif self.values[0] == 'ServerBoosts':
            await self.view.ServerBoosts(interaction,self.values)
        elif self.values[0] == 'Subscription':
            await self.view.summonTV(interaction,self.values)
        elif self.values[0] == 'GameCredits':
            await self.view.summonGC(interaction,self.values)
        elif self.values[0] == 'SteamGames':
            await self.view.SG(interaction,self.values)
        elif self.values[0] == 'AgedAccounts':
            await self.view.AA(interaction,self.values)
        elif self.values[0] == 'SocialBoosts':
            await self.view.summonSB(interaction,self.values)
        elif self.values[0] == 'ServerMembers':
            await self.view.SM(interaction,self.values)
        elif self.values[0] == 'Other':
            await self.view.OTHER(interaction,self.values)

class MainView(discord.ui.View):
    def __init__(self):
        super().__init__()

        # Adds the dropdown to our view object.
        self.add_item(OrderDropdown())

    async def summonDC(self, interaction:discord.Interaction, choice1):
        self.children[0].disabled= True
        self.add_item(DCview())
        await interaction.message.edit(view=self)
        await interaction.response.defer()

    async def NitroBasic(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(NitroBasic())

    async def NitroBoostm(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(NitroBoostm())

    async def NitroBoosty(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(NitroBoosty())

    async def AA(self, interaction:discord.Interaction, choice):
        self.children[0].disabled= True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(AA())

    async def SM(self, interaction:discord.Interaction, choice):
        self.children[0].disabled= True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(SM())
    
    async def Minecraft(self, interaction:discord.Interaction, choice2):
        self.ORDER1 = choice2
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(Minecraft())

    async def Netflix(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(Netflix())

    async def Sonyliv(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(Sonyliv())

    async def Crunchyroll(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(Crunchyroll())

    async def spotify(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(Spotify())

    async def youtube(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(Youtube())

    async def Prime(self, interaction:discord.Interaction, choice2):
        self.ORDER1 = choice2
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(Prime())

    async def SBINSTA(self, interaction:discord.Interaction, choice2):
        self.ORDER1 = choice2
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(SBINSTA())

    async def SBYT(self, interaction:discord.Interaction, choice2):
        self.ORDER1 = choice2
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(SBYT())

    async def SBTIKTOK(self, interaction:discord.Interaction, choice2):
        self.ORDER1 = choice2
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(SBTIKTOK())

    async def SBTWITCH(self, interaction:discord.Interaction, choice2):
        self.ORDER1 = choice2
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(SBTWITCH())

    async def SBTWITTER(self, interaction:discord.Interaction, choice2):
        self.ORDER1 = choice2
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(SBTWITTER())

    async def SBTELEGRAM(self, interaction:discord.Interaction, choice2):
        self.ORDER1 = choice2
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(SBTELEGRAM())

    async def Robux(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(Robux())

    async def Vbucks(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(Vbucks())

    async def SG(self, interaction:discord.Interaction, choice2):
        self.children[0].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(SG())

    async def PDmod(self, interaction:discord.Interaction, choice2):
        self.children[0].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(PDmod())

    async def OTHER(self, interaction:discord.Interaction, choice2):
        self.ORDER2 = choice2
        self.children[0].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(OTHER())

    async def ServerBoosts(self, interaction:discord.Interaction, choice2):
        self.children[0].disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_modal(ServerBoost())

    async def summonTV(self, interaction:discord.Interaction, choice1):
        self.children[0].disabled= True
        self.add_item(TVview())
        await interaction.message.edit(view=self)
        await interaction.response.defer() 

    async def summonGC(self, interaction:discord.Interaction, choice1):
        self.children[0].disabled= True
        self.add_item(GCview())
        await interaction.message.edit(view=self)
        await interaction.response.defer()

    async def summonSB(self, interaction:discord.Interaction, choice1):
        self.children[0].disabled= True
        self.add_item(SBview())
        await interaction.message.edit(view=self)
        await interaction.response.defer() 

    async def ESM(self, interaction:discord.Interaction, choice2):
        self.children[1].disabled= True
        await interaction.message.edit(view=self)
        self.stop()

@bot.command()
async def order(ctx):
    view=MainView()
    chan = ctx.guild.get_channel(channel)
    await ctx.send(f'What would you like to buy <a:m_kerohi:1221301733658198046>?', delete_after = 120)
    await ctx.send(view=view, delete_after=120)
    await view.wait()
    await view.wait()

@bot.command()
async def ab(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send(f"# <:m_greenheart:1230018368338133054> Type order to place an order!")

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong <a:m_kerohi:1221301733658198046>")
    
@bot.command()
async def setup(ctx):
    await ctx.send(f"Type the following: \n- ID of order recieving channel \n- ID of order submission channel \n- Guild ID")

@bot.command()
async def ltc(ctx):
    embed = discord.Embed(
        colour=discord.Colour.green(),
        description= "### La2hXs2BGrkNPzgJYEvwY7NLkHi9JDRQiU",
        title= "Pay here",
    )
    embed.add_field(name='', value='', inline=False)
    embed.set_footer(text = "discord.com/matcha")
    embed.add_field(name='<:m_greenheart:1230018368338133054> ***Provide SS of payment***', value='<a:m_cowroll:1233436664328753245> *No SS = No transaction*')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/920899490574110730/1248869818937901136/a_7dd45d52d7262c3a764ec9f82908def2.gif?ex=66653c27&is=6663eaa7&hm=4f3cf9846ec7c3f87e6f3ef01a49e27e57518a28f96230f34641e94751d57024&')

    await ctx.send(embed = embed)

@bot.command()
async def upi(ctx):
    embed = discord.Embed(
        colour=discord.Colour.green(),
        description= "### 02aryan@fam",
        title= "Pay here",
    )
    embed.add_field(name='', value='', inline=False)
    embed.set_footer(text = "discord.com/matcha")
    embed.add_field(name='<:m_greenheart:1230018368338133054> ***Provide SS of payment***', value='<a:m_cowroll:1233436664328753245> *No SS = No transaction*')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/920899490574110730/1248869818937901136/a_7dd45d52d7262c3a764ec9f82908def2.gif?ex=66653c27&is=6663eaa7&hm=4f3cf9846ec7c3f87e6f3ef01a49e27e57518a28f96230f34641e94751d57024&')

    await ctx.send(embed = embed)

@bot.command()
async def pp(ctx):
    embed = discord.Embed(
        colour=discord.Colour.green(),
        description= "## SEND IN FRIENDS AND FAMILY ONLY",
        title= "Instructions",
    )
    embed.set_footer(text = "discord.com/matcha")
    embed.add_field(name='Send the amount in `euros[€]`',value='<a:m_greenstar:1230018378719297566> DO **NOT** ATTACH ANY __NOTES__ \n<a:m_greenstar:1230018378719297566> SEND FROM PAYPAL **BALANCE**, NOT *CARD* OR *BANK*\n<a:m_greenstar:1230018378719297566> ***TOS BROKEN = NO REFUND***', inline=False)
    embed.add_field(name='<:m_greenheart:1230018368338133054> ***Provide SS of payment***', value='<a:m_cowroll:1233436664328753245> *No SS = No transaction*')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/920899490574110730/1248869818937901136/a_7dd45d52d7262c3a764ec9f82908def2.gif?ex=66653c27&is=6663eaa7&hm=4f3cf9846ec7c3f87e6f3ef01a49e27e57518a28f96230f34641e94751d57024&')

    await ctx.send(embed = embed)

@bot.command()
async def queue(ctx):
    embed = discord.Embed(
        colour=discord.Colour.dark_green(),
        description= "## __Order is now processing!__",
        title= "Order Status update",
    )
    embed.add_field(name='Thank you for ordering!',value='- You can check your order status in https://discord.com/channels/1221251673888919633/1221251674258014210\n- ETA of orders is usually 0-2 days!', inline=False)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/920899490574110730/1248869818937901136/a_7dd45d52d7262c3a764ec9f82908def2.gif?ex=66653c27&is=6663eaa7&hm=4f3cf9846ec7c3f87e6f3ef01a49e27e57518a28f96230f34641e94751d57024&')
    embed.set_footer(text = "discord.com/matcha")

    await ctx.send(embed = embed)

@bot.command()
async def comp(ctx):
    embed = discord.Embed(
        colour=discord.Colour.dark_green(),
        description= "## __Order is now complete!__",
        title= "Order Status update",
    )
    embed.add_field(name='Thank you for trusting us!',value='- Check your dms <3\n- Vouch to activate warranty\n- Hope to see you again!', inline=False)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/920899490574110730/1248869818937901136/a_7dd45d52d7262c3a764ec9f82908def2.gif?ex=66653c27&is=6663eaa7&hm=4f3cf9846ec7c3f87e6f3ef01a49e27e57518a28f96230f34641e94751d57024&')
    embed.set_footer(text = "discord.com/matcha")

    await ctx.send(embed = embed)



bot.run(' token here ')
