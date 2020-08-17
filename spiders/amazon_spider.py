import scrapy 

class PhoneSpider(scrapy.Spider):
    name='amazon'
    start_urls=['https://www.amazon.in/s?k=phones&i=electronics&rh=n%3A1805560031%2Cp_n_operating_system_browse-bin%3A1485077031&dc&qid=1597564839&rnid=1485076031&ref=sr_nr_p_n_operating_system_browse-bin_1']
    page_number = 2
    def parse(self , response):
        #all_div = response.css('.sg-col-24-of-28 .sg-col-inner')
        name = response.css('.a-color-base.a-text-normal::text').extract()
        price = response.css('.a-price-whole::text').extract()
        discount = response.css('.a-letter-space+ span::text').extract()
        rating = response.css('.aok-align-bottom span.a-icon-alt::text').extract()
        image = response.css('.s-image::attr(src)').extract()
        for (name,price,discount,rating,image) in zip(name,price,discount,rating,image):
            yield{'Name':name,'Price':price,'Discount':discount,'Rating':rating,'ImageLink':image}

        next_page = 'https://www.amazon.in/s?k=phones&i=electronics&rh=n%3A1805560031%2Cp_n_operating_system_browse-bin%3A1485077031&dc&page='+str(PhoneSpider.page_number)+'&qid=1597651281&rnid=1485076031&ref=sr_pg_2'
        if PhoneSpider.page_number <=5:
           PhoneSpider.page_number+=1
           yield response.follow(next_page,callback = self.parse)     
            