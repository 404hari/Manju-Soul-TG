from pyrogram import Client, filters 
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery
import random
import datetime

SOULTG = Client(
    name="Manju",
    api_id= "19383278",
    api_hash= "6e6c8100d5564c59bfd82a7a86aadb95",
    bot_token= "7420317399:AAE5mHLDtn7HuPxaaFwYEj9arGahTCE0qdQ"
)

PICS = [
 "https://telegra.ph/file/9befe93227525cc5de3d7.jpg",
 "https://telegra.ph/file/a04afd5b0353d65c07050.jpg",
 "https://telegra.ph/file/1a3f98bd9e7eb4ea8d4ba.jpg",
 "https://telegra.ph/file/0922c5d8e5a378e716beb.jpg",
 "https://telegra.ph/file/693f33f82212da4b1dfc1.jpg",
 "https://telegra.ph/file/08627a85ed831456f6797.jpg"
]

@SOULTG.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=START_MESSAGE.format{get} (message.from_user.mention),
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("CHANNEL 📢", url="t.me/ManjuUpdates"),
            ],[
            InlineKeyboardButton("CREATOR 👨‍💻", url="www.github.com/SOULTG/"),
            InlineKeyboardButton("SUPPORT 🗣", url="t.me/SoulBotzz")
            ]]
            )
        )
        
START_MESSAGE = f"""
𝗛𝗘𝗟𝗟𝗢 
𝗠𝗬 𝗡𝗔𝗠𝗘 𝗜𝗦 [𝗠𝗔𝗡𝗝𝗨 💖](t.me/MANJUTGBOT)
𝗜 𝗖𝗔𝗡 𝗣𝗥𝗢𝗩𝗜𝗗𝗘 𝗠𝗔𝗟𝗔𝗬𝗔𝗟𝗔𝗠 𝗠𝗢𝗩𝗜𝗘𝗦 𝗙𝗢𝗥 𝗬𝗢𝗨 😎
𝗝𝗨𝗦𝗧 𝗚𝗢 𝗧𝗢 𝗛𝗘𝗟𝗣 𝗦𝗘𝗖𝗧𝗜𝗢𝗡 𝗔𝗡𝗗 𝗙𝗢𝗟𝗟𝗢𝗪 𝗜𝗡𝗦𝗧𝗥𝗨𝗖𝗧𝗜𝗢𝗡𝗦.
𝗛𝗔𝗩𝗘 𝗬𝗢𝗨 𝗔𝗡𝗬 𝗗𝗢𝗨𝗕𝗧 𝗛𝗜𝗧 𝗛𝗘𝗥𝗘 👉🏻 /help 🛠
@SoulBotzz"""
        
    

@SOULTG.on_message(filters.command("help"))
async def help_cmd(client, message):
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=HELP_MESSAGE.format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("CHANNEL 📢", url="t.me/ManjuUpdates"),
            ],[
            InlineKeyboardButton("CREATOR 👨‍💻", url="www.github.com/SOULTG/"),
            InlineKeyboardButton("SUPPORT 🗣", url="t.me/SoulBotzz")
            ]]
            )
        )
        
HELP_MESSAGE = """ 
𝗛𝗘𝗬 
𝗧𝗛𝗜𝗦 𝗜𝗦 𝗠𝗬 𝗛𝗘𝗟𝗣 𝗦𝗘𝗖𝗧𝗜𝗢𝗡!
𝗛𝗘𝗥𝗘 𝗜𝗦 𝗠𝗬 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦...

/start  : 𝗖𝗛𝗘𝗖𝗞 𝗜 𝗔𝗠 𝗔𝗟𝗜𝗩𝗘
/help   : 𝗛𝗢𝗪 𝗧𝗢 𝗨𝗦𝗘 𝗠𝗘
/about  : 𝗔𝗕𝗢𝗨𝗧 𝗠𝗘
/search : 𝗧𝗢 𝗦𝗘𝗔𝗥𝗖𝗛 𝗠𝗢𝗩𝗜𝗘𝗦
/info   : 𝗗𝗘𝗧𝗔𝗜𝗟𝗦 𝗔𝗕𝗢𝗨𝗧 𝗬𝗢𝗨

@SoulBotzz"""
        
    
@SOULTG.on_message(filters.command("about"))
async def about_cmd(client, message):
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=ABOUT_MESSAGE,
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("CHANNEL 📢", url="t.me/ManjuUpdates"),
            ],[
            InlineKeyboardButton("CREATOR 👨‍💻", url="www.github.com/SOULTG/"),
            InlineKeyboardButton("SUPPORT 🗣", url="t.me/SoulBotzz")
            ]]
            )
        )
        
        
ABOUT_MESSAGE = """
⭕️𝗡𝗔𝗠𝗘        : 𝗠𝗔𝗡𝗝𝗨 💖
        
⭕️𝗖𝗥𝗘𝗔𝗧𝗢𝗥     : [𝗦𝗢𝗨𝗟 𝗕𝗢𝗧𝗭𝗭](t.me/SoulBotzz)

⭕️𝗟𝗜𝗕𝗥𝗔𝗥𝗬      : [𝗣𝗬𝗥𝗢𝗚𝗥𝗔𝗠](https://docs.pyrogram.org/)

⭕️𝗟𝗔𝗡𝗚𝗨𝗔𝗚𝗘    : [𝗣𝗬𝗧𝗛𝗢𝗡𝟯](www.python.org)

⭕️𝗦𝗘𝗥𝗩𝗘𝗥       : [𝗥𝗔𝗜𝗟𝗪𝗔𝗬](https://railway.app/)

⭕️𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗢𝗗𝗘 : [𝗖𝗟𝗜𝗖𝗞 𝗛𝗘𝗥𝗘](t.me/ManjuUpdates)

@SoulBotzz
"""
    
@SOULTG.on_message(filters.command("search"))
async def search_cmd(client, message):
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=SEARCH_MESSAGE,
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("SEARCH NOW 🔍", switch_inline_query_current_chat='')
            ]]
            )
        )
        

SEARCH_MESSAGE = """
𝗧𝗢 𝗦𝗘𝗔𝗥𝗖𝗛 𝗔 𝗠𝗢𝗩𝗜𝗘 𝗜𝗦 𝗔 𝗦𝗜𝗠𝗣𝗟𝗘 𝗧𝗛𝗜𝗡𝗚.
𝗝𝗨𝗦𝗧 𝗧𝗔𝗣 𝗢𝗡 𝗧𝗛𝗘 𝗕𝗘𝗟𝗢𝗪 𝗕𝗨𝗧𝗧𝗢𝗡 𝗔𝗡𝗗 𝗘𝗡𝗝𝗢𝗬 😍

@SoulBotzz
"""

@SOULTG.on_message(filters.command("info"))
async def info_cmd(client, message):
    await message.reply_photo(
        photo=random.choice(PICS),
        caption="""f
⭕️𝗙𝗜𝗥𝗦𝗧 𝗡𝗔𝗠𝗘   : {message.from_user.first_name}
⭕️𝗟𝗔𝗦𝗧 𝗡𝗔𝗠𝗘    : {message.from_user.last_name}
⭕️𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘     : {message.from_user.username}
⭕️𝗨𝗦𝗘𝗥 𝗠𝗘𝗡𝗧𝗜𝗢𝗡 : {message.from_user.mention}
"""
)
        
print("I AM OK DEAR")

SOULTG.run()
