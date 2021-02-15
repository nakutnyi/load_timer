import json
import time
import asyncio
from aiohttp import ClientSession
from aiohttp.client_exceptions import ClientConnectorError


async def load_time(session, urls_dict, url):
    start = time.time()
    try:
        async with session.get(url) as response:
            await response.text()
            urls_dict[url] = time.time() - start
    except ClientConnectorError:
        urls_dict[url] = 'Could not connect'


async def crawl(urls_dict):
    async with ClientSession() as session:
        tasks = []
        for url in urls_dict:
            tasks.append(load_time(session, urls_dict, url))
        await asyncio.gather(*tasks)


def load_timer(event, context):

    urls = json.loads(event["body"])
    urls_dict = dict.fromkeys(urls)
    asyncio.run(crawl(urls_dict))

    body = {
        "input": event,
        "output": urls_dict,
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
