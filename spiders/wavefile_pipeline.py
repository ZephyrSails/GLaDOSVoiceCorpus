import os
import scrapy
from urllib.parse import urlparse

from scrapy.pipelines.files import FilesPipeline


class WaveFilesPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        return "full/%s" % (request.meta.get('name'))

    def get_media_requests(self, item, info):
        file_url = item['file_urls'][0]
        meta = {'name': item['name']}
        yield scrapy.Request(url=file_url, meta=meta)
