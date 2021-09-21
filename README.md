# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                            | job_title                                                                                               | update_time   |
|---:|:---------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [Algotech_新加坡商艾高科技股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6blc6n?jobsource=jolist_c_date)  | [Python前後端工程師](https://www.104.com.tw/job/7duf1?jobsource=jolist_c_date)                                | 9/21          |
|  2 | [xarefit享健身_香港商宇晨品牌顧問有限公司台灣分公司](https://www.104.com.tw/company/1a2x6blkn9?jobsource=jolist_c_date) | [【擴大徵才中】後端工程師 Backend Engineer](https://www.104.com.tw/job/791ud?jobsource=jolist_c_date)               | 9/20          |
|  3 | [中信金控_台灣人壽保險股份有限公司](https://www.104.com.tw/company/1mtr7vs?jobsource=jolist_c_date)                | [資訊_資深Python工程師（Senior Python Programmer）](https://www.104.com.tw/job/77drj?jobsource=jolist_c_date)    | 9/20          |
|  4 | [小柿智檢科技股份有限公司](https://www.104.com.tw/company/1a2x6bl77l?jobsource=jolist_c_date)                  | [後端工程師 Back-End Engineer](https://www.104.com.tw/job/71bmd?jobsource=jolist_c_date)                     | 9/18          |
|  5 | [小柿智檢科技股份有限公司](https://www.104.com.tw/company/1a2x6bl77l?jobsource=jolist_c_date)                  | [全端工程師 Full-Stack Engineer](https://www.104.com.tw/job/71bmz?jobsource=jolist_c_date)                   | 9/18          |
|  6 | [昱峰智能大數據科技股份有限公司](https://www.104.com.tw/company/1a2x6bkbn6?jobsource=jolist_c_date)               | [RD[資深]後端工程師](https://www.104.com.tw/job/5x0lo?jobsource=jolist_c_date)                                 | 9/20          |
|  7 | [普匯金融科技股份有限公司](https://www.104.com.tw/company/1a2x6bkhzg?jobsource=jolist_c_date)                  | [python工程師](https://www.104.com.tw/job/7ark5?jobsource=jolist_c_date)                                   | 9/21          |
|  8 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_c_relevance)                  | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_c_relevance)                | 9/13          |
|  9 | [紫式大數據決策股份有限公司](https://www.104.com.tw/company/1a2x6bkygn?jobsource=jolist_c_date)                 | [後端工程師--機器學習系統整合開發](https://www.104.com.tw/job/6p2d5?jobsource=jolist_c_date)                           | 9/21          |
| 10 | [聚典資訊股份有限公司](https://www.104.com.tw/company/1a2x6bl0ew?jobsource=jolist_c_date)                    | [軟體工程師 Software engineer/full-stack Engineer](https://www.104.com.tw/job/78evf?jobsource=jolist_c_date) | 9/21          |
| 11 | [艾斯移動股份有限公司](https://www.104.com.tw/company/cv8shww?jobsource=jolist_c_date)                       | [Python工程師](https://www.104.com.tw/job/6nml7?jobsource=jolist_c_date)                                   | 9/20          |
| 12 | [艾斯移動股份有限公司](https://www.104.com.tw/company/cv8shww?jobsource=jolist_c_date)                       | [自然語言處理工程師 (NLP Engineer)](https://www.104.com.tw/job/6nmld?jobsource=jolist_c_date)                    | 9/20          |
| 13 | [萊泀有限公司](https://www.104.com.tw/company/1a2x6blg3t?jobsource=jolist_c_date)                        | [Python (Django、Flask)程式設計師](https://www.104.com.tw/job/7cs5e?jobsource=jolist_c_date)                  | 9/20          |
| 14 | [萊泀有限公司](https://www.104.com.tw/company/1a2x6blg3t?jobsource=jolist_c_relevance)                   | [Python (Django、Flask)程式設計師](https://www.104.com.tw/job/7cs5e?jobsource=jolist_c_relevance)             | 9/20          |
| 15 | [長佳智能股份有限公司](https://www.104.com.tw/company/1a2x6bkoxb?jobsource=jolist_c_date)                    | [Backend Engineer (PHP/Python)](https://www.104.com.tw/job/716px?jobsource=jolist_c_date)               | 9/20          |

### Platform - 1111


|    | company                                              | job_title                                      | update_time   |
|---:|:-----------------------------------------------------|:-----------------------------------------------|:--------------|
|  1 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/) | [後端工程師](https://www.1111.com.tw/job/85012186/) | 2021-09-19    |



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
