# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                          | job_title                                                                                                                | update_time   |
|---:|:-------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [光禾感知科技股份有限公司](https://www.104.com.tw/company/1a2x6bks9s?jobsource=jolist_d_date)                | [Python後端工程師](https://www.104.com.tw/job/71j4l?jobsource=jolist_d_date)                                                  | 1/18          |
|  2 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_a_relevance)             | [Python後端工程師](https://www.104.com.tw/job/76vbt?jobsource=jolist_a_relevance)                                             | 1/12          |
|  3 | [淼森科技股份有限公司](https://www.104.com.tw/company/1a2x6blm7t?jobsource=jolist_a_relevance)             | [Web App Backend Developer 後端工程師 AWS/Flask/Postman/MySQL](https://www.104.com.tw/job/7a7i3?jobsource=jolist_a_relevance) | 1/15          |
|  4 | [艾酷互動股份有限公司](https://www.104.com.tw/company/1a2x6bkq17?jobsource=jolist_d_date)                  | [數據⼯程師](https://www.104.com.tw/job/7275w?jobsource=jolist_d_date)                                                        | 1/18          |
|  5 | [迪威智能股份有限公司](https://www.104.com.tw/company/1a2x6bl035?jobsource=jolist_d_date)                  | [Senior/Junior AI Engineer AI工程師](https://www.104.com.tw/job/7ecqj?jobsource=jolist_d_date)                              | 1/18          |
|  6 | [金正禾數位有限公司](https://www.104.com.tw/company/1a2x6bl4su?jobsource=jolist_d_date)                   | [資深後端工程師 Senior Backend Engineer](https://www.104.com.tw/job/720ep?jobsource=jolist_d_date)                              | 1/18          |
|  7 | [雄獅資訊科技股份有限公司](https://www.104.com.tw/company/13kq7dpk?jobsource=jolist_d_date)                  | [python工程師](https://www.104.com.tw/job/71rxc?jobsource=jolist_d_date)                                                    | 1/18          |
|  8 | [點睛品_英屬維爾京群島商周生生珠寶行股份有限公司台灣分公司](https://www.104.com.tw/company/152ckz00?jobsource=jolist_d_date) | [Python工程師](https://www.104.com.tw/job/7hq8v?jobsource=jolist_d_date)                                                    | 1/18          |

### Platform - 1111


|    | company                                                                          | job_title                                                                                                | update_time   |
|---:|:---------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [(獵頭)Accurate愛客獵股份有限公司(1111 高階獵才)](https://www.1111.com.tw/corp/69647966/)       | [直播平台_Senior Backend Developer(3002871)](https://www.1111.com.tw/job/85960420/)                          | 2020-05-15    |
|  2 | [台灣美光晶圓科技股份有限公司](https://www.1111.com.tw/corp/9622349/)                          | [Full Stack SMAI Solution Developer](https://www.1111.com.tw/job/98479119/)                              | 2022-01-18    |
|  3 | [沛思坦網路股份有限公司](https://www.1111.com.tw/corp/73457881/)                            | [【台北內湖】資深Python後端工程師 Python Back-end Engineer (Senior) (月薪7萬-9萬)](https://www.1111.com.tw/job/97541124/) | 2022-01-17    |
|  4 | [美超微電腦股份有限公司(Super Micro Computer, Inc.)](https://www.1111.com.tw/corp/9530088/) | [Software Engineer-TC21167](https://www.1111.com.tw/job/98544764/)                                       | 2022-01-12    |



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
