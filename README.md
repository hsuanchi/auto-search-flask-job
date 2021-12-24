# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                      | job_title                                                                                                                | update_time   |
|---:|:---------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [吉音資訊有限公司](https://www.104.com.tw/company/10uhacsw?jobsource=jolist_d_date)                  | [高薪徵PHP程式開發人才(專案聘請 2-3年職(視情況再延長 ;Cable或電信業))](https://www.104.com.tw/job/2j2kp?jobsource=jolist_d_date)                  | 12/24         |
|  2 | [太奇雲端股份有限公司](https://www.104.com.tw/company/1a2x6bjj3y?jobsource=jolist_d_date)              | [前端工程師 (Front-end Developer)](https://www.104.com.tw/job/7fyy6?jobsource=jolist_d_date)                                  | 12/24         |
|  3 | [小柿智檢科技股份有限公司](https://www.104.com.tw/company/1a2x6bl77l?jobsource=jolist_d_date)            | [後端工程師 Back-End Engineer](https://www.104.com.tw/job/71bmd?jobsource=jolist_d_date)                                      | 12/25         |
|  4 | [小柿智檢科技股份有限公司](https://www.104.com.tw/company/1a2x6bl77l?jobsource=jolist_d_date)            | [全端工程師 Full-Stack Engineer](https://www.104.com.tw/job/71bmz?jobsource=jolist_d_date)                                    | 12/25         |
|  5 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_c_relevance)         | [Python後端工程師](https://www.104.com.tw/job/76vbt?jobsource=jolist_c_relevance)                                             | 12/20         |
|  6 | [淼森科技股份有限公司](https://www.104.com.tw/company/1a2x6blm7t?jobsource=jolist_c_relevance)         | [Web App Backend Developer 後端工程師 AWS/Flask/Postman/MySQL](https://www.104.com.tw/job/7a7i3?jobsource=jolist_c_relevance) | 12/22         |
|  7 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_c_relevance)            | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_c_relevance)                                 | 12/21         |
|  8 | [英屬開曼群島商萬里雲互聯股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bk5cu?jobsource=jolist_d_date) | [Machine Learning Engineer 機器學習工程師 ](https://www.104.com.tw/job/6c61u?jobsource=jolist_d_date)                           | 12/24         |
|  9 | [雙成數位行銷股份有限公司](https://www.104.com.tw/company/1a2x6bkqua?jobsource=jolist_d_date)            | [【Python工程師】](https://www.104.com.tw/job/7ftte?jobsource=jolist_d_date)                                                  | 12/24         |

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
