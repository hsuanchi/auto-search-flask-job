import re
import json

import pandas as pd
import requests
from bs4 import BeautifulSoup


headers = {
    'Referer':'https://www.cakeresume.com/',
    "User-Agent": "Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
}

page = 1
keyword = "flask"

url = f"https://www.cakeresume.com/jobs?q={keyword}&page={page}"

resp = requests.post(
        url=url, headers=headers
    )
soup = BeautifulSoup(resp.text, "html.parser")

print(soup)



# for config in configs:
#     # while True:
#     # if break_flag:
#     # break

#     resp = requests.get(
#         url=config["platform_url"].format(keyword, page), headers=headers
#     )
#     soup = BeautifulSoup(resp.text, "html.parser")

#     # job_list =  soup.find("ul",class_="list-result").find_all("script")
#     job_list = soup.find_all("ul", class_="si-item")

#     for job in job_list:
#         print("=" * 10)
#         # title
#         print(job.find(class_="date").text.replace("更新時間：", ""))
#         print(job.find("a").get("title"))
#         print(job.find("a").get("href"))
#         print(job.find(class_="it-md").find("a", class_="d-block organ").text)
#         print(job.find(class_="it-md").find("a", class_="d-block organ").get("href"))
#         # print(job.text)
#         # print(data['name'])
#     #     if not re.match(f".*{keyword}.*", str(job), re.IGNORECASE):
#     #         break_flag = True
#     #         # break
#     #         print("break ===========")

#     #     # print(job)
#     #     print('='*10)
#     #     print(eval('job.get("data-cust-name")'))
#     #     print(eval('job.get("data-job-name")'))
#     #     print(job.find_all('a', class_='js-job-link')[0]['href'].replace("//",""))

#     #     print(job.find_all("a")[1].get("href").replace("//",""))
#     #     print(job.find("span",class_="b-tit__date").text.strip())

#     # company_name = eval(config["company_name_element"])
#     # company_list = eval(config["company_link_element"])
#     # job_name = eval(config["job_name_element"]).replace("|", "/")
#     # job_link = eval(config["job_link_element"])
#     # job_dict = {
#     #     "company_name": f"[{company_name}]({company_list})",
#     #     "platform_name": config["platform_name"],
#     #     "job_name": f"[{job_name}]({job_link})",
#     #     "job_update_time": eval(config["job_update_time_element"]),

#     # print(company_name)

#     # break_flag=True
