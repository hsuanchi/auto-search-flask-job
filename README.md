# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                                | job_title                                                                                      | update_time   |
|---:|:-------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------|:--------------|
|  1 | [Gorilla Technology Group_大猩猩科技股份有限公司](https://www.104.com.tw/company/wilokdc?jobsource=jolist_d_date) | [Sr. Java Software Developer](https://www.104.com.tw/job/3yh2d?jobsource=jolist_d_date)        | 9/22          |
|  2 | [伊諾科技有限公司](https://www.104.com.tw/company/1a2x6bkxph?jobsource=jolist_d_date)                          | [(真摯徵求) Python後端工程師](https://www.104.com.tw/job/70asp?jobsource=jolist_d_date)                 | 9/22          |
|  3 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_d_date)                        | [Python後端開發工程師(DevOps整合平台)](https://www.104.com.tw/job/7asvo?jobsource=jolist_d_date)          | 9/22          |
|  4 | [漢康生技股份有限公司](https://www.104.com.tw/company/1a2x6blf97?jobsource=jolist_d_date)                        | [細胞培養工藝開發研究員/副研究員/助理研究員](https://www.104.com.tw/job/7cccb?jobsource=jolist_d_date)             | 9/22          |
|  5 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_c_relevance)                      | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_c_relevance)       | 9/22          |
|  6 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_d_date)                           | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_d_date)            | 9/22          |
|  7 | [英商引達取有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bkz0n?jobsource=jolist_d_date)                    | [【台北】Data Engineer](https://www.104.com.tw/job/6pki0?jobsource=jolist_d_date)                  | 9/22          |
|  8 | [英屬開曼群島商萬里雲互聯股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bk5cu?jobsource=jolist_d_date)           | [Backend Engineer 後端工程師](https://www.104.com.tw/job/6xipk?jobsource=jolist_d_date)             | 9/22          |
|  9 | [英屬開曼群島商萬里雲互聯股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bk5cu?jobsource=jolist_d_date)           | [Machine Learning Engineer 機器學習工程師 ](https://www.104.com.tw/job/6c61u?jobsource=jolist_d_date) | 9/22          |
| 10 | [萊泀有限公司](https://www.104.com.tw/company/1a2x6blg3t?jobsource=jolist_c_relevance)                       | [Python (Django、Flask)程式設計師](https://www.104.com.tw/job/7cs5e?jobsource=jolist_c_relevance)    | 9/20          |
| 11 | [霖園關係企業_神坊資訊股份有限公司](https://www.104.com.tw/company/wdapdfc?jobsource=jolist_d_date)                    | [新創電商技術主管 EC Tech Team leader](https://www.104.com.tw/job/7aelb?jobsource=jolist_d_date)       | 9/22          |
| 12 | [霖園關係企業_神坊資訊股份有限公司](https://www.104.com.tw/company/wdapdfc?jobsource=jolist_d_date)                    | [新創電商Frontend Engineer](https://www.104.com.tw/job/7aen9?jobsource=jolist_d_date)              | 9/22          |

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
