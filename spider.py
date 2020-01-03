import requests
import time
import random
from openpyxl import Workbook
def get_want():#获取需要查询的信息
    position = input("输入你想获取的职位：")
    page = int(input("输入你想要抓取的页数(1-50)："))
    return position,page
def get_data(url,page,position):#获取拉勾网的数据
    header = {
        "Host": "www.lagou.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Anit-Forge-Token": "None",
        "X-Anit-Forge-Code": "0",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Length": "25",
        "Origin": "https://www.lagou.com",
        "Connection": "keep-alive",
        "Referer": "https://www.lagou.com/jobs/list_python/p-city_0?&cl=false&fromSearch=true&labelWords=&suginput="
    }
    post_data = {"first":"false","pn":page,"kd":position}#post的表单格式
    json = requests.post(url,post_data,headers=header).json()#requests的post请求获取json数据
    print(json)
    content_list = json['content']['positionResult']['result']#获取目标数据列表
    informations = []
    for content in content_list:#利用get方法获得每个职位信息
        information = []
        information.append(content.get("companyShortName","无"))
        information.append(content.get("companyFullName", "无"))
        information.append(content.get("industryField", "无"))
        information.append(content.get("companySize", "无"))
        information.append(content.get("city", "无"))
        information.append(content.get("district", "无"))
        information.append(content.get("education", "无"))
        information.append(content.get("salary", "无"))
        informations.append(information)
    return informations
def main():
    position,page = get_want()
    wb = Workbook()#打开excel工作簿
    ws1 = wb.active
    ws1.title = position
    url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
    for i in range(1,page+1):
        informations = get_data(url,i,position)
        time.sleep(random.randint(10, 20))
        for row in informations:
            ws1.append(row)
    wb.save('{}职位信息.xlsx'.format(position))
if __name__ == "__main__":
    main()