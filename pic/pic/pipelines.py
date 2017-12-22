import urllib.request
import os


class PicPipeline(object):
    def process_item(self, item, spider):

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'}
        print(item['addr'])
        req = urllib.request.Request(url=item['addr'], headers=headers)
        #print(req)
        res = urllib.request.urlopen(req)
        #print(res.read())
        file_name = os.path.join(r'D:\BeautifulPicture\xh', item['name'] + '.jpg')
        print(file_name)
        with open(file_name, 'wb') as fp:
            fp.write(res.read())