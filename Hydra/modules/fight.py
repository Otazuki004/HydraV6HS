from pyrogram import filters
from Hydra import pgram as bot
from Hydra import prefix
from Hydra.modules.main import ask_to_dm_first
from Hydra.database.main import get_users_list
from Hydra.database.coins import get_coins_from_users
from Hydra.database.fight import fight

@bot.on_message(filters.command("fight", prefix))
async def fighting(_, message):
    user_id = message.from_user.id
    if user_id not in (await get_users_list()):
         return await ask_to_dm_first(message)
    if not message.reply_to_message:
        
          return await message.reply("Reply to the User")
    replied_user_id = message.reply_to_message.from_user.id
    coins = await get_coins_from_users(user_id)

    if coins < 1000:
         return await message.reply("you atleast hand 1000 coins to fight!")

    coins = await get_coins_from_users(replied_user_id)
    if coins < 1000:
         return await message.reply("you atleast hand 1000 coins to fight!")

    from_user_id = user_id
    x = await message.reply("Let's Begin The Fight UwU")
    await fight(
         message=x,
         symbol="⚇⚇⚇⚇⚇⚇⚇⚇",
         from_user_id=from_user_id, 
         replied_user_id=replied_user_id
)
         
     
