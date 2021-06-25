# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                 | job_title                                                                                                                 | update_time   |
|---:|:----------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [宏佳騰動力科技股份有限公司](https://www.104.com.tw/company/111bwt14?jobsource=2018indexpoc)         | [Python全端工程師](https://www.104.com.tw/job/6s9aa?jobsource=2018indexpoc)                                                    | 6/25          |
|  2 | [愛卡拉互動媒體股份有限公司](https://www.104.com.tw/company/oi6pygw?jobsource=2018indexpoc)          | [【iKala Cloud】資深 資料工程師(CDP) Senior Data Engineer, CDP](https://www.104.com.tw/job/79zex?jobsource=2018indexpoc)           | 6/25          |
|  3 | [新加坡商蝦皮娛樂電商有限公司台灣分公司](https://www.104.com.tw/company/1a2x6blcz2?jobsource=2018indexpoc) | [Front-end Web Developer 網頁前端工程師 / Business Intelligence 數據分析部門](https://www.104.com.tw/job/72m5h?jobsource=2018indexpoc) | 6/25          |
|  4 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_b_relevance)    | [Python後端開發工程師(DevOps整合平台)](https://www.104.com.tw/job/7asvo?jobsource=jolist_b_relevance)                                | 6/24          |
|  5 | [英商引達取有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bkz0n?jobsource=2018indexpoc)      | [【台北】Data Engineer](https://www.104.com.tw/job/6pki0?jobsource=2018indexpoc)                                              | 6/25          |
|  6 | [長興材料工業股份有限公司](https://www.104.com.tw/company/ylywbj4?jobsource=2018indexpoc)           | [製程工程師(製程技術)-屏東枋寮](https://www.104.com.tw/job/4izei?jobsource=2018indexpoc)                                               | 6/25          |

### Platform - 1111


|    | company                                              | job_title                                            | update_time   |
|---:|:-----------------------------------------------------|:-----------------------------------------------------|:--------------|
|  1 | [億力資訊股份有限公司](https://www.1111.com.tw/corp/54937860/) | [python工程師](https://www.1111.com.tw/job/97374762/)   | 2021-06-23    |
|  2 | [美維科技股份有限公司](https://www.1111.com.tw/corp/69592323/) | [【就業雄青】後端工程師](https://www.1111.com.tw/job/97446846/) | 2021-06-24    |
|  3 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/) | [後端工程師](https://www.1111.com.tw/job/85012186/)       | 2021-06-21    |



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
