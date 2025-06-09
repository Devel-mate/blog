from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all() # Django will call get_absolute_url() on each item
    
    def lastmod(self, obj):
        return obj.updated