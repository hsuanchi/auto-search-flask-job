# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                     | job_title                                                                                                       | update_time   |
|---:|:--------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [亞洲指標數位行銷顧問股份有限公司](https://www.104.com.tw/company/d8qa7g0?jobsource=2018indexpoc)           | [[RD] 後端工程師(backend engineer)](https://www.104.com.tw/job/65dkg?jobsource=2018indexpoc)                         | 7/13          |
|  2 | [同步科技股份有限公司](https://www.104.com.tw/company/1a2x6ble88?jobsource=2018indexpoc)              | [後端工程師](https://www.104.com.tw/job/76q8x?jobsource=2018indexpoc)                                                | 7/13          |
|  3 | [德義資訊股份有限公司](https://www.104.com.tw/company/oe84aqo?jobsource=2018indexpoc)                 | [Backend 系統開發工程師](https://www.104.com.tw/job/7awmz?jobsource=2018indexpoc)                                      | 7/13          |
|  4 | [德義資訊股份有限公司](https://www.104.com.tw/company/oe84aqo?jobsource=jolist_d_relevance)           | [Backend 系統開發工程師](https://www.104.com.tw/job/7awmz?jobsource=jolist_d_relevance)                                | 7/13          |
|  5 | [愛卡拉互動媒體股份有限公司](https://www.104.com.tw/company/oi6pygw?jobsource=2018indexpoc)              | [【iKala Cloud】資深 資料工程師(CDP) Senior Data Engineer, CDP](https://www.104.com.tw/job/79zex?jobsource=2018indexpoc) | 7/13          |
|  6 | [新加坡商威兆科技有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bjqez?jobsource=jolist_d_relevance) | [Junior IT Developer (助理 IT 程式設計師)](https://www.104.com.tw/job/7bely?jobsource=jolist_d_relevance)              | 7/01          |
|  7 | [永昕生物醫藥股份有限公司](https://www.104.com.tw/company/5xfw7xk?jobsource=2018indexpoc)               | [細胞產程開發研究員(台北)](https://www.104.com.tw/job/6ujnv?jobsource=2018indexpoc)                                        | 7/13          |
|  8 | [童綜合醫療社團法人童綜合醫院](https://www.104.com.tw/company/kw8xsls?jobsource=2018indexpoc)             | [資訊部Python 工程師](https://www.104.com.tw/job/6upji?jobsource=2018indexpoc)                                        | 7/13          |
|  9 | [美商美創資通股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bjdsb?jobsource=jolist_d_relevance) | [資深Web後端工程師](https://www.104.com.tw/job/6y6f0?jobsource=jolist_d_relevance)                                     | 7/12          |
| 10 | [英屬開曼群島商萬里雲互聯股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bk5cu?jobsource=2018indexpoc) | [Machine Learning Engineer 機器學習工程師 ](https://www.104.com.tw/job/6c61u?jobsource=2018indexpoc)                   | 7/13          |
| 11 | [英屬開曼群島商萬里雲互聯股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bk5cu?jobsource=2018indexpoc) | [Backend Engineer 後端工程師](https://www.104.com.tw/job/6xipk?jobsource=2018indexpoc)                               | 7/13          |
| 12 | [霖園關係企業_神坊資訊股份有限公司](https://www.104.com.tw/company/wdapdfc?jobsource=2018indexpoc)          | [新創電商技術主管 EC Tech Team leader](https://www.104.com.tw/job/7aelb?jobsource=2018indexpoc)                         | 7/13          |
| 13 | [霖園關係企業_神坊資訊股份有限公司](https://www.104.com.tw/company/wdapdfc?jobsource=2018indexpoc)          | [新創電商Backend Engineer (Python)](https://www.104.com.tw/job/7aenr?jobsource=2018indexpoc)                        | 7/13          |

### Platform - 1111


|    | company                                              | job_title                                      | update_time   |
|---:|:-----------------------------------------------------|:-----------------------------------------------|:--------------|
|  1 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/) | [後端工程師](https://www.1111.com.tw/job/85012186/) | 2021-07-11    |



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
