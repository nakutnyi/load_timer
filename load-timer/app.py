from flask import Flask, request, copy_current_request_context
app = Flask(__name__)

import time
import asyncio
from aiohttp import ClientSession
#from aiohttp.client_exceptions import ClientConnectorError


URLS_SET = {
    'https://google.com',
    'https://facebook.com',
    # 'https://bash.im',
    'https://dou.ua',
    'https://stackoverflow.com',
    'https://youtube.com',
    }

URLS_DICT = dict.fromkeys(URLS_SET)


async def load_time(session, url):
    start = time.time()
    async with session.get(url) as response:
        await response.text()
        URLS_DICT[url] = time.time() - start


async def crawl(urls: set):
    async with ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(load_time(session, url))
        await asyncio.gather(*tasks)


@app.route("/", methods=["POST"])
def load_timer2(*args):

    # print("\n\n\n")
    # print(args)
    # print("\n\n\n")

    return 'test'

    # with app.app_context():
    #
    #     urls = request.form.getlist('urls')
    #     urls_dict = dict.fromkeys(urls)
    #     asyncio.run(crawl(urls_dict))
    #
    #     return urls_dict
