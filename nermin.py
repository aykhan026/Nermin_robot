# Bu repo aykhan_s tərəfindən 29.11.2022 tarixində yığılıb
# Bu repodan icazəsiz hər hansı kodu sətri məlumatı kopyalıyıb
# Öz adına çıxaran peysərdi
# Bu yazıları silmədən işlədin

# t.me/RoBotlarimTg | YouTube: RoBotlarimTg |
# t.me/aykhan_s | insta: aykhan026 | 
# GitHub: aykhan026


from komekci.aykhan import Nermin
import base64
from mesajlar.mesaj import salam, necesen, sagol, getdim, geldim, sesizKOLGE, ban
from mesajlar.bot import yeni_user, start
from telethon import events, Button
import random


# Yeni istifadəçi mesajı
@Nermin.on(events.ChatAction)
async def handler(event):
    if event.user_joined:
        await event.reply(f"{random.choice(yeni_user)}")

nermin_start = b"\x42\x6F\x74\x20\x42\x61\xC5\x9F\x6C\x61\x64\xC4\xB1\x6C\x64\xC4\xB1\x2E\x2E\x2E\x0A\x4F\x77\x6E\x65\x72\x3A\x20\x61\x79\x6B\x68\x61\x6E\x5F\x73\x20\x7C\x20\x61\x79\x6B\x68\x61\x6E\x30\x32\x36\x0A\x74\x2E\x6D\x65\x2F\x52\x6F\x42\x6F\x74\x6C\x61\x72\x69\x6D\x54\x67"
@Nermin.on(events.NewMessage(pattern='(?i)/start+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(start)}"),
  
reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴍᴇɴɪ ǫʀᴜᴘᴀ ᴇʟᴀᴠᴇ ᴇᴛ ❱ ➕", url=f"https://t.me/Gecemusiqi_bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 ᴀsɪsᴛᴀɴ", url="https://t.me/GeceMavisiAsistant"
                    ),
                    InlineKeyboardButton(
                        "📚  sᴜᴘᴘᴏʀᴛ", url="https://t.me/UlviSup"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧩 ᴇᴍʀʟᴇʀ" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "📚 ᴋᴀɴᴀʟ", url=f"https://t.me/UlviProject"
                    )
                ]
                
           ]
        ),
    )


@Nermin.on(events.NewMessage(pattern='(?i)salam+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(salam)}")

@Nermin.on(events.NewMessage(pattern='(?i)necəsən+'))
@Nermin.on(events.NewMessage(pattern='(?i)necesen+'))
@Nermin.on(events.NewMessage(pattern='(?i)nətərsən+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(necesen)}")

@Nermin.on(events.NewMessage(pattern='(?i)sağol+'))
@Nermin.on(events.NewMessage(pattern='(?i)sagol+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(sagol)}")

@Nermin.on(events.NewMessage(pattern='(?i)getdim+'))
@Nermin.on(events.NewMessage(pattern='(?i)gedim+'))
@Nermin.on(events.NewMessage(pattern='(?i)gedirəm+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(getdim)}")

@Nermin.on(events.NewMessage(pattern='(?i)gəldim+'))
@Nermin.on(events.NewMessage(pattern='(?i)geldim+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(geldim)}")

@Nermin.on(events.NewMessage(pattern='(?i)sesizKOLGE+'))
@Nermin.on(events.NewMessage(pattern='(?i)KOLGE+'))
@Nermin.on(events.NewMessage(pattern='(?i)KOLGƏ+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(sesizKOLGE)}")

@Nermin.on(events.NewMessage(pattern='(?i)ban+'))
@Nermin.on(events.NewMessage(pattern='(?i)kick+'))
@Nermin.on(events.NewMessage(pattern='(?i)mute+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(ban)}")


nermin_run = nermin_start.decode("utf8")
print(">> Chat bot işləyir ♿ <<")
print(f"{nermin_run}")
Nermin.run_until_disconnected()
