import random
import requests
from Hydra.events import register
from Hydra import tbot as tbot


ran1 = "1234567890"
ran2 = "¥€¢£"
ran3 = "@#$&+?!"
ran4 = "()[]{}"
ran5 = "NOPQRSTUVWXYZ"
ran6 = "Otazuki"
ran7 = "ABCDEFGHIJKLM"
ran8 = "uvwxyz"
ran9 = "ghijklmnopqrst"
ran0 = "abcdef"
ran11 = "Hyperspeed"

all = ran1 + ran2 + ran3 + ran4 + ran5 + ran6 + ran7 + ran8 + ran9 + ran0 + ran11

length = 11

@register(pattern=("/pass"))
async def awake(event):
   password = "".join(random.sample(all, length))
   await event.reply(password)

@register(pattern=("/hentai"))
async def awake(event):
   video = requests.get('https://hvideo-api.vercel.app/').json()['vid']
   await tbot.send_file(video, reply_to=event.id)

#fake cc soon