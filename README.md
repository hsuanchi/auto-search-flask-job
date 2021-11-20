# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                                | job_title                                                                                         | update_time   |
|---:|:-------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------|:--------------|
|  1 | [Algotech_新加坡商艾高科技股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6blc6n?jobsource=jolist_a_relevance) | [產品工程師/Python工程師](https://www.104.com.tw/job/7duf1?jobsource=jolist_a_relevance)                  | 11/15         |
|  2 | [太奇雲端股份有限公司](https://www.104.com.tw/company/1a2x6bjj3y?jobsource=jolist_b_date)                        | [前端工程師 (Front-end Developer)](https://www.104.com.tw/job/7fyy6?jobsource=jolist_b_date)           | 11/20         |
|  3 | [太奇雲端股份有限公司](https://www.104.com.tw/company/1a2x6bjj3y?jobsource=jolist_b_date)                        | [資深前端工程師 (Senior Front-end Developer)](https://www.104.com.tw/job/5284c?jobsource=jolist_b_date)  | 11/20         |
|  4 | [小柿智檢科技股份有限公司](https://www.104.com.tw/company/1a2x6bl77l?jobsource=jolist_b_date)                      | [全端工程師 Full-Stack Engineer](https://www.104.com.tw/job/71bmz?jobsource=jolist_b_date)             | 11/20         |
|  5 | [小柿智檢科技股份有限公司](https://www.104.com.tw/company/1a2x6bl77l?jobsource=jolist_b_date)                      | [後端工程師 Back-End Engineer](https://www.104.com.tw/job/71bmd?jobsource=jolist_b_date)               | 11/20         |
|  6 | [思納捷科技股份有限公司](https://www.104.com.tw/company/1a2x6bk977?jobsource=jolist_a_relevance)                  | [前端工程師(Python)](https://www.104.com.tw/job/7g8nn?jobsource=jolist_a_relevance)                    | 11/19         |
|  7 | [思納捷科技股份有限公司](https://www.104.com.tw/company/1a2x6bk977?jobsource=jolist_b_date)                       | [前端工程師(Python)](https://www.104.com.tw/job/7g8nn?jobsource=jolist_b_date)                         | 11/19         |
|  8 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_a_relevance)                   | [Python後端工程師](https://www.104.com.tw/job/76vbt?jobsource=jolist_a_relevance)                      | 11/15         |
|  9 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_a_relevance)                      | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_a_relevance)          | 11/15         |
| 10 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_a_relevance)                      | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_a_relevance)          | 11/15         |
| 11 | [蓋特資訊系統股份有限公司](https://www.104.com.tw/company/1a2x6biptb?jobsource=jolist_a_relevance)                 | [Senior Machine Learning Engineer](https://www.104.com.tw/job/6e6r8?jobsource=jolist_a_relevance) | 11/15         |

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
