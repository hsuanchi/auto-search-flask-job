# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                           | job_title                                                                                    | update_time   |
|---:|:----------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------|:--------------|
|  1 | [中國醫藥大學附設醫院](https://www.104.com.tw/company/o5x51w0?jobsource=jolist_b_date)      | [10R0-大數據中心 系統工程師](https://www.104.com.tw/job/7ancv?jobsource=jolist_b_date)                 | 9/17          |
|  2 | [中國醫藥大學附設醫院](https://www.104.com.tw/company/o5x51w0?jobsource=jolist_b_date)      | [1JZ0-人工智慧醫學診斷中心 系統開發工程師(後端)](https://www.104.com.tw/job/798gy?jobsource=jolist_b_date)      | 9/17          |
|  3 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_d_relevance) | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_d_relevance)     | 9/13          |
|  4 | [萊泀有限公司](https://www.104.com.tw/company/1a2x6blg3t?jobsource=jolist_d_relevance)  | [Python (Django、Flask)程式設計師](https://www.104.com.tw/job/7cs5e?jobsource=jolist_d_relevance)  | 8/16          |
|  5 | [蓋特資訊系統股份有限公司](https://www.104.com.tw/company/1a2x6biptb?jobsource=jolist_b_date) | [Senior Machine Learning Engineer](https://www.104.com.tw/job/6e6r8?jobsource=jolist_b_date) | 9/17          |
|  6 | [雲動科技股份有限公司](https://www.104.com.tw/company/1a2x6biwgs?jobsource=jolist_b_date)   | [Sr. Backend Engineer](https://www.104.com.tw/job/4vmq8?jobsource=jolist_b_date)             | 9/17          |

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
