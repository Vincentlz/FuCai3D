# -*- coding: utf-8 -*-
''' ---------------------------------------
   程序：Lottery3D.py
   版本：Vincent © 1.0
   作者：vincentlz
   日期：2017/9/8 10:58
   环境：Python 3.6 PyCharm
   简介：
  ---------------------------------------
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛'''
                  
import urllib.request
import re
import xlwt

#定义一个函数，获取开奖页面html源码
def get_3d_html():
    #生成页码列表，这里显示的是前12页的源码
    page_num=range(1,14)
    b=''
    #循环获取
    for page in page_num:
        #通过分析链接页码拼接
        url='http://kaijiang.zhcw.com/zhcw/html/3d/list_'+str(page_num[page-1])+'.html'
        #打开链接
        a=urllib.request.urlopen(url)
        #读取
        html=a.read()
        #转码
        html=html.decode('utf-8')
        b=b+html
    return b
# print(get_3d_html())
#构建正则提取需要的数据
def get_3d_num():
    html=get_3d_html()
    reg=re.compile(r'<tr>.*?<td align="center">'
                   r'(.*?)</td>.*?<td align="center">'
                   r'(.*?)</td>.*?<td align="center" '
                   r'style="padding-left:20px;">'
                   r'<em>(.*?)</em>.*?<em>(.*?)</em>.*?<em>(.*?)</em></td>',re.S)
    it=re.findall(reg,html)
    return it
# print(get_3d_num())
#定义excel函数，参数为get_3d_num()获取到的数据
def excel_create(ceshi):
    newTable='fucai_3d.xls'
    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('test1')
    headData=['开奖日期','期号','百位','十位','个位']
    for col in range(0,5):
        ws.write(0,col,headData[col])

    index=1
    for j in ceshi:
        for i in range(0,5):
            # print(j[i])
            ws.write(index,i,j[i])
        index +=1

        wb.save(newTable)

if __name__=='__main__':
    w=get_3d_num()
    excel_create(w)

#最频繁出现概率最高的数字
def analyze_popu_nums(w):
    import collections
    all_nums=[]
    bw_nums=[]
    sw_nums=[]
    gw_nums=[]
    for each in w:
        for n in each[-3:]:
            all_nums.append(n)
        bw_nums.append(each[2])
        sw_nums.append(each[3])
        gw_nums.append(each[4])

    print('全年最火的三个数：',collections.Counter(all_nums).most_common(3))
    print('百位最火的三个数：',collections.Counter(bw_nums).most_common(3))
    print('十位最火的三个数：',collections.Counter(sw_nums).most_common(3))
    print('个位最火的三个数：',collections.Counter(gw_nums).most_common(3))
    print('-----------------------------------------------------------------')

#分析每期重复出现的数字概率，这个没理解清楚
def duplicat_num(w):
    dup_count=0
    for each in w:
        if len(set(each[-3:]))<3:
            dup_count += 1
    print(dup_count)
    dup_percet=round(dup_count/len(w),4)
    print('duplicate num percent:{}%'.format(float(dup_percet)*100))

#最后记得要调用函数，不然没有分析数据
analyze_popu_nums(w)
duplicat_num(w)