# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                              | job_title                                                                                               | update_time   |
|---:|:-------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [今時科技股份有限公司](https://www.104.com.tw/company/1a2x6bl2u4?jobsource=2018indexpoc)       | [網頁開發工程師  * 歡迎兼職論件計酬](https://www.104.com.tw/job/75jgv?jobsource=2018indexpoc)                          | 6/26          |
|  2 | [今時科技股份有限公司](https://www.104.com.tw/company/1a2x6bl2u4?jobsource=2018indexpoc)       | [網頁前端程式設計師](https://www.104.com.tw/job/79aqn?jobsource=2018indexpoc)                                    | 6/26          |
|  3 | [博思資訊管理顧問有限公司](https://www.104.com.tw/company/1a2x6blhw5?jobsource=2018indexpoc)     | [Python工程師(可遠端工作)](https://www.104.com.tw/job/78f5b?jobsource=2018indexpoc)                             | 6/26          |
|  4 | [同步科技股份有限公司](https://www.104.com.tw/company/1a2x6ble88?jobsource=jolist_c_relevance) | [後端工程師](https://www.104.com.tw/job/76q8x?jobsource=jolist_c_relevance)                                  | 6/24          |
|  5 | [展市華科技有限公司](https://www.104.com.tw/company/1a2x6blbgu?jobsource=jolist_c_relevance)  | [後端網頁工程師](https://www.104.com.tw/job/71amu?jobsource=jolist_c_relevance)                                | 6/22          |
|  6 | [德義資訊股份有限公司](https://www.104.com.tw/company/oe84aqo?jobsource=jolist_c_relevance)    | [Backend 系統開發工程師](https://www.104.com.tw/job/7awmz?jobsource=jolist_c_relevance)                        | 6/22          |
|  7 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_c_relevance) | [Python後端開發工程師(DevOps整合平台)](https://www.104.com.tw/job/7asvo?jobsource=jolist_c_relevance)              | 6/24          |
|  8 | [禾新數位有限公司](https://www.104.com.tw/company/1a2x6bjs3i?jobsource=2018indexpoc)         | [[ E-C03 ] Full Stack Engineer（線上面試+因應疫情居家上班）](https://www.104.com.tw/job/76q8f?jobsource=2018indexpoc) | 6/26          |
|  9 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_c_relevance)    | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_c_relevance)                | 6/18          |
| 10 | [萊鎂醫療器材股份有限公司](https://www.104.com.tw/company/bkgh1dc?jobsource=jolist_c_relevance)  | [雲端應用工程師](https://www.104.com.tw/job/791cq?jobsource=jolist_c_relevance)                                | 6/23          |

### Platform - 1111


|    | company                                              | job_title                                          | update_time   |
|---:|:-----------------------------------------------------|:---------------------------------------------------|:--------------|
|  1 | [億力資訊股份有限公司](https://www.1111.com.tw/corp/54937860/) | [python工程師](https://www.1111.com.tw/job/97374762/) | 2021-06-23    |
|  2 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/) | [後端工程師](https://www.1111.com.tw/job/85012186/)     | 2021-06-26    |



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
