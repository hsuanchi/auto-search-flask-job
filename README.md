# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                | job_title                                                                                                                | update_time   |
|---:|:---------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [倫發科技有限公司](https://www.104.com.tw/company/1a2x6biyl9?jobsource=jolist_a_date)          | [開發運維工程師(Python) DevOps Engineer](https://www.104.com.tw/job/70v91?jobsource=jolist_a_date)                              | 1/04          |
|  2 | [光禾感知科技股份有限公司](https://www.104.com.tw/company/1a2x6bks9s?jobsource=jolist_a_date)      | [Python後端工程師](https://www.104.com.tw/job/71j4l?jobsource=jolist_a_date)                                                  | 1/04          |
|  3 | [友威資訊服務股份有限公司](https://www.104.com.tw/company/1a2x6blnx5?jobsource=jolist_a_date)      | [Python 智慧製造系統工程師【世界知名半導體代工廠】，工作穩定，薪資優渥](https://www.104.com.tw/job/7f138?jobsource=jolist_a_date)                       | 1/04          |
|  4 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_b_relevance)   | [Python後端工程師](https://www.104.com.tw/job/76vbt?jobsource=jolist_b_relevance)                                             | 12/29         |
|  5 | [淼森科技股份有限公司](https://www.104.com.tw/company/1a2x6blm7t?jobsource=jolist_b_relevance)   | [Web App Backend Developer 後端工程師 AWS/Flask/Postman/MySQL](https://www.104.com.tw/job/7a7i3?jobsource=jolist_b_relevance) | 12/29         |
|  6 | [禾向數位科技有限公司](https://www.104.com.tw/company/1a2x6bl8h8?jobsource=jolist_a_date)        | [Python Backend Engineer](https://www.104.com.tw/job/71i7c?jobsource=jolist_a_date)                                      | 1/04          |
|  7 | [美商美創資通股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bjdsb?jobsource=jolist_a_date) | [資深Web後端工程師](https://www.104.com.tw/job/6y6f0?jobsource=jolist_a_date)                                                   | 1/04          |
|  8 | [迅杰智能股份有限公司](https://www.104.com.tw/company/1a2x6bjffz?jobsource=jolist_a_date)        | [Python後端工程師](https://www.104.com.tw/job/7f43q?jobsource=jolist_a_date)                                                  | 1/04          |
|  9 | [雄獅資訊科技股份有限公司](https://www.104.com.tw/company/13kq7dpk?jobsource=jolist_a_date)        | [python工程師](https://www.104.com.tw/job/71rxc?jobsource=jolist_a_date)                                                    | 1/04          |

### Platform - 1111


|    | company                                                                          | job_title                                                                             | update_time   |
|---:|:---------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|:--------------|
|  1 | [(獵頭)Accurate愛客獵股份有限公司(1111 高階獵才)](https://www.1111.com.tw/corp/69647966/)       | [直播平台_Senior Backend Developer(3002871)](https://www.1111.com.tw/job/85960420/)       | 2020-05-15    |
|  2 | [中租迪和股份有限公司](https://www.1111.com.tw/corp/2850037/)                              | [【中租超利士】中台架構師](https://www.1111.com.tw/job/97507405/)                                 | 2021-12-31    |
|  3 | [台灣美光晶圓科技股份有限公司](https://www.1111.com.tw/corp/9622349/)                          | [【桃園/台中廠擴大招募】SR Data Engineer, Smart MFG & AI](https://www.1111.com.tw/job/97430508/) | 2022-01-03    |
|  4 | [美超微電腦股份有限公司(Super Micro Computer, Inc.)](https://www.1111.com.tw/corp/9530088/) | [Software Engineer-TC21167](https://www.1111.com.tw/job/98544764/)                    | 2021-12-30    |



# Getting started
## Setup Development Environment
▍Method 1 - Python Built-in venv

- Create your virtual environment
```
$ python3 -m venv venv
```
- And enable virtual environment
```
$ . venv/bin/activate
```
- Install requirements
```
$ pip install -r requirements.txt 
```

▍Method 2 - Poetry
- Install requirements
```
$ poetry install
```
- And enable virtual environment
```
$ poetry shell
```

## Setup Keyword & Run

Setup Your Keyword in [main.py](./main.py#L88)
```
if __name__ == "__main__":
    keyword = "flask"
    crawler = JobCrawler(keyword)
    crawler.run()
```

Run Crawler
```
$ python3 main.py
```

# Contributors
PRs are welcome!

This project exists thanks to all the people who contribute.

<a href="https://github.com/hsuanchi/auto-search-flask-job/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=hsuanchi/auto-search-flask-job"/>
</a>
