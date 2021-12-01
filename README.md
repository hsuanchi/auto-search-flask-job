# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                  | job_title                                                                                                                    | update_time   |
|---:|:-----------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [倫發科技有限公司](https://www.104.com.tw/company/1a2x6biyl9?jobsource=jolist_d_date)            | [開發運維工程師(Python) DevOps Engineer](https://www.104.com.tw/job/70v91?jobsource=jolist_d_date)                                  | 12/01         |
|  2 | [合翔資訊科技有限公司](https://www.104.com.tw/company/1a2x6blmxr?jobsource=jolist_d_date)          | [Python Backend 工程師](https://www.104.com.tw/job/7fif4?jobsource=jolist_d_date)                                               | 12/01         |
|  3 | [新加坡商蝦皮娛樂電商有限公司台灣分公司](https://www.104.com.tw/company/1a2x6blcz2?jobsource=jolist_d_date) | [Back-end Engineer Intern 後端工程師實習生 / Business Intelligence 數據分析部門](https://www.104.com.tw/job/7ecrl?jobsource=jolist_d_date) | 12/01         |
|  4 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_d_relevance)     | [Python後端工程師](https://www.104.com.tw/job/76vbt?jobsource=jolist_d_relevance)                                                 | 11/29         |
|  5 | [普匯金融科技股份有限公司](https://www.104.com.tw/company/1a2x6bkhzg?jobsource=jolist_d_date)        | [python工程師](https://www.104.com.tw/job/7ark5?jobsource=jolist_d_date)                                                        | 12/01         |
|  6 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_d_relevance)        | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_d_relevance)                                     | 11/30         |
|  7 | [雄獅資訊科技股份有限公司](https://www.104.com.tw/company/13kq7dpk?jobsource=jolist_d_date)          | [python工程師](https://www.104.com.tw/job/71rxc?jobsource=jolist_d_date)                                                        | 12/01         |

### Platform - 1111


|    | company                                                                          | job_title                                                          | update_time   |
|---:|:---------------------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------|
|  1 | [美超微電腦股份有限公司(Super Micro Computer, Inc.)](https://www.1111.com.tw/corp/9530088/) | [Software Engineer-TC21167](https://www.1111.com.tw/job/98544764/) | 2021-11-27    |



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
