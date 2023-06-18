from Hydra import tbot as tbot
from Hydra.events import register

PHOTO1 = "https://te.legra.ph/file/c4b3a0fb319744a2e41fd.jpg"


@register(pattern=("/updates"))
async def awake(event):
    HYDRA1 = f"""
**Hydra V-6💖🔥

Features ⁉️

- Vplay (soon)
- New UI
- Running On 4 instance
- Supet Fast ⚡
- Welcome MessageS Updated
- Paste Error Fix
- Renamer
- New Network 

Powered by: @Hyper_Speed0💖
Support: @FutureCity005❤️**"""
    await tbot.send_file(event.chat_id, PHOTO1, caption=HYDRA1)
