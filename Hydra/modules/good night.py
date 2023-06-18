from Hydra import tbot as tbot
from Hydra.events import register

PHOTO4 = "https://te.legra.ph/file/4e959d8f074bef7061463.mp4"


@register(pattern=("Good night"))
async def awake(event):
    HYDRA4 = f"Good night I hope tomorrow is the best day in your life. {event.sender.first_name}"
    await tbot.send_file(event.chat_id, PHOTO4, caption=HYDRA4)

from Hydra import tbot as tbot
from Hydra.events import register

PHOTO3 = "https://te.legra.ph/file/4e959d8f074bef7061463.mp4"


@register(pattern=("good night"))
async def awake(event):
    HYDRA3 = f"Good night I hope tomorrow is the best day in your life. {event.sender.first_name}"
    await tbot.send_file(event.chat_id, PHOTO3, caption=HYDRA3)
    
from Hydra import tbot as tbot
from Hydra.events import register

PHOTO2 = "https://te.legra.ph/file/4e959d8f074bef7061463.mp4"


@register(pattern=("GN"))
async def awake(event):
    HYDRA2 = f"Good night I hope tomorrow is the best day in your life. {event.sender.first_name}"
    await tbot.send_file(event.chat_id, PHOTO2, caption=HYDRA2)
    
from Hydra import tbot as tbot
from Hydra.events import register

PHOTO1 = "https://te.legra.ph/file/4e959d8f074bef7061463.mp4"


@register(pattern=("GN"))
async def awake(event):
    HYDRA1 = f"Good night I hope tomorrow is the best day in your life. {event.sender.first_name}"
    await tbot.send_file(event.chat_id, PHOTO1, caption=HYDRA1)


