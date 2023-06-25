from Hydra.Music.queues import QUEUE, get_queue, pop_an_item, clear_queue
from Hydra import music, call_py
from pytgcalls import StreamType
from pyrogram import Client
from pyrogram.raw.base import Update
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.stream import StreamAudioEnded  
from pytgcalls.types.input_stream.quality import HighQualityAudio
from pytgcalls.types.input_stream.quality import HighQualityVideo, MediumQualityVideo, LowQualityVideo

async def skip_current_song(chat_id):
   if chat_id in QUEUE:
      chat_queue = get_queue(chat_id)
      if len(chat_queue)==1:
         await call_py.leave_group_call(chat_id)
         clear_queue(chat_id)
         return 1
      else:
       try:
         songname = chat_queue[1][0]
         url = chat_queue[1][1]
         link = chat_queue[1][2]
         type = chat_queue[1][3]
         Q = chat_queue[1][4]
         if type=="Audio":
            await call_py.change_stream(
               chat_id,
               AudioPiped(
                  url,
               )
            ) 
         elif type=="Video":
            if Q==720:
               hm = HighQualityVideo()
            elif Q==480:
               hm = MediumQualityVideo()
            elif Q==360:
               hm = LowQualityVideo()
            await call_py.change_stream(
               chat_id,
               AudioVideoPiped(
                  url,
                  HighQualityAudio(),
                  hm
               )
            ) 
         pop_an_item(chat_id)
         return [songname, link, type]
       except:
         await call_py.leave_group_call(chat_id)
         clear_queue(chat_id)
         return 2
   else:
      return 0

async def skip_item(chat_id, h):
   if chat_id in QUEUE:
      chat_queue = get_queue(chat_id)
      try:
         x = int(h)
         songname = chat_queue[x][0]
         chat_queue.pop(x)
         return songname
      except Exception as e:
         print(e)
         return 0
   else:
      return 0
      

@call_py.on_stream_end()
async def on_end_handler(client, update: Update):
   if isinstance(update, StreamAudioEnded):
      chat_id = update.chat_id
      print(chat_id)
      op = await skip_current_song(chat_id)
      if op==1:
         await bot.send_message(chat_id, "`Queue is Empty, Leaving Fucking Voice Chat...`")
      elif op==2:
         await bot.send_message(chat_id, "**Some Error Occurred** \n`Clearing the Queues and Leaving the Voice Chat...`")
      else:
         await bot.send_message(chat_id, f"**🎧 Now Playing** \n[{op[0]}]({op[1]}) | `{op[2]}`", disable_web_page_preview=True)
   else:
      pass
