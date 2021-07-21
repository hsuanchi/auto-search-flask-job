# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                       | job_title                                                                             | update_time   |
|---:|:----------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|:--------------|
|  1 | [展市華科技有限公司](https://www.104.com.tw/company/1a2x6blbgu?jobsource=jolist_d_relevance)           | [網頁開發工程師](https://www.104.com.tw/job/78do7?jobsource=jolist_d_relevance)              | 7/14          |
|  2 | [新加坡商齊舵管理顧問有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bldr7?jobsource=jolist_d_relevance) | [影像處理軟體工程師](https://www.104.com.tw/job/77vw9?jobsource=jolist_d_relevance)            | 4/30          |
|  3 | [永昕生物醫藥股份有限公司](https://www.104.com.tw/company/5xfw7xk?jobsource=2018indexpoc)                 | [細胞產程開發研究員(台北)](https://www.104.com.tw/job/6ujnv?jobsource=2018indexpoc)              | 7/21          |
|  4 | [皮智股份有限公司](https://www.104.com.tw/company/1a2x6bkeyt?jobsource=2018indexpoc)                  | [後端程式設計師 (Backend Engineer)](https://www.104.com.tw/job/62qs2?jobsource=2018indexpoc) | 7/21          |
|  5 | [禾向數位科技有限公司](https://www.104.com.tw/company/1a2x6bl8h8?jobsource=2018indexpoc)                | [Python Backend Engineer](https://www.104.com.tw/job/71i7c?jobsource=2018indexpoc)    | 7/21          |

### Platform - 1111


|    | company                                              | job_title                                          | update_time   |
|---:|:-----------------------------------------------------|:---------------------------------------------------|:--------------|
|  1 | [億力資訊股份有限公司](https://www.1111.com.tw/corp/54937860/) | [python工程師](https://www.1111.com.tw/job/97374762/) | 2021-07-18    |
|  2 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/) | [後端工程師](https://www.1111.com.tw/job/85012186/)     | 2021-07-21    |



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
