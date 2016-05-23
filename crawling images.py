import  requests,urllib.request,time
from bs4 import BeautifulSoup
# 仿真实用户的请求,路径:chrom>>检查>>network)
headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2',
    'Cache-Control':'max-age=0',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
url='http://jandan.net/pic/page-93'

# 此网站会有针对 ip 的反爬取，可以采用代理的方式
proxies = {"http": "http://121.69.29.162:8118"}

def get_imgs(url,data=None,proxies=None):
    web_data=requests.get(url,headers=headers,proxies=proxies)
    if web_data.status_code!=200:
        return

    Soup=BeautifulSoup(web_data.text,'lxml')

    download_link=[]   #创建一个列表以遍历
    folder_path='/Users/cenguangda/Desktop/example/'

    for pick_tag in Soup.find_all('img'):   #通过标签查找所有img标签的数据
        pick_link=pick_tag.get('src')       #返回link.
        download_link.append(pick_link)

    for item in download_link:
        urllib.request.urlretrieve(item,folder_path+item[-10:])  #下载图片函数参数为:链接,文件夹+文件名(取自链接-10位后)
        print('done')

def get_page(start,end):
    for one in range(start,end):
        get_imgs(url+str(one))
        time.sleep(0.5)    # 间隔时间,应对网站反爬取

get_page(30,40)
