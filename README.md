# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                            | job_title                                                                                 | update_time   |
|---:|:---------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------|:--------------|
|  1 | [xarefit享健身_香港商宇晨品牌顧問有限公司台灣分公司](https://www.104.com.tw/company/1a2x6blkn9?jobsource=jolist_a_date) | [【擴大徵才中】後端工程師 Backend Engineer](https://www.104.com.tw/job/791ud?jobsource=jolist_a_date) | 11/04         |
|  2 | [九七科技股份有限公司](https://www.104.com.tw/company/1a2x6bl9vu?jobsource=jolist_a_date)                    | [資料科學家](https://www.104.com.tw/job/7fde6?jobsource=jolist_a_date)                         | 11/04         |
|  3 | [九七科技股份有限公司](https://www.104.com.tw/company/1a2x6bl9vu?jobsource=jolist_b_relevance)               | [資料科學家](https://www.104.com.tw/job/7fde6?jobsource=jolist_b_relevance)                    | 11/04         |
|  4 | [歐立威科技股份有限公司](https://www.104.com.tw/company/b8gl75c?jobsource=jolist_a_date)                      | [軟體開發工程師](https://www.104.com.tw/job/6q2ao?jobsource=jolist_a_date)                       | 11/04         |
|  5 | [米約科技有限公司](https://www.104.com.tw/company/1a2x6bl97m?jobsource=jolist_a_date)                      | [Python工程師](https://www.104.com.tw/job/6zey2?jobsource=jolist_a_date)                     | 11/04         |
|  6 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_b_relevance)                  | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_b_relevance)  | 10/27         |
|  7 | [艾酷互動股份有限公司](https://www.104.com.tw/company/1a2x6bkq17?jobsource=jolist_a_date)                    | [數據⼯程師](https://www.104.com.tw/job/7275w?jobsource=jolist_a_date)                         | 11/04         |
|  8 | [雙子星雲端運算股份有限公司](https://www.104.com.tw/company/1a2x6bjeye?jobsource=jolist_a_date)                 | [雲端軟體工程師(可視訊面試)](https://www.104.com.tw/job/58it4?jobsource=jolist_a_date)                | 11/04         |

### Platform - 1111


|    | company                                              | job_title                                      | update_time   |
|---:|:-----------------------------------------------------|:-----------------------------------------------|:--------------|
|  1 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/) | [後端工程師](https://www.1111.com.tw/job/85012186/) | 2021-11-03    |



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
