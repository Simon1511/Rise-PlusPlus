# Copyright 2022 Simon1511@github
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

try:
    # >= 4.0.0
    from userbot.version import VERSION as hubot_version
except:
    # <= 3.0.4
    from userbot import VERSION as hubot_version


def isSupportedVersion(version: str) -> bool:
    try:
        bot_ver = tuple(map(int, hubot_version.split(".")))
        req_ver = tuple(map(int, version.split(".")))
        if bot_ver >= req_ver:
            return True
    except:
        pass
    return False


if not isSupportedVersion("5.0.1"):
    raise ValueError(f"Unsupported HyperUBot version ({hubot_version}). "
                      "Minimum required version is 5.0.1")

from userbot.sysutils.configuration import getConfig  # noqa: E402
from userbot.sysutils.event_handler import EventHandler  # noqa: E402
from userbot.sysutils.registration import (register_cmd_usage,  # noqa: E402
                                           register_module_desc,  # noqa: E402
                                           register_module_info)  # noqa: E402
from logging import getLogger  # noqa: E402
from asyncio import sleep  # noqa: E402

log = getLogger(__name__)
ehandler = EventHandler(log)
LOGGING = getConfig("LOGGING")


@ehandler.on(command="lmao", hasArgs=True, outgoing=True)
async def lmao(event):
    args = event.pattern_match.group(1)
    lmao = "lmao"
    for i in range(5):
        lmao2 = lmao[0:1].upper() + 'mao'
        await event.edit(lmao2)
        sleep(1)
        lmao2 = lmao[0:1].lower() + 'mao'
        lmao2 = 'l' + lmao[1:2].upper() + 'ao'
        await event.edit(lmao2)
        sleep(1)
        lmao2 = 'l' + lmao[1:2].lower() + 'ao'
        lmao2 = 'lm' + lmao[2:3].upper() + 'o'
        await event.edit(lmao2)
        sleep(1)
        lmao2 = 'lm' + lmao[2:3].lower() + 'o'
        lmao2 = 'lma' + lmao[3:4].upper()
        await event.edit(lmao2)
        sleep(1)
        lmao2 = 'lma' + lmao[3:4].lower()
        await event.edit(lmao2)
    return

DESC = (
    "This module offers LMAO "
)
register_cmd_usage(
    "lmao",
    "",
    "Funny animated lmao"
)
register_module_desc(DESC)
register_module_info(
    name="lmao",
    authors="Simon1511",
    version="1.0.0"
)
