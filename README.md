# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                     | job_title                                                                                                                | update_time   |
|---:|:--------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [合翔資訊科技有限公司](https://www.104.com.tw/company/1a2x6blmxr?jobsource=jolist_c_date)             | [Python Backend 工程師](https://www.104.com.tw/job/7fif4?jobsource=jolist_c_date)                                           | 12/22         |
|  2 | [吉音資訊有限公司](https://www.104.com.tw/company/10uhacsw?jobsource=jolist_c_date)                 | [高薪徵PHP程式開發人才(專案聘請 2-3年職(視情況再延長 ;Cable或電信業))](https://www.104.com.tw/job/2j2kp?jobsource=jolist_c_date)                  | 12/22         |
|  3 | [太奇雲端股份有限公司](https://www.104.com.tw/company/1a2x6bjj3y?jobsource=jolist_c_date)             | [前端工程師 (Front-end Developer)](https://www.104.com.tw/job/7fyy6?jobsource=jolist_c_date)                                  | 12/22         |
|  4 | [思納捷科技股份有限公司](https://www.104.com.tw/company/1a2x6bk977?jobsource=jolist_a_relevance)       | [前端工程師(Python)](https://www.104.com.tw/job/7g8nn?jobsource=jolist_a_relevance)                                           | 12/16         |
|  5 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_a_relevance)        | [Python後端工程師](https://www.104.com.tw/job/76vbt?jobsource=jolist_a_relevance)                                             | 12/20         |
|  6 | [普匯金融科技股份有限公司](https://www.104.com.tw/company/1a2x6bkhzg?jobsource=jolist_c_date)           | [python工程師](https://www.104.com.tw/job/7ark5?jobsource=jolist_c_date)                                                    | 12/22         |
|  7 | [淼森科技股份有限公司](https://www.104.com.tw/company/1a2x6blm7t?jobsource=jolist_a_relevance)        | [Web App Backend Developer 後端工程師 AWS/Flask/Postman/MySQL](https://www.104.com.tw/job/7a7i3?jobsource=jolist_a_relevance) | 12/22         |
|  8 | [淼森科技股份有限公司](https://www.104.com.tw/company/1a2x6blm7t?jobsource=jolist_c_date)             | [Web App Backend Developer 後端工程師 AWS/Flask/Postman/MySQL](https://www.104.com.tw/job/7a7i3?jobsource=jolist_c_date)      | 12/22         |
|  9 | [漢康生技股份有限公司](https://www.104.com.tw/company/1a2x6blf97?jobsource=jolist_c_date)             | [細胞培養工藝開發研究員/副研究員/助理研究員](https://www.104.com.tw/job/7cccb?jobsource=jolist_c_date)                                       | 12/22         |
| 10 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_a_relevance)           | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_a_relevance)                                 | 12/21         |
| 11 | [薩摩亞商動見科技有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bkwvs?jobsource=jolist_a_relevance) | [後端工程師 Backend engineer](https://www.104.com.tw/job/7ei4a?jobsource=jolist_a_relevance)                                  | 10/14         |
| 12 | [詩嫚特集團_斯曼特企業股份有限公司](https://www.104.com.tw/company/12q3kt2w?jobsource=jolist_c_date)        | [後端工程師(javascript)](https://www.104.com.tw/job/7h3cp?jobsource=jolist_c_date)                                            | 12/22         |
| 13 | [迪威智能股份有限公司](https://www.104.com.tw/company/1a2x6bl035?jobsource=jolist_c_date)             | [Senior/Junior Back-end Engineer 後端工程師](https://www.104.com.tw/job/7ecqo?jobsource=jolist_c_date)                        | 12/22         |
| 14 | [雄獅資訊科技股份有限公司](https://www.104.com.tw/company/13kq7dpk?jobsource=jolist_c_date)             | [python工程師](https://www.104.com.tw/job/71rxc?jobsource=jolist_c_date)                                                    | 12/22         |

### Platform - 1111


|    | company                                                                          | job_title                                                          | update_time   |
|---:|:---------------------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------|
|  1 | [美超微電腦股份有限公司(Super Micro Computer, Inc.)](https://www.1111.com.tw/corp/9530088/) | [Software Engineer-TC21167](https://www.1111.com.tw/job/98544764/) | 2021-12-16    |



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
