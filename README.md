# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                              | job_title                                                                                | update_time   |
|---:|:-------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|:--------------|
|  1 | [展市華科技有限公司](https://www.104.com.tw/company/1a2x6blbgu?jobsource=2018indexpoc)        | [網頁開發工程師](https://www.104.com.tw/job/78do7?jobsource=2018indexpoc)                       | 4/28          |
|  2 | [日新軟體股份有限公司](https://www.104.com.tw/company/oi77qwg?jobsource=jolist_c_relevance)    | [Python 資深工程師](https://www.104.com.tw/job/6yfn5?jobsource=jolist_c_relevance)            | 4/27          |
|  3 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_c_relevance) | [Python後端工程師(IoT物聯網)](https://www.104.com.tw/job/76vbt?jobsource=jolist_c_relevance)     | 4/22          |
|  4 | [禾向數位科技有限公司](https://www.104.com.tw/company/1a2x6bl8h8?jobsource=2018indexpoc)       | [Python Backend Engineer](https://www.104.com.tw/job/71i7c?jobsource=2018indexpoc)       | 4/28          |
|  5 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_c_relevance)    | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_c_relevance) | 4/22          |
|  6 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_c_relevance)    | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_c_relevance) | 4/22          |

### Platform - 1111


|    | company                                                                      | job_title                                                                      | update_time   |
|---:|:-----------------------------------------------------------------------------|:-------------------------------------------------------------------------------|:--------------|
|  1 | [(派遣)新加坡商立可人事顧問有限公司(Recruit Express)](https://www.1111.com.tw/corp/9992537/) | [AL-Python Engineer，外商網路公司，年薪800K~1.2M](https://www.1111.com.tw/job/91212698/) | 2021-04-20    |
|  2 | [億力資訊股份有限公司](https://www.1111.com.tw/corp/54937860/)                         | [python工程師](https://www.1111.com.tw/job/97374762/)                             | 2021-04-23    |
|  3 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/)                         | [後端工程師](https://www.1111.com.tw/job/85012186/)                                 | 2021-04-27    |

### Platform - CakeResume


|    | company                                                                               | job_title                                                                                                                           | update_time           |
|---:|:--------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
|  1 | [Cathay Financial Holdings 國泰金控](https://www.cakeresume.com/companies/cathayholdings) | [軟體開發工程師 Python Software Engineer(數數發中心, DDT)](https://www.cakeresume.com/companies/cathayholdings/jobs/f5c69a)                     | Updated a month ago   |
|  2 | [Proto 新語科技有限公司](https://www.cakeresume.com/companies/proto-cx)                       | [Backend Developer (Python)](https://www.cakeresume.com/companies/proto-cx/jobs/backend-developer-python)                           | Updated a month ago   |
|  3 | [愛飛媒平股份有限公司](https://www.cakeresume.com/companies/avmapping)                          | [Python網頁後端工程師](https://www.cakeresume.com/companies/avmapping/jobs/web-backend-engineer-c24e5a)                                    | Updated 10 days ago   |
|  4 | [玉山商業銀行股份有限公司](https://www.cakeresume.com/companies/esunbank)                         | [後端工程師 Back-end Enginee](https://www.cakeresume.com/companies/esunbank/jobs/back-end-enginee)                                       | Updated 21 days ago   |
|  5 | [紅門互動股份有限公司](https://www.cakeresume.com/companies/eagleeye-5332f1)                    | [Python Flask網站開發工程師(台北)](https://www.cakeresume.com/companies/eagleeye-5332f1/jobs/python-flask-web-development-engineer-taipei)   | Updated 8 months ago  |
|  6 | [紅門互動股份有限公司](https://www.cakeresume.com/companies/eagleeye-5332f1)                    | [Python Flask網站研發工程師(台中)](https://www.cakeresume.com/companies/eagleeye-5332f1/jobs/python-flask-website-r-amp-d-engineer-taichung) | Updated a year ago    |
|  7 | [菜蟲農食股份有限公司](https://www.cakeresume.com/companies/tsaitung)                           | [後端工程師 (初階、資深)](https://www.cakeresume.com/companies/tsaitung/jobs/back-end-engineer-initial-senior)                                | Updated a month ago   |
|  8 | [菜蟲農食股份有限公司](https://www.cakeresume.com/companies/tsaitung)                           | [Backend Developer (Junior & Senior)](https://www.cakeresume.com/companies/tsaitung/jobs/backend-developer-junior-senior)           | Updated a month ago   |
|  9 | [訊真科技有限公司](https://www.cakeresume.com/companies/truetel)                              | [Cloud Service 軟體工程師](https://www.cakeresume.com/companies/truetel/jobs/cloud-service-software-engineer)                            | Updated 10 months ago |



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
