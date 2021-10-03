# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                           | job_title                                                                                               | update_time   |
|---:|:----------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [今時科技股份有限公司](https://www.104.com.tw/company/1a2x6bl2u4?jobsource=jolist_c_date)   | [網頁開發工程師  * 歡迎兼職論件計酬](https://www.104.com.tw/job/75jgv?jobsource=jolist_c_date)                         | 10/03         |
|  2 | [今時科技股份有限公司](https://www.104.com.tw/company/1a2x6bl2u4?jobsource=jolist_c_date)   | [網頁前端程式設計師](https://www.104.com.tw/job/79aqn?jobsource=jolist_c_date)                                   | 10/03         |
|  3 | [吉音資訊有限公司](https://www.104.com.tw/company/10uhacsw?jobsource=jolist_c_date)       | [高薪徵PHP程式開發人才(專案聘請 2-3年職(視情況再延長 ;Cable或電信業))](https://www.104.com.tw/job/2j2kp?jobsource=jolist_c_date) | 10/03         |
|  4 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_d_relevance) | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_d_relevance)                | 9/29          |
|  5 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_d_relevance) | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_d_relevance)                | 9/29          |
|  6 | [華翰物產實業股份有限公司](https://www.104.com.tw/company/10xb8hsw?jobsource=jolist_c_date)   | [資深資料科學家(Senior Data Scientist)](https://www.104.com.tw/job/72vx2?jobsource=jolist_c_date)              | 10/03         |
|  7 | [萊泀有限公司](https://www.104.com.tw/company/1a2x6blg3t?jobsource=jolist_d_relevance)  | [Python (Django、Flask)程式設計師](https://www.104.com.tw/job/7cs5e?jobsource=jolist_d_relevance)             | 9/28          |
|  8 | [蓋特資訊系統股份有限公司](https://www.104.com.tw/company/1a2x6biptb?jobsource=jolist_c_date) | [Senior Machine Learning Engineer](https://www.104.com.tw/job/6e6r8?jobsource=jolist_c_date)            | 10/03         |

### Platform - 1111


|    | company                                                                    | job_title                                                                             | update_time   |
|---:|:---------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|:--------------|
|  1 | [(獵頭)Accurate愛客獵股份有限公司(1111 高階獵才)](https://www.1111.com.tw/corp/69647966/) | [直播平台_Senior Backend Developer(3002871)](https://www.1111.com.tw/job/85960420/)       | 2020-05-15    |
|  2 | [(獵頭)Accurate愛客獵股份有限公司(1111 高階獵才)](https://www.1111.com.tw/corp/69647966/) | [Dev (Develop Engineer)前端_知名電子公司 (3005070)](https://www.1111.com.tw/job/97460023/)    | 2021-07-05    |
|  3 | [(獵頭)Accurate愛客獵股份有限公司(1111 高階獵才)](https://www.1111.com.tw/corp/69647966/) | [Dev (Develop Engineer)後端_知名電子公司 (3005117)](https://www.1111.com.tw/job/97460074/)    | 2021-07-05    |
|  4 | [(獵頭)Accurate愛客獵股份有限公司(1111 高階獵才)](https://www.1111.com.tw/corp/69647966/) | [Dev (Technical Lead)_知名電子公司 (3005066)](https://www.1111.com.tw/job/97459998/)        | 2021-07-05    |
|  5 | [中租迪和股份有限公司](https://www.1111.com.tw/corp/2850037/)                        | [【中租超利士】中台架構師](https://www.1111.com.tw/job/97507405/)                                 | 2021-10-02    |
|  6 | [台灣美光晶圓科技股份有限公司](https://www.1111.com.tw/corp/9622349/)                    | [【桃園/台中廠擴大招募】SR Data Engineer, Smart MFG & AI](https://www.1111.com.tw/job/97430508/) | 2021-10-01    |
|  7 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/)                       | [後端工程師](https://www.1111.com.tw/job/85012186/)                                        | 2021-09-29    |



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
