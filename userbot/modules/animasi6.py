# Edit By @pikyus1

from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import Xa_cmd


@Xa_cmd(pattern='thanks(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("●▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬●\n"
                     "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄\n"
                     "╔══╦╗────╔╗─╔╗╔╗\n"
                     "╚╗╔╣╚╦═╦═╣╚╗║╚╝╠═╦╦╗\n"
                     "─║║║║║╬║║║╩║╚╗╔╣║║║║\n"
                     "─╚╝╚╩╩╩╩╩╩╩╝─╚╝╚═╩═╝\n"
                     "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄\n"
                     "●▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬●")


@Xa_cmd(pattern='malam(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("╔═╦═╦╗╔═╦══╦═╦══╗\n"
                     "║═╣═╣║║╬║║║║╬╠╗╔╝\n"
                     "╠═║═╣╚╣║║║║║║║║║\n"
                     "╚═╩═╩═╩╩╩╩╩╩╩╝╚╝\n\n"
                     "╔══╦═╦╗╔═╦══╗\n"
                     "║║║║╬║║║╬║║║║\n"
                     "║║║║║║╚╣║║║║║\n"
                     "╚╩╩╩╩╩═╩╩╩╩╩╝")


@Xa_cmd(pattern='rumah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAMBAR RUMAH**\n"
                     "╱◥◣\n"
                     "│∩ │◥███◣ ╱◥███◣\n"
                     "╱◥◣ ◥████◣▓∩▓│∩ ║\n"
                     "│╱◥█◣║∩∩∩ ║◥█▓ ▓█◣\n"
                     "││∩│ ▓ ║∩田│║▓ ▓ ▓∩ ║\n"
                     "๑۩๑๑۩๑๑ ۩๑๑۩๑▓๑۩๑๑۩๑")


@Xa_cmd(pattern='join(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("_/﹋\\_\n"
                     "(҂`_´)\n"
                     "<,︻╦╤─ ҉\n"
                     r"_/﹋\_"
                     "\n**ᴊᴏɪɴ ʟɪɴᴋ ʙɪᴏ😡**")


CMD_HELP.update({
    "animasi6":
    f"`{cmd}rumah` ; `{cmd}join` ; `{cmd}malam` ; `{cmd}thanks`\
    \nUsage: test aja."
})
