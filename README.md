# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                           | job_title                                                                                                 | update_time   |
|---:|:--------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [伊諾科技有限公司](https://www.104.com.tw/company/1a2x6bkxph?jobsource=jolist_b_date)                     | [(真摯徵求) Python後端工程師](https://www.104.com.tw/job/70asp?jobsource=jolist_b_date)                            | 9/14          |
|  2 | [台灣浩鼎生技股份有限公司](https://www.104.com.tw/company/60trb48?jobsource=jolist_b_date)                    | [R&amp;D- Scientist (Fermentation development)](https://www.104.com.tw/job/75d9g?jobsource=jolist_b_date) | 9/14          |
|  3 | [城科國際_CYBILL TEK SOFTWARE INC](https://www.104.com.tw/company/1a2x6bl0gd?jobsource=jolist_b_date) | [(遠端)Python工程師](https://www.104.com.tw/job/7a4xc?jobsource=jolist_b_date)                                 | 9/14          |
|  4 | [童綜合醫療社團法人童綜合醫院](https://www.104.com.tw/company/kw8xsls?jobsource=jolist_b_date)                  | [資訊部Python 工程師](https://www.104.com.tw/job/6upji?jobsource=jolist_b_date)                                 | 9/14          |
|  5 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_c_relevance)                 | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_c_relevance)                  | 9/13          |
|  6 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_c_relevance)                 | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_c_relevance)                  | 9/13          |
|  7 | [紫式大數據決策股份有限公司](https://www.104.com.tw/company/1a2x6bkygn?jobsource=jolist_b_date)                | [後端工程師--機器學習系統整合開發](https://www.104.com.tw/job/6p2d5?jobsource=jolist_b_date)                             | 9/14          |
|  8 | [聚典資訊股份有限公司](https://www.104.com.tw/company/1a2x6bl0ew?jobsource=jolist_b_date)                   | [軟體工程師 Software engineer/full-stack Engineer](https://www.104.com.tw/job/78evf?jobsource=jolist_b_date)   | 9/14          |
|  9 | [英屬開曼群島商萬里雲互聯股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bk5cu?jobsource=jolist_b_date)      | [Backend Engineer 後端工程師](https://www.104.com.tw/job/6xipk?jobsource=jolist_b_date)                        | 9/14          |
| 10 | [英屬開曼群島商萬里雲互聯股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bk5cu?jobsource=jolist_b_date)      | [Machine Learning Engineer 機器學習工程師 ](https://www.104.com.tw/job/6c61u?jobsource=jolist_b_date)            | 9/14          |
| 11 | [萊泀有限公司](https://www.104.com.tw/company/1a2x6blg3t?jobsource=jolist_c_relevance)                  | [Python (Django、Flask)程式設計師](https://www.104.com.tw/job/7cs5e?jobsource=jolist_c_relevance)               | 8/16          |

### Platform - 1111


|    | company                                              | job_title                                      | update_time   |
|---:|:-----------------------------------------------------|:-----------------------------------------------|:--------------|
|  1 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/) | [後端工程師](https://www.1111.com.tw/job/85012186/) | 2021-09-14    |



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
