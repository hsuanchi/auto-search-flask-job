# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                              | job_title                                                                                                                | update_time   |
|---:|:-------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [合翔資訊科技有限公司](https://www.104.com.tw/company/1a2x6blmxr?jobsource=jolist_c_date)      | [Python Backend 工程師](https://www.104.com.tw/job/7fif4?jobsource=jolist_c_date)                                           | 12/29         |
|  2 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_c_date)      | [Python後端工程師](https://www.104.com.tw/job/76vbt?jobsource=jolist_c_date)                                                  | 12/29         |
|  3 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_c_relevance) | [Python後端工程師](https://www.104.com.tw/job/76vbt?jobsource=jolist_c_relevance)                                             | 12/29         |
|  4 | [淼森科技股份有限公司](https://www.104.com.tw/company/1a2x6blm7t?jobsource=jolist_c_date)      | [Web App Backend Developer 後端工程師 AWS/Flask/Postman/MySQL](https://www.104.com.tw/job/7a7i3?jobsource=jolist_c_date)      | 12/29         |
|  5 | [淼森科技股份有限公司](https://www.104.com.tw/company/1a2x6blm7t?jobsource=jolist_c_relevance) | [Web App Backend Developer 後端工程師 AWS/Flask/Postman/MySQL](https://www.104.com.tw/job/7a7i3?jobsource=jolist_c_relevance) | 12/29         |
|  6 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_c_relevance)    | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_c_relevance)                                 | 12/28         |
|  7 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_c_relevance)    | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_c_relevance)                                 | 12/28         |

### Platform - 1111


|    | company                                                                          | job_title                                                          | update_time   |
|---:|:---------------------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------|
|  1 | [美超微電腦股份有限公司(Super Micro Computer, Inc.)](https://www.1111.com.tw/corp/9530088/) | [Software Engineer-TC21167](https://www.1111.com.tw/job/98544764/) | 2021-12-23    |



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
