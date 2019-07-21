# -*- coding: utf-8 -*-
import scrapy
from ..items import RecipesItem


class RecipesSpider(scrapy.Spider):
    name = 'recipes'
    start_urls = ['https://www.allrecipes.com/recipes/233/world-cuisine/asian/indian/?page=1']

    def parse(self, response):

        item = RecipesItem()
        recipes_list = response.css('.fixed-recipe-card')

        for recipe in recipes_list:
            title = recipe.css('span.fixed-recipe-card__title-link::text').extract()
            url = recipe.css('.fixed-recipe-card__h3 a').xpath("@href").extract()
            item['title'] = title
            item['url'] = url
            yield item