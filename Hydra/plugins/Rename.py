import os
from pyrogram import filters
from Hydra import prefix
from Hydra import pub as Hydra
from Hydra import DEV_USERS as hss

@Hydra.on_message(filters.command("rename", prefixes=prefix) & filters.user(hss))
async def rename(_, message):
  try:
    filename = message.text.replace(message.text.split("rename")[1], "")

    except Exception as e:
        print(e)
      if reply := message.reply_to_message:
        x = await message.reply_text("Downloading.....")
        path = await reply.download(file_name=filename)
        await x.edit("Uploading.....")
        await message.reply_document(path)
#hs
