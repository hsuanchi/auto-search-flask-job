# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                                | job_title                                                                                               | update_time   |
|---:|:-------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [Gorilla Technology Group_大猩猩科技股份有限公司](https://www.104.com.tw/company/wilokdc?jobsource=jolist_a_date) | [Jr. / Sr. Front End Engineer](https://www.104.com.tw/job/6o30x?jobsource=jolist_a_date)                | 10/29         |
|  2 | [Gorilla Technology Group_大猩猩科技股份有限公司](https://www.104.com.tw/company/wilokdc?jobsource=jolist_a_date) | [Sr. Java Software Developer](https://www.104.com.tw/job/3yh2d?jobsource=jolist_a_date)                 | 10/29         |
|  3 | [光禾感知科技股份有限公司](https://www.104.com.tw/company/1a2x6bks9s?jobsource=jolist_a_date)                      | [Python後端工程師](https://www.104.com.tw/job/71j4l?jobsource=jolist_a_date)                                 | 10/29         |
|  4 | [德義資訊股份有限公司](https://www.104.com.tw/company/oe84aqo?jobsource=jolist_b_relevance)                      | [Backend 系統開發工程師](https://www.104.com.tw/job/7awmz?jobsource=jolist_b_relevance)                        | 10/26         |
|  5 | [禾向數位科技有限公司](https://www.104.com.tw/company/1a2x6bl8h8?jobsource=jolist_a_date)                        | [Python Backend Engineer](https://www.104.com.tw/job/71i7c?jobsource=jolist_a_date)                     | 10/29         |
|  6 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_b_relevance)                      | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_b_relevance)                | 10/27         |
|  7 | [聚典資訊股份有限公司](https://www.104.com.tw/company/1a2x6bl0ew?jobsource=jolist_a_date)                        | [軟體工程師 Software engineer/full-stack Engineer](https://www.104.com.tw/job/78evf?jobsource=jolist_a_date) | 10/29         |
|  8 | [英屬開曼群島商萬里雲互聯股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bk5cu?jobsource=jolist_a_date)           | [Backend Engineer 後端工程師](https://www.104.com.tw/job/6xipk?jobsource=jolist_a_date)                      | 10/29         |
|  9 | [英屬開曼群島商萬里雲互聯股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bk5cu?jobsource=jolist_a_date)           | [Machine Learning Engineer 機器學習工程師 ](https://www.104.com.tw/job/6c61u?jobsource=jolist_a_date)          | 10/29         |

### Platform - 1111


|    | company                                                                    | job_title                                                                          | update_time   |
|---:|:---------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|:--------------|
|  1 | [(獵頭)Accurate愛客獵股份有限公司(1111 高階獵才)](https://www.1111.com.tw/corp/69647966/) | [直播平台_Senior Backend Developer(3002871)](https://www.1111.com.tw/job/85960420/)    | 2020-05-15    |
|  2 | [(獵頭)Accurate愛客獵股份有限公司(1111 高階獵才)](https://www.1111.com.tw/corp/69647966/) | [Dev (Develop Engineer)前端_知名電子公司 (3005070)](https://www.1111.com.tw/job/97460023/) | 2021-07-05    |
|  3 | [(獵頭)Accurate愛客獵股份有限公司(1111 高階獵才)](https://www.1111.com.tw/corp/69647966/) | [Dev (Develop Engineer)後端_知名電子公司 (3005117)](https://www.1111.com.tw/job/97460074/) | 2021-07-05    |
|  4 | [(獵頭)Accurate愛客獵股份有限公司(1111 高階獵才)](https://www.1111.com.tw/corp/69647966/) | [Dev (Technical Lead)_知名電子公司 (3005066)](https://www.1111.com.tw/job/97459998/)     | 2021-07-05    |
|  5 | [中租迪和股份有限公司](https://www.1111.com.tw/corp/2850037/)                        | [【中租超利士】中台架構師](https://www.1111.com.tw/job/97507405/)                              | 2021-10-27    |
|  6 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/)                       | [後端工程師](https://www.1111.com.tw/job/85012186/)                                     | 2021-10-29    |



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
