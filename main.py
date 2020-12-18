import re
import requests
import pandas as pd

from pprint import pprint
from bs4 import BeautifulSoup
from config import configs


class Craw:
    def __init__(self):
        self.data_list = []
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
        }

    def fetch_data(self, config, keyword):
        break_flag = False
        page = 1

        while True:
            if break_flag:
                break

            resp = requests.get(
                url=config["platform_url"].format(keyword, page), headers=self.headers
            )
            soup = BeautifulSoup(resp.text, "html.parser")
            job_list = eval(config["jobs_list_element"])

            for job in job_list:
                if not re.match(f".*{keyword}.*", str(job), re.IGNORECASE):
                    break_flag = True
                    break

                company_name = eval(config["company_name_element"]).replace("|", "/")
                company_list = eval(config["company_link_element"])
                job_name = eval(config["job_name_element"]).replace("|", "/")
                job_link = eval(config["job_link_element"])
                job_dict = {
                    "company_name": f"[{company_name}]({company_list})",
                    "platform_name": config["platform_name"],
                    "job_name": f"[{job_name}]({job_link})",
                    "job_update_time": eval(config["job_update_time_element"]),
                }

                self.data_list.append(job_dict)
            page += 1

    def mkd_to_readme(self, data_list):
        df = (
            pd.DataFrame(data_list)
            .sort_values(["company_name", "platform_name"])
            .reset_index(drop=True)
        )
        mkd = '## Auto searching job include Flask in Taiwan'
        mkd += '\n\n\n'+df.to_markdown()

        with open("README.md", "w+") as f:
            f.write(mkd)


if __name__ == "__main__":

    keyword = "flask"

    run = Craw()
    for config in configs:
        run.fetch_data(config, keyword)
    run.mkd_to_readme(run.data_list)
