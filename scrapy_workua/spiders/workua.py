import scrapy
from scrapy import Request

class WorkuaSpider(scrapy.Spider):
    name = 'workua'
    allowed_domains = ['work.ua']
    start_urls = ['https://www.work.ua/ru/resumes-odesa/']

    site_url = 'https://work.ua'

    def parse(self, response):

        for person in response.css('div.card.resume-link'):
            name = person.css('div > b::text').get()
            age = person.css('div > span:nth-child(3)::text').get()
            salary = person.css('div > h2 > span:nth-child(2)::text').get()

         #  print(name, age, cost, )

            yield {
                'name': name,
                'age' : age,
                'salary': salary,
            }

        next_url = response.css('ul.pagination-small li a::attr(href)').getall()
        #print(next_url)
        if next_url:
            next_page_url = self.site_url + next_url[-1]
            yield Request(next_page_url)








