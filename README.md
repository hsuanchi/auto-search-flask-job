# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                            | job_title                                                                                | update_time   |
|---:|:-----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|:--------------|
|  1 | [展市華科技有限公司](https://www.104.com.tw/company/1a2x6blbgu?jobsource=2018indexpoc)      | [後端網頁工程師](https://www.104.com.tw/job/71amu?jobsource=2018indexpoc)                       | 6/22          |
|  2 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=2018indexpoc)     | [Python後端開發工程師(DevOps整合平台)](https://www.104.com.tw/job/7asvo?jobsource=2018indexpoc)     | 6/24          |
|  3 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=2018indexpoc)        | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=2018indexpoc)       | 6/28          |
|  4 | [網聯科技股份有限公司](https://www.104.com.tw/company/1a2x6bkpi3?jobsource=2018indexpoc)     | [後端工程師](https://www.104.com.tw/job/76n8r?jobsource=2018indexpoc)                         | 6/29          |
|  5 | [萊鎂醫療器材股份有限公司](https://www.104.com.tw/company/bkgh1dc?jobsource=2018indexpoc)      | [雲端應用工程師](https://www.104.com.tw/job/791cq?jobsource=2018indexpoc)                       | 6/23          |
|  6 | [霖園關係企業_神坊資訊股份有限公司](https://www.104.com.tw/company/wdapdfc?jobsource=2018indexpoc) | [新創電商Backend Engineer (Python)](https://www.104.com.tw/job/7aenr?jobsource=2018indexpoc) | 6/28          |
|  7 | [霖園關係企業_神坊資訊股份有限公司](https://www.104.com.tw/company/wdapdfc?jobsource=2018indexpoc) | [新創電商技術主管 EC Tech Team leader](https://www.104.com.tw/job/7aelb?jobsource=2018indexpoc)  | 6/28          |
|  8 | [霖園關係企業_神坊資訊股份有限公司](https://www.104.com.tw/company/wdapdfc?jobsource=2018indexpoc) | [新創電商Frontend Engineer](https://www.104.com.tw/job/7aen9?jobsource=2018indexpoc)         | 6/28          |

### Platform - 1111


|    | company                                              | job_title                                            | update_time   |
|---:|:-----------------------------------------------------|:-----------------------------------------------------|:--------------|
|  1 | [億力資訊股份有限公司](https://www.1111.com.tw/corp/54937860/) | [python工程師](https://www.1111.com.tw/job/97374762/)   | 2021-06-28    |
|  2 | [美維科技股份有限公司](https://www.1111.com.tw/corp/69592323/) | [【就業雄青】後端工程師](https://www.1111.com.tw/job/97446846/) | 2021-06-24    |
|  3 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/) | [後端工程師](https://www.1111.com.tw/job/85012186/)       | 2021-06-26    |



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
