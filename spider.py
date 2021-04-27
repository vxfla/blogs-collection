import requests
from lxml import etree

data = {}

def get():
    resp = requests.get('https://www.cnblogs.com/')
    selector = etree.HTML(resp.text)

    data['title'] = selector.xpath('//*[@id="post_list"]/article/section/div[1]/a[1]/text()')
    data['link'] = selector.xpath('//*[@id="post_list"]/article/section/div[1]/a[1]/@href')
    data['writer'] = selector.xpath('//*[@id="post_list"]/article/section/footer/a[1]/span/text()')
    return data

# 写入csv
# time = [pd.datetime.now()]
# dataframe = pd.DataFrame.from_dict(data)
# dataframe_t = pd.DataFrame(time,index = ['更新时间'])
# dataframe_t.to_csv("unblogs.csv",mode = 'a' ,index=True,header=False,sep=',',encoding = "gb2312")
# dataframe.to_csv("unblogs.csv",mode = 'a' ,index=False,sep=',',encoding = "gb2312")

# 写入txt
def to_txt():
    fileObject = open('cnblogs.txt','w')
    for i in range(len(data['title'])):
        fileObject.write(data['title'][i])
        fileObject.write('\t')
        # fileObject.write(data['link'][i])
        # fileObject.write('\t')
        # fileObject.write(data['writer'][i])
        # fileObject.write('\n')
    fileObject.close()

# # 写入xlsx
# fileObject = open('cnblogs.xlsx','a')
# fileObject.write('更新时间： ')
# fileObject.write(str(pd.datetime.now()))
# for i in range(len(data['title'])):
#     fileObject.write(data['title'][i])
#     fileObject.write('\t')
#     fileObject.write(data['link'][i])
#     fileObject.write('\t')
#     fileObject.write(data['writer'][i])
#     fileObject.write('\t')
#     fileObject.write(data['like'][i])
#     fileObject.write('\n')
# fileObject.close()

get()
to_txt()