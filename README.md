# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                                | job_title                                                                                                      | update_time   |
|---:|:-------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [Gorilla Technology Group_大猩猩科技股份有限公司](https://www.104.com.tw/company/wilokdc?jobsource=jolist_b_date) | [Software Engineer _　Jr. / Sr. Frontend Development](https://www.104.com.tw/job/6o30x?jobsource=jolist_b_date) | 11/12         |
|  2 | [Gorilla Technology Group_大猩猩科技股份有限公司](https://www.104.com.tw/company/wilokdc?jobsource=jolist_b_date) | [Software Engineer _ Senior Java Development](https://www.104.com.tw/job/3yh2d?jobsource=jolist_b_date)        | 11/12         |
|  3 | [展市華科技有限公司](https://www.104.com.tw/company/1a2x6blbgu?jobsource=jolist_b_date)                         | [網頁開發工程師](https://www.104.com.tw/job/78do7?jobsource=jolist_b_date)                                            | 11/12         |
|  4 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_d_relevance)                      | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_d_relevance)                       | 11/08         |
|  5 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_d_relevance)                      | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_d_relevance)                       | 11/08         |

### Platform - 1111


|    | company                                              | job_title                                      | update_time   |
|---:|:-----------------------------------------------------|:-----------------------------------------------|:--------------|
|  1 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/) | [後端工程師](https://www.1111.com.tw/job/85012186/) | 2021-11-11    |



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
