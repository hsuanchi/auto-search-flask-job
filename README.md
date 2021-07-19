# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                          | job_title                                                                                 | update_time   |
|---:|:---------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------|:--------------|
|  1 | [博思資訊管理顧問有限公司](https://www.104.com.tw/company/1a2x6blhw5?jobsource=2018indexpoc) | [Python工程師(可遠端工作)](https://www.104.com.tw/job/78f5b?jobsource=2018indexpoc)               | 7/19          |
|  2 | [宏佳騰動力科技股份有限公司](https://www.104.com.tw/company/111bwt14?jobsource=2018indexpoc)  | [Python全端工程師](https://www.104.com.tw/job/6s9aa?jobsource=2018indexpoc)                    | 7/19          |
|  3 | [瑪樂愛迪科技股份有限公司](https://www.104.com.tw/company/1a2x6bld1f?jobsource=2018indexpoc) | [Data Engineer / Python（Remote）](https://www.104.com.tw/job/77ymq?jobsource=2018indexpoc) | 7/19          |
|  4 | [艾斯移動股份有限公司](https://www.104.com.tw/company/cv8shww?jobsource=2018indexpoc)      | [自然語言處理工程師 (NLP Engineer)](https://www.104.com.tw/job/6nmld?jobsource=2018indexpoc)       | 7/19          |

### Platform - 1111


|    | company                                              | job_title                                          | update_time   |
|---:|:-----------------------------------------------------|:---------------------------------------------------|:--------------|
|  1 | [億力資訊股份有限公司](https://www.1111.com.tw/corp/54937860/) | [python工程師](https://www.1111.com.tw/job/97374762/) | 2021-07-18    |
|  2 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/) | [後端工程師](https://www.1111.com.tw/job/85012186/)     | 2021-07-16    |



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
