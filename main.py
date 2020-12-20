import re
import requests
import pandas as pd

from bs4 import BeautifulSoup

from config import configs


class Crawer:

    def __init__(self, keyword):
        self.keyword = keyword
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
        }
        self.create_new_readme()
        self.fetch_data()

    def fetch_data(self):
        for config in configs:
            data_list = []
            page = 1

            while page <3:

                resp = requests.get(
                    url=config["platform_url"].format(self.keyword, page), headers=self.headers
                )
                soup = BeautifulSoup(resp.text, "html.parser")
                job_list = eval(config["jobs_list_element"])

                for job in job_list:
                    if not re.search(f".*{self.keyword}.*", str(job), re.IGNORECASE):
                        print('pass')
                        break
                    company_name = eval(config["company_name_element"]).replace("|", "/")
                    print(company_name)
                    company_list = eval(config["company_link_element"])
                    job_name = eval(config["job_name_element"]).replace("|", "/")
                    job_link = eval(config["job_link_element"])
                    platform_name = config["platform_name"]
                    job_dict = {
                        "company": f"[{company_name}]({company_list})",
                        # "platform_name": platform_name,
                        "job_title": f"[{job_name}]({job_link})",
                        "update_time": eval(config["job_update_time_element"]),
                    }

                    data_list.append(job_dict)
                page += 1
            self.insert_to_readme(data_list,platform_name)

    def create_new_readme(self):
        mkd = f'# Auto searching job include {self.keyword} in Taiwan'

        with open("README.md", "w+") as f:
            f.write(mkd) 

    def insert_to_readme(self,data_list,platform_name):
        df = (
            pd.DataFrame(data_list)
            .sort_values(["company"])
            .reset_index(drop=True)
            # .set_index("company",drop=True)
        )
        df.index += 1
        mkd = f'\n\n\n ### Platform - {platform_name}'
        mkd += '\n\n\n\n'+df.to_markdown()

        with open("README.md", "a") as f:
            f.write(mkd)


if __name__ == "__main__":

    keyword = "flask"
    run = Crawer(keyword)
