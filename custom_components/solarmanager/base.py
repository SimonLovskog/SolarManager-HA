import aiohttp

client = aiohttp.ClientSession()

async def getData(host):
    response = await client.get("http://{}/currentData".format(host))
    return await response.json()