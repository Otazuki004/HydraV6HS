from pyrogram import filters
from Hydra import prefix
from Hydra import DEV_USERS as uuu
from Hydra import pub as bot


@bot.on_message(filters.command("join", prefixes=prefix) & filters.user(uuu))
async def join_chat(_, m):
    if len(m.command) < 2:
        m.reply_text("ɢɪᴠᴇ ᴀ ᴊᴏɪɴ ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ɪɴᴠɪᴛᴇ  ʟɪɴᴋ")
        return
    link = m.text.split(" ")[1]
    bot.join_chat(link)
    chat = bot.get_chat(link)
    name = m.chat.title
    await m.reply_text(f"Successfully joined {name}")


@bot.on_message(filters.command("leave", prefixes=prefix) & filters.user(uuu))
async def leave_chat(_, m):
    if len(m.command) < 2:
        m.reply_text("ɢɪᴠᴇ ᴀ ʟᴇғᴛ ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ɪɴᴠɪᴛᴇ  ʟɪɴᴋ")
        return
    link = m.text.split(" ")[1]
    bot.leave_chat(link)
    chat = bot.get_chat(link)
    name = m.chat.title
    await m.reply_text(f"Successfully left {name}")
