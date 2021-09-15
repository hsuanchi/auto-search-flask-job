# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                                | job_title                                                                                   | update_time   |
|---:|:-------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------|:--------------|
|  1 | [Algotech_新加坡商艾高科技股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6blc6n?jobsource=jolist_c_relevance) | [Python前後端工程師](https://www.104.com.tw/job/7duf1?jobsource=jolist_c_relevance)               | 9/14          |
|  2 | [和瑞科技股份有限公司](https://www.104.com.tw/company/1a2x6biv1c?jobsource=jolist_c_date)                        | [資深軟體工程師](https://www.104.com.tw/job/7c8o0?jobsource=jolist_c_date)                         | 9/15          |
|  3 | [德義資訊股份有限公司](https://www.104.com.tw/company/oe84aqo?jobsource=jolist_c_relevance)                      | [Backend 系統開發工程師](https://www.104.com.tw/job/7awmz?jobsource=jolist_c_relevance)            | 9/09          |
|  4 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_c_relevance)                      | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_c_relevance)    | 9/13          |
|  5 | [英商引達取有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bkz0n?jobsource=jolist_c_date)                    | [【台北】Data Engineer](https://www.104.com.tw/job/6pki0?jobsource=jolist_c_date)               | 9/15          |
|  6 | [萊泀有限公司](https://www.104.com.tw/company/1a2x6blg3t?jobsource=jolist_c_relevance)                       | [Python (Django、Flask)程式設計師](https://www.104.com.tw/job/7cs5e?jobsource=jolist_c_relevance) | 8/16          |
|  7 | [雙子星雲端運算股份有限公司](https://www.104.com.tw/company/1a2x6bjeye?jobsource=jolist_c_date)                     | [雲端軟體工程師(可視訊面試)](https://www.104.com.tw/job/58it4?jobsource=jolist_c_date)                  | 9/15          |

### Platform - 1111


|    | company                                              | job_title                                      | update_time   |
|---:|:-----------------------------------------------------|:-----------------------------------------------|:--------------|
|  1 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/) | [後端工程師](https://www.1111.com.tw/job/85012186/) | 2021-09-14    |



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
