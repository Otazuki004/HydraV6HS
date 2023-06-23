import os
from pyrogram import filters
from Hydra import prefix as HANDLER
from Hydra import pub as Hydra
from Hydra import DEV_USERS as OWNER_ID

@Hydra.on_message(filters.command("rename", prefixes=HANDLER) & filters.user(OWNER_ID))
async def rename(_, message):

    try:
        filename = await message.text.replace(message.text.split(" ")[0], "")

    except Exception as e:
        print(e)

    if reply := message.reply_to_message:
        x = await message.reply_text("Downloading.....")
        path = await reply.download(file_name=filename)
        await x.edit("Uploading.....")
        await message.reply_document(path)
        os.remove(path)
