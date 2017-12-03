# scrapy_mysql
爬取豆瓣电影top250，并保存到mysql
使用pycharm的朋友 
scrapy_mysql/
    .idea/
    movie_top250/
        movie_top250/
            ...
在第一个 movie_top250 右键mark dirctory as sources root, 否则pycharm下导包会找不到路径。但不影响使用
进入scrapy_mysql/movie_top250 后 scrapy  crawl  douban_movie 即可
