# lagouspider
Tron'blog
https://blog.tronsafe.cn/

获取职位信息spider

通过对拉钩网进行请求解析

并将请求获取的json文件存为Excel

从而完成对任意职位工资的分析

运行时输入你需要获取的工作名称和爬取页数即可自动保存到Excel文件

方便进行数据分析

说明：需要自己在spider.py 第24行添加自己的cookie，因为拉钩网没有登录账号会限制请求次数，其次因为爬取请求间隔时间过短会被限制，设置了停顿25-40秒随机，防止ip被禁

![image](http://ypy.tronsafe.cn/GitHub/Excel.png)

![image](http://ypy.tronsafe.cn/GitHub/lagouspider.png)
