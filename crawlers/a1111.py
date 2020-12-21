import re

from bs4 import BeautifulSoup, PageElement
from bs4.element import ResultSet, Tag

from .base_crawler import BaseCrawler


class A1111(BaseCrawler):
    platform_name = "1111"
    platform_url = "https://www.1111.com.tw/search/job?ks={}&page={}&fs=1"

    def get_job_list(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("ul", class_="si-item")

    def get_company_name(self, job: Tag) -> str:
        return job.find(class_="it-md").find("a", class_="d-block organ").text.replace("|", "/")

    def get_company_link(self, job: Tag) -> str:
        return job.find(class_="it-md").find("a", class_="d-block organ").get("href")

    def get_job_name(self, job: Tag) -> str:
        return job.find("a").get("title").replace("|", "/")

    def get_job_link(self, job: Tag) -> str:
        return job.find("a").get("href")

    def update_time(self, job: Tag) -> str:
        return job.find(class_="date").text.replace("更新時間：","")
