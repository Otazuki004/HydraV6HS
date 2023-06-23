import os
from pyrogram import filters
from Hydra import prefix
from Hydra import pub as Hydra


@Hydra.on_message(filters.command("rename", prefixes=prefix))
async def rename(_, message):
	try:
        filename = message.text.replace(message.text.split(" ")[0], "")
        if reply := message.reply_to_message:
        	x = await message.reply_text("Downloading.....")
        path = await reply.download(file_name=filename)
        await x.edit("Uploading.....")
       await message.reply_document(path)
        os.remove(path)