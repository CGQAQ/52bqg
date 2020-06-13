#!/bin/env python3
# author: CGQAQ <m.jason.liu@outlook.com>

from requests import get
from pyquery import PyQuery as pq

from typing import TextIO

from codecs import open
import time

from argparse import ArgumentParser


def get_full_url(id: int) -> str:
    return f'https://www.52bqg.com/book_{id}/'


def fetch_main_page(id: int) -> str:
    url = get_full_url(id)
    c = get(url).content.decode('gbk')
    return c


def get_ep_list(content: str):
    # html body div.box_con div#list dl dd
    d = pq(content)
    d: pq = d('html body div.box_con div#list dl dd > a')
    print(d.size())

    ret = []
    d.each(lambda a, b: ret.append({'name': b.text, 'url': b.attrib['href']}))
    return ret


def get_fiction_content(id: int, page_uri: str) -> str:
    url = f'{get_full_url(id)}{page_uri}'
    page_content = get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}).content.decode(
        'gbk')
    d = pq(page_content)
    d = d('#content')
    d: str = d.text()
    return d.replace('\n', '')


def create_file(filename: str) -> TextIO:
    return open(filename, mode='w', encoding='utf-8')


if __name__ == '__main__':
    a = ArgumentParser(description='fiction downloader for 52bqg.com')
    a.add_argument('--id', default=0, type=int, dest='id')
    a.add_argument('filename', default='fiction.txt', nargs='?', metavar='filename', )
    args = a.parse_args()

    print(args.id)

    p = fetch_main_page(args.id)
    li = get_ep_list(p)

    file = create_file(args.filename)

    for i in li:
        print(i['name'], end='')
        print('\t下载中.', end='')
        file.write(i['name'])
        print('.', end='')
        file.write('\n')
        print('.', end='')
        # print(get_fiction_content(args.id, i['url']))
        file.write(get_fiction_content(args.id, i['url']))
        print('.', end='')

        # print('\n')
        file.write('\n')
        print('.', end='')
        file.write('\n')
        print('.', end='')

        print('成功！', end='\n')
        time.sleep(0.3)
