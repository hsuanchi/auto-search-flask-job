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
        self.csv_path = "./doc/job_count.csv"
        self.img_path = "./doc/plot_img.jpg"

    def _init_readme(self):

        with open("./README.md", "w+") as f:
            f.write("\n")

        with open("./doc/header.md", "w+") as f:
            f.write(
                f"# Auto searching jobs\n\n## Jobs include `{self.keyword}` in Taiwan \n\n ![image]({self.img_path})"
            )

    def _insert_to_readme(self, data_list: List[dict], platform_name: str):
        df = pd.DataFrame(data_list).sort_values(["company"]).reset_index(drop=True)
        df.index += 1
        mkd = f"\n\n### Platform - {platform_name}"
        mkd += "\n\n\n" + df.to_markdown()

        with open("./README.md", "a") as f:
            f.write(mkd)

    def _create_final_readme(self):

        with open("./doc/header.md", "r+") as f:
            header = f.read()

        with open("./README.md", "r+") as f:
            base = f.read()

        with open("./doc/footer.md", "r+") as f:
            footer = f.read()

        with open("README.md", "w") as f:
            f.write(header + base + footer)

    def _save_to_csv(self):
        df = pd.DataFrame([self.count_result])
        df["Total"] = df[df.columns.values[1:]].sum(1)
        if os.path.exists(self.csv_path):
            df.to_csv(self.csv_path, index=False, mode="a", header=False)
        else:
            df.to_csv(self.csv_path, index=False)

    def _save_to_img(self):
        import matplotlib.pyplot as plt

        df = pd.read_csv(self.csv_path)
        print("save to img")
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
            self.img_path,  # 儲存圖檔
        )
        plt.close()

    def run(self):
        self._init_readme()

        for JobBank in JOB_BANK_LIST:
            job_bank = JobBank(self.keyword)
            job_bank.fetch_data()
            self._insert_to_readme(job_bank.data_list, job_bank.platform_name)
            self.count_result[job_bank.platform_name] = len(job_bank.data_list)

        self._save_to_csv()
        self._save_to_img()
        self._create_final_readme()


if __name__ == "__main__":
    keyword = "flask"
    print(f"You search keywords: {keyword}")
    crawler = JobCrawler(keyword)
    crawler.run()
