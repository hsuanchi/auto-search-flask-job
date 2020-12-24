
import re

from bs4 import BeautifulSoup, PageElement
from bs4.element import ResultSet, Tag

from .base_crawler import BaseCrawler


class MeetJobs(BaseCrawler):
    HOST = 'https://meet.jobs'
    platform_name = "MeetJobs"
    platform_url = HOST + "/zh-TW/jobs?order=match&place=Taipei&q={}&page={}"
    need_include_keyword = False

    def get_job_list(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all(
            "div",
            class_="job-card card"
        )

    def get_company_name(self, job: Tag) -> str:
        return job.find("h5", class_="employer-name").get_text()

    def get_company_link(self, job: Tag) -> str:
        return self.HOST + job.find_all("a")[1].get("href")

    def get_job_name(self, job: Tag) -> str:
        return job.find("h3", class_="job-title").get_text()

    def get_job_link(self, job: Tag) -> str:
        return self.HOST + job.find_all("a")[0].get("href")

    def update_time(self, job: Tag) -> str:
        return 'N/A'
