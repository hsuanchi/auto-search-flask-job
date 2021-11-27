# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                              | job_title                                                                                | update_time   |
|---:|:-------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|:--------------|
|  1 | [卓航科技有限公司](https://www.104.com.tw/company/1a2x6blmrv?jobsource=jolist_b_date)        | [[近微風廣場]自動化系統開發人員  (福利佳)](https://www.104.com.tw/job/7b0eo?jobsource=jolist_b_date)      | 11/27         |
|  2 | [卓航科技有限公司](https://www.104.com.tw/company/1a2x6blmrv?jobsource=jolist_b_date)        | [[近微風廣場]自動化Automation  (福利佳)](https://www.104.com.tw/job/7b0ev?jobsource=jolist_b_date)  | 11/27         |
|  3 | [小柿智檢科技股份有限公司](https://www.104.com.tw/company/1a2x6bl77l?jobsource=jolist_b_date)    | [後端工程師 Back-End Engineer](https://www.104.com.tw/job/71bmd?jobsource=jolist_b_date)      | 11/27         |
|  4 | [小柿智檢科技股份有限公司](https://www.104.com.tw/company/1a2x6bl77l?jobsource=jolist_b_date)    | [全端工程師 Full-Stack Engineer](https://www.104.com.tw/job/71bmz?jobsource=jolist_b_date)    | 11/27         |
|  5 | [展市華科技有限公司](https://www.104.com.tw/company/1a2x6blbgu?jobsource=jolist_b_date)       | [網頁開發工程師](https://www.104.com.tw/job/78do7?jobsource=jolist_b_date)                      | 11/27         |
|  6 | [展市華科技有限公司](https://www.104.com.tw/company/1a2x6blbgu?jobsource=jolist_b_date)       | [後端網頁工程師](https://www.104.com.tw/job/71amu?jobsource=jolist_b_date)                      | 11/27         |
|  7 | [展市華科技有限公司](https://www.104.com.tw/company/1a2x6blbgu?jobsource=jolist_b_date)       | [系統工程師](https://www.104.com.tw/job/71erc?jobsource=jolist_b_date)                        | 11/27         |
|  8 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_b_relevance) | [Python後端工程師](https://www.104.com.tw/job/76vbt?jobsource=jolist_b_relevance)             | 11/22         |
|  9 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_b_relevance)    | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_b_relevance) | 11/23         |

### Platform - 1111


|    | company                                                                          | job_title                                                          | update_time   |
|---:|:---------------------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------|
|  1 | [美超微電腦股份有限公司(Super Micro Computer, Inc.)](https://www.1111.com.tw/corp/9530088/) | [Software Engineer-TC21167](https://www.1111.com.tw/job/98544764/) | 2021-11-27    |



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
