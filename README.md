# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                       | job_title                                                                                               | update_time   |
|---:|:----------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [伊諾科技有限公司](https://www.104.com.tw/company/1a2x6bkxph?jobsource=2018indexpoc)                  | [(真摯徵求) Python後端工程師](https://www.104.com.tw/job/70asp?jobsource=2018indexpoc)                           | 5/27          |
|  2 | [大數據股份有限公司](https://www.104.com.tw/company/1a2x6bjjhc?jobsource=2018indexpoc)                 | [分析研發工程師: AI, Deep Learning, Machine Learning](https://www.104.com.tw/job/54ffa?jobsource=2018indexpoc) | 5/27          |
|  3 | [新加坡商齊舵管理顧問有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bldr7?jobsource=jolist_b_relevance) | [影像處理軟體工程師](https://www.104.com.tw/job/77vw9?jobsource=jolist_b_relevance)                              | 4/30          |
|  4 | [日新軟體股份有限公司](https://www.104.com.tw/company/oi77qwg?jobsource=jolist_b_relevance)             | [Python 資深工程師](https://www.104.com.tw/job/6yfn5?jobsource=jolist_b_relevance)                           | 5/25          |
|  5 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=2018indexpoc)                | [Python後端工程師(IoT物聯網)](https://www.104.com.tw/job/76vbt?jobsource=2018indexpoc)                          | 5/27          |
|  6 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_b_relevance)          | [Python後端工程師(IoT物聯網)](https://www.104.com.tw/job/76vbt?jobsource=jolist_b_relevance)                    | 5/27          |
|  7 | [永昕生物醫藥股份有限公司](https://www.104.com.tw/company/5xfw7xk?jobsource=2018indexpoc)                 | [細胞產程開發研究員(台北)](https://www.104.com.tw/job/6ujnv?jobsource=2018indexpoc)                                | 5/27          |
|  8 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_b_relevance)             | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_b_relevance)                | 5/27          |
|  9 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_b_relevance)             | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_b_relevance)                | 5/27          |
| 10 | [英商引達取有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bkz0n?jobsource=2018indexpoc)            | [[台北] Data Engineer](https://www.104.com.tw/job/6pki0?jobsource=2018indexpoc)                           | 5/27          |
| 11 | [英商引達取有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bkz0n?jobsource=2018indexpoc)            | [[台北]前端/全端工程師](https://www.104.com.tw/job/6pki1?jobsource=2018indexpoc)                                 | 5/27          |
| 12 | [華翰物產實業股份有限公司](https://www.104.com.tw/company/10xb8hsw?jobsource=2018indexpoc)                | [資深資料科學家(Senior Data Scientist)](https://www.104.com.tw/job/72vx2?jobsource=2018indexpoc)               | 5/27          |

### Platform - 1111


|    | company                                              | job_title                                          | update_time   |
|---:|:-----------------------------------------------------|:---------------------------------------------------|:--------------|
|  1 | [億力資訊股份有限公司](https://www.1111.com.tw/corp/54937860/) | [python工程師](https://www.1111.com.tw/job/97374762/) | 2021-05-21    |
|  2 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/) | [後端工程師](https://www.1111.com.tw/job/85012186/)     | 2021-05-27    |



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
