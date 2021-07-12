# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                       | job_title                                                                                               | update_time   |
|---:|:----------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [亞洲指標數位行銷顧問股份有限公司](https://www.104.com.tw/company/d8qa7g0?jobsource=2018indexpoc)             | [[RD] 後端工程師(backend engineer)](https://www.104.com.tw/job/65dkg?jobsource=2018indexpoc)                 | 7/12          |
|  2 | [博思資訊管理顧問有限公司](https://www.104.com.tw/company/1a2x6blhw5?jobsource=2018indexpoc)              | [Python工程師(可遠端工作)](https://www.104.com.tw/job/78f5b?jobsource=2018indexpoc)                             | 7/12          |
|  3 | [大數據股份有限公司](https://www.104.com.tw/company/1a2x6bjjhc?jobsource=2018indexpoc)                 | [分析研發工程師: AI, Deep Learning, Machine Learning](https://www.104.com.tw/job/54ffa?jobsource=2018indexpoc) | 7/12          |
|  4 | [宏佳騰動力科技股份有限公司](https://www.104.com.tw/company/111bwt14?jobsource=2018indexpoc)               | [Python全端工程師](https://www.104.com.tw/job/6s9aa?jobsource=2018indexpoc)                                  | 7/12          |
|  5 | [德義資訊股份有限公司](https://www.104.com.tw/company/oe84aqo?jobsource=jolist_a_relevance)             | [Backend 系統開發工程師](https://www.104.com.tw/job/7awmz?jobsource=jolist_a_relevance)                        | 7/06          |
|  6 | [新加坡商齊舵管理顧問有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bldr7?jobsource=jolist_a_relevance) | [影像處理軟體工程師](https://www.104.com.tw/job/77vw9?jobsource=jolist_a_relevance)                              | 4/30          |
|  7 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_a_relevance)          | [Python後端開發工程師(DevOps整合平台)](https://www.104.com.tw/job/7asvo?jobsource=jolist_a_relevance)              | 7/08          |
|  8 | [瑪樂愛迪科技股份有限公司](https://www.104.com.tw/company/1a2x6bld1f?jobsource=2018indexpoc)              | [Data Engineer / Python（Remote）](https://www.104.com.tw/job/77ymq?jobsource=2018indexpoc)               | 7/12          |
|  9 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_a_relevance)             | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_a_relevance)                | 7/09          |
| 10 | [美商美創資通股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bjdsb?jobsource=2018indexpoc)         | [資深Web後端工程師](https://www.104.com.tw/job/6y6f0?jobsource=2018indexpoc)                                   | 7/12          |
| 11 | [蓋特資訊系統股份有限公司](https://www.104.com.tw/company/1a2x6biptb?jobsource=jolist_a_relevance)        | [Senior Machine Learning Engineer](https://www.104.com.tw/job/6e6r8?jobsource=jolist_a_relevance)       | 6/04          |
| 12 | [薩摩亞商連影科技有限公司台灣分公司](https://www.104.com.tw/company/1a2x6blcyw?jobsource=2018indexpoc)         | [(Sr./Jr.) Backend Developer 後端工程師](https://www.104.com.tw/job/72kyd?jobsource=2018indexpoc)            | 7/12          |

### Platform - 1111


|    | company                                              | job_title                                          | update_time   |
|---:|:-----------------------------------------------------|:---------------------------------------------------|:--------------|
|  1 | [億力資訊股份有限公司](https://www.1111.com.tw/corp/54937860/) | [python工程師](https://www.1111.com.tw/job/97374762/) | 2021-07-06    |
|  2 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/) | [後端工程師](https://www.1111.com.tw/job/85012186/)     | 2021-07-11    |



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
