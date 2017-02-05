#coding:utf-8
import urllib,re
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

def get_content(page):
    url = 'http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=000000%2C00&district=000000&funtype=0000&industrytype=00&issuedate=9&providesalary=99&keyword=python&keywordtype=2&curr_page=1&lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=0&confirmdate=9'.format(page)
    a = urllib.urlopen(url)
    html = a.read()
    html = html.decode('gbk') #解码GBK
    print html
    return html

def get(html):
    reg = re.compile(r'class="t1 ">.*?<a target="_blank" title="(.*?)".*?<span class="t2"><a target="_blank" title="(.*?).*?"<span class="t3">(.*?)</span>')

a = get_content(1)
