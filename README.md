# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                     | job_title                                                                                       | update_time   |
|---:|:--------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------|:--------------|
|  1 | [台灣浩鼎生技股份有限公司](https://www.104.com.tw/company/60trb48?jobsource=2018indexpoc)               | [Scientist (Fermentation development)](https://www.104.com.tw/job/75d9g?jobsource=2018indexpoc) | 7/06          |
|  2 | [展市華科技有限公司](https://www.104.com.tw/company/1a2x6blbgu?jobsource=2018indexpoc)               | [網頁開發工程師](https://www.104.com.tw/job/78do7?jobsource=2018indexpoc)                              | 7/06          |
|  3 | [普匯金融科技股份有限公司](https://www.104.com.tw/company/1a2x6bkhzg?jobsource=2018indexpoc)            | [python工程師](https://www.104.com.tw/job/7ark5?jobsource=2018indexpoc)                            | 7/06          |
|  4 | [永昕生物醫藥股份有限公司](https://www.104.com.tw/company/5xfw7xk?jobsource=2018indexpoc)               | [細胞產程開發研究員(台北)](https://www.104.com.tw/job/6ujnv?jobsource=2018indexpoc)                        | 7/06          |
|  5 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_c_relevance)           | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_c_relevance)        | 6/28          |
|  6 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_c_relevance)           | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_c_relevance)        | 6/28          |
|  7 | [英屬開曼群島商萬里雲互聯股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bk5cu?jobsource=2018indexpoc) | [Machine Learning Engineer 機器學習工程師 ](https://www.104.com.tw/job/6c61u?jobsource=2018indexpoc)   | 7/06          |
|  8 | [英屬開曼群島商萬里雲互聯股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bk5cu?jobsource=2018indexpoc) | [Backend Engineer 後端工程師](https://www.104.com.tw/job/6xipk?jobsource=2018indexpoc)               | 7/06          |
|  9 | [霖園關係企業_神坊資訊股份有限公司](https://www.104.com.tw/company/wdapdfc?jobsource=2018indexpoc)          | [新創電商Backend Engineer (Python)](https://www.104.com.tw/job/7aenr?jobsource=2018indexpoc)        | 7/06          |

### Platform - 1111


|    | company                                              | job_title                                          | update_time   |
|---:|:-----------------------------------------------------|:---------------------------------------------------|:--------------|
|  1 | [億力資訊股份有限公司](https://www.1111.com.tw/corp/54937860/) | [python工程師](https://www.1111.com.tw/job/97374762/) | 2021-07-06    |
|  2 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/) | [後端工程師](https://www.1111.com.tw/job/85012186/)     | 2021-07-06    |



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
