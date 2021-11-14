# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                | job_title                                                                                         | update_time   |
|---:|:---------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------|:--------------|
|  1 | [今時科技股份有限公司](https://www.104.com.tw/company/1a2x6bl2u4?jobsource=jolist_b_date)        | [網頁開發工程師  * 歡迎兼職論件計酬](https://www.104.com.tw/job/75jgv?jobsource=jolist_b_date)                   | 11/14         |
|  2 | [今時科技股份有限公司](https://www.104.com.tw/company/1a2x6bl2u4?jobsource=jolist_b_date)        | [網頁前端程式設計師](https://www.104.com.tw/job/79aqn?jobsource=jolist_b_date)                             | 11/14         |
|  3 | [光禾感知科技股份有限公司](https://www.104.com.tw/company/1a2x6bks9s?jobsource=jolist_b_date)      | [Python後端工程師](https://www.104.com.tw/job/71j4l?jobsource=jolist_b_date)                           | 11/14         |
|  4 | [小柿智檢科技股份有限公司](https://www.104.com.tw/company/1a2x6bl77l?jobsource=jolist_b_date)      | [全端工程師 Full-Stack Engineer](https://www.104.com.tw/job/71bmz?jobsource=jolist_b_date)             | 11/13         |
|  5 | [小柿智檢科技股份有限公司](https://www.104.com.tw/company/1a2x6bl77l?jobsource=jolist_b_date)      | [後端工程師 Back-End Engineer](https://www.104.com.tw/job/71bmd?jobsource=jolist_b_date)               | 11/13         |
|  6 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_a_relevance)      | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_a_relevance)          | 11/08         |
|  7 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_a_relevance)      | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_a_relevance)          | 11/08         |
|  8 | [蓋特資訊系統股份有限公司](https://www.104.com.tw/company/1a2x6biptb?jobsource=jolist_a_relevance) | [Senior Machine Learning Engineer](https://www.104.com.tw/job/6e6r8?jobsource=jolist_a_relevance) | 11/08         |

### Platform - 1111


|    | company                                              | job_title                                      | update_time   |
|---:|:-----------------------------------------------------|:-----------------------------------------------|:--------------|
|  1 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/) | [後端工程師](https://www.1111.com.tw/job/85012186/) | 2021-11-11    |



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
