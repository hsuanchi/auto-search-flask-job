import re

from bs4 import BeautifulSoup, PageElement
from bs4.element import ResultSet, Tag

from .base_crawler import BaseCrawler


class A1111(BaseCrawler):
    platform_name = "1111"
    platform_url = "https://www.1111.com.tw/search/job?ks={}&page={}&fs=1"

    def get_job_list(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("div", class_="item__job")

    def get_company_name(self, job: Tag) -> str:
        return job.find(class_="item__job-organ--link").get("aria-label")

    def get_company_link(self, job: Tag) -> str:
        return job.find(class_="item__job-organ--link").get("href")

    def get_job_name(self, job: Tag) -> str:
        return job.find(class_="item__job-info--link").text

    def get_job_link(self, job: Tag) -> str:
        return job.find(class_="item__job-info--link").get("href")

    def update_time(self, job: Tag) -> str:
        return (
            job.find(class_="item__job-control-datechange").get("data-yyyy")
            + "-"
            + job.find(class_="item__job-control-datechange").get("data-mmdd")
        )
