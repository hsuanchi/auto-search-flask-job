import re
import requests
import pandas as pd

from bs4 import BeautifulSoup

from config import configs


class Crawer:
    def __init__(self, keyword):
        self.data_list = []
        self.keyword = keyword
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
        }

    def fetch_data(self):
        for config in configs:

            break_flag = False
            page = 1

            while page <5:
                # if break_flag:
                    # break

                resp = requests.get(
                    url=config["platform_url"].format(self.keyword, page), headers=self.headers
                )
                soup = BeautifulSoup(resp.text, "html.parser")
                job_list = eval(config["jobs_list_element"])

                for job in job_list:
                    print('='*10)
                    # print(re.search(".*Flask.*", str(job), re.IGNORECASE))
                    if not re.search(f".*{self.keyword}.*", str(job), re.IGNORECASE):
                        print('pass')
                        # break_flag = True
                        break
                    company_name = eval(config["company_name_element"]).replace("|", "/")
                    print(config["platform_url"].format(self.keyword, page))
                    print(company_name)
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
                print(page)
                page += 1

    def mkd_to_readme(self):
        df = (
            pd.DataFrame(self.data_list)
            .sort_values(["company_name", "platform_name"])
            .reset_index(drop=True)
        )
        mkd = f'## Auto searching job include {self.keyword} in Taiwan'
        mkd += '\n\n\n'+df.to_markdown()

        with open("README.md", "w+") as f:
            f.write(mkd)


if __name__ == "__main__":

    keyword = "Flask"

    run = Crawer(keyword)
    run.fetch_data()
    run.mkd_to_readme()
