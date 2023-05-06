# copyright 2023 @Mohamed Rizad
# Telegram @riz4d
# Instagram @riz.4d

#---------------------------------
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#---------------------------------

import os
import time
import datetime
import ffmpeg
import requests
from pyrogram import filters, Client, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ChatAction
from pyrogram import *
import json
import re
from instaloader import Instaloader, Post, TwoFactorAuthRequiredException
from modules.reels import download_instagram_video
from modules.post import download_instagram_post
from modules.sessionloader import sessiongen
from config import bot_token,api_hash,api_id,owner_id,owner_username

# Developer : Mohamed Rizad | @riz4d 
# queries Are Drop At @riz4d on Telegram

loader = Instaloader(download_videos=True, download_geotags=False, download_comments=False, compress_json=False)
instadown = Client("InstaDown",api_id=int(api_id),api_hash=api_hash,bot_token=bot_token)

@instadown.on_message(filters.command('start'))
async def start_msg(client,message):
    user_id=str(message.from_user.id)
    name=message.from_user.first_name
    user_id=str(message.from_user.id)
    await message.reply(f"__**Hey {name}👋🏻**\n\nI'm **InstaDown Bot!!**, Developed by @riz4d ,designed to download instagram medias__")

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


@instadown.on_message(filters.command('login'))
async def start_msg(client,message):
    user_id=str(message.from_user.id)
    name=message.from_user.first_name
    msg_cnt=str(message.text)
    if user_id!=str(owner_id):
       pass
    else:
        try:
           username=msg_cnt.split(" ")[1]
           password=msg_cnt.split(" ")[2]
           loger=sessiongen(username, password)
           await message.reply(f"__**{loger}**__")
        except Exception as e:
          print(e)
          await message.reply(f"__Send the username and password along with the command \n\n**syntax : /login username password**__")
    

@instadown.on_message(filters.regex(r"(?i)^(https?\:\/\/)?(www\.instagram\.com)\/reel\/.+$"))
async def ig_reel_dl(client,message):
    user_id=str(message.from_user.id)
    name=str(message.from_user.first_name)
    if os.path.isfile(os.path.join("instadownsession")):
      try:
         reel_link=str(message.text)
         await message.reply_chat_action(action=ChatAction.RECORD_VIDEO)
         m=await message.reply_text('__Downloading Video..__⏳')
         reel_location_dl=download_instagram_video(reel_link)
         await message.reply_chat_action(action=ChatAction.UPLOAD_VIDEO)
         await m.edit('__Uploading Video..__⏳')
         print(reel_location_dl)
         capyn=f"**Original Post : ** [Link 🗞]({reel_link})\n\n**Developer : ** [Rizaa🖤](https://t.me/riz4d)"
         await m.delete()
         await message.reply_video(reel_location_dl,caption=capyn)
         os.remove(reel_location_dl)
      except Exception as e:
          print(e)
          await message.reply("__❗️ Invalid Instagram Reel Link__")
    else:
        if user_id==owner_id:
           await message.reply_text("**Login a instagram account to use this bot \n\n/login**")
        else:
            await message.reply_text(f'__there is a some configuration problem with admin report it @{owner_username}__⏳')
        
@instadown.on_message(filters.regex(r"(?i)^(https?\:\/\/)?(www\.instagram\.com)\/p\/.+$"))
async def ig_post_dl(client,message):
    user_id=str(message.from_user.id)
    name=str(message.from_user.first_name)
    post_link=message.text
    if os.path.isfile(os.path.join("instadownsession")):
       try:
         await message.reply_chat_action(action=ChatAction.PLAYING)
         m = await message.reply_text('__Downloading Post..__⏳')
         post_location_dl=download_instagram_post(post_link)
         print(post_location_dl)
         await message.reply_chat_action(action=ChatAction.UPLOAD_PHOTO)
         await m.edit('__Uploading Post..__⏳')
         print(post_location_dl)
         capyn=f"**Original Post : ** [Link 🗞]({post_link})\n\n**Developer : ** [Rizaa🖤](https://t.me/riz4d)"
         await m.delete()
         await message.reply_photo(post_location_dl,caption=capyn)
         os.remove(post_location_dl)
       except Exception as e:
           print(e)
           await message.reply("__❗️ Invalid Instagram Post Link__")
    else:
        if user_id==owner_id:
           await message.reply_text("**Login a instagram account to use this bot \n\n/login**")
        else:
            await message.reply_text(f'__there is a some configuration problem with admin. \n\nreport it @{owner_username}__')
        
        
instadown.run()
