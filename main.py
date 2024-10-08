import gevent.monkey
gevent.monkey.patch_all(thread=False)

import logging

from crawler import Crawler
from crawler.config import default_config

import os, sys

if __name__ == '__main__':
    config = {
        ## 目标网站主页
        'main_url': sys.argv[1],
        ## 抓取深度, 从当前页面算起, 1表示只抓当前页, 0表示无限制
        'max_depth': sys.argv[2],
        'headers': {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
        },
        'logging_config': {
            'level': logging.DEBUG,
            ## %(name)s表示模块路径(其实是__name__的值)
            'format': '%(asctime)s %(levelname)-7s %(name)s - %(filename)s:%(lineno)d %(message)s',
        }
    }
    config = dict(default_config, **config)

    logging.basicConfig(**config['logging_config'])
    ## logger.setLevel(logging.DEBUG)
    try:
        c = Crawler(config)
        c.start()
    except KeyboardInterrupt:
        c.stop()
