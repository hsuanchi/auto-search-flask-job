# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                     | job_title                                                                                         | update_time   |
|---:|:--------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------|:--------------|
|  1 | [伊諾科技有限公司](https://www.104.com.tw/company/1a2x6bkxph?jobsource=2018indexpoc)                | [(真摯徵求) Python後端工程師](https://www.104.com.tw/job/70asp?jobsource=2018indexpoc)                     | 8/10          |
|  2 | [同步科技股份有限公司](https://www.104.com.tw/company/1a2x6ble88?jobsource=2018indexpoc)              | [後端工程師](https://www.104.com.tw/job/76q8x?jobsource=2018indexpoc)                                  | 8/10          |
|  3 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_a_relevance)           | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_a_relevance)          | 8/03          |
|  4 | [英屬開曼群島商萬里雲互聯股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bk5cu?jobsource=2018indexpoc) | [Backend Engineer 後端工程師](https://www.104.com.tw/job/6xipk?jobsource=2018indexpoc)                 | 8/10          |
|  5 | [英屬開曼群島商萬里雲互聯股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bk5cu?jobsource=2018indexpoc) | [Machine Learning Engineer 機器學習工程師 ](https://www.104.com.tw/job/6c61u?jobsource=2018indexpoc)     | 8/10          |
|  6 | [蓋特資訊系統股份有限公司](https://www.104.com.tw/company/1a2x6biptb?jobsource=jolist_a_relevance)      | [Senior Machine Learning Engineer](https://www.104.com.tw/job/6e6r8?jobsource=jolist_a_relevance) | 7/28          |

### Platform - 1111


|    | company                                              | job_title                                      | update_time   |
|---:|:-----------------------------------------------------|:-----------------------------------------------|:--------------|
|  1 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/) | [後端工程師](https://www.1111.com.tw/job/85012186/) | 2021-08-10    |



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
