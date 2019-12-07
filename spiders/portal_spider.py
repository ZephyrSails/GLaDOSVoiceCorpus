# Crawling voice line from https://theportalwiki.com/wiki/GLaDOS_voice_lines

import scrapy
import re


def normalize_file_name(file_name_ext):
    ext = file_name_ext.split(".")[-1]
    file_name = re.sub('[^0-9a-zA-Z]+', '_', "_".join(
        file_name_ext.split(".")[:-1]))
    return "{}.{}".format(file_name, ext)


class PortalSpider(scrapy.Spider):
    name = "portal spider"
    start_urls = ['https://theportalwiki.com/wiki/GLaDOS_voice_lines']

    def parse(self, response):
        for content in response.css('div.mw-content-ltr'):
            for ul in content.xpath('ul'):
                for li in ul.xpath('li'):
                    file_name_ext = li.xpath('span[1]/a/@title').get()
                    if (file_name_ext != None):
                        yield {
                            'text': li.xpath('i/text()').get(),
                            'file_urls': [li.xpath('span[1]/a/@href').get()],
                            'name': normalize_file_name(file_name_ext),
                            'folder': 'portal'
                        }
                    file_name_ext = li.xpath('a/@title').get()
                    if (file_name_ext != None):
                        yield {
                            'text': li.xpath('a/text()').get(),
                            'file_urls': [li.xpath('a/@href').get()],
                            'name': normalize_file_name(file_name_ext),
                            'folder': 'portal'
                        }
