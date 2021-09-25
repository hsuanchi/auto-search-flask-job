# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                     | job_title                                                                                   | update_time   |
|---:|:--------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------|:--------------|
|  1 | [Deep Sentinel_亞齊國際有限公司](https://www.104.com.tw/company/1a2x6blbly?jobsource=jolist_c_date) | [Full Stack Engineer](https://www.104.com.tw/job/7e67z?jobsource=jolist_c_date)             | 9/25          |
|  2 | [和瑞科技股份有限公司](https://www.104.com.tw/company/1a2x6biv1c?jobsource=jolist_c_date)             | [資深軟體工程師](https://www.104.com.tw/job/7c8o0?jobsource=jolist_c_date)                         | 9/24          |
|  3 | [小柿智檢科技股份有限公司](https://www.104.com.tw/company/1a2x6bl77l?jobsource=jolist_c_date)           | [後端工程師 Back-End Engineer](https://www.104.com.tw/job/71bmd?jobsource=jolist_c_date)         | 9/25          |
|  4 | [小柿智檢科技股份有限公司](https://www.104.com.tw/company/1a2x6bl77l?jobsource=jolist_c_date)           | [全端工程師 Full-Stack Engineer](https://www.104.com.tw/job/71bmz?jobsource=jolist_c_date)       | 9/25          |
|  5 | [新加坡商遠豪科技有限公司(籌備處)](https://www.104.com.tw/company/1a2x6blrab?jobsource=jolist_c_date)      | [全端工程師](https://www.104.com.tw/job/7e64n?jobsource=jolist_c_date)                           | 9/25          |
|  6 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_d_relevance)           | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_d_relevance)    | 9/22          |
|  7 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_d_relevance)           | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_d_relevance)    | 9/22          |
|  8 | [萊泀有限公司](https://www.104.com.tw/company/1a2x6blg3t?jobsource=jolist_d_relevance)            | [Python (Django、Flask)程式設計師](https://www.104.com.tw/job/7cs5e?jobsource=jolist_d_relevance) | 9/20          |

### Platform - 1111


|    | company                                              | job_title                                      | update_time   |
|---:|:-----------------------------------------------------|:-----------------------------------------------|:--------------|
|  1 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/) | [後端工程師](https://www.1111.com.tw/job/85012186/) | 2021-09-24    |



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
