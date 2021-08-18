# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                     | job_title                                                                                               | update_time   |
|---:|:--------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [大數據股份有限公司](https://www.104.com.tw/company/1a2x6bjjhc?jobsource=2018indexpoc)               | [分析研發工程師: AI, Deep Learning, Machine Learning](https://www.104.com.tw/job/54ffa?jobsource=2018indexpoc) | 8/18          |
|  2 | [展市華科技有限公司](https://www.104.com.tw/company/1a2x6blbgu?jobsource=jolist_d_relevance)         | [後端網頁工程師](https://www.104.com.tw/job/71amu?jobsource=jolist_d_relevance)                                | 8/12          |
|  3 | [新加坡商威兆科技有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bjqez?jobsource=jolist_d_relevance) | [Junior IT Developer (助理 IT 程式設計師)](https://www.104.com.tw/job/7bely?jobsource=jolist_d_relevance)      | 7/15          |
|  4 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_d_relevance)           | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_d_relevance)                | 8/18          |
|  5 | [網聯科技股份有限公司](https://www.104.com.tw/company/1a2x6bkpi3?jobsource=jolist_d_relevance)        | [後端工程師](https://www.104.com.tw/job/76n8r?jobsource=jolist_d_relevance)                                  | 8/08          |
|  6 | [萊泀有限公司](https://www.104.com.tw/company/1a2x6blg3t?jobsource=jolist_d_relevance)            | [Python (Django、Flask)程式設計師](https://www.104.com.tw/job/7cs5e?jobsource=jolist_d_relevance)             | 8/16          |
|  7 | [雙子星雲端運算股份有限公司](https://www.104.com.tw/company/1a2x6bjeye?jobsource=2018indexpoc)           | [雲端軟體工程師(可視訊面試)](https://www.104.com.tw/job/58it4?jobsource=2018indexpoc)                               | 8/18          |

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
