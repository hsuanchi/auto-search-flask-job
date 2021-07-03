# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                             | job_title                                                                                               | update_time   |
|---:|:------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [博思資訊管理顧問有限公司](https://www.104.com.tw/company/1a2x6blhw5?jobsource=2018indexpoc)    | [Python工程師(可遠端工作)](https://www.104.com.tw/job/78f5b?jobsource=2018indexpoc)                             | 7/03          |
|  2 | [小柿智檢科技股份有限公司](https://www.104.com.tw/company/1a2x6bl77l?jobsource=2018indexpoc)    | [後端工程師 Back-End Engineer](https://www.104.com.tw/job/71bmd?jobsource=2018indexpoc)                      | 7/03          |
|  3 | [小柿智檢科技股份有限公司](https://www.104.com.tw/company/1a2x6bl77l?jobsource=2018indexpoc)    | [全端工程師 Full-Stack Engineer](https://www.104.com.tw/job/71bmz?jobsource=2018indexpoc)                    | 7/03          |
|  4 | [桔畝智慧股份有限公司](https://www.104.com.tw/company/1a2x6blm8y?jobsource=2018indexpoc)      | [Back-End Development Engineer後端工程師](https://www.104.com.tw/job/7a80a?jobsource=2018indexpoc)           | 7/02          |
|  5 | [禾新數位有限公司](https://www.104.com.tw/company/1a2x6bjs3i?jobsource=2018indexpoc)        | [[ E-C03 ] Full Stack Engineer（線上面試+因應疫情居家上班）](https://www.104.com.tw/job/76q8f?jobsource=2018indexpoc) | 7/03          |
|  6 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_a_relevance)   | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_a_relevance)                | 6/28          |
|  7 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_a_relevance)   | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_a_relevance)                | 6/28          |
|  8 | [英商引達取有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bkz0n?jobsource=2018indexpoc)  | [【台北】Data Engineer](https://www.104.com.tw/job/6pki0?jobsource=2018indexpoc)                            | 7/02          |
|  9 | [萊鎂醫療器材股份有限公司](https://www.104.com.tw/company/bkgh1dc?jobsource=jolist_a_relevance) | [雲端應用工程師](https://www.104.com.tw/job/791cq?jobsource=jolist_a_relevance)                                | 6/30          |

### Platform - 1111


|    | company                                              | job_title                                      | update_time   |
|---:|:-----------------------------------------------------|:-----------------------------------------------|:--------------|
|  1 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/) | [後端工程師](https://www.1111.com.tw/job/85012186/) | 2021-07-01    |



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
