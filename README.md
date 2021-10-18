# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                               | job_title                                                                                                | update_time   |
|---:|:--------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [普匯金融科技股份有限公司](https://www.104.com.tw/company/1a2x6bkhzg?jobsource=jolist_d_date)     | [python工程師](https://www.104.com.tw/job/7ark5?jobsource=jolist_d_date)                                    | 10/19         |
|  2 | [環球睿視股份有限公司](https://www.104.com.tw/company/1a2x6bjtu2?jobsource=jolist_d_date)       | [(全職)AI Chatbot語意機器人/語音機器人系統平台開發建置[視需要使用視訊面談]](https://www.104.com.tw/job/6rddw?jobsource=jolist_d_date) | 10/18         |
|  3 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_c_relevance)     | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_c_relevance)                 | 10/13         |
|  4 | [美商_睿科網路科技有限公司](https://www.104.com.tw/company/bjr7240?jobsource=jolist_d_date)       | [[HOT!] Senior Full-Stack Web Developer 全端工程師](https://www.104.com.tw/job/7ca8w?jobsource=jolist_d_date) | 10/18         |
|  5 | [雲磐科技有限公司](https://www.104.com.tw/company/1a2x6blkbl?jobsource=jolist_d_date)         | [Python Backend / Automation Engineer](https://www.104.com.tw/job/7eymp?jobsource=jolist_d_date)         | 10/18         |
|  6 | [香港商凱渤維思有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bkgaj?jobsource=jolist_d_date) | [前端(全棧)開發人員](https://www.104.com.tw/job/6aiim?jobsource=jolist_d_date)                                   | 10/18         |

### Platform - 1111


|    | company                                                                    | job_title                                                                          | update_time   |
|---:|:---------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|:--------------|
|  1 | [(獵頭)Accurate愛客獵股份有限公司(1111 高階獵才)](https://www.1111.com.tw/corp/69647966/) | [直播平台_Senior Backend Developer(3002871)](https://www.1111.com.tw/job/85960420/)    | 2020-05-15    |
|  2 | [(獵頭)Accurate愛客獵股份有限公司(1111 高階獵才)](https://www.1111.com.tw/corp/69647966/) | [Dev (Develop Engineer)前端_知名電子公司 (3005070)](https://www.1111.com.tw/job/97460023/) | 2021-07-05    |
|  3 | [(獵頭)Accurate愛客獵股份有限公司(1111 高階獵才)](https://www.1111.com.tw/corp/69647966/) | [Dev (Develop Engineer)後端_知名電子公司 (3005117)](https://www.1111.com.tw/job/97460074/) | 2021-07-05    |
|  4 | [(獵頭)Accurate愛客獵股份有限公司(1111 高階獵才)](https://www.1111.com.tw/corp/69647966/) | [Dev (Technical Lead)_知名電子公司 (3005066)](https://www.1111.com.tw/job/97459998/)     | 2021-07-05    |
|  5 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/)                       | [後端工程師](https://www.1111.com.tw/job/85012186/)                                     | 2021-10-14    |



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
