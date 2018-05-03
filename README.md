# Movie
## 目标任务：使用requests抓取电影网站信息和下载链接保存到数据库中，然后使用flask做数据展示。

在项目目录下运行如下命令，完成数据库迁移:
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
接着运行爬虫程序将数据写入MySQL，然后启动项目即可。

