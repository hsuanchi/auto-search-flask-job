# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                              | job_title                                                                                                                | update_time   |
|---:|:-------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [吉音資訊有限公司](https://www.104.com.tw/company/10uhacsw?jobsource=jolist_a_relevance)     | [高薪徵PHP程式開發人才(專案聘請 2-3年職(視情況再延長 ;Cable或電信業))](https://www.104.com.tw/job/2j2kp?jobsource=jolist_a_relevance)             | 12/16         |
|  2 | [吉音資訊有限公司](https://www.104.com.tw/company/10uhacsw?jobsource=jolist_b_date)          | [高薪徵PHP程式開發人才(專案聘請 2-3年職(視情況再延長 ;Cable或電信業))](https://www.104.com.tw/job/2j2kp?jobsource=jolist_b_date)                  | 12/16         |
|  3 | [展市華科技有限公司](https://www.104.com.tw/company/1a2x6blbgu?jobsource=jolist_a_relevance)  | [系統工程師](https://www.104.com.tw/job/71erc?jobsource=jolist_a_relevance)                                                   | 12/13         |
|  4 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_a_relevance) | [Python後端工程師](https://www.104.com.tw/job/76vbt?jobsource=jolist_a_relevance)                                             | 12/13         |
|  5 | [淼森科技股份有限公司](https://www.104.com.tw/company/1a2x6blm7t?jobsource=jolist_a_relevance) | [Web App Backend Developer 後端工程師 AWS/Flask/Postman/MySQL](https://www.104.com.tw/job/7a7i3?jobsource=jolist_a_relevance) | 12/15         |
|  6 | [米約科技有限公司](https://www.104.com.tw/company/1a2x6bl97m?jobsource=jolist_b_date)        | [Python工程師](https://www.104.com.tw/job/6zey2?jobsource=jolist_b_date)                                                    | 12/16         |
|  7 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_a_relevance)    | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_a_relevance)                                 | 12/14         |
|  8 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_a_relevance)    | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_a_relevance)                                 | 12/14         |
|  9 | [金正禾數位有限公司](https://www.104.com.tw/company/1a2x6bl4su?jobsource=jolist_a_relevance)  | [Backend Engineer 後端工程師](https://www.104.com.tw/job/720ep?jobsource=jolist_a_relevance)                                  | 12/10         |
| 10 | [雙成數位行銷股份有限公司](https://www.104.com.tw/company/1a2x6bkqua?jobsource=jolist_b_date)    | [【Python工程師】](https://www.104.com.tw/job/7ftte?jobsource=jolist_b_date)                                                  | 12/16         |

### Platform - 1111


|    | company                                                                          | job_title                                                                                                 | update_time   |
|---:|:---------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [(獵頭)Accurate愛客獵股份有限公司(1111 高階獵才)](https://www.1111.com.tw/corp/69647966/)       | [直播平台_Senior Backend Developer(3002871)](https://www.1111.com.tw/job/85960420/)                           | 2020-05-15    |
|  2 | [(獵頭)Accurate愛客獵股份有限公司(1111 高階獵才)](https://www.1111.com.tw/corp/69647966/)       | [Dev (Develop Engineer)前端_知名電子公司 (3005070)](https://www.1111.com.tw/job/97460023/)                        | 2021-07-05    |
|  3 | [(獵頭)Accurate愛客獵股份有限公司(1111 高階獵才)](https://www.1111.com.tw/corp/69647966/)       | [Dev (Develop Engineer)後端_知名電子公司 (3005117)](https://www.1111.com.tw/job/97460074/)                        | 2021-07-05    |
|  4 | [(獵頭)Accurate愛客獵股份有限公司(1111 高階獵才)](https://www.1111.com.tw/corp/69647966/)       | [Dev (Technical Lead)_知名電子公司 (3005066)](https://www.1111.com.tw/job/97459998/)                            | 2021-07-05    |
|  5 | [中租迪和股份有限公司](https://www.1111.com.tw/corp/2850037/)                              | [【中租超利士】中台架構師](https://www.1111.com.tw/job/97507405/)                                                     | 2021-12-16    |
|  6 | [台灣美光晶圓科技股份有限公司](https://www.1111.com.tw/corp/9622349/)                          | [【2021畢業生報名專區】Data Engineer, Smart MFG & AI (Taichung or Taoyuan)](https://www.1111.com.tw/job/97430572/) | 2021-12-10    |
|  7 | [美超微電腦股份有限公司(Super Micro Computer, Inc.)](https://www.1111.com.tw/corp/9530088/) | [Software Engineer-TC21167](https://www.1111.com.tw/job/98544764/)                                        | 2021-12-16    |



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
