BOT_NAME = 'movie_top250'

SPIDER_MODULES = ['movie_top250.spiders']
NEWSPIDER_MODULE = 'movie_top250.spiders'

from faker import Factory
f = Factory.create()
USER_AGENT = f.user_agent()
ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
   'movie_top250.pipelines.MovieTop250Pipeline': 300,
}