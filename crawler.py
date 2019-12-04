import argparse
from scrapy.crawler import CrawlerProcess

parser = argparse.ArgumentParser()
parser.add_argument(
    '--corpus', type=str, help='valid options: [portal, portal2]')


def crawl(spider):
    process = CrawlerProcess(
        {'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'})

    process.crawl(spider)
    process.start()


if __name__ == "__main__":
    args = parser.parse_args()

    if args.corpus == "portal":
        from spiders.portal_spider import PortalSpider
        crawl(PortalSpider)
    elif args.corpus == "portal2":
        from spiders.portal2_spider import Portal2Spider
        crawl(Portal2Spider)
    elif args.corpus == "example":
        from spiders.example_spider import ExampleSpider
        crawl(ExampleSpider)
