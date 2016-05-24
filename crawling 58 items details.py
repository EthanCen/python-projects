# -*- coding: utf-8 -*-

import requests,urllib
from bs4 import BeautifulSoup

# 抓取做了反爬虫，因此加上header信息，不然返回为空
headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

def get_links(url,headers=headers):
    web_data=requests.get(url,headers=headers)
    if web_data.status_code==200:  # 判断状态码，检查是否被网站封ip
        soup=BeautifulSoup(web_data.text,'lxml')   # 转utf-8编码
        href=soup.select('td.img > a')
        web_links=[]
        for links in href:
            web_links.append(links.get('href')) #list 没有get方法,list转成字符串才可以用get方法
            #print(len(web_links))
        return web_links      #返回所有详情页链接组成一个列表

def get_item_details(class_rent=0):
    url = 'http://bj.58.com/pbdn/{}/pn2/'.format(class_rent)   #判断是个人还是商家房源
    web_links=get_links(url)
    for link in web_links:
        get_link=requests.get(link,headers=headers)
        if get_link.status_code == 200:
            Soup = BeautifulSoup(get_link.text, 'lxml')
            titles=Soup.select('#content > div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.mainTitle > h1')
            prices=Soup.select('.price')
            zones=Soup.select('.c_25d')
            cate ='个人' if class_rent==0 else '商家'
            for title,price,zone,cate in zip(titles,prices,zones,cate):
                    data={
                          'title':title.get_text(),
                          'price':price.get_text(),
                          'zone':list(zone.stripped_strings),
                            'cate':cate }

                    with open('/Users/cenguangda/Desktop/example/download.txt', 'a') as f:
                        print(f.write(str(data)))

# 只有直接执行脚本才会运行下面的函数，如果其他文件引用这个文件，下面的函数不会执行
if __name__ == '__main__':
    get_item_details()









