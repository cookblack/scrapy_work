import scrapy
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
import re
import urllib
import os


class XiaoHuarSpider(scrapy.spiders.Spider):
    name = "s1"
    allowed_domains = ["xiaohuar.com"]
    start_urls = [
        "http://www.xiaohuar.com/list-1-1.html",
    ]

    def parse(self, response):
        # 分析页面
        # 找到页面中符合规则的内容（校花图片），保存
        # 找到所有的a标签，再访问其他a标签，一层一层的搞下去

        hxs = HtmlXPathSelector(response)  # 创建查询对象
        ptint()
        # 如果url是 http://www.xiaohuar.com/list-1-\d+.html
        if re.match('http://www.xiaohuar.com/list-1-\d+.html', response.url):
            print(re)
            items = hxs.select('//div[@class="item_list infinite_scroll"]/div')  # //表示找到所有的div
            for i in range(len(items)):
                # 查询所有img标签的src属性，即获取校花图片地址
                srcs = hxs.select('//div[@class="item_list infinite_scroll"]'
                                  '/div[%d]//div[@class="img"]/a/img/@src' % i).extract()
                # 获取span的文本内容，即校花姓名
                names = hxs.select('//div[@class="item_list infinite_scroll"]'
                                   '/div[%d]//div[@class="img"]/span/text()' % i).extract()
                # 获取a的文本内容，即学校名
                schools = hxs.select('//div[@class="item_list infinite_scroll"]'
                                     '/div[%d]//div[@class="img"]/div[@class="btns"]/a/text()' % i).extract()
                if srcs and names and schools:  # 拿到第一个学校的校花图片和名字
                    print
                    names[0], schools[0], srcs[0]
                if srcs:
                    ab_src = "http://www.xiaohuar.com" + srcs[0]  # 拼接绝对路径；就是要爬的url的地址

                    # 文件名，以自己的名字命名；因为python27默认编码格式是unicode编码，因此我们需要编码成utf-8
                    file_name = "%s_%s.jpg" % (schools[0].encode('utf-8'), names[0].encode('utf-8'))
                    file_path = os.path.join("d:\\BeautifulPicture\\picture", file_name)  # 存放下载图片的路径；E:\\picture是我本地存放路径
                    urllib.urlretrieve(ab_src, file_path)
