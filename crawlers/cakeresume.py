import re

from bs4 import BeautifulSoup, PageElement
from bs4.element import ResultSet, Tag

from .base_crawler import BaseCrawler


class CakeResume(BaseCrawler):
    platform_name = "CakeResume"
    platform_url = "https://www.cakeresume.com/jobs?q={}&page={}"

    def get_job_list(self, soup: BeautifulSoup) -> ResultSet:
        return soup.findAll("div", class_="job")

    def get_company_name(self, job: Tag) -> str:
        return job.find("h5", "page-name").find("a").text.replace("|", "/")

    def get_company_link(self, job: Tag) -> str:
        return job.find("h5", "page-name").find("a").get("href")

    def get_job_name(self, job: Tag) -> str:
        return job.find("a", "job-link").text.replace("|", "/")

    def get_job_link(self, job: Tag) -> str:
        return job.find("a", "job-link").get("href")

    def update_time(self, job: Tag) -> str:
        return job.find("span", "update-section").text
