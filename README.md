# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                          | job_title                                                                                                                                             | update_time   |
|---:|:-------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [城科國際_CYBILL TEK SOFTWARE INC](https://www.104.com.tw/company/1a2x6bl0gd?jobsource=2018indexpoc) | [台灣-Python後端工程師](https://www.104.com.tw/job/7a4xc?jobsource=2018indexpoc)                                                                             | 7/27          |
|  2 | [新加坡商齊舵管理顧問有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bldr7?jobsource=jolist_b_relevance)    | [影像處理軟體工程師](https://www.104.com.tw/job/77vw9?jobsource=jolist_b_relevance)                                                                            | 4/30          |
|  3 | [智理管理顧問股份有限公司](https://www.104.com.tw/company/1a2x6bj38r?jobsource=2018indexpoc)                 | [★全球前三大供應商★台灣上市母公司成立AI新創單位★前端工程師 Frontend Engineer (React)★後端工程師 Backend Engineer (Python)★](https://www.104.com.tw/job/7bofr?jobsource=2018indexpoc) | 7/27          |
|  4 | [童綜合醫療社團法人童綜合醫院](https://www.104.com.tw/company/kw8xsls?jobsource=2018indexpoc)                  | [資訊部Python 工程師](https://www.104.com.tw/job/6upji?jobsource=2018indexpoc)                                                                              | 7/27          |
|  5 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_b_relevance)                | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_b_relevance)                                                              | 7/27          |
|  6 | [英屬開曼群島商萬里雲互聯股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bk5cu?jobsource=2018indexpoc)      | [Backend Engineer 後端工程師](https://www.104.com.tw/job/6xipk?jobsource=2018indexpoc)                                                                     | 7/27          |
|  7 | [英屬開曼群島商萬里雲互聯股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bk5cu?jobsource=2018indexpoc)      | [Machine Learning Engineer 機器學習工程師 ](https://www.104.com.tw/job/6c61u?jobsource=2018indexpoc)                                                         | 7/27          |
|  8 | [薩摩亞商連影科技有限公司台灣分公司](https://www.104.com.tw/company/1a2x6blcyw?jobsource=2018indexpoc)            | [(Sr./Jr.) Backend Developer 後端工程師](https://www.104.com.tw/job/72kyd?jobsource=2018indexpoc)                                                          | 7/27          |
|  9 | [龍騰文化事業股份有限公司](https://www.104.com.tw/company/au6siqw?jobsource=2018indexpoc)                    | [後端工程師(資深工程師)](https://www.104.com.tw/job/7bmv8?jobsource=2018indexpoc)                                                                               | 7/27          |

### Platform - 1111


|    | company                                              | job_title                                          | update_time   |
|---:|:-----------------------------------------------------|:---------------------------------------------------|:--------------|
|  1 | [億力資訊股份有限公司](https://www.1111.com.tw/corp/54937860/) | [python工程師](https://www.1111.com.tw/job/97374762/) | 2021-07-26    |
|  2 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/) | [後端工程師](https://www.1111.com.tw/job/85012186/)     | 2021-07-26    |



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
