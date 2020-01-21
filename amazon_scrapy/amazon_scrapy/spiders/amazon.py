# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonScrapyItem 

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 2
    start_urls = [
                'https://www.amazon.in/s?k=books&i=stripbooks&rh=n%3A976389031%2Cp_n_publication_date%3A2684819031&dc&qid=1566459747&rnid=2684818031&ref=sr_nr_p_n_publication_date_1'
                ]

    def parse(self, response):
        
        item = AmazonScrapyItem()
        
        product_name = response.css('.a-color-base.a-text-normal').css('::text').extract()
        product_author = response.css('span.a-size-base+ .a-size-base , .a-color-secondary .a-size-base.a-link-normal').css('::text').extract()
        product_price = response.css('.a-price-fraction , .a-spacing-top-small .a-price-whole').css('::text').extract()
        product_image = response.css('.s-image').css('::attr(src)').extract()
        
        item['product_name'] = product_name
        item['product_author'] = product_author
        item['product_price'] = product_price
        item['product_image'] = product_image
        
        yield item
        
        next_page = 'https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&page=' + str(AmazonSpider.page_number) + '&fst=as%3Aoff&qid=1566374570&rnid=1250225011&ref=sr_pg_2'
        
        if AmazonSpider.page_number <= 75:
            AmazonSpider.page_number += 1 
            yield response.follow(next_page, callback= self.parse)



