# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                     | job_title                                                                                                                | update_time   |
|---:|:--------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [Deep Sentinel_亞齊國際有限公司](https://www.104.com.tw/company/1a2x6blbly?jobsource=jolist_c_date) | [Full Stack Engineer 全端工程師](https://www.104.com.tw/job/7e67z?jobsource=jolist_c_date)                                    | 1/21          |
|  2 | [太奇雲端股份有限公司](https://www.104.com.tw/company/1a2x6bjj3y?jobsource=jolist_c_date)             | [前端工程師 (Front-end Developer)](https://www.104.com.tw/job/7fyy6?jobsource=jolist_c_date)                                  | 1/21          |
|  3 | [好好證券股份有限公司](https://www.104.com.tw/company/1a2x6bjpjb?jobsource=jolist_c_date)             | [Backend Engineer(熟 Python、RESTful API )](https://www.104.com.tw/job/5572i?jobsource=jolist_c_date)                      | 1/21          |
|  4 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_b_relevance)        | [Python後端工程師](https://www.104.com.tw/job/76vbt?jobsource=jolist_b_relevance)                                             | 1/19          |
|  5 | [智勝科技股份有限公司](https://www.104.com.tw/company/10ukqxdc?jobsource=jolist_c_date)               | [211111 資訊工程師](https://www.104.com.tw/job/7gnhc?jobsource=jolist_c_date)                                                 | 1/21          |
|  6 | [淼森科技股份有限公司](https://www.104.com.tw/company/1a2x6blm7t?jobsource=jolist_b_relevance)        | [Web App Backend Developer 後端工程師 AWS/Flask/Postman/MySQL](https://www.104.com.tw/job/7a7i3?jobsource=jolist_b_relevance) | 1/15          |
|  7 | [雲端互動股份有限公司](https://www.104.com.tw/company/bjd57go?jobsource=jolist_b_relevance)           | [Python Back-End Developer 後端工程師_Flask](https://www.104.com.tw/job/73trn?jobsource=jolist_b_relevance)                   | 1/20          |
|  8 | [霖園關係企業_神坊資訊股份有限公司](https://www.104.com.tw/company/wdapdfc?jobsource=jolist_c_date)         | [後端開發工程師 (Backend Engineer) - 小樹生活圈](https://www.104.com.tw/job/7f5jf?jobsource=jolist_c_date)                           | 1/21          |

### Platform - 1111


|    | company                                                                          | job_title                                                                                                | update_time   |
|---:|:---------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [(獵頭)Accurate愛客獵股份有限公司(1111 高階獵才)](https://www.1111.com.tw/corp/69647966/)       | [直播平台_Senior Backend Developer(3002871)](https://www.1111.com.tw/job/85960420/)                          | 2020-05-15    |
|  2 | [台灣美光晶圓科技股份有限公司](https://www.1111.com.tw/corp/9622349/)                          | [Full Stack SMAI Solution Developer](https://www.1111.com.tw/job/98479119/)                              | 2022-01-19    |
|  3 | [沛思坦網路股份有限公司](https://www.1111.com.tw/corp/73457881/)                            | [【台北內湖】資深Python後端工程師 Python Back-end Engineer (Senior) (月薪7萬-9萬)](https://www.1111.com.tw/job/97541124/) | 2022-01-21    |
|  4 | [美超微電腦股份有限公司(Super Micro Computer, Inc.)](https://www.1111.com.tw/corp/9530088/) | [Software Engineer-TC21167](https://www.1111.com.tw/job/98544764/)                                       | 2022-01-19    |



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
