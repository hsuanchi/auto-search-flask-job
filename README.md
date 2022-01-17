# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                            | job_title                                                                                                                | update_time   |
|---:|:---------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [威旭資訊有限公司](https://www.104.com.tw/company/1a2x6bk39d?jobsource=jolist_a_date)                      | [(資深)後端工程師-數據組 (Senior) Backend Engineer, Python](https://www.104.com.tw/job/7h65u?jobsource=jolist_a_date)              | 1/17          |
|  2 | [宏達電 HTC Corporation_宏達國際電子股份有限公司](https://www.104.com.tw/company/7co2xio?jobsource=jolist_a_date) | [(Vive R&amp;D) Vive - Machine Learning Scientist - J01803](https://www.104.com.tw/job/7er6w?jobsource=jolist_a_date)    | 1/17          |
|  3 | [展市華科技有限公司](https://www.104.com.tw/company/1a2x6blbgu?jobsource=jolist_a_date)                     | [網頁開發工程師](https://www.104.com.tw/job/78do7?jobsource=jolist_a_date)                                                      | 1/17          |
|  4 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_b_relevance)               | [Python後端工程師](https://www.104.com.tw/job/76vbt?jobsource=jolist_b_relevance)                                             | 1/12          |
|  5 | [淼森科技股份有限公司](https://www.104.com.tw/company/1a2x6blm7t?jobsource=jolist_b_relevance)               | [Web App Backend Developer 後端工程師 AWS/Flask/Postman/MySQL](https://www.104.com.tw/job/7a7i3?jobsource=jolist_b_relevance) | 1/15          |
|  6 | [漢康生技股份有限公司](https://www.104.com.tw/company/1a2x6blf97?jobsource=jolist_a_date)                    | [細胞培養工藝開發研究員/副研究員/助理研究員](https://www.104.com.tw/job/7cccb?jobsource=jolist_a_date)                                       | 1/17          |
|  7 | [英屬開曼群島商萬里雲互聯股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bk5cu?jobsource=jolist_a_date)       | [Machine Learning Engineer 機器學習工程師 ](https://www.104.com.tw/job/6c61u?jobsource=jolist_a_date)                           | 1/17          |
|  8 | [英屬開曼群島商萬里雲互聯股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bk5cu?jobsource=jolist_a_date)       | [Solution Architect (Presales) 解決方案架構師](https://www.104.com.tw/job/6c62k?jobsource=jolist_a_date)                        | 1/17          |

### Platform - 1111


|    | company                                                                          | job_title                                                                       | update_time   |
|---:|:---------------------------------------------------------------------------------|:--------------------------------------------------------------------------------|:--------------|
|  1 | [(派遣)萬寶華企業管理顧問股份有限公司](https://www.1111.com.tw/corp/9590529/)                     | [美商玻璃基板大廠_全端工程師Full Stack Engineer](https://www.1111.com.tw/job/98565216/)      | 2022-01-17    |
|  2 | [(獵頭)Accurate愛客獵股份有限公司(1111 高階獵才)](https://www.1111.com.tw/corp/69647966/)       | [直播平台_Senior Backend Developer(3002871)](https://www.1111.com.tw/job/85960420/) | 2020-05-15    |
|  3 | [中租迪和股份有限公司](https://www.1111.com.tw/corp/2850037/)                              | [【中租超利士】中台架構師](https://www.1111.com.tw/job/97507405/)                           | 2022-01-15    |
|  4 | [美超微電腦股份有限公司(Super Micro Computer, Inc.)](https://www.1111.com.tw/corp/9530088/) | [Software Engineer-TC21167](https://www.1111.com.tw/job/98544764/)              | 2022-01-12    |



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
