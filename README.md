# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                               | job_title                                                                                                                | update_time   |
|---:|:--------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [威旭資訊有限公司](https://www.104.com.tw/company/1a2x6bk39d?jobsource=jolist_a_date)         | [資深後端工程師-數據組 Sr. Backend Engineer, Python](https://www.104.com.tw/job/7h65u?jobsource=jolist_a_date)                     | 12/23         |
|  2 | [威旭資訊有限公司](https://www.104.com.tw/company/1a2x6bk39d?jobsource=jolist_a_date)         | [資深全端開發工程師 Senior Full-Stack Engineer, Python](https://www.104.com.tw/job/7h64p?jobsource=jolist_a_date)                 | 12/23         |
|  3 | [思納捷科技股份有限公司](https://www.104.com.tw/company/1a2x6bk977?jobsource=jolist_a_date)      | [前端工程師(Python)](https://www.104.com.tw/job/7g8nn?jobsource=jolist_a_date)                                                | 12/23         |
|  4 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_b_relevance)  | [Python後端工程師](https://www.104.com.tw/job/76vbt?jobsource=jolist_b_relevance)                                             | 12/20         |
|  5 | [淼森科技股份有限公司](https://www.104.com.tw/company/1a2x6blm7t?jobsource=jolist_b_relevance)  | [Web App Backend Developer 後端工程師 AWS/Flask/Postman/MySQL](https://www.104.com.tw/job/7a7i3?jobsource=jolist_b_relevance) | 12/22         |
|  6 | [米約科技有限公司](https://www.104.com.tw/company/1a2x6bl97m?jobsource=jolist_a_date)         | [Python工程師](https://www.104.com.tw/job/6zey2?jobsource=jolist_a_date)                                                    | 12/23         |
|  7 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_b_relevance)     | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_b_relevance)                                 | 12/21         |
|  8 | [香港商凱渤維思有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bkgaj?jobsource=jolist_a_date) | [前端(全棧)開發人員](https://www.104.com.tw/job/6aiim?jobsource=jolist_a_date)                                                   | 12/23         |

### Platform - 1111


|    | company                                                                          | job_title                                                          | update_time   |
|---:|:---------------------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------|
|  1 | [美超微電腦股份有限公司(Super Micro Computer, Inc.)](https://www.1111.com.tw/corp/9530088/) | [Software Engineer-TC21167](https://www.1111.com.tw/job/98544764/) | 2021-12-23    |



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
