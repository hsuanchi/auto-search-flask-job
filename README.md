# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                                                  | job_title                                                                                                                         | update_time   |
|---:|:-------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [台灣美光(台灣美光晶圓科技股份有限公司/台灣美光記憶體股份有限公司/美商美光亞太科技股份有限公司台灣分公司)](https://www.104.com.tw/company/10ww9gpk?jobsource=2018indexpoc) | [【2021應屆畢業生報名專區】Data Engineer, Smart MFG &amp; AI (Taichung or Taoyuan)](https://www.104.com.tw/job/7ag8f?jobsource=2018indexpoc) | 8/06          |
|  2 | [吉音資訊有限公司](https://www.104.com.tw/company/10uhacsw?jobsource=2018indexpoc)                                               | [高薪徵PHP程式開發人才(專案聘請 2-3年職(視情況再延長 ;Cable或電信業))](https://www.104.com.tw/job/2j2kp?jobsource=2018indexpoc)                            | 8/07          |
|  3 | [小柿智檢科技股份有限公司](https://www.104.com.tw/company/1a2x6bl77l?jobsource=2018indexpoc)                                         | [後端工程師 Back-End Engineer](https://www.104.com.tw/job/71bmd?jobsource=2018indexpoc)                                                | 8/07          |
|  4 | [小柿智檢科技股份有限公司](https://www.104.com.tw/company/1a2x6bl77l?jobsource=2018indexpoc)                                         | [全端工程師 Full-Stack Engineer](https://www.104.com.tw/job/71bmz?jobsource=2018indexpoc)                                              | 8/07          |
|  5 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_a_relevance)                                        | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_a_relevance)                                          | 8/03          |
|  6 | [網聯科技股份有限公司](https://www.104.com.tw/company/1a2x6bkpi3?jobsource=2018indexpoc)                                           | [後端工程師](https://www.104.com.tw/job/76n8r?jobsource=2018indexpoc)                                                                  | 8/08          |
|  7 | [蓋特資訊系統股份有限公司](https://www.104.com.tw/company/1a2x6biptb?jobsource=jolist_a_relevance)                                   | [Senior Machine Learning Engineer](https://www.104.com.tw/job/6e6r8?jobsource=jolist_a_relevance)                                 | 7/28          |

### Platform - 1111


|    | company                                              | job_title                                          | update_time   |
|---:|:-----------------------------------------------------|:---------------------------------------------------|:--------------|
|  1 | [億力資訊股份有限公司](https://www.1111.com.tw/corp/54937860/) | [python工程師](https://www.1111.com.tw/job/97374762/) | 2021-08-05    |
|  2 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/) | [後端工程師](https://www.1111.com.tw/job/85012186/)     | 2021-08-05    |



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
