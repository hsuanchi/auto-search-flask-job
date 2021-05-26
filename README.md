# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                       | job_title                                                                                     | update_time   |
|---:|:----------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|:--------------|
|  1 | [今時科技股份有限公司](https://www.104.com.tw/company/1a2x6bl2u4?jobsource=2018indexpoc)                | [網頁開發工程師  * 歡迎兼職論件計酬](https://www.104.com.tw/job/75jgv?jobsource=2018indexpoc)                | 5/26          |
|  2 | [今時科技股份有限公司](https://www.104.com.tw/company/1a2x6bl2u4?jobsource=2018indexpoc)                | [網頁前端程式設計師](https://www.104.com.tw/job/79aqn?jobsource=2018indexpoc)                          | 5/26          |
|  3 | [博思資訊管理顧問有限公司](https://www.104.com.tw/company/1a2x6blhw5?jobsource=2018indexpoc)              | [Python工程師](https://www.104.com.tw/job/78f5b?jobsource=2018indexpoc)                          | 5/26          |
|  4 | [愛卡拉互動媒體股份有限公司](https://www.104.com.tw/company/oi6pygw?jobsource=2018indexpoc)                | [【iKala Cloud】資料工程師 Data Engineer](https://www.104.com.tw/job/79zex?jobsource=2018indexpoc)   | 5/26          |
|  5 | [新加坡商齊舵管理顧問有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bldr7?jobsource=jolist_a_relevance) | [影像處理軟體工程師](https://www.104.com.tw/job/77vw9?jobsource=jolist_a_relevance)                    | 4/30          |
|  6 | [日新軟體股份有限公司](https://www.104.com.tw/company/oi77qwg?jobsource=jolist_a_relevance)             | [Python 資深工程師](https://www.104.com.tw/job/6yfn5?jobsource=jolist_a_relevance)                 | 5/25          |
|  7 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_a_relevance)          | [Python後端工程師(IoT物聯網)](https://www.104.com.tw/job/76vbt?jobsource=jolist_a_relevance)          | 5/20          |
|  8 | [桔畝智慧股份有限公司](https://www.104.com.tw/company/1a2x6blm8y?jobsource=2018indexpoc)                | [Back-End Development Engineer後端工程師](https://www.104.com.tw/job/7a80a?jobsource=2018indexpoc) | 5/27          |
|  9 | [樂播科技股份有限公司](https://www.104.com.tw/company/1a2x6bkuvp?jobsource=2018indexpoc)                | [網頁前端工程師](https://www.104.com.tw/job/71llp?jobsource=2018indexpoc)                            | 5/26          |
| 10 | [玉山銀行_玉山商業銀行股份有限公司](https://www.104.com.tw/company/13quahyo?jobsource=2018indexpoc)           | [【金融科技】後端工程師 Back-end Engineer(新人)](https://www.104.com.tw/job/775i7?jobsource=2018indexpoc)  | 5/26          |
| 11 | [禾向數位科技有限公司](https://www.104.com.tw/company/1a2x6bl8h8?jobsource=2018indexpoc)                | [Python Backend Engineer](https://www.104.com.tw/job/71i7c?jobsource=2018indexpoc)            | 5/26          |
| 12 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_a_relevance)             | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_a_relevance)      | 5/20          |
| 13 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_a_relevance)             | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_a_relevance)      | 5/20          |
| 14 | [長佳智能股份有限公司](https://www.104.com.tw/company/1a2x6bkoxb?jobsource=2018indexpoc)                | [後端工程師](https://www.104.com.tw/job/6qa54?jobsource=2018indexpoc)                              | 5/26          |

### Platform - 1111


|    | company                                              | job_title                                          | update_time   |
|---:|:-----------------------------------------------------|:---------------------------------------------------|:--------------|
|  1 | [億力資訊股份有限公司](https://www.1111.com.tw/corp/54937860/) | [python工程師](https://www.1111.com.tw/job/97374762/) | 2021-05-21    |
|  2 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/) | [後端工程師](https://www.1111.com.tw/job/85012186/)     | 2021-05-27    |



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
