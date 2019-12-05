import os
from urllib.parse import urlparse

from scrapy.pipelines.files import FilesPipeline

class MyFilesPipeline(FilesPipeline):

    def file_path(self, request, response, info):
        return 'files/' + os.path.basename(urlparse(request.url).path)

    def get_media_requests(self, item, info):
        for file_url in item['file_urls']:
            yield scrapy.Request(file_url)
