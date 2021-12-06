# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                              | job_title                                                                                         | update_time   |
|---:|:-------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------|:--------------|
|  1 | [光禾感知科技股份有限公司](https://www.104.com.tw/company/1a2x6bks9s?jobsource=jolist_c_date)    | [Python後端工程師](https://www.104.com.tw/job/71j4l?jobsource=jolist_c_date)                           | 12/06         |
|  2 | [思納捷科技股份有限公司](https://www.104.com.tw/company/1a2x6bk977?jobsource=jolist_c_date)     | [前端工程師(Python)](https://www.104.com.tw/job/7g8nn?jobsource=jolist_c_date)                         | 12/06         |
|  3 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_b_relevance) | [Python後端工程師](https://www.104.com.tw/job/76vbt?jobsource=jolist_b_relevance)                      | 12/06         |
|  4 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_c_date)      | [Python後端工程師](https://www.104.com.tw/job/76vbt?jobsource=jolist_c_date)                           | 12/06         |
|  5 | [物聯網股份有限公司](https://www.104.com.tw/company/1a2x6bk3uw?jobsource=jolist_c_date)       | [資深Python工程師-台北(DF2)](https://www.104.com.tw/job/7du8c?jobsource=jolist_c_date)                   | 12/06         |
|  6 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_b_relevance)    | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_b_relevance)          | 11/30         |
|  7 | [迪威智能股份有限公司](https://www.104.com.tw/company/1a2x6bl035?jobsource=jolist_c_date)      | [Senior/Junior Back-end Engineer 後端工程師](https://www.104.com.tw/job/7ecqo?jobsource=jolist_c_date) | 12/07         |
|  8 | [迪威智能股份有限公司](https://www.104.com.tw/company/1a2x6bl035?jobsource=jolist_c_date)      | [Senior/Junior AI Engineer AI工程師](https://www.104.com.tw/job/7ecqj?jobsource=jolist_c_date)       | 12/07         |

### Platform - 1111


|    | company                                                                          | job_title                                                                          | update_time   |
|---:|:---------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|:--------------|
|  1 | [(獵頭)Accurate愛客獵股份有限公司(1111 高階獵才)](https://www.1111.com.tw/corp/69647966/)       | [直播平台_Senior Backend Developer(3002871)](https://www.1111.com.tw/job/85960420/)    | 2020-05-15    |
|  2 | [(獵頭)Accurate愛客獵股份有限公司(1111 高階獵才)](https://www.1111.com.tw/corp/69647966/)       | [Dev (Develop Engineer)前端_知名電子公司 (3005070)](https://www.1111.com.tw/job/97460023/) | 2021-07-05    |
|  3 | [(獵頭)Accurate愛客獵股份有限公司(1111 高階獵才)](https://www.1111.com.tw/corp/69647966/)       | [Dev (Develop Engineer)後端_知名電子公司 (3005117)](https://www.1111.com.tw/job/97460074/) | 2021-07-05    |
|  4 | [(獵頭)Accurate愛客獵股份有限公司(1111 高階獵才)](https://www.1111.com.tw/corp/69647966/)       | [Dev (Technical Lead)_知名電子公司 (3005066)](https://www.1111.com.tw/job/97459998/)     | 2021-07-05    |
|  5 | [中租迪和股份有限公司](https://www.1111.com.tw/corp/2850037/)                              | [【中租超利士】中台架構師](https://www.1111.com.tw/job/97507405/)                              | 2021-12-06    |
|  6 | [美超微電腦股份有限公司(Super Micro Computer, Inc.)](https://www.1111.com.tw/corp/9530088/) | [Software Engineer-TC21167](https://www.1111.com.tw/job/98544764/)                 | 2021-12-02    |



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
