# Crawling voice line from https://theportalwiki.com/wiki/GLaDOS_voice_lines

import scrapy
import re
import csv


def normalize_file_name(file_name_ext):
    ext = file_name_ext.split(".")[-1]
    file_name = re.sub('[^0-9a-zA-Z]+', '_', "_".join(
        file_name_ext.split(".")[:-1]))
    return file_name, "{}.{}".format(file_name, ext)


def write_to_csv(prompts, name, prompt):
    prompts.write("{}\t{}\n".format(name, prompt))


kFOLDER = "portal"


class PortalSpider(scrapy.Spider):
    name = "portal spider"
    start_urls = ['https://theportalwiki.com/wiki/GLaDOS_voice_lines']

    def parse(self, response):
        with open('prompts.csv', mode='w') as prompts:
            for content in response.css('div.mw-content-ltr'):
                for ul in content.xpath('ul'):
                    for li in ul.xpath('li'):
                        file_name_ext = li.xpath('span[1]/a/@title').get()
                        if (file_name_ext != None):
                            name, file_name_ext = normalize_file_name(
                                file_name_ext)
                            text = li.xpath('i/text()').get()
                            write_to_csv(prompts, name, text)
                            yield {
                                'text': text,
                                'file_urls':
                                [li.xpath('span[1]/a/@href').get()],
                                'name': file_name_ext,
                                'folder': kFOLDER
                            }

                        file_name_ext = li.xpath('a/@title').get()
                        if (file_name_ext != None):
                            name, file_name_ext = normalize_file_name(
                                file_name_ext)
                            text = li.xpath('a/text()').get()
                            write_to_csv(prompts, name, text)
                            yield {
                                'text': text,
                                'file_urls': [li.xpath('a/@href').get()],
                                'name': file_name_ext,
                                'folder': kFOLDER
                            }
