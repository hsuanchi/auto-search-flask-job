# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                                | job_title                                                                                   | update_time   |
|---:|:-------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------|:--------------|
|  1 | [Algotech_新加坡商艾高科技股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6blc6n?jobsource=jolist_c_relevance) | [產品工程師/Python工程師](https://www.104.com.tw/job/7duf1?jobsource=jolist_c_relevance)            | 11/03         |
|  2 | [九七科技股份有限公司](https://www.104.com.tw/company/1a2x6bl9vu?jobsource=jolist_c_relevance)                   | [資料科學家](https://www.104.com.tw/job/7fde6?jobsource=jolist_c_relevance)                      | 11/04         |
|  3 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_c_relevance)                      | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_c_relevance)    | 11/08         |
|  4 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_c_relevance)                      | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_c_relevance)    | 11/08         |
|  5 | [財團法人生物技術開發中心](https://www.104.com.tw/company/2kmb67c?jobsource=jolist_c_relevance)                    | [【生物工程組】副研究員](https://www.104.com.tw/job/7dqek?jobsource=jolist_c_relevance)                | 11/08         |
|  6 | [迪威智能股份有限公司](https://www.104.com.tw/company/1a2x6bl035?jobsource=jolist_d_date)                        | [Senior/Junior AI Engineer AI工程師](https://www.104.com.tw/job/7ecqj?jobsource=jolist_d_date) | 11/08         |

### Platform - 1111


|    | company                                              | job_title                                                | update_time   |
|---:|:-----------------------------------------------------|:---------------------------------------------------------|:--------------|
|  1 | [華新麗華股份有限公司](https://www.1111.com.tw/corp/1845183/)  | [先進排程開發工程師 (台中廠)](https://www.1111.com.tw/job/98520581/) | 2021-11-08    |
|  2 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/) | [後端工程師](https://www.1111.com.tw/job/85012186/)           | 2021-11-08    |



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
