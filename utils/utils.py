import asyncio
from typing import Dict, List

import aiohttp


async def _download(url: str, result: Dict[str, str]):
    """ async download method """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result[url] = await response.text()


def download_urls(urls: List[str]) -> Dict[str, List[str]]:
    """ donwload multiplied ss subscription resource """
    if len(urls) == 0:
        return {}
    contents: Dict[str, str] = {}
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    tasks = [_download(url, contents) for url in urls]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    return contents
