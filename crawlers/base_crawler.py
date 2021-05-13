import re
from abc import ABC, abstractmethod

import requests
from bs4 import BeautifulSoup


class BaseCrawler(ABC):
    def __init__(self, keyword: str):
        self.keyword = keyword
        self.data_list = []
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
        }

    @abstractmethod
    def get_job_list(self):
        return NotImplemented

    @abstractmethod
    def get_company_name(self):
        return NotImplemented

    @abstractmethod
    def get_company_link(self):
        return NotImplemented

    @abstractmethod
    def get_job_name(self):
        return NotImplemented

    @abstractmethod
    def get_job_link(self):
        return NotImplemented

    @abstractmethod
    def update_time(self):
        return NotImplemented

    def fetch_data(self):
        page = 1
        print(self.platform_name)

        while page < 3:

            resp = requests.get(
                url=self.platform_url.format(self.keyword, page), headers=self.headers
            )
            soup = BeautifulSoup(resp.text, "html.parser")

            job_list = self.get_job_list(soup)

            for job in job_list:
                if not re.search(f".*{self.keyword}.*", str(job), re.IGNORECASE):
                    print("pass")
                    break

                company_name = self.get_company_name(job)
                company_link = self.get_company_link(job)
                job_name = self.get_job_name(job)
                job_link = self.get_job_link(job)
                update_time = self.update_time(job)

                job_dict = {
                    "company": f"[{company_name}]({company_link})",
                    # "platform_name": platform_name,
                    "job_title": f"[{job_name}]({job_link})",
                    "update_time": update_time,
                }

                self.data_list.append(job_dict)

            page += 1
