import scrapy

class CatWorkout(scrapy.Spider):
    name = "CatWorkout"
    start_urls = ['https://www.muscleandstrength.com/workout-routines']
    def parse(self, response):
        with open('../../data/website3/categories.txt', 'w') as f:
            for category in response.css('div.cell'):
                category_name = category.css('div.category-name::text').get()
                if category_name:
                    f.write(category_name + '\n')
