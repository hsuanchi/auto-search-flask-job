import asyncio
import aiohttp
import async_timeout

import pandas as pd
from bs4 import BeautifulSoup
import os
import json
import time
import datetime
import re
import random


class Crawler:
    def __init__(self):
        self.keyword = "flask"
        self.platform_url = "https://www.104.com.tw/jobs/search/?&jobsource=2018indexpoc&keyword={}&order={}"
        self.data_list = []
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
            "Referer": "https://www.104.com.tw",
        }

    def craw(self):
        async def parser_job_html(html):
            soup = json.loads(html)
            if not re.search(f".*{self.keyword}.*", str(soup), re.IGNORECASE):
                print("=" * 10)
            else:
                # TODO: clean
                job_name = soup["data"]["header"]["jobName"]
                job_link = "TBC"
                update_time = soup["data"]["header"]["appearDate"]
                company_name = soup["data"]["header"]["custName"]
                company_link = soup["data"]["header"]["custUrl"]

                job_dict = {
                    "company": f"[{company_name}]({company_link})",
                    "job_title": f"[{job_name}]({job_link})",
                    "update_time": update_time,
                }

                self.data_list.append(job_dict)

        async def get_job_detail(client, crawl_url):
            try:
                async with client.get(crawl_url) as response:
                    html = await response.text()
                    assert response.status == 200
                    await parser_job_html(html)
            except Exception as e:
                print("-Exception-:", e)

        async def parser_search_html(html):
            jobs_url = []
            soup = BeautifulSoup(html, "html.parser")

            jobs = soup.find_all(
                "article",
                class_="js-job-item",
                attrs={"data-jobsource": re.compile(r"(.*list.*|2018.*)")},
            )

            for job in jobs:
                jobs_url.append(
                    "https://www.104.com.tw/job/ajax/content/"
                    + re.match(
                        r".*job\/(.*)\?.*",
                        job.find_all("a", class_="js-job-link")[0]["href"],
                    ).group(1)
                )
            return jobs_url

        async def get_search_detail(client, crawl_url):
            try:
                async with client.get(crawl_url) as response:
                    html = await response.text()
                    assert response.status == 200
                    return await parser_search_html(html)
            except Exception as e:
                print("-Exception-:", e)

        async def asyncio_chain(client, crawl_url):
            job_urls = await get_search_detail(client, crawl_url)
            for job_url in job_urls:
                print(job_url)
                await get_job_detail(client, job_url)

        async def main(crawl_urls):
            async with aiohttp.ClientSession(
                connector=aiohttp.TCPConnector(ssl=False, limit=100),
                headers=self.headers,
            ) as client:
                tasks = [asyncio_chain(client, crawl_url) for crawl_url in crawl_urls]
                await asyncio.gather(*tasks)

        crawl_urls = []
        for page in range(3):
            print(self.platform_url.format(self.keyword, page))
            crawl_urls.append(self.platform_url.format(self.keyword, page))
        asyncio.run(main(crawl_urls))


if __name__ == "__main__":

    time_start = time.time()

    do = Crawler()
    do.craw()

    print(time.time() - time_start)
