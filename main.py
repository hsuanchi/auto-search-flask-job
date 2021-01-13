import sys
import os.path
from typing import List

import pandas as pd
import numpy as np
from datetime import date

from crawlers import JOB_BANK_LIST


class JobCrawler:
    def __init__(self, keyword):
        self.keyword = keyword
        self.count_result = {"datetime": date.today().strftime("%Y/%m/%d")}
        self.file_path = "job_count.csv"

    def _create_new_readme(self):
        mkd = f"\n"

        with open("README.md", "w+") as f:
            f.write(mkd)

    def _create_description_readme(self):
        mkd = f"# Auto searching jobs\n\n## Jobs include `{self.keyword}` in Taiwan \n\n ![image](./plot_img.jpg)"

        with open("README.md", "r+") as f:
            updatedfile = mkd + f.read()
        with open("README.md", "w") as f:
            f.write(updatedfile)

    def _insert_to_readme(self, data_list: List[dict], platform_name: str):
        df = pd.DataFrame(data_list).sort_values(["company"]).reset_index(drop=True)
        df.index += 1
        mkd = f"\n\n\n ### Platform - {platform_name}"
        mkd += "\n\n\n\n" + df.to_markdown()

        with open("README.md", "a") as f:
            f.write(mkd)

    def _save_to_csv(self):
        df = pd.DataFrame([self.count_result])
        df["Total"] = df[df.columns.values[1:]].sum(1)
        if os.path.exists(self.file_path):
            df.to_csv(self.file_path, index=False, mode="a", header=False)
        else:
            df.to_csv(self.file_path, index=False)

    def _save_to_img(self):
        import matplotlib.pyplot as plt

        df = pd.read_csv(self.file_path)
        datetime = df["datetime"]
        columns_name = df.columns.values[1:]

        plt.style.use("ggplot")
        for column in columns_name:
            plt.plot(datetime, df[column])  # 繪製資料

        # # 設定圖例，參數為標籤、位置
        plt.legend(labels=columns_name, loc="upper right")  # 設定圖例
        plt.ylabel("Number of jobs", fontweight="bold")  # 設定y軸標題及粗體
        plt.title(
            "Jobs count", fontsize=18, fontweight="bold", y=1.1
        )  # 設定標題、文字大小、粗體及位置
        plt.tight_layout()
        plt.gcf().autofmt_xdate()
        plt.savefig(
            "plot_img.jpg",  # 儲存圖檔
        )
        plt.close()

    def run(self):
        self._create_new_readme()

        for JobBank in JOB_BANK_LIST:
            job_bank = JobBank(self.keyword)
            job_bank.fetch_data()
            self._insert_to_readme(job_bank.data_list, job_bank.platform_name)
            self.count_result[job_bank.platform_name] = len(job_bank.data_list)

        self._save_to_csv()
        self._save_to_img()
        self._create_description_readme()


if __name__ == "__main__":
    keyword = "flask"
    print(f"You search keywords: {keyword}")
    crawler = JobCrawler(keyword)
    crawler.run()
