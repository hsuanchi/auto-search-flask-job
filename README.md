# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                        | job_title                                                                                       | update_time   |
|---:|:-----------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------|:--------------|
|  1 | [Pinkoi_香港商果翼科技股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6biidu?jobsource=jolist_b_date) | [Backend Engineer](https://www.104.com.tw/job/7eeac?jobsource=jolist_b_date)                    | 10/07         |
|  2 | [亞達科技股份有限公司](https://www.104.com.tw/company/1a2x6bkc3s?jobsource=jolist_b_date)                | [System Integration/backend engineer](https://www.104.com.tw/job/7en5d?jobsource=jolist_b_date) | 10/07         |
|  3 | [德義資訊股份有限公司](https://www.104.com.tw/company/oe84aqo?jobsource=jolist_b_date)                   | [Backend 系統開發工程師](https://www.104.com.tw/job/7awmz?jobsource=jolist_b_date)                     | 10/07         |
|  4 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_a_relevance)           | [Python後端開發工程師 (DevOps整合平台)](https://www.104.com.tw/job/7asvo?jobsource=jolist_a_relevance)     | 10/06         |
|  5 | [昱峰智能大數據科技股份有限公司](https://www.104.com.tw/company/1a2x6bkbn6?jobsource=jolist_b_date)           | [RD[資深]後端工程師](https://www.104.com.tw/job/5x0lo?jobsource=jolist_b_date)                         | 10/07         |
|  6 | [昱峰智能大數據科技股份有限公司](https://www.104.com.tw/company/1a2x6bkbn6?jobsource=jolist_b_date)           | [RD[資深]全端工程師/全端工程技術經理](https://www.104.com.tw/job/62za4?jobsource=jolist_b_date)                | 10/07         |
|  7 | [杰倫智能科技股份有限公司](https://www.104.com.tw/company/1a2x6bkirw?jobsource=jolist_b_date)              | [資深網頁前端開發工程師(AI平台)](https://www.104.com.tw/job/6hxnt?jobsource=jolist_b_date)                   | 10/07         |
|  8 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_a_relevance)              | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_a_relevance)        | 10/06         |
|  9 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_a_relevance)              | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_a_relevance)        | 10/06         |
| 10 | [萊泀有限公司](https://www.104.com.tw/company/1a2x6blg3t?jobsource=jolist_a_relevance)               | [Python (Django、Flask)程式設計師](https://www.104.com.tw/job/7cs5e?jobsource=jolist_a_relevance)     | 10/06         |

### Platform - 1111


|    | company                                                                    | job_title                                                                                                 | update_time   |
|---:|:---------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [(獵頭)Accurate愛客獵股份有限公司(1111 高階獵才)](https://www.1111.com.tw/corp/69647966/) | [直播平台_Senior Backend Developer(3002871)](https://www.1111.com.tw/job/85960420/)                           | 2020-05-15    |
|  2 | [(獵頭)Accurate愛客獵股份有限公司(1111 高階獵才)](https://www.1111.com.tw/corp/69647966/) | [Dev (Develop Engineer)前端_知名電子公司 (3005070)](https://www.1111.com.tw/job/97460023/)                        | 2021-07-05    |
|  3 | [(獵頭)Accurate愛客獵股份有限公司(1111 高階獵才)](https://www.1111.com.tw/corp/69647966/) | [Dev (Develop Engineer)後端_知名電子公司 (3005117)](https://www.1111.com.tw/job/97460074/)                        | 2021-07-05    |
|  4 | [(獵頭)Accurate愛客獵股份有限公司(1111 高階獵才)](https://www.1111.com.tw/corp/69647966/) | [Dev (Technical Lead)_知名電子公司 (3005066)](https://www.1111.com.tw/job/97459998/)                            | 2021-07-05    |
|  5 | [中租迪和股份有限公司](https://www.1111.com.tw/corp/2850037/)                        | [【中租超利士】中台架構師](https://www.1111.com.tw/job/97507405/)                                                     | 2021-10-07    |
|  6 | [台灣美光晶圓科技股份有限公司](https://www.1111.com.tw/corp/9622349/)                    | [【2021畢業生報名專區】Data Engineer, Smart MFG & AI (Taichung or Taoyuan)](https://www.1111.com.tw/job/97430572/) | 2021-10-06    |
|  7 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/)                       | [後端工程師](https://www.1111.com.tw/job/85012186/)                                                            | 2021-10-04    |



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
