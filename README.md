# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                                | job_title                                                                                                      | update_time   |
|---:|:-------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [Algotech_新加坡商艾高科技股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6blc6n?jobsource=jolist_d_relevance) | [產品工程師/Python工程師](https://www.104.com.tw/job/7duf1?jobsource=jolist_d_relevance)                               | 11/03         |
|  2 | [Gorilla Technology Group_大猩猩科技股份有限公司](https://www.104.com.tw/company/wilokdc?jobsource=jolist_c_date) | [Software Engineer _　Jr. / Sr. Frontend Development](https://www.104.com.tw/job/6o30x?jobsource=jolist_c_date) | 11/05         |
|  3 | [Gorilla Technology Group_大猩猩科技股份有限公司](https://www.104.com.tw/company/wilokdc?jobsource=jolist_c_date) | [Software Engineer _ Senior Java Development](https://www.104.com.tw/job/3yh2d?jobsource=jolist_c_date)        | 11/05         |
|  4 | [九七科技股份有限公司](https://www.104.com.tw/company/1a2x6bl9vu?jobsource=jolist_d_relevance)                   | [資料科學家](https://www.104.com.tw/job/7fde6?jobsource=jolist_d_relevance)                                         | 11/04         |
|  5 | [光禾感知科技股份有限公司](https://www.104.com.tw/company/1a2x6bks9s?jobsource=jolist_c_date)                      | [Python後端工程師](https://www.104.com.tw/job/71j4l?jobsource=jolist_c_date)                                        | 11/05         |
|  6 | [同步科技股份有限公司](https://www.104.com.tw/company/1a2x6ble88?jobsource=jolist_c_date)                        | [後端工程師](https://www.104.com.tw/job/76q8x?jobsource=jolist_c_date)                                              | 11/05         |
|  7 | [囿宇資訊有限公司](https://www.104.com.tw/company/1a2x6bldgy?jobsource=jolist_c_date)                          | [【Senior Backend Engineer】資深Python後端工程師](https://www.104.com.tw/job/7dr0z?jobsource=jolist_c_date)             | 11/05         |
|  8 | [小柿智檢科技股份有限公司](https://www.104.com.tw/company/1a2x6bl77l?jobsource=jolist_c_date)                      | [後端工程師 Back-End Engineer](https://www.104.com.tw/job/71bmd?jobsource=jolist_c_date)                            | 11/06         |
|  9 | [小柿智檢科技股份有限公司](https://www.104.com.tw/company/1a2x6bl77l?jobsource=jolist_c_date)                      | [全端工程師 Full-Stack Engineer](https://www.104.com.tw/job/71bmz?jobsource=jolist_c_date)                          | 11/06         |
| 10 | [禾向數位科技有限公司](https://www.104.com.tw/company/1a2x6bl8h8?jobsource=jolist_c_date)                        | [Python Backend Engineer](https://www.104.com.tw/job/71i7c?jobsource=jolist_c_date)                            | 11/05         |
| 11 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_d_relevance)                      | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_d_relevance)                       | 10/27         |
| 12 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_d_relevance)                      | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_d_relevance)                       | 10/27         |
| 13 | [香港商俊思海外有限公司台灣分公司](https://www.104.com.tw/company/wiwdx20?jobsource=jolist_c_date)                     | [Backend developer (Lane Crawford Joyce Group)](https://www.104.com.tw/job/70uyc?jobsource=jolist_c_date)      | 11/06         |
| 14 | [香港商俊思海外有限公司台灣分公司](https://www.104.com.tw/company/wiwdx20?jobsource=jolist_c_date)                     | [Full stack developer  (Lane Crawford Joyce Group)](https://www.104.com.tw/job/76ao6?jobsource=jolist_c_date)  | 11/06         |

### Platform - 1111


|    | company                                              | job_title                                      | update_time   |
|---:|:-----------------------------------------------------|:-----------------------------------------------|:--------------|
|  1 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/) | [後端工程師](https://www.1111.com.tw/job/85012186/) | 2021-11-03    |



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
