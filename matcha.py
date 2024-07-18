from unicodedata import category
import discord
import random 
from discord.ext import commands
from typing import Optional
import io
from datetime import datetime, timezone
import pytz
from discord.utils import MISSING
import chat_exporter
from github import Github
import asyncio
import time
import os
 
token = ''
gittoken = ''


bot = commands.Bot(command_prefix=',', intents=discord.Intents.all())

#ticketcategory = category under which the tickets should open
ticketcategory = 1221296687234945024   
categories = ["1221296687234945024 - orders (matcha)", 
              "1254554932003078235 - Sussy baka (boot)"]
#logchannel = channel where the transcript wagera has to be sent
logchannel = 1221251674518065292 #boot log channel
logchannels = ["1221251674518065292 - Ticket-logs (matcha)",
               "1256131499355410493 - log-channel (boot)"]


@bot.event
async def on_ready():

    bot.add_view(TicketOpener())
    bot.add_view(TicketCloser())
    bot.add_view(TicketDestroyer())
    bot.add_view(Start())


    print("All oiled up for you daddy <3 UwU")

#trans
async def get_transcript(member: discord.Member, channel: discord.TextChannel):
    export = await chat_exporter.export(channel=channel)
    file_name=f"{member.id}.html"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(export)

#upload
def upload(file_path: str, member_name: str):
    github = Github(gittoken)
    repo = github.get_repo("nooblej/Ticket-Trans")
    file_name = f"{int(time.time())}"
    repo.create_file(
        path=f"tickets/{file_name}.html",
        message="Ticket Log for {0}".format(member_name),
        branch="main",
        content=open(f"{file_path}","r",encoding="utf-8").read()
    )
    os.remove(file_path)

    return file_name

#TICKET RELATED CLASSES
class TicketOpener(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)


    @discord.ui.button(label="Create Ticket!", style=discord.ButtonStyle.blurple, emoji="<a:m_kerohi:1221301733658198046>", custom_id="ticketopen")
    async def ticket(self, interaction:discord.Interaction, button: discord.Button):
        await interaction.response.defer(ephemeral=True)
        category: discord.CategoryChannel = discord.utils.get(interaction.guild.categories, id = ticketcategory)
        overwrites = {
            interaction.guild.default_role: discord.PermissionOverwrite(read_messages = False),
            interaction.user: discord.PermissionOverwrite(read_messages = True, send_messages = True),
            interaction.guild.me: discord.PermissionOverwrite(read_messages = True, send_messages = True)
        }
        ist = pytz.timezone('Asia/Kolkata')
        now_utc = datetime.now(pytz.utc)
        now_ist = now_utc.astimezone(ist)
        time_str1 = now_ist.strftime('%H %M %S %d %m %Y')
        channel = await category.create_text_channel(
            name=f"{interaction.user}'s ticket ",
            topic= f"{interaction.user.id} Place Order {time_str1}",
            overwrites=overwrites
        )
        embed2=discord.Embed(
                title=f"Ticket Created!",
                description=f"Staff will be here to assist you soon!",
                color=discord.Color.green(),)
        embed2.set_footer(text=f"discord.gg/matcha")
        embed2.add_field(name=f"Opener:", value=f"{interaction.user.mention} ")
        role_id = 1221251673926668359
        guild = interaction.guild
        role = guild.get_role(role_id)
        await channel.send(f"{interaction.user.mention} {role.mention}",embed=embed2,view=TicketCloser())
        
        embed1 = discord.Embed(
            title=(f"Welcome! <a:m_kerohi:1221301733658198046> "),
            color=discord.Color.gold()
        )
        embed1.add_field(name=f"**Click 'Start Order' to start placing an order!**", value=("- If youd like to check what we offer, press the 'Show menu' button! \n- For further details and pricing, please check the respective discord channels!"), inline=True)
        
        await channel.send(embed=embed1, view=Start())
        await interaction.followup.send(
            embed=discord.Embed(
                description= "Created your ticket in {0}".format(channel.mention),
                color=discord.Color.gold()
            ), ephemeral=True
        )
        
class TicketCloser(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="Close the ticket",style=discord.ButtonStyle.red,custom_id="closeticket",emoji="🔒")
    async def close(self, interaction: discord.Interaction, button: discord.Button):
        await interaction.response.defer(ephemeral=True)

        await interaction.channel.send("Closing ticket", delete_after=2)

        category: discord.CategoryChannel = discord.utils.get(interaction.guild.categories, id = ticketcategory)
        overwrites = {
            interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            interaction.guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }
        ist = pytz.timezone('Asia/Kolkata')
        now_utc = datetime.now(pytz.utc)
        now_ist = now_utc.astimezone(ist)
        time_str2 = now_ist.strftime('%d/%m/%Y - %H:%M:%S')
        await interaction.channel.edit(overwrites=overwrites)
        await interaction.channel.send(
            embed= discord.Embed(
                description="Ticket Closed!",
                color = discord.Color.red()
            ), view=TicketDestroyer()
        )

        member = interaction.guild.get_member(int(interaction.channel.topic.split(" ")[0]))
        hour = (interaction.channel.topic.split(" ")[3])
        minute = (interaction.channel.topic.split(" ")[4])
        second = (interaction.channel.topic.split(" ")[5])
        day = (interaction.channel.topic.split(" ")[6])
        month = (interaction.channel.topic.split(" ")[7])
        year = (interaction.channel.topic.split(" ")[8])
        teem = [hour,minute,second]
        deet = [day,month,year]
        stitched_time = ":".join(teem)
        stitched_date = "/".join(deet)

        await get_transcript(member=member, channel=interaction.channel)
        file_name = upload(f'{member.id}.html',member.name)
        link = f"https://nooblej.github.io/Ticket-Trans/tickets/{file_name}"
         
        log_channel= interaction.guild.get_channel(logchannel)
        embed= discord.Embed(
            title="Ticket Closed!",
            color=discord.Color.green()
        )
        embed.add_field(name="Opened by", value=f"{member.mention}")
        embed.add_field(name="  ", value="  ")
        embed.add_field(name="Opened on", value=f"{stitched_date} - {stitched_time}")
        embed.add_field(name="Closed by", value=f"{interaction.user.mention}")
        embed.add_field(name="  ", value="  ")
        embed.add_field(name="Closed on", value=f"{time_str2}")
        embed.add_field(name='Transcript', value=f"[Link]({link})",inline=False)
        await log_channel.send(embed=embed)
        await log_channel.send(f"Transcript link will take a minute to upload, by the time this message disappears the link should be ready.", delete_after=100)

class TicketDestroyer(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Delete the ticket", style=discord.ButtonStyle.red, emoji="🚮", custom_id="trash")
    async def trash(self, interaction: discord.Interaction, button: discord.Button):
        await interaction.response.defer()
        await interaction.channel.send("Deleting ticket")
        

        await interaction.channel.delete()
        
@bot.command()
@commands.has_permissions(administrator=True)
async def ticket(ctx):
    embed = discord.Embed(
            title=(f"__Place an order!__"),
            color=discord.Color.green()
        )
    embed.add_field(name=f"₊˚๑ **open a ticket to place an order. <:m_froggyheart:1230018352873738301> **", value=(""), inline=False)
    embed.add_field(name=f" ", value=("<:m_frogangry:1230018348595544136> *please do not open a ticket for no reason*"), inline=False)
    embed.set_footer(text="discord.gg/matcha")
    await ctx.send(embed=embed, view=TicketOpener())

class Menu(discord.ui.View):

    embed2 = discord.Embed(
            title=(f" Page 2/2"),
            color=discord.Color.green()
        )
    embed2.add_field(name=f"**Social Boosts**", value=("- Instagram\n- Youtube\n- Tiktok\n- Twitter\n- Twitch\n- Telegram"), inline=True)
    embed2.add_field(name=f"**Steam games**", value=("- Most offline triple A games, some popular online games like GTA online."), inline=True)
    embed2.add_field(name=f"**Aged Accounts**", value=("- Accounts from 2016 to 2022"), inline=False)
    embed2.add_field(name=f"**Server Members**", value=("- Botted but always online \n- Real via paid invites"), inline=True)
    embed2.add_field(name=f"**Other**", value=("- Check to see if other OTTs or specific subscriptions are available"), inline=True)
    embed2.set_footer(text="discord.gg/matcha")

    @discord.ui.button(label="Page 2", style=discord.ButtonStyle.green, emoji="⏩", custom_id="Nextpage")
    async def page_2(self, interaction: discord.Interaction, button: discord.Button):
        await interaction.response.edit_message(embed=self.embed2,view=menu2())

    @discord.ui.button(label="Close menu", style=discord.ButtonStyle.green, emoji="❌",custom_id="cancel")
    async def close_menu(self, interaction: discord.Interaction, button: discord.Button):
        view = Start()
        embed = discord.Embed(
            title=(f"Welcome!"),
            color=discord.Color.gold()
        )
        embed.add_field(name=f"**Click 'Start Order' to start placing an order!**", value=("- If youd like to check what we offer, press the 'Show menu' button! \n- For further details and pricing, please check the respective discord channels!"), inline=True)
        await interaction.response.edit_message(embed=embed, view=view)
    
class menu2(discord.ui.View):
    embed1 = discord.Embed(
            title=(f" Page 1/2"),
            color=discord.Color.green()
        )
    embed1.add_field(name=f"**Nitro**", value=("- Nitro Boost (monthly)      \n- Nitro Boost (yearly)    \n- Nitro Basic"), inline=True)
    embed1.add_field(name=f"**Server Boosts**", value=("- 1m / 3m \n- 4x / 8x / 14x"), inline=True)
    embed1.add_field(name=f"**Game Credits**", value=("- Robux\n- Vbucks"), inline=False)
    embed1.add_field(name=f"**Profile Decorations**", value=("- Feelin' Retro \n- Pirates \n- Galaxy\n- Lofi \n- Anime\n- Elements\n- Cyberpunk\n- Fantasy\n- Springtoons\n- Arcade!"), inline=True)
    embed1.add_field(name=f"**Subscriptions**", value=("- Netflix\n- Spotify\n- Youtube premium\n- Sony Liv\n- Crunchyroll\n- Minecraft\n- Prime Video"), inline=True)

    @discord.ui.button(label="Page 1", style=discord.ButtonStyle.green, emoji="⏪",custom_id="previouspage")
    async def page_1(self, interaction: discord.Interaction, button: discord.Button):
        await interaction.response.edit_message(embed=self.embed1, view=Menu())

    @discord.ui.button(label="Close menu", style=discord.ButtonStyle.green, emoji="❌", custom_id="cancel2")
    async def close_menu(self, interaction: discord.Interaction, button: discord.Button):
        view = Start()
        embed = discord.Embed(
            title=(f"Welcome!"),
            color=discord.Color.gold()
        )
        embed.add_field(name=f"**Click 'Start Order' to start placing an order!**", value=("- If youd like to check what we offer, press the 'Show menu' button! \n- For further details and pricing, please check the respective discord channels!"), inline=True)
        await interaction.response.edit_message(embed=embed, view=view)

    # @discord.ui.button(label="Page 1", style=discord.ButtonStyle.green, emoji="⏪")
    # async def page_1(self, interaction: discord.Interaction, button: discord.Button):
    #     self.current_page = 1
    #     await self.update_message(interaction)

    # @discord.ui.button(label="Page 2", style=discord.ButtonStyle.green, emoji="⏩")
    # async def page_2(self, interaction: discord.Interaction, button: discord.Button):
    #     self.current_page = 2
    #     await self.update_message(interaction)

    # async def update_message(self, interaction):
    #     if self.current_page == 1:
    #         embed = self.embed1
    #         buttons = [self.page_2]  # Only show Page 2 button
    #     else:
    #         embed = self.embed2
    #         buttons = [self.page_1]  # Only show Page 1 button
    #     await interaction.response.edit_message(embed=embed, view=self.clear_items().add_item(*buttons))

class Start(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Start order!", style=discord.ButtonStyle.blurple, emoji="📃",custom_id="start")
    async def confirm(self, interaction : discord.Interaction, button : discord.Button):
        button.disabled=True
        await interaction.response.edit_message(view=self)
        view=MainView()
        await interaction.channel.send(f'What would you like to buy <a:m_kerohi:1221301733658198046>?')
        await interaction.channel.send(view=view)
        await view.wait()
        await view.wait()
        self.stop

    embed1 = discord.Embed(
            title=(f" Page 1/2"),
            color=discord.Color.green()
        )
    embed1.add_field(name=f"**Nitro**", value=("- Nitro Boost (monthly)      \n- Nitro Boost (yearly)    \n- Nitro Basic"), inline=True)
    embed1.add_field(name=f"**Server Boosts**", value=("- 1m / 3m \n- 4x / 8x / 14x"), inline=True)
    embed1.add_field(name=f"**Game Credits**", value=("- Robux\n- Vbucks"), inline=False)
    embed1.add_field(name=f"**Profile Decorations**", value=("- Feelin' Retro \n- Pirates \n- Galaxy\n- Lofi \n- Anime\n- Elements\n- Cyberpunk\n- Fantasy\n- Springtoons\n- Arcade!"), inline=True)
    embed1.add_field(name=f"**Subscriptions**", value=("- Netflix\n- Spotify\n- Youtube premium\n- Sony Liv\n- Crunchyroll\n- Minecraft\n- Prime Video"), inline=True)

    @discord.ui.button(label="Show Menu", style= discord.ButtonStyle.green, emoji="🛎", custom_id="showmenu")
    async def show(self, interaction: discord.Interaction, button: discord.Button):
        view = Menu()
        await interaction.response.edit_message(embed=self.embed1,view=view)

class ConCan(discord.ui.View):

    @discord.ui.button(label="Confirm", style=discord.ButtonStyle.success, emoji="✅")
    async def confirm(self, interaction : discord.Interaction, button : discord.Button):
        self.disable_all_items()
        await interaction.response.edit_message(view=self)
        await interaction.channel.send(f"✅ Order has been confirmed! Please wait for one of our admins to contact you.")
        self.stop

    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.danger, emoji="❎")
    async def cancel(self, interaction : discord.Interaction, button: discord.Button):
        self.disable_all_items()
        await interaction.response.edit_message(view=self)
        await interaction.channel.send(f"❎ Order has been canceled. Please type `,order` to try again!")
        self.stop


    def disable_all_items(self):
        for child in self.children:
            child.disabled = True

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
        placeholder="1,2,3......"
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
        embed.set_footer(text="discord.gg/matcha")
        view = ConCan()
        await interaction.response.send_message(embed=embed, view=view)
    
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
        embed.set_footer(text="discord.gg/matcha")
        view = ConCan()
        await interaction.response.send_message(embed=embed, view=view)
    
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
        embed.set_footer(text="discord.gg/matcha")
        view = ConCan()
        await interaction.response.send_message(embed=embed, view=view)

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
        embed.set_footer(text="discord.gg/matcha")
        view = ConCan()
        await interaction.response.send_message(embed=embed, view=view)

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
        embed.set_footer(text="discord.gg/matcha")
        view = ConCan()
        await interaction.response.send_message(embed=embed, view=view)

class Minecraft(discord.ui.Modal, title = "Order placement"): #reworked

    Qty = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="How many accounts would you like to buy?",
        required=True,
        placeholder="1,2,3......"
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
        embed.set_footer(text="discord.gg/matcha")
        view = ConCan()
        await interaction.response.send_message(embed=embed, view=view)

class PDmod(discord.ui.Modal, title = 'Profile decoration'):#reworked

    PD = discord.ui.TextInput(
        style=discord.TextStyle.long,
        label="Which decoration would you like to buy?",
        required=True,
        max_length=500,
        placeholder="Feelin' Retro, Pirates, Galaxy, Lofi , Anime, Elements, Cyberpunk, Fantasy, Springtoons and Arcade!"
    )

    Qty = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="What Quantity?",
        required=True,
        placeholder="1,2,3......"
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
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Decoration:** {self.PD.value}", value=(f" "), inline= False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Quantity:** {self.Qty.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Payment Via:** {self.Pmt.value}", value=(f''), inline=False)
        embed.set_footer(text="discord.gg/matcha")
        view = ConCan()
        await interaction.response.send_message(embed=embed, view=view)

class NitroBasic(discord.ui.Modal, title = "Order placement"):#reworked

    Qty = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="What Quantity?",
        required=True,
        placeholder="1,2,3......"
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
        embed.set_footer(text="discord.gg/matcha")
        view = ConCan()
        await interaction.response.send_message(embed=embed, view=view)

class NitroBoostm(discord.ui.Modal, title = "Order placement"):#reworked

    Qty = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="What Quantity?",
        required=True,
        placeholder="1,2,3......"
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
        embed.set_footer(text="discord.gg/matcha")
        view = ConCan()
        await interaction.response.send_message(embed=embed, view=view)

class NitroBoosty(discord.ui.Modal, title = "Order placement"):#reworked

    Qty = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="What Quantity?",
        required=True,
        placeholder="1,2,3......"
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
        embed.set_footer(text="discord.gg/matcha")
        view = ConCan()
        await interaction.response.send_message(embed=embed, view=view)

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

        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Number of Months:** {self.Duration.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Number of Boosts:** {self.Quantity.value}", value=(f" "), inline=False)
        embed.add_field(name=f"<a:m_greenstar:1230018378719297566> **Payment Via:** {self.Pmt.value}", value=(f''), inline=False)
        embed.set_footer(text="discord.gg/matcha")
        view = ConCan()
        await interaction.response.send_message(embed=embed, view=view)

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
        placeholder="1,2,3......"
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
        embed.set_footer(text="discord.gg/matcha")
        view = ConCan()
        await interaction.response.send_message(embed=embed, view=view)

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
        placeholder="1,2,3......"
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
        embed.set_footer(text="discord.gg/matcha")
        view = ConCan()
        await interaction.response.send_message(embed=embed, view=view)

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
        placeholder="1,2,3......"
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
        embed.set_footer(text="discord.gg/matcha")
        view = ConCan()
        await interaction.response.send_message(embed=embed, view=view)

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
        placeholder="1,2,3......"
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
        embed.set_footer(text="discord.gg/matcha")
        view = ConCan()
        await interaction.response.send_message(embed=embed, view=view)

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
        placeholder="1,2,3......"
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
        embed.set_footer(text="discord.gg/matcha")
        view = ConCan()
        await interaction.response.send_message(embed=embed, view=view)

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
        placeholder="1,2,3......"
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
        embed.set_footer(text="discord.gg/matcha")
        view = ConCan()
        await interaction.response.send_message(embed=embed, view=view)

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
        embed.set_footer(text="discord.gg/matcha")
        view = ConCan()
        await interaction.response.send_message(embed=embed, view=view)

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
        embed.set_footer(text="discord.gg/matcha")
        view = ConCan()
        await interaction.response.send_message(embed=embed, view=view)

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
        embed.set_footer(text="discord.gg/matcha")
        view = ConCan()
        await interaction.response.send_message(embed=embed, view=view)

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
        embed.set_footer(text="discord.gg/matcha")
        view = ConCan()
        await interaction.response.send_message(embed=embed, view=view)

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
        embed.set_footer(text="discord.gg/matcha")
        view = ConCan()
        await interaction.response.send_message(embed=embed, view=view)

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
        embed.set_footer(text="discord.gg/matcha")
        view = ConCan()
        await interaction.response.send_message(embed=embed, view=view)

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
        embed.set_footer(text="discord.gg/matcha")
        view = ConCan()
        await interaction.response.send_message(embed=embed, view=view)

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
        super().__init__(options=options, placeholder='What would you like to purchase?', max_values=1, min_values=1)

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

# DISABLED LISTENER (REASON = TOO GOOD)
# @bot.event    
# async def on_guild_channel_create(channel):
#     embed = discord.Embed(
#             title=(f"Welcome!"),
#             color=discord.Color.gold()
#         )
#     embed.add_field(name=f"**Click 'Start Order' to start placing an order!**", value=("- If youd like to check what we offer, press the 'Show menu' button! \n- For further details and pricing, please check the respective discord channels!"), inline=True)
#     view = Start()
#     await channel.send(embed = embed, view=view)
#     await view.wait()
#     await view.wait()

@bot.command()
async def ping(ctx):

    await ctx.send(f"Pong <a:m_kerohi:1221301733658198046>" )
    
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
    embed.set_footer(text = "discord.gg/matcha")
    embed.add_field(name='<:m_greenheart:1230018368338133054> ***Provide SS of payment***', value='<a:m_cowroll:1233436664328753245> *No SS = No transaction*')
    embed.set_image(url='https://cdn.discordapp.com/attachments/920899490574110730/1250860724951973908/image0.jpg?ex=666d2314&is=666bd194&hm=6e06a69cbe297a39577824b1ff8bd7d2d5043ead39dc8d840f74784afd2037fd&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/920899490574110730/1248869818937901136/a_7dd45d52d7262c3a764ec9f82908def2.gif?ex=66653c27&is=6663eaa7&hm=4f3cf9846ec7c3f87e6f3ef01a49e27e57518a28f96230f34641e94751d57024&')
    await ctx.channel.purge(limit=1)
    await ctx.send(embed = embed)

@bot.command()
async def upi(ctx):
    embed = discord.Embed(
        colour=discord.Colour.green(),
        description= "### 02aryan@fam",
        title= "Pay here",
    )
    embed.add_field(name='', value='', inline=False)
    embed.set_image(url='https://cdn.discordapp.com/attachments/920899490574110730/1250408245646852156/Screenshot_2024-06-12-16-45-26-43_ba41e9a642e6e0e2b03656bfbbffd6e4.jpg?ex=666ad4ed&is=6669836d&hm=7642c48de36693112cf1346a87f907eb7d6d14bafb9ad3d7242edad4b712b85d&')
    embed.set_footer(text = "discord.gg/matcha")
    embed.add_field(name='<:m_greenheart:1230018368338133054> ***Provide SS of payment***', value='<a:m_cowroll:1233436664328753245> *No SS = No transaction*')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/920899490574110730/1248869818937901136/a_7dd45d52d7262c3a764ec9f82908def2.gif?ex=66653c27&is=6663eaa7&hm=4f3cf9846ec7c3f87e6f3ef01a49e27e57518a28f96230f34641e94751d57024&')
    await ctx.channel.purge(limit=1)
    await ctx.send(embed = embed)

@bot.command()
async def pp(ctx):
    embed = discord.Embed(
        colour=discord.Colour.green(),
        description= "## SEND IN FRIENDS AND FAMILY ONLY",
        title= "Instructions",
    )
    embed.set_footer(text = "discord.gg/matcha")
    embed.add_field(name='Send the amount in `euros[€]`',value='<a:m_greenstar:1230018378719297566> DO **NOT** ATTACH ANY __NOTES__ \n<a:m_greenstar:1230018378719297566> SEND FROM PAYPAL **BALANCE**, NOT *CARD* OR *BANK*\n<a:m_greenstar:1230018378719297566> ***TOS BROKEN = NO REFUND***', inline=False)
    embed.add_field(name='<:m_greenheart:1230018368338133054> ***Provide SS of payment***', value='<a:m_cowroll:1233436664328753245> *No SS = No transaction*')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/920899490574110730/1248869818937901136/a_7dd45d52d7262c3a764ec9f82908def2.gif?ex=66653c27&is=6663eaa7&hm=4f3cf9846ec7c3f87e6f3ef01a49e27e57518a28f96230f34641e94751d57024&')
    await ctx.channel.purge(limit=1)
    await ctx.send(embed = embed)

@bot.command()
async def queue(ctx):
    embed = discord.Embed(
        colour=discord.Colour.dark_green(),
        description= "## <:m_greenbow:1230017722252001363> __Order is now processing!__ <:m_greenbow:1230017722252001363>",
        title= "Order Status update",
    )
    embed.add_field(name='<:m_greenheart:1230018368338133054> Thank you for ordering!',value='- ETA of orders is usually 0-2 days!', inline=False)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/920899490574110730/1248869818937901136/a_7dd45d52d7262c3a764ec9f82908def2.gif?ex=66653c27&is=6663eaa7&hm=4f3cf9846ec7c3f87e6f3ef01a49e27e57518a28f96230f34641e94751d57024&')
    embed.set_footer(text = "discord.gg/matcha")
    await ctx.channel.purge(limit=1)
    await ctx.send(embed = embed)

@bot.command()
async def com(ctx):
    embed = discord.Embed(
        colour=discord.Colour.dark_green(),
        description= "## <:m_greenbow:1230017722252001363> __Order is now complete!__ <:m_greenbow:1230017722252001363>",
        title= "Order Status update",
    )
    embed.add_field(name='<:m_greenheart:1230018368338133054> Thank you for trusting us!',value='- Check your dms <3\n- Vouch to activate warranty\n- Hope to see you again!', inline=False)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/920899490574110730/1248869818937901136/a_7dd45d52d7262c3a764ec9f82908def2.gif?ex=66653c27&is=6663eaa7&hm=4f3cf9846ec7c3f87e6f3ef01a49e27e57518a28f96230f34641e94751d57024&')
    embed.set_footer(text = "discord.gg/matcha")
    await ctx.channel.purge(limit=1)
    await ctx.send(embed = embed)

@bot.command()
async def comp(ctx, id: discord.Member | int):
    message = f"Your order is complete. Thank you so much for ordering <3"
    await ctx.message.delete()
    if not(has_staff_perms(ctx.author) or ctx.author.guild_permissions.administrator):
        await ctx.send("https://media.discordapp.net/attachments/920882963103756298/939096996483039252/shut-up-low-rank-low-rank.gif?ex=668bb7bb&is=668a663b&hm=05a2127b4a0a14a1fa20a5b77045360cc3b8ea46e3d4e696a1e642bef6444ab9&", delete_after = 10)
    else:
        if id is int:
            user_id = id
            user = await bot.fetch_user(user_id)
            await user.send((message))
            await ctx.send(f'Sent message to {user}', delete_after=10)
        else:
            await id.send((message))
            await ctx.send(f'Sent message to {id}', delete_after=10)

    embed = discord.Embed(
        colour=discord.Colour.dark_green(),
        description= "## <:m_greenbow:1230017722252001363> __Order is now complete!__ <:m_greenbow:1230017722252001363>",
        title= "Order Status update",
    )
    embed.add_field(name='<:m_greenheart:1230018368338133054> Thank you for trusting us!',value='- Check your dms <3\n- Vouch to activate warranty\n- Hope to see you again!', inline=False)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/920899490574110730/1248869818937901136/a_7dd45d52d7262c3a764ec9f82908def2.gif?ex=66653c27&is=6663eaa7&hm=4f3cf9846ec7c3f87e6f3ef01a49e27e57518a28f96230f34641e94751d57024&')
    embed.set_footer(text = "discord.gg/matcha")
    await ctx.channel.purge(limit=1)
    await ctx.send(embed = embed)


@bot.command()
async def order(ctx):

    embed = discord.Embed(
            title=(f"Welcome! ‎‏ <a:m_kerohi:1221301733658198046> "),
            color=discord.Color.gold()
        )
    embed.add_field(name=f"**Click 'Start Order' to start placing an order!**", value=("- If you'd like to check what we offer, press the 'Show Menu' button! \n- For details and pricing, please check the respective discord channels!"), inline=True)
    view = Start()

    await ctx.send(embed=embed,view=view)

@bot.command()
async def menu(ctx):
    view = Menu()
    embed1 = discord.Embed(
            title=(f" Page 1/2"),
            color=discord.Color.green()
        )
    embed1.add_field(name=f"**Nitro**", value=("- Nitro Boost (monthly)      \n- Nitro Boost (yearly)    \n- Nitro Basic"), inline=True)
    embed1.add_field(name=f"**Server Boosts**", value=("- 1m / 3m \n- 4x / 8x / 14x"), inline=True)
    embed1.add_field(name=f"**Game Credits**", value=("- Robux\n- Vbucks"), inline=False)
    embed1.add_field(name=f"**Profile Decorations**", value=("- Feelin' Retro \n- Pirates \n- Galaxy\n- Lofi \n- Anime\n- Elements\n- Cyberpunk\n- Fantasy\n- Springtoons\n- Arcade!"), inline=True)
    embed1.add_field(name=f"**Subscriptions**", value=("- Netflix\n- Spotify\n- Youtube premium\n- Sony Liv\n- Crunchyroll\n- Minecraft\n- Prime Video"), inline=True)
    await ctx.send(embed=embed1,view=view)

@bot.command()
async def dm(ctx, id: discord.Member | int , *msg):
    await ctx.message.delete()
    if not(has_staff_perms(ctx.author) or ctx.author.guild_permissions.administrator):
        await ctx.send("https://media.discordapp.net/attachments/920882963103756298/939096996483039252/shut-up-low-rank-low-rank.gif?ex=668bb7bb&is=668a663b&hm=05a2127b4a0a14a1fa20a5b77045360cc3b8ea46e3d4e696a1e642bef6444ab9&", delete_after = 10)
    else:
        if id is int:
            user_id = id
            user = await bot.fetch_user(user_id)
            await user.send(' '.join(msg))
            await ctx.send(f'Sent message to {user}')
        else:
            await id.send(' '.join(msg))
            await ctx.send(f'Sent message to {id}')

@bot.command()
async def dms(ctx, id: discord.Member | int , *msg):
    message = ' '.join(msg)
    await ctx.message.delete()
    if not(has_staff_perms(ctx.author) or ctx.author.guild_permissions.administrator):
        await ctx.send("https://media.discordapp.net/attachments/920882963103756298/939096996483039252/shut-up-low-rank-low-rank.gif?ex=668bb7bb&is=668a663b&hm=05a2127b4a0a14a1fa20a5b77045360cc3b8ea46e3d4e696a1e642bef6444ab9&", delete_after = 10)
    else:
        if id is int:
            user_id = id
            user = await bot.fetch_user(user_id)
            await user.send(' '.join(message))
            await ctx.send(f'Sent message to {user}')
        else:
            await id.send(' '.join(message))
            await ctx.send(f'Sent message to {id}')
        
@bot.command()
async def say(ctx, *msg):
    await ctx.message.delete()
    if not (has_staff_perms(ctx.author) or ctx.author.guild_permissions.administrator):
        await ctx.send("https://media.discordapp.net/attachments/920882963103756298/939096996483039252/shut-up-low-rank-low-rank.gif?ex=668bb7bb&is=668a663b&hm=05a2127b4a0a14a1fa20a5b77045360cc3b8ea46e3d4e696a1e642bef6444ab9&", delete_after = 10)
        return
    else:
        await ctx.send(' '.join(msg))

def has_staff_perms(member: discord.Member) -> bool:
    staff_roles = {"❝⠀staff⠀₊˚ʚ⠀🍐 ⠀❞","❝⠀own⠀₊˚ʚ⠀🥝 ⠀❞"} 
    for role in member.roles:
        if role.name in staff_roles:
            return True
    return False
    
@bot.command()
async def close(ctx, *reason):
    member = ctx.guild.get_member(int(ctx.channel.topic.split(" ")[0]))
    view = TicketCloser()
    if not reason:
        reason = ('None',)
    reson = ' '.join(reason)
    await member.send(f"Your ticket has been closed. Reason: {reson}")
    await ctx.send(view=view)


bot.run(token)

# @bot.event
# async def on_message(message):
#   """
#   This event listener checks every message sent in the channel.
#   """
#   # Check if the channel ID matches the one you want to monitor (replace with your actual channel ID)
#   if message.channel.id == chat:
#     await bot.process_commands(message)
#     return
  
#   if message.author == bot.user:
#     await bot.process_commands(message)
#     return
#   # Convert message content to lowercase for case-insensitive check
#   content = message.content.lower()
#   if "order" in content:
#     view=MainView()
#     await message.channel.send(f'What would you like to buy <a:m_kerohi:1221301733658198046>?', delete_after = 120)
#     await message.channel.send(view=view, delete_after=120)
#     await view.wait()
#     await view.wait()

#   if "order" not in content:
#     await bot.process_commands(message)
