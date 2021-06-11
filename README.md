# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                       | job_title                                                                                     | update_time   |
|---:|:----------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|:--------------|
|  1 | [德義資訊股份有限公司](https://www.104.com.tw/company/oe84aqo?jobsource=jolist_a_relevance)             | [Backend 系統開發工程師](https://www.104.com.tw/job/7awmz?jobsource=jolist_a_relevance)              | 6/08          |
|  2 | [新加坡商齊舵管理顧問有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bldr7?jobsource=jolist_a_relevance) | [影像處理軟體工程師](https://www.104.com.tw/job/77vw9?jobsource=jolist_a_relevance)                    | 4/30          |
|  3 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_a_relevance)          | [Python後端工程師](https://www.104.com.tw/job/76vbt?jobsource=jolist_a_relevance)                  | 6/10          |
|  4 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_a_relevance)          | [Python爬蟲工程師(高雄)](https://www.104.com.tw/job/7aydm?jobsource=jolist_a_relevance)              | 6/10          |
|  5 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_a_relevance)          | [Python爬蟲工程師(台北)](https://www.104.com.tw/job/7aydt?jobsource=jolist_a_relevance)              | 6/10          |
|  6 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_a_relevance)          | [Python後端開發工程師(DevOps整合平台)](https://www.104.com.tw/job/7asvo?jobsource=jolist_a_relevance)    | 6/10          |
|  7 | [桔畝智慧股份有限公司](https://www.104.com.tw/company/1a2x6blm8y?jobsource=2018indexpoc)                | [Back-End Development Engineer後端工程師](https://www.104.com.tw/job/7a80a?jobsource=2018indexpoc) | 6/11          |
|  8 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_a_relevance)             | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_a_relevance)      | 6/10          |
|  9 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_a_relevance)             | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_a_relevance)      | 6/10          |
| 10 | [英商引達取有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bkz0n?jobsource=2018indexpoc)            | [【台北】前端/全端工程師](https://www.104.com.tw/job/6pki1?jobsource=2018indexpoc)                       | 6/11          |
| 11 | [英商引達取有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bkz0n?jobsource=2018indexpoc)            | [【台北】Data Engineer](https://www.104.com.tw/job/6pki0?jobsource=2018indexpoc)                  | 6/11          |

### Platform - 1111


|    | company                                                                      | job_title                                                                                                 | update_time   |
|---:|:-----------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [(派遣)新加坡商立可人事顧問有限公司(Recruit Express)](https://www.1111.com.tw/corp/9992537/) | [AL-Python Engineer，外商網路公司，年薪800K~1.2M](https://www.1111.com.tw/job/91212698/)                            | 2021-05-14    |
|  2 | [(獵頭)1111獵才顧問中心](https://www.1111.com.tw/corp/69647966/)                     | [直播平台_Senior Backend Developer(3002871)](https://www.1111.com.tw/job/85960420/)                           | 2020-05-15    |
|  3 | [億力資訊股份有限公司](https://www.1111.com.tw/corp/54937860/)                         | [python工程師](https://www.1111.com.tw/job/97374762/)                                                        | 2021-06-08    |
|  4 | [台灣美光晶圓科技股份有限公司](https://www.1111.com.tw/corp/9622349/)                      | [【2021畢業生報名專區】Data Engineer, Smart MFG & AI (Taichung or Taoyuan)](https://www.1111.com.tw/job/97430572/) | 2021-06-05    |
|  5 | [台灣美光晶圓科技股份有限公司](https://www.1111.com.tw/corp/9622349/)                      | [【桃園/台中廠擴大招募】SR Data Engineer, Smart MFG & AI](https://www.1111.com.tw/job/97430508/)                     | 2021-06-05    |
|  6 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/)                         | [後端工程師](https://www.1111.com.tw/job/85012186/)                                                            | 2021-06-11    |



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
