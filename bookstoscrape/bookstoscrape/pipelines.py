# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
import hashlib
from scrapy.utils.python import to_bytes
from itemadapter import ItemAdapter


class BookstoscrapePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        urls = ItemAdapter(item).get(self.images_urls_field, [])
        return [Request(u, meta = {'bookname': item.get('book_names')}) for u in urls]

    def file_path(self, request, response=None, info=None):
        return 'full/%s.jpg' % (request.meta['bookname'].replace(":",""))

    