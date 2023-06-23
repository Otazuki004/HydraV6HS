from pyrogram import filters
from Hydra import prefix
from Hydra import pub as Hydra
import requests

@Hydra.on_message(filters.command("hentai", prefixes=prefix))
async def hentai(_, message):
  video = requests.get('https://hvideo-api.vercel.app/').json()['vid']
  await Hydra.send_video(video)
