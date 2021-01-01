import re

from bs4 import BeautifulSoup, PageElement
from bs4.element import ResultSet, Tag

from .base_crawler import BaseCrawler


class A104(BaseCrawler):
    platform_name = "104"
    platform_url = "https://www.104.com.tw/jobs/search/?&jobsource=2018indexpoc&keyword={}&order={}"

    def get_job_list(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all(
            "article",
            class_="js-job-item",
            attrs={"data-jobsource": re.compile(r"(.*list.*|2018.*)")},
        )

    def get_company_name(self, job: Tag) -> str:
        return job.get("data-cust-name").replace("|", "/")

    def get_company_link(self, job: Tag) -> str:
        return "https:" + job.find_all("a")[1].get("href")

    def get_job_name(self, job: Tag) -> str:
        return job.get("data-job-name").replace("|", "/")

    def get_job_link(self, job: Tag) -> str:
        return "https:" + job.find_all("a", class_="js-job-link")[0]["href"]

    def update_time(self, job: Tag) -> str:
        return job.find("span", class_="b-tit__date").text.strip()
