import random 
from Hydra.events import register
from Hydra import tbot as tot

Text = (
    "Do you have Lover?", "Which Game You long time played?", "Are you played Game With Big youtuber?", "any girls Seen your dick?",
    "Any time you shared Your Browing History To Others?",
    "Are you Changed Tv Channel In Your dad/mother watching TV?", "Do you have any Ex", "Any girl shared her number to you", "do you like girls", "Are you Sigma", "Do you have Any brothers", "do you Pokemon fan", "Doremon best or his devices best", "What Is Your Favourite Cartoon", "If any girls love you, are you accept her love?", "What is your Dad income", "Are you Completed college Are Not?", "how many crushes You have", "Any scamer scamed You?", "What type of YouTube videos you like?", "any time you helped poor peoples?",
)



@register(pattern=("/truth"))
async def awake(event):
  hs = random.choice(Text)
  await event.reply(hs)

Text1 = (
    "Share Your Browsing History to others", "Buy briyani And Show Me", "play minecraft java in your phone", "Give me your Telegram GF ID", "Go to park Propose Any one", "switch off your phone for 10 mins", "Help any Poor peoples", "Go to tea shop Drink tea for free", "give me 1rs", "Join @Toon_LinkZ", "go and exchange your Lover phone", "Just Start me in dm", "go and swim for 30 mins", "Off your Phone And study",
)



@register(pattern=("/dare"))
async def awake(event):
  l = random.choice(Text1)
  await event.reply(l)
