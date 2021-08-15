# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                                                  | job_title                                                                                                                         | update_time   |
|---:|:-------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [台灣美光(台灣美光晶圓科技股份有限公司/台灣美光記憶體股份有限公司/美商美光亞太科技股份有限公司台灣分公司)](https://www.104.com.tw/company/10ww9gpk?jobsource=2018indexpoc) | [【2021應屆畢業生報名專區】Data Engineer, Smart MFG &amp; AI (Taichung or Taoyuan)](https://www.104.com.tw/job/7ag8f?jobsource=2018indexpoc) | 8/13          |
|  2 | [小柿智檢科技股份有限公司](https://www.104.com.tw/company/1a2x6bl77l?jobsource=2018indexpoc)                                         | [後端工程師 Back-End Engineer](https://www.104.com.tw/job/71bmd?jobsource=2018indexpoc)                                                | 8/14          |
|  3 | [小柿智檢科技股份有限公司](https://www.104.com.tw/company/1a2x6bl77l?jobsource=2018indexpoc)                                         | [全端工程師 Full-Stack Engineer](https://www.104.com.tw/job/71bmz?jobsource=2018indexpoc)                                              | 8/14          |
|  4 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_b_relevance)                                        | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_b_relevance)                                          | 8/11          |
|  5 | [美商美創資通股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bjdsb?jobsource=2018indexpoc)                                    | [資深Web後端工程師](https://www.104.com.tw/job/6y6f0?jobsource=2018indexpoc)                                                             | 8/13          |
|  6 | [蓋特資訊系統股份有限公司](https://www.104.com.tw/company/1a2x6biptb?jobsource=jolist_b_relevance)                                   | [Senior Machine Learning Engineer](https://www.104.com.tw/job/6e6r8?jobsource=jolist_b_relevance)                                 | 8/13          |
|  7 | [貸先生資訊平台有限公司](https://www.104.com.tw/company/1a2x6blnk6?jobsource=2018indexpoc)                                          | [系統部-網站後端API開發工程師 (可遠距工作/每週進公司開會/全職/限台中) [NO.D4]](https://www.104.com.tw/job/7bfnu?jobsource=2018indexpoc)                        | 8/14          |

### Platform - 1111


|    | company                                              | job_title                                      | update_time   |
|---:|:-----------------------------------------------------|:-----------------------------------------------|:--------------|
|  1 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/) | [後端工程師](https://www.1111.com.tw/job/85012186/) | 2021-08-15    |



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
