# originally writen by @levina-lab on github
# copyright (C) 2021 by veez project

"""
π Commands Available -
β’ `{i}pong`
   ketik <handler>pong untuk melihat kecepatan sakura userbot mu.
"""

import asyncio

@ultroid_cmd(pattern="pong")
async def dsb(ult):
	await ult.edit("`pong!....`")
	await asyncio.sleep(0.5)
	await ult.edit("`pong..!..`")
	await asyncio.sleep(0.5)
	await ult.edit("`pong....!`")
	await asyncio.sleep(0.5)
	await ult.edit("`πΈπΈ PONG πΈπΈ\n\nβ₯ SAKURA AI\nβ₯ 69.69ms\nβ₯ SAKURA UBOT BY:`@dlwrml")
	
# By @levina-lab π

