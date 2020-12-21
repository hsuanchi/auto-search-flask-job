from typing import List

import pandas as pd

from crawlers import JOB_BANK_LIST

class JobCrawler:
    def __init__(self, keyword):
        self.keyword = keyword

    def _create_new_readme(self):
        mkd = f"# Auto searching job include {self.keyword} in Taiwan"

        with open("README.md", "w+") as f:
            f.write(mkd)

    def _insert_to_readme(self, data_list: List[dict], platform_name: str):
        df = (
            pd.DataFrame(data_list) \
                .sort_values(["company"]) \
                .reset_index(drop=True)
        )
        df.index += 1
        mkd = f"\n\n\n ### Platform - {platform_name}"
        mkd += "\n\n\n\n" + df.to_markdown()

        with open("README.md", "a") as f:
            f.write(mkd)

    def run(self):
        self._create_new_readme()

        for JobBank in JOB_BANK_LIST:
            job_bank = JobBank(keyword)
            job_bank.fetch_data()
            self._insert_to_readme(job_bank.data_list, job_bank.platform_name)


if __name__ == "__main__":
    keyword = "flask"
    crawler = JobCrawler(keyword)
    crawler.run()
