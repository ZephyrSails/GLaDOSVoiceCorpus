# Crawling voice line from https://theportalwiki.com/wiki/GLaDOS_voice_lines

import scrapy


class PortalSpider(scrapy.Spider):
    name = "portal spider"
    start_urls = ['https://theportalwiki.com/wiki/GLaDOS_voice_lines']

    def parse(self, response):
        for content in response.css('div.mw-content-ltr'):
            for ul in content.xpath('ul'):
                for li in ul.xpath('li'):
                    yield {
                        'text': li.xpath('i/text()').get(),
                        'url': li.xpath('span[1]/a/@href').get(),
                        'name': li.xpath('span[1]/a/@title').get(),
                    }
