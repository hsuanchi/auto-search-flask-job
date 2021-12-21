# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                                | job_title                                                                                                                | update_time   |
|---:|:-------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [Gorilla Technology Group_大猩猩科技股份有限公司](https://www.104.com.tw/company/wilokdc?jobsource=jolist_b_date) | [Software Engineer _　Jr. / Sr. Frontend Development](https://www.104.com.tw/job/6o30x?jobsource=jolist_b_date)           | 12/21         |
|  2 | [九七科技股份有限公司](https://www.104.com.tw/company/1a2x6bl9vu?jobsource=jolist_b_date)                        | [Junior and Senior Data scientist](https://www.104.com.tw/job/7fde6?jobsource=jolist_b_date)                             | 12/21         |
|  3 | [九七科技股份有限公司](https://www.104.com.tw/company/1a2x6bl9vu?jobsource=jolist_b_date)                        | [python data engineer (python 後端資料工程師) (台北AI部門)](https://www.104.com.tw/job/7fwwj?jobsource=jolist_b_date)               | 12/21         |
|  4 | [光禾感知科技股份有限公司](https://www.104.com.tw/company/1a2x6bks9s?jobsource=jolist_b_date)                      | [Python後端工程師](https://www.104.com.tw/job/71j4l?jobsource=jolist_b_date)                                                  | 12/21         |
|  5 | [思納捷科技股份有限公司](https://www.104.com.tw/company/1a2x6bk977?jobsource=jolist_b_relevance)                  | [前端工程師(Python)](https://www.104.com.tw/job/7g8nn?jobsource=jolist_b_relevance)                                           | 12/16         |
|  6 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_b_relevance)                   | [Python後端工程師](https://www.104.com.tw/job/76vbt?jobsource=jolist_b_relevance)                                             | 12/20         |
|  7 | [歐立威科技股份有限公司](https://www.104.com.tw/company/b8gl75c?jobsource=jolist_b_date)                          | [軟體開發工程師](https://www.104.com.tw/job/6q2ao?jobsource=jolist_b_date)                                                      | 12/21         |
|  8 | [淼森科技股份有限公司](https://www.104.com.tw/company/1a2x6blm7t?jobsource=jolist_b_relevance)                   | [Web App Backend Developer 後端工程師 AWS/Flask/Postman/MySQL](https://www.104.com.tw/job/7a7i3?jobsource=jolist_b_relevance) | 12/15         |
|  9 | [童綜合醫療社團法人童綜合醫院](https://www.104.com.tw/company/kw8xsls?jobsource=jolist_b_date)                       | [資訊部Python 工程師](https://www.104.com.tw/job/6upji?jobsource=jolist_b_date)                                                | 12/21         |
| 10 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_b_date)                           | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_b_date)                                      | 12/21         |
| 11 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_b_relevance)                      | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_b_relevance)                                 | 12/21         |
| 12 | [艾酷互動股份有限公司](https://www.104.com.tw/company/1a2x6bkq17?jobsource=jolist_b_date)                        | [數據⼯程師](https://www.104.com.tw/job/7275w?jobsource=jolist_b_date)                                                        | 12/21         |

### Platform - 1111


|    | company                                                                          | job_title                                                          | update_time   |
|---:|:---------------------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------|
|  1 | [美超微電腦股份有限公司(Super Micro Computer, Inc.)](https://www.1111.com.tw/corp/9530088/) | [Software Engineer-TC21167](https://www.1111.com.tw/job/98544764/) | 2021-12-16    |



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
