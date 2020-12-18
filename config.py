configs = [
    {
        "platform_name": "cakeresume",
        "platform_url": "https://www.cakeresume.com/jobs?q={}&page={}",
        "jobs_list_element": 'soup.findAll("div", class_="job")',
        "job_link_element": 'job.find("a", "job-link").get("href")',
        "job_name_element": 'job.find("a", "job-link").text',
        "job_description_element": 'job.find("p", "job-desc").text',
        "job_update_time_element": 'job.find("span", "update-section").text',
        "company_name_element": 'job.find("h5", "page-name").find("a").text',
        "company_link_element": 'job.find("h5", "page-name").find("a").get("href")',
    }
]
