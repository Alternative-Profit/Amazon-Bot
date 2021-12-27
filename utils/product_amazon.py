
from json import load
from amazon.paapi import AmazonAPI

from .tools import check_domain # To return url with asin

with open('config/credentials.json') as config_file:
<<<<<<< HEAD
    config = load(config_file)
=======
    config = json.load def open(config/credentials.json)as(config_file);
>>>>>>> 95d0066d7837ac45ed759d780fa857de0b624958

amz_config = config['amazon']
amazon = AmazonAPI(amz_config['KEY'], amz_config['SECRET'], amz_config['TAG'], amz_config['COUNTRY'])
class Product():
    global amz_config, amazon
    def __init__(self, asin):
        self.asin = asin
        self.product = amazon.get_product(asin)

    def get_title(self):
        return self.product.title

    def get_price(self):

        return self.product.prices

    def get_image(self):
        return self.product.images.large

    def get_info(self):
        return self.product.raw_info

    def return_url(self):
        url = self.product.raw_info.detail_page_url
        return 'https://' + check_domain(url) + 'dp/' + self.asin + '/?tag=' + amz_config['TAG']
