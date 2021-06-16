# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                        | job_title                                                                                     | update_time   |
|---:|:-------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|:--------------|
|  1 | [富萱科技股份有限公司](https://www.104.com.tw/company/1a2x6bkf9i?jobsource=2018indexpoc) | [Back End 研發工程師](https://www.104.com.tw/job/7ambq?jobsource=2018indexpoc)                     | 6/16          |
|  2 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=2018indexpoc) | [Python爬蟲工程師(高雄)](https://www.104.com.tw/job/7aydm?jobsource=2018indexpoc)                    | 6/10          |
|  3 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=2018indexpoc) | [Python爬蟲工程師(台北)](https://www.104.com.tw/job/7aydt?jobsource=2018indexpoc)                    | 6/10          |
|  4 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=2018indexpoc) | [Python後端開發工程師(DevOps整合平台)](https://www.104.com.tw/job/7asvo?jobsource=2018indexpoc)          | 6/10          |
|  5 | [桔畝智慧股份有限公司](https://www.104.com.tw/company/1a2x6blm8y?jobsource=2018indexpoc) | [Back-End Development Engineer後端工程師](https://www.104.com.tw/job/7a80a?jobsource=2018indexpoc) | 6/17          |
|  6 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=2018indexpoc)    | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=2018indexpoc)            | 6/10          |
|  7 | [艾斯移動股份有限公司](https://www.104.com.tw/company/cv8shww?jobsource=2018indexpoc)    | [自然語言處理工程師 (NLP Engineer)](https://www.104.com.tw/job/6nmld?jobsource=2018indexpoc)           | 6/16          |

### Platform - 1111


|    | company                                                                      | job_title                                                                             | update_time   |
|---:|:-----------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|:--------------|
|  1 | [(派遣)新加坡商立可人事顧問有限公司(Recruit Express)](https://www.1111.com.tw/corp/9992537/) | [AL-Python Engineer，外商網路公司，年薪800K~1.2M](https://www.1111.com.tw/job/91212698/)        | 2021-05-14    |
|  2 | [(獵頭)1111獵才顧問中心](https://www.1111.com.tw/corp/69647966/)                     | [直播平台_Senior Backend Developer(3002871)](https://www.1111.com.tw/job/85960420/)       | 2020-05-15    |
|  3 | [億力資訊股份有限公司](https://www.1111.com.tw/corp/54937860/)                         | [python工程師](https://www.1111.com.tw/job/97374762/)                                    | 2021-06-13    |
|  4 | [台灣美光晶圓科技股份有限公司](https://www.1111.com.tw/corp/9622349/)                      | [【桃園/台中廠擴大招募】SR Data Engineer, Smart MFG & AI](https://www.1111.com.tw/job/97430508/) | 2021-06-05    |
|  5 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/)                         | [後端工程師](https://www.1111.com.tw/job/85012186/)                                        | 2021-06-16    |



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
