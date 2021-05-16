# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                 | job_title                                                                                           | update_time   |
|---:|:----------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------|:--------------|
|  1 | [中信金控_台灣人壽保險股份有限公司](https://www.104.com.tw/company/1mtr7vs?jobsource=2018indexpoc)      | [資訊_資深Python工程師（Senior Python Programmer）](https://www.104.com.tw/job/77drj?jobsource=2018indexpoc) | 5/15          |
|  2 | [台灣多耐福股份有限公司](https://www.104.com.tw/company/1a2x6bj2a7?jobsource=2018indexpoc)         | [軟體系統分析師 System Analyst](https://www.104.com.tw/job/78ee8?jobsource=2018indexpoc)                   | 5/15          |
|  3 | [好好投資科技股份有限公司](https://www.104.com.tw/company/1a2x6bjpjb?jobsource=2018indexpoc)        | [Backend Engineer(需熟Python、RESTful API )](https://www.104.com.tw/job/5572i?jobsource=2018indexpoc)  | 5/16          |
|  4 | [小柿智檢科技股份有限公司](https://www.104.com.tw/company/1a2x6bl77l?jobsource=2018indexpoc)        | [後端工程師 Back-End Engineer](https://www.104.com.tw/job/71bmd?jobsource=2018indexpoc)                  | 5/15          |
|  5 | [小柿智檢科技股份有限公司](https://www.104.com.tw/company/1a2x6bl77l?jobsource=2018indexpoc)        | [全端工程師 Full-Stack Engineer](https://www.104.com.tw/job/71bmz?jobsource=2018indexpoc)                | 5/15          |
|  6 | [工智聯科技股份有限公司](https://www.104.com.tw/company/1a2x6bksdx?jobsource=2018indexpoc)         | [網頁前端設計師](https://www.104.com.tw/job/6kwdo?jobsource=2018indexpoc)                                  | 5/16          |
|  7 | [新加坡商齊舵管理顧問有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bldr7?jobsource=2018indexpoc) | [影像處理軟體工程師](https://www.104.com.tw/job/77vw9?jobsource=2018indexpoc)                                | 4/30          |
|  8 | [日新軟體股份有限公司](https://www.104.com.tw/company/oi77qwg?jobsource=2018indexpoc)             | [Python 資深工程師](https://www.104.com.tw/job/6yfn5?jobsource=2018indexpoc)                             | 5/10          |
|  9 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=2018indexpoc)          | [Python後端工程師(IoT物聯網)](https://www.104.com.tw/job/76vbt?jobsource=2018indexpoc)                      | 5/13          |
| 10 | [禾新數位有限公司](https://www.104.com.tw/company/1a2x6bjs3i?jobsource=2018indexpoc)            | [[ N-01 ] Developer 開發工程師 (Python)](https://www.104.com.tw/job/6rrkz?jobsource=2018indexpoc)        | 5/15          |
| 11 | [禾新數位有限公司](https://www.104.com.tw/company/1a2x6bjs3i?jobsource=2018indexpoc)            | [[ E-C03 ] Full Stack Engineer](https://www.104.com.tw/job/76q8f?jobsource=2018indexpoc)            | 5/15          |
| 12 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=2018indexpoc)             | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=2018indexpoc)                  | 5/13          |
| 13 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=2018indexpoc)             | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=2018indexpoc)                  | 5/13          |

### Platform - 1111


|    | company                                              | job_title                                          | update_time   |
|---:|:-----------------------------------------------------|:---------------------------------------------------|:--------------|
|  1 | [億力資訊股份有限公司](https://www.1111.com.tw/corp/54937860/) | [python工程師](https://www.1111.com.tw/job/97374762/) | 2021-05-16    |
|  2 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/) | [後端工程師](https://www.1111.com.tw/job/85012186/)     | 2021-05-12    |



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
