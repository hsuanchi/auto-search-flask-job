# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                           | job_title                                                                                    | update_time   |
|---:|:----------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------|:--------------|
|  1 | [日新軟體股份有限公司](https://www.104.com.tw/company/oi77qwg?jobsource=jolist_a_relevance) | [Python 資深工程師](https://www.104.com.tw/job/6yfn5?jobsource=jolist_a_relevance)                | 1/12          |
|  2 | [禾新數位有限公司](https://www.104.com.tw/company/1a2x6bjs3i?jobsource=2018indexpoc)      | [[ S-01 ] Developer 開發工程師 (Python)](https://www.104.com.tw/job/6rrkz?jobsource=2018indexpoc) | 1/16          |
|  3 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_a_relevance) | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_a_relevance)     | 1/08          |

### Platform - 1111


|    | company                                                  | job_title                                           | update_time   |
|---:|:---------------------------------------------------------|:----------------------------------------------------|:--------------|
|  1 | [展市華科技有限公司](https://www.1111.com.tw/corp/72520572/)      | [全端網頁工程師](https://www.1111.com.tw/job/91503317/)    | 2021-01-17    |
|  2 | [展市華科技有限公司](https://www.1111.com.tw/corp/72520572/)      | [後端開發工程師](https://www.1111.com.tw/job/92133533/)    | 2021-01-17    |
|  3 | [展市華科技有限公司](https://www.1111.com.tw/corp/72520572/)      | [網頁工程師](https://www.1111.com.tw/job/91605448/)      | 2021-01-17    |
|  4 | [諾客網科股份有限公司](https://www.1111.com.tw/corp/73092077/)     | [Python 工程師](https://www.1111.com.tw/job/92163911/) | 2020-12-25    |
|  5 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/)     | [後端工程師](https://www.1111.com.tw/job/85012186/)      | 2021-01-17    |
|  6 | [鼎漢國際工程顧問股份有限公司](https://www.1111.com.tw/corp/51468466/) | [後端工程師](https://www.1111.com.tw/job/85884563/)      | 2021-01-13    |

### Platform - CakeResume


|    | company                                                                               | job_title                                                                                                                           | update_time          |
|---:|:--------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------|:---------------------|
|  1 | [Cathay Financial Holdings 國泰金控](https://www.cakeresume.com/companies/cathayholdings) | [數位研發專業人員-Python Software Engineer(數數發中心, DDT)](https://www.cakeresume.com/companies/cathayholdings/jobs/f5c69a)                    | Updated 6 days ago   |
|  2 | [愛碼市智能科技股份有限公司](https://www.cakeresume.com/companies/imarts)                          | [全端工程師 (台北)](https://www.cakeresume.com/companies/imarts/jobs/full-engineer-a09a83)                                                 | Updated 4 days ago   |
|  3 | [愛碼市智能科技股份有限公司](https://www.cakeresume.com/companies/imarts)                          | [網頁後端工程師 (台北)](https://www.cakeresume.com/companies/imarts/jobs/senior-software-engineer-10852a)                                    | Updated 24 days ago  |
|  4 | [愛飛媒平股份有限公司](https://www.cakeresume.com/companies/avmapping)                          | [Python網頁後端工程師](https://www.cakeresume.com/companies/avmapping/jobs/web-backend-engineer-c24e5a)                                    | Updated 15 days ago  |
|  5 | [紅門互動股份有限公司](https://www.cakeresume.com/companies/eagleeye-5332f1)                    | [Python Flask網站開發工程師(台北)](https://www.cakeresume.com/companies/eagleeye-5332f1/jobs/python-flask-web-development-engineer-taipei)   | Updated 5 months ago |
|  6 | [紅門互動股份有限公司](https://www.cakeresume.com/companies/eagleeye-5332f1)                    | [Python Flask網站研發工程師(台中)](https://www.cakeresume.com/companies/eagleeye-5332f1/jobs/python-flask-website-r-amp-d-engineer-taichung) | Updated 8 months ago |
|  7 | [菜蟲農食股份有限公司](https://www.cakeresume.com/companies/tsaitung)                           | [後端工程師 (初階、資深)](https://www.cakeresume.com/companies/tsaitung/jobs/back-end-engineer-initial-senior)                                | Updated a month ago  |
|  8 | [菜蟲農食股份有限公司](https://www.cakeresume.com/companies/tsaitung)                           | [Backend Developer (Junior & Senior)](https://www.cakeresume.com/companies/tsaitung/jobs/backend-developer-junior-senior)           | Updated a month ago  |
|  9 | [訊真科技股份有限公司](https://www.cakeresume.com/companies/truetel)                            | [Cloud Service 軟體工程師](https://www.cakeresume.com/companies/truetel/jobs/cloud-service-software-engineer)                            | Updated 6 months ago |



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
