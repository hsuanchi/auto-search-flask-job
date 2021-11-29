# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                                     | job_title                                                                                                             | update_time   |
|---:|:------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [Gorilla Technology Group_大猩猩科技股份有限公司](https://www.104.com.tw/company/wilokdc?jobsource=jolist_a_relevance) | [Software Engineer _　Jr. / Sr. Frontend Development](https://www.104.com.tw/job/6o30x?jobsource=jolist_a_relevance)   | 11/29         |
|  2 | [Gorilla Technology Group_大猩猩科技股份有限公司](https://www.104.com.tw/company/wilokdc?jobsource=jolist_b_date)      | [Software Engineer _　Jr. / Sr. Frontend Development](https://www.104.com.tw/job/6o30x?jobsource=jolist_b_date)        | 11/29         |
|  3 | [Gorilla Technology Group_大猩猩科技股份有限公司](https://www.104.com.tw/company/wilokdc?jobsource=jolist_b_date)      | [Software Engineer _ Senior Java Development](https://www.104.com.tw/job/3yh2d?jobsource=jolist_b_date)               | 11/29         |
|  4 | [中國醫藥大學附設醫院](https://www.104.com.tw/company/o5x51w0?jobsource=jolist_b_date)                                | [10R0-大數據中心 系統工程師](https://www.104.com.tw/job/7ancv?jobsource=jolist_b_date)                                          | 11/29         |
|  5 | [光禾感知科技股份有限公司](https://www.104.com.tw/company/1a2x6bks9s?jobsource=jolist_b_date)                           | [Python後端工程師](https://www.104.com.tw/job/71j4l?jobsource=jolist_b_date)                                               | 11/29         |
|  6 | [太奇雲端股份有限公司](https://www.104.com.tw/company/1a2x6bjj3y?jobsource=jolist_b_date)                             | [前端工程師 (Front-end Developer)](https://www.104.com.tw/job/7fyy6?jobsource=jolist_b_date)                               | 11/29         |
|  7 | [宏佳騰動力科技股份有限公司](https://www.104.com.tw/company/111bwt14?jobsource=jolist_b_date)                            | [Python全端工程師](https://www.104.com.tw/job/6s9aa?jobsource=jolist_b_date)                                               | 11/29         |
|  8 | [宏達電 HTC Corporation_宏達國際電子股份有限公司](https://www.104.com.tw/company/7co2xio?jobsource=jolist_b_date)          | [(Vive R&amp;D) Vive - Machine Learning Scientist - J01803](https://www.104.com.tw/job/7er6w?jobsource=jolist_b_date) | 11/29         |
|  9 | [思納捷科技股份有限公司](https://www.104.com.tw/company/1a2x6bk977?jobsource=jolist_a_relevance)                       | [前端工程師(Python)](https://www.104.com.tw/job/7g8nn?jobsource=jolist_a_relevance)                                        | 11/19         |
| 10 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_a_relevance)                        | [Python後端工程師](https://www.104.com.tw/job/76vbt?jobsource=jolist_a_relevance)                                          | 11/29         |
| 11 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_b_date)                             | [Python後端工程師](https://www.104.com.tw/job/76vbt?jobsource=jolist_b_date)                                               | 11/29         |
| 12 | [澤喆數位科技股份有限公司](https://www.104.com.tw/company/1a2x6bl2y0?jobsource=jolist_b_date)                           | [後端工程師(Back-end Engineer )](https://www.104.com.tw/job/6uvmx?jobsource=jolist_b_date)                                 | 11/29         |
| 13 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_a_relevance)                           | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_a_relevance)                              | 11/23         |
| 14 | [迪威智能股份有限公司](https://www.104.com.tw/company/1a2x6bl035?jobsource=jolist_b_date)                             | [Senior/Junior AI Engineer AI工程師](https://www.104.com.tw/job/7ecqj?jobsource=jolist_b_date)                           | 11/29         |
| 15 | [迪威智能股份有限公司](https://www.104.com.tw/company/1a2x6bl035?jobsource=jolist_b_date)                             | [Senior/Junior Back-end Engineer 後端工程師](https://www.104.com.tw/job/7ecqo?jobsource=jolist_b_date)                     | 11/29         |

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
