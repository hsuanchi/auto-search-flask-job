# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                 | job_title                                                                                                                 | update_time   |
|---:|:----------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [今時科技股份有限公司](https://www.104.com.tw/company/1a2x6bl2u4?jobsource=2018indexpoc)          | [網頁開發工程師  * 歡迎兼職論件計酬](https://www.104.com.tw/job/75jgv?jobsource=2018indexpoc)                                            | 6/26          |
|  2 | [今時科技股份有限公司](https://www.104.com.tw/company/1a2x6bl2u4?jobsource=2018indexpoc)          | [網頁前端程式設計師](https://www.104.com.tw/job/79aqn?jobsource=2018indexpoc)                                                      | 6/26          |
|  3 | [博思資訊管理顧問有限公司](https://www.104.com.tw/company/1a2x6blhw5?jobsource=2018indexpoc)        | [Python工程師(可遠端工作)](https://www.104.com.tw/job/78f5b?jobsource=2018indexpoc)                                               | 6/26          |
|  4 | [宏佳騰動力科技股份有限公司](https://www.104.com.tw/company/111bwt14?jobsource=2018indexpoc)         | [Python全端工程師](https://www.104.com.tw/job/6s9aa?jobsource=2018indexpoc)                                                    | 6/25          |
|  5 | [小柿智檢科技股份有限公司](https://www.104.com.tw/company/1a2x6bl77l?jobsource=2018indexpoc)        | [後端工程師 Back-End Engineer](https://www.104.com.tw/job/71bmd?jobsource=2018indexpoc)                                        | 6/26          |
|  6 | [小柿智檢科技股份有限公司](https://www.104.com.tw/company/1a2x6bl77l?jobsource=2018indexpoc)        | [全端工程師 Full-Stack Engineer](https://www.104.com.tw/job/71bmz?jobsource=2018indexpoc)                                      | 6/26          |
|  7 | [愛卡拉互動媒體股份有限公司](https://www.104.com.tw/company/oi6pygw?jobsource=2018indexpoc)          | [【iKala Cloud】資深 資料工程師(CDP) Senior Data Engineer, CDP](https://www.104.com.tw/job/79zex?jobsource=2018indexpoc)           | 6/25          |
|  8 | [新加坡商蝦皮娛樂電商有限公司台灣分公司](https://www.104.com.tw/company/1a2x6blcz2?jobsource=2018indexpoc) | [Front-end Web Developer 網頁前端工程師 / Business Intelligence 數據分析部門](https://www.104.com.tw/job/72m5h?jobsource=2018indexpoc) | 6/25          |
|  9 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_b_relevance)    | [Python後端開發工程師(DevOps整合平台)](https://www.104.com.tw/job/7asvo?jobsource=jolist_b_relevance)                                | 6/24          |
| 10 | [禾新數位有限公司](https://www.104.com.tw/company/1a2x6bjs3i?jobsource=2018indexpoc)            | [[ E-C03 ] Full Stack Engineer（線上面試+因應疫情居家上班）](https://www.104.com.tw/job/76q8f?jobsource=2018indexpoc)                   | 6/26          |
| 11 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_b_relevance)       | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_b_relevance)                                  | 6/18          |
| 12 | [英商引達取有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bkz0n?jobsource=2018indexpoc)      | [【台北】Data Engineer](https://www.104.com.tw/job/6pki0?jobsource=2018indexpoc)                                              | 6/25          |
| 13 | [萊鎂醫療器材股份有限公司](https://www.104.com.tw/company/bkgh1dc?jobsource=jolist_b_relevance)     | [雲端應用工程師](https://www.104.com.tw/job/791cq?jobsource=jolist_b_relevance)                                                  | 6/23          |
| 14 | [長興材料工業股份有限公司](https://www.104.com.tw/company/ylywbj4?jobsource=2018indexpoc)           | [製程工程師(製程技術)-屏東枋寮](https://www.104.com.tw/job/4izei?jobsource=2018indexpoc)                                               | 6/25          |

### Platform - 1111


|    | company                                              | job_title                                            | update_time   |
|---:|:-----------------------------------------------------|:-----------------------------------------------------|:--------------|
|  1 | [億力資訊股份有限公司](https://www.1111.com.tw/corp/54937860/) | [python工程師](https://www.1111.com.tw/job/97374762/)   | 2021-06-23    |
|  2 | [美維科技股份有限公司](https://www.1111.com.tw/corp/69592323/) | [【就業雄青】後端工程師](https://www.1111.com.tw/job/97446846/) | 2021-06-24    |
|  3 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/) | [後端工程師](https://www.1111.com.tw/job/85012186/)       | 2021-06-26    |



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
