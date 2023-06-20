from pyrogram import __version__ as pyro
from pyrogram import filters
from Hydra import pub as bot
from Hydra import prefix, IMG, gamerhs


@bot.on_message(filters.command("alive", prefixes=prefix) & filters.user(5965055071))
async def alive(_, m):
    you = bot.get_me()
    await m.reply_photo(
        IMG, caption = f"""~  𝐻𝑦𝑑𝑟𝑎 𝑆𝑦𝑠𝑡𝑒𝑚:**
━━━━━━━━━━━━━━━━━━━

❥ **𝑂𝑊𝑁𝐸𝑅**: {you}
❥ **𝑉𝐸𝑅𝑆𝐼𝑂𝑁:** {pyro}
❥ **𝐺𝐴𝑀𝐸 𝑉𝐸𝑅𝑆𝐼𝑂𝑁:** {gamerhs}
❥ **𝑁𝐸𝑇𝑊𝑂𝑅𝐾:** @Hyper_Speed0

━━━━━━━━━━━━━━━━━━━
**Meet Me Here🙈 @FutureCity005 ✨🥀**
""")
