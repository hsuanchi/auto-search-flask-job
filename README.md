# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                     | job_title                                                                                     | update_time   |
|---:|:--------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|:--------------|
|  1 | [同步科技股份有限公司](https://www.104.com.tw/company/1a2x6ble88?jobsource=jolist_c_relevance)        | [後端工程師](https://www.104.com.tw/job/76q8x?jobsource=jolist_c_relevance)                        | 6/24          |
|  2 | [展市華科技有限公司](https://www.104.com.tw/company/1a2x6blbgu?jobsource=2018indexpoc)               | [後端網頁工程師](https://www.104.com.tw/job/71amu?jobsource=2018indexpoc)                            | 6/29          |
|  3 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_c_relevance)        | [Python後端開發工程師(DevOps整合平台)](https://www.104.com.tw/job/7asvo?jobsource=jolist_c_relevance)    | 6/24          |
|  4 | [普匯金融科技股份有限公司](https://www.104.com.tw/company/1a2x6bkhzg?jobsource=2018indexpoc)            | [python工程師](https://www.104.com.tw/job/7ark5?jobsource=2018indexpoc)                          | 6/29          |
|  5 | [禾向數位科技有限公司](https://www.104.com.tw/company/1a2x6bl8h8?jobsource=2018indexpoc)              | [Python Backend Engineer](https://www.104.com.tw/job/71i7c?jobsource=2018indexpoc)            | 6/29          |
|  6 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_c_relevance)           | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_c_relevance)      | 6/28          |
|  7 | [英屬開曼群島商萬里雲互聯股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bk5cu?jobsource=2018indexpoc) | [Backend Engineer 後端工程師](https://www.104.com.tw/job/6xipk?jobsource=2018indexpoc)             | 6/29          |
|  8 | [英屬開曼群島商萬里雲互聯股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bk5cu?jobsource=2018indexpoc) | [Machine Learning Engineer 機器學習工程師 ](https://www.104.com.tw/job/6c61u?jobsource=2018indexpoc) | 6/29          |
|  9 | [萊鎂醫療器材股份有限公司](https://www.104.com.tw/company/bkgh1dc?jobsource=jolist_c_relevance)         | [雲端應用工程師](https://www.104.com.tw/job/791cq?jobsource=jolist_c_relevance)                      | 6/23          |

### Platform - 1111


|    | company                                              | job_title                                      | update_time   |
|---:|:-----------------------------------------------------|:-----------------------------------------------|:--------------|
|  1 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/) | [後端工程師](https://www.1111.com.tw/job/85012186/) | 2021-06-26    |



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
