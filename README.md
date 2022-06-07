# RentalScraper
A scrapy web-crawler to crawl rental sites.
Currently contains a spider for zoopla and onthemarket.
To change the scope of properties you're searching for edit the start_url of the respective spider.

This scraper can be deployed using scrapyd
The steps to do this are as follows:
- Installing scrapyd and scrapyd-client:
    pip install scrapyd
    pip install git+https://github.com/scrapy/scrapyd-client.git
- Start the scrapyd daemon:
    scrapyd
- Start the scrapy project on the daemon
    scrapyd-deploy default
