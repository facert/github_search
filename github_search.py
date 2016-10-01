# coding: utf-8
import time
import json
import requests
from db import REDIS

REPO_SHOW = '1'
REPO_HIDDEN = '0'

SEARCH_API = 'https://api.github.com/search/repositories?q=%s&sort=updated&order=desc&page=%s'


def search_github(keyword):
    # 爬取 20 页最新的列表
    for i in range(1, 21):
        res = requests.get(SEARCH_API % (keyword, i))
        repo_list = res.json()['items']
        for repo in repo_list:
            repo_name = repo['html_url']
            desc = {
                'repo_desc': repo['description'],
                'star': repo['stargazers_count'],
                'is_show': REPO_SHOW
            }
            if REDIS.hsetnx('repos', repo_name, json.dumps(desc)):
                print repo_name
        time.sleep(10)


if __name__ == '__main__':
    keywords = ['爬虫', 'spider', 'crawl']
    REDIS.set('keywords', ' '.join(keywords))
    for keyword in keywords:
        search_github(keyword)
