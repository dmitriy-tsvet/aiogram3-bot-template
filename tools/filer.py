import aiofiles


async def read_txt(path: str, encoding="utf-8"):
    async with aiofiles.open("bot/data/text/{}.txt".format(path), "r", encoding=encoding) as file:
        text = await file.read()
    return text
