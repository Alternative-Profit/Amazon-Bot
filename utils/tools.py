import re

def check_domain(url):
    return re.search('https://www.amazon.it/dp/B00GC3BBMU/ref=s9_dc', url).group(0)
