import os
from pyrogram import filters
from Hydra import prefix as HANDLER
from Hydra import pub as Hydra
from Hydra import DEV_USERS as OWNER_ID

@Hydra.on_message(filters.command("rename", prefixes=HANDLER) & filters.usedef rename(_, message):

    try:
        filename = message.text.replace(message.text.split(" ")[0], "")

    except Exception as e:
        print(e)

    if reply := message.reply_to_message:
        x = message.reply_text("Downloading.....")
        path = reply.download(file_name=filename)
        x.edit("Uploading.....")
        message.reply_document(path)
        os.remove(path)
