# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                       | job_title                                                                                | update_time   |
|---:|:----------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|:--------------|
|  1 | [新加坡商齊舵管理顧問有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bldr7?jobsource=jolist_a_relevance) | [影像處理軟體工程師](https://www.104.com.tw/job/77vw9?jobsource=jolist_a_relevance)               | 3/12          |
|  2 | [日新軟體股份有限公司](https://www.104.com.tw/company/oi77qwg?jobsource=jolist_a_relevance)             | [Python 資深工程師](https://www.104.com.tw/job/6yfn5?jobsource=jolist_a_relevance)            | 4/07          |
|  3 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_a_relevance)          | [Python後端工程師(IoT物聯網)](https://www.104.com.tw/job/76vbt?jobsource=jolist_a_relevance)     | 4/08          |
|  4 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_a_relevance)             | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_a_relevance) | 4/08          |

### Platform - 1111


|    | company                                              | job_title                                      | update_time   |
|---:|:-----------------------------------------------------|:-----------------------------------------------|:--------------|
|  1 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/) | [後端工程師](https://www.1111.com.tw/job/85012186/) | 2021-04-12    |

### Platform - CakeResume


|    | company                                                                               | job_title                                                                                                                           | update_time          |
|---:|:--------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------|:---------------------|
|  1 | [Cathay Financial Holdings 國泰金控](https://www.cakeresume.com/companies/cathayholdings) | [軟體開發工程師 Python Software Engineer(數數發中心, DDT)](https://www.cakeresume.com/companies/cathayholdings/jobs/f5c69a)                     | Updated 13 days ago  |
|  2 | [Proto 新語科技有限公司](https://www.cakeresume.com/companies/proto-cx)                       | [Backend Developer (Python)](https://www.cakeresume.com/companies/proto-cx/jobs/backend-developer-python)                           | Updated 19 days ago  |
|  3 | [Robert Walters](https://www.cakeresume.com/companies/robert-walters)                 | [【國際SaaS新創】Senior Python Fullstack developer](https://www.cakeresume.com/companies/robert-walters/jobs/f70aba)                      | Updated 19 days ago  |
|  4 | [愛飛媒平股份有限公司](https://www.cakeresume.com/companies/avmapping)                          | [Python網頁後端工程師](https://www.cakeresume.com/companies/avmapping/jobs/web-backend-engineer-c24e5a)                                    | Updated 6 days ago   |
|  5 | [玉山商業銀行股份有限公司](https://www.cakeresume.com/companies/esunbank)                         | [後端工程師 Back-end Enginee](https://www.cakeresume.com/companies/esunbank/jobs/back-end-enginee)                                       | Updated 5 days ago   |
|  6 | [紅門互動股份有限公司](https://www.cakeresume.com/companies/eagleeye-5332f1)                    | [Python Flask網站開發工程師(台北)](https://www.cakeresume.com/companies/eagleeye-5332f1/jobs/python-flask-web-development-engineer-taipei)   | Updated 7 months ago |
|  7 | [紅門互動股份有限公司](https://www.cakeresume.com/companies/eagleeye-5332f1)                    | [Python Flask網站研發工程師(台中)](https://www.cakeresume.com/companies/eagleeye-5332f1/jobs/python-flask-website-r-amp-d-engineer-taichung) | Updated a year ago   |
|  8 | [菜蟲農食股份有限公司](https://www.cakeresume.com/companies/tsaitung)                           | [後端工程師 (初階、資深)](https://www.cakeresume.com/companies/tsaitung/jobs/back-end-engineer-initial-senior)                                | Updated 13 days ago  |
|  9 | [菜蟲農食股份有限公司](https://www.cakeresume.com/companies/tsaitung)                           | [Backend Developer (Junior & Senior)](https://www.cakeresume.com/companies/tsaitung/jobs/backend-developer-junior-senior)           | Updated 13 days ago  |
| 10 | [訊真科技有限公司](https://www.cakeresume.com/companies/truetel)                              | [Cloud Service 軟體工程師](https://www.cakeresume.com/companies/truetel/jobs/cloud-service-software-engineer)                            | Updated 9 months ago |



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
