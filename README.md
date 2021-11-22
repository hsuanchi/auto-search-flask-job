# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                                | job_title                                                                                                             | update_time   |
|---:|:-------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [Algotech_新加坡商艾高科技股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6blc6n?jobsource=jolist_a_date)      | [產品工程師/Python工程師](https://www.104.com.tw/job/7duf1?jobsource=jolist_a_date)                                           | 11/22         |
|  2 | [Algotech_新加坡商艾高科技股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6blc6n?jobsource=jolist_a_relevance) | [產品工程師/Python工程師](https://www.104.com.tw/job/7duf1?jobsource=jolist_a_relevance)                                      | 11/22         |
|  3 | [光禾感知科技股份有限公司](https://www.104.com.tw/company/1a2x6bks9s?jobsource=jolist_a_date)                      | [Python後端工程師](https://www.104.com.tw/job/71j4l?jobsource=jolist_a_date)                                               | 11/22         |
|  4 | [宏達電 HTC Corporation_宏達國際電子股份有限公司](https://www.104.com.tw/company/7co2xio?jobsource=jolist_a_date)     | [(Vive R&amp;D) Vive - Machine Learning Scientist - J01803](https://www.104.com.tw/job/7er6w?jobsource=jolist_a_date) | 11/22         |
|  5 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_a_date)                        | [Python後端工程師](https://www.104.com.tw/job/76vbt?jobsource=jolist_a_date)                                               | 11/22         |
|  6 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_a_relevance)                   | [Python後端工程師](https://www.104.com.tw/job/76vbt?jobsource=jolist_a_relevance)                                          | 11/22         |
|  7 | [歐立威科技股份有限公司](https://www.104.com.tw/company/b8gl75c?jobsource=jolist_a_date)                          | [軟體開發工程師](https://www.104.com.tw/job/6q2ao?jobsource=jolist_a_date)                                                   | 11/22         |
|  8 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_a_relevance)                      | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_a_relevance)                              | 11/15         |
|  9 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_a_relevance)                      | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_a_relevance)                              | 11/15         |
| 10 | [迪威智能股份有限公司](https://www.104.com.tw/company/1a2x6bl035?jobsource=jolist_a_date)                        | [Senior/Junior AI Engineer AI工程師](https://www.104.com.tw/job/7ecqj?jobsource=jolist_a_date)                           | 11/22         |
| 11 | [香港商宇晨品牌顧問有限公司台灣分公司](https://www.104.com.tw/company/1a2x6blkn9?jobsource=jolist_a_date)                | [【擴大徵才中】後端工程師 Backend Engineer](https://www.104.com.tw/job/791ud?jobsource=jolist_a_date)                             | 11/22         |

### Platform - 1111


|    | company                                              | job_title                                      | update_time   |
|---:|:-----------------------------------------------------|:-----------------------------------------------|:--------------|
|  1 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/) | [後端工程師](https://www.1111.com.tw/job/85012186/) | 2021-11-18    |



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
