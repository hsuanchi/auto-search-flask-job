# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                                | job_title                                                                                                      | update_time   |
|---:|:-------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [Algotech_新加坡商艾高科技股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6blc6n?jobsource=jolist_c_relevance) | [產品工程師/Python工程師](https://www.104.com.tw/job/7duf1?jobsource=jolist_c_relevance)                               | 11/15         |
|  2 | [Gorilla Technology Group_大猩猩科技股份有限公司](https://www.104.com.tw/company/wilokdc?jobsource=jolist_d_date) | [Software Engineer _ Senior Java Development](https://www.104.com.tw/job/3yh2d?jobsource=jolist_d_date)        | 11/19         |
|  3 | [Gorilla Technology Group_大猩猩科技股份有限公司](https://www.104.com.tw/company/wilokdc?jobsource=jolist_d_date) | [Software Engineer _　Jr. / Sr. Frontend Development](https://www.104.com.tw/job/6o30x?jobsource=jolist_d_date) | 11/19         |
|  4 | [九七科技股份有限公司](https://www.104.com.tw/company/1a2x6bl9vu?jobsource=jolist_d_date)                        | [Junior and Senior Data scientist](https://www.104.com.tw/job/7fde6?jobsource=jolist_d_date)                   | 11/19         |
|  5 | [九七科技股份有限公司](https://www.104.com.tw/company/1a2x6bl9vu?jobsource=jolist_d_date)                        | [Data engineer and back-end (台北AI部門)](https://www.104.com.tw/job/7fwwj?jobsource=jolist_d_date)                | 11/19         |
|  6 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_c_relevance)                   | [Python後端工程師](https://www.104.com.tw/job/76vbt?jobsource=jolist_c_relevance)                                   | 11/15         |
|  7 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_c_relevance)                      | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_c_relevance)                       | 11/15         |
|  8 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_c_relevance)                      | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_c_relevance)                       | 11/15         |
|  9 | [英屬開曼群島商萬里雲互聯股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bk5cu?jobsource=jolist_d_date)           | [Backend Engineer 後端工程師](https://www.104.com.tw/job/6xipk?jobsource=jolist_d_date)                             | 11/19         |
| 10 | [英屬開曼群島商萬里雲互聯股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bk5cu?jobsource=jolist_d_date)           | [Machine Learning Engineer 機器學習工程師 ](https://www.104.com.tw/job/6c61u?jobsource=jolist_d_date)                 | 11/19         |
| 11 | [詩嫚特集團_斯曼特企業股份有限公司](https://www.104.com.tw/company/12q3kt2w?jobsource=jolist_d_date)                   | [後端工程師](https://www.104.com.tw/job/7fywv?jobsource=jolist_d_date)                                              | 11/19         |

### Platform - 1111


|    | company                                              | job_title                                      | update_time   |
|---:|:-----------------------------------------------------|:-----------------------------------------------|:--------------|
|  1 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/) | [後端工程師](https://www.1111.com.tw/job/85012186/) | 2021-11-18    |



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
