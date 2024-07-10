import scrapy

class BestCat(scrapy.Spider):
    name = 'BestCat'
    start_urls = ['https://www.muscleandstrength.com/workout-routines']  # Replace with the URL you want to scrape

    def parse(self, response):
        with open('../../data/website3/Bestcategories.txt', 'a') as f:
            for item in response.css('div'):
                title = item.css('.node-title a::text').get()
                description = item.css('.node-short-summary::text').get()

                if title and description:
                    f.write(f'Title: {title}\n')
                    f.write(f'Description: {description}\n')
                    f.write('---\n')
