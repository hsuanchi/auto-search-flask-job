# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                              | job_title                                                                                                                | update_time   |
|---:|:-------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [九七科技股份有限公司](https://www.104.com.tw/company/1a2x6bl9vu?jobsource=jolist_b_date)      | [Junior and Senior Data scientist](https://www.104.com.tw/job/7fde6?jobsource=jolist_b_date)                             | 1/11          |
|  2 | [光禾感知科技股份有限公司](https://www.104.com.tw/company/1a2x6bks9s?jobsource=jolist_b_date)    | [Python後端工程師](https://www.104.com.tw/job/71j4l?jobsource=jolist_b_date)                                                  | 1/11          |
|  3 | [友威資訊服務股份有限公司](https://www.104.com.tw/company/1a2x6blnx5?jobsource=jolist_b_date)    | [Python 智慧製造系統工程師【世界知名半導體代工廠】，工作穩定，薪資優渥](https://www.104.com.tw/job/7f138?jobsource=jolist_b_date)                       | 1/11          |
|  4 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_c_relevance) | [Python後端工程師](https://www.104.com.tw/job/76vbt?jobsource=jolist_c_relevance)                                             | 1/05          |
|  5 | [淼森科技股份有限公司](https://www.104.com.tw/company/1a2x6blm7t?jobsource=jolist_c_relevance) | [Web App Backend Developer 後端工程師 AWS/Flask/Postman/MySQL](https://www.104.com.tw/job/7a7i3?jobsource=jolist_c_relevance) | 1/06          |
|  6 | [物聯網股份有限公司](https://www.104.com.tw/company/1a2x6bk3uw?jobsource=jolist_b_date)       | [資深Python工程師-台北(DF2)](https://www.104.com.tw/job/7du8c?jobsource=jolist_b_date)                                          | 1/11          |
|  7 | [禾向數位科技有限公司](https://www.104.com.tw/company/1a2x6bl8h8?jobsource=jolist_b_date)      | [Python Backend Engineer](https://www.104.com.tw/job/71i7c?jobsource=jolist_b_date)                                      | 1/11          |
|  8 | [紐奧谷科技股份有限公司](https://www.104.com.tw/company/1a2x6blk60?jobsource=jolist_b_date)     | [Developer 開發工程師 (Python)](https://www.104.com.tw/job/78o4v?jobsource=jolist_b_date)                                     | 1/12          |
|  9 | [艾酷互動股份有限公司](https://www.104.com.tw/company/1a2x6bkq17?jobsource=jolist_b_date)      | [數據⼯程師](https://www.104.com.tw/job/7275w?jobsource=jolist_b_date)                                                        | 1/11          |
| 10 | [金正禾數位有限公司](https://www.104.com.tw/company/1a2x6bl4su?jobsource=jolist_b_date)       | [Backend Engineer 後端工程師](https://www.104.com.tw/job/720ep?jobsource=jolist_b_date)                                       | 1/11          |
| 11 | [長川資訊股份有限公司](https://www.104.com.tw/company/1a2x6bi3xl?jobsource=jolist_b_date)      | [Python全端工程師](https://www.104.com.tw/job/7h9wo?jobsource=jolist_b_date)                                                  | 1/11          |
| 12 | [雄獅資訊科技股份有限公司](https://www.104.com.tw/company/13kq7dpk?jobsource=jolist_b_date)      | [python工程師](https://www.104.com.tw/job/71rxc?jobsource=jolist_b_date)                                                    | 1/11          |

### Platform - 1111


|    | company                                                                          | job_title                                                                             | update_time   |
|---:|:---------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|:--------------|
|  1 | [(派遣)萬寶華企業管理顧問股份有限公司](https://www.1111.com.tw/corp/9590529/)                     | [美商玻璃基板大廠_全端工程師Full Stack Engineer](https://www.1111.com.tw/job/98565216/)            | 2022-01-10    |
|  2 | [(獵頭)Accurate愛客獵股份有限公司(1111 高階獵才)](https://www.1111.com.tw/corp/69647966/)       | [直播平台_Senior Backend Developer(3002871)](https://www.1111.com.tw/job/85960420/)       | 2020-05-15    |
|  3 | [中租迪和股份有限公司](https://www.1111.com.tw/corp/2850037/)                              | [【中租超利士】中台架構師](https://www.1111.com.tw/job/97507405/)                                 | 2022-01-10    |
|  4 | [台灣美光晶圓科技股份有限公司](https://www.1111.com.tw/corp/9622349/)                          | [【桃園/台中廠擴大招募】SR Data Engineer, Smart MFG & AI](https://www.1111.com.tw/job/97430508/) | 2022-01-03    |
|  5 | [美超微電腦股份有限公司(Super Micro Computer, Inc.)](https://www.1111.com.tw/corp/9530088/) | [Software Engineer-TC21167](https://www.1111.com.tw/job/98544764/)                    | 2022-01-05    |



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
