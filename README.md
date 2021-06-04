# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                       | job_title                                                                                     | update_time   |
|---:|:----------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|:--------------|
|  1 | [新加坡商齊舵管理顧問有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bldr7?jobsource=jolist_b_relevance) | [影像處理軟體工程師](https://www.104.com.tw/job/77vw9?jobsource=jolist_b_relevance)                    | 4/30          |
|  2 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_b_relevance)          | [Python後端工程師(IoT物聯網)](https://www.104.com.tw/job/76vbt?jobsource=jolist_b_relevance)          | 6/03          |
|  3 | [桔畝智慧股份有限公司](https://www.104.com.tw/company/1a2x6blm8y?jobsource=2018indexpoc)                | [Back-End Development Engineer後端工程師](https://www.104.com.tw/job/7a80a?jobsource=2018indexpoc) | 6/05          |
|  4 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_b_relevance)             | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_b_relevance)      | 6/03          |
|  5 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_b_relevance)             | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_b_relevance)      | 6/03          |
|  6 | [英商引達取有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bkz0n?jobsource=2018indexpoc)            | [【台北】前端/全端工程師](https://www.104.com.tw/job/6pki1?jobsource=2018indexpoc)                       | 6/04          |

### Platform - 1111


|    | company                                                                      | job_title                                                                      | update_time   |
|---:|:-----------------------------------------------------------------------------|:-------------------------------------------------------------------------------|:--------------|
|  1 | [(派遣)新加坡商立可人事顧問有限公司(Recruit Express)](https://www.1111.com.tw/corp/9992537/) | [AL-Python Engineer，外商網路公司，年薪800K~1.2M](https://www.1111.com.tw/job/91212698/) | 2021-05-14    |
|  2 | [億力資訊股份有限公司](https://www.1111.com.tw/corp/54937860/)                         | [python工程師](https://www.1111.com.tw/job/97374762/)                             | 2021-06-03    |
|  3 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/)                         | [後端工程師](https://www.1111.com.tw/job/85012186/)                                 | 2021-06-01    |



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
