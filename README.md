# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                              | job_title                                                                                                                | update_time   |
|---:|:-------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [卓航科技有限公司](https://www.104.com.tw/company/1a2x6blmrv?jobsource=jolist_d_date)        | [[近微風廣場] 壓力測試專員  (福利佳)](https://www.104.com.tw/job/7et5p?jobsource=jolist_d_date)                                        | 12/31         |
|  2 | [卓航科技有限公司](https://www.104.com.tw/company/1a2x6blmrv?jobsource=jolist_d_date)        | [[近微風廣場]自動化Automation  (福利佳)](https://www.104.com.tw/job/7b0ev?jobsource=jolist_d_date)                                  | 12/31         |
|  3 | [卓航科技有限公司](https://www.104.com.tw/company/1a2x6blmrv?jobsource=jolist_d_date)        | [[近微風廣場]自動化系統開發人員  (福利佳)](https://www.104.com.tw/job/7b0eo?jobsource=jolist_d_date)                                      | 12/31         |
|  4 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_b_relevance) | [Python後端工程師](https://www.104.com.tw/job/76vbt?jobsource=jolist_b_relevance)                                             | 12/29         |
|  5 | [樂播科技股份有限公司](https://www.104.com.tw/company/1a2x6bkuvp?jobsource=jolist_d_date)      | [網頁前端工程師](https://www.104.com.tw/job/71llp?jobsource=jolist_d_date)                                                      | 12/31         |
|  6 | [樂播科技股份有限公司](https://www.104.com.tw/company/1a2x6bkuvp?jobsource=jolist_d_date)      | [後端工程師](https://www.104.com.tw/job/71lmv?jobsource=jolist_d_date)                                                        | 12/31         |
|  7 | [樂播科技股份有限公司](https://www.104.com.tw/company/1a2x6bkuvp?jobsource=jolist_d_date)      | [全端工程師](https://www.104.com.tw/job/71b33?jobsource=jolist_d_date)                                                        | 12/31         |
|  8 | [淼森科技股份有限公司](https://www.104.com.tw/company/1a2x6blm7t?jobsource=jolist_b_relevance) | [Web App Backend Developer 後端工程師 AWS/Flask/Postman/MySQL](https://www.104.com.tw/job/7a7i3?jobsource=jolist_b_relevance) | 12/29         |
|  9 | [米約科技有限公司](https://www.104.com.tw/company/1a2x6bl97m?jobsource=jolist_d_date)        | [Python工程師](https://www.104.com.tw/job/6zey2?jobsource=jolist_d_date)                                                    | 12/30         |
| 10 | [金正禾數位有限公司](https://www.104.com.tw/company/1a2x6bl4su?jobsource=jolist_d_date)       | [Backend Engineer 後端工程師](https://www.104.com.tw/job/720ep?jobsource=jolist_d_date)                                       | 12/31         |

### Platform - 1111


|    | company                                                                          | job_title                                                          | update_time   |
|---:|:---------------------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------|
|  1 | [美超微電腦股份有限公司(Super Micro Computer, Inc.)](https://www.1111.com.tw/corp/9530088/) | [Software Engineer-TC21167](https://www.1111.com.tw/job/98544764/) | 2021-12-30    |



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
