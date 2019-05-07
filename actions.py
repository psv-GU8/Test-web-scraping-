import requests
from bs4 import BeautifulSoup

def get_ball_data():
    url="https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=football&_sacat=0"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')
    products = {}
    container = soup.find_all('li')
    slug = 0
    for li in container:
        temp = {}
        for h3 in li.find_all('h3', 's-item__title'):
            temp['title'] = h3.text
        for a in li.find_all('a','s-item__link'):
            temp['ref'] = a["href"]
        for img in li.find_all('img','s-item__image-img'):
            temp['img'] = img["src"]
        for price in li.find_all('span', 's-item__price'):
            temp['price'] =  price.text
        if temp:
            slug+=1
            products[slug] = temp
    return products


def get_band_data():
    url="https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=smart+bands&_sacat=0"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')
    products = {}
    container = soup.find_all('li')
    slug = 0
    for li in container:
        temp = {}
        for h3 in li.find_all('h3', 's-item__title'):
            temp['title'] = h3.text
        for a in li.find_all('a','s-item__link'):
            temp['ref'] = a["href"]
        for img in li.find_all('img','s-item__image-img'):
            temp['img'] = img["src"]
        for price in li.find_all('span', 's-item__price'):
            temp['price'] =  price.text
        if temp:
            slug+=1
            products[slug] = temp
    return products

def get_cap_data():
    url="https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=caps&_sacat=0"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')
    products = {}
    container = soup.find_all('li')
    slug = 0
    for li in container:
        temp = {}
        for h3 in li.find_all('h3', 's-item__title'):
            temp['title'] = h3.text
        for a in li.find_all('a','s-item__link'):
            temp['ref'] = a["href"]
        for img in li.find_all('img','s-item__image-img'):
            temp['img'] = img["src"]
        for price in li.find_all('span', 's-item__price'):
            temp['price'] =  price.text
        if temp:
            slug+=1
            products[slug] = temp
    return products

def get_memory_data():
    url="https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=memory+card&_sacat=0"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')
    products = {}
    container = soup.find_all('li')
    slug = 0
    for li in container:
        temp = {}
        for h3 in li.find_all('h3', 's-item__title'):
            temp['title'] = h3.text
        for a in li.find_all('a','s-item__link'):
            temp['ref'] = a["href"]
        for img in li.find_all('img','s-item__image-img'):
            temp['img'] = img["src"]
        for price in li.find_all('span', 's-item__price'):
            temp['price'] =  price.text
        if temp:
            slug+=1
            products[slug] = temp
    return products

def get_mobile_data():
    url="https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=mobiles&_sacat=0"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')
    products = {}
    container = soup.find_all('li')
    slug = 0
    for li in container:
        temp = {}
        for h3 in li.find_all('h3', 's-item__title'):
            temp['title'] = h3.text
        for a in li.find_all('a','s-item__link'):
            temp['ref'] = a["href"]
        for img in li.find_all('img','s-item__image-img'):
            temp['img'] = img["src"]
        for price in li.find_all('span', 's-item__price'):
            temp['price'] =  price.text
        if temp:
            slug+=1
            products[slug] = temp
    return products

def get_mouse_data():
    url="https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=mouse&_sacat=0"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')
    products = {}
    container = soup.find_all('li')
    slug = 0
    for li in container:
        temp = {}
        for h3 in li.find_all('h3', 's-item__title'):
            temp['title'] = h3.text
        for a in li.find_all('a','s-item__link'):
            temp['ref'] = a["href"]
        for img in li.find_all('img','s-item__image-img'):
            temp['img'] = img["src"]
        for price in li.find_all('span', 's-item__price'):
            temp['price'] =  price.text
        if temp:
            slug+=1
            products[slug] = temp
    return products

def get_pant_data():
    url="https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=pants&_sacat=0"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')
    products = {}
    container = soup.find_all('li')
    slug = 0
    for li in container:
        temp = {}
        for h3 in li.find_all('h3', 's-item__title'):
            temp['title'] = h3.text
        for a in li.find_all('a','s-item__link'):
            temp['ref'] = a["href"]
        for img in li.find_all('img','s-item__image-img'):
            temp['img'] = img["src"]
        for price in li.find_all('span', 's-item__price'):
            temp['price'] =  price.text
        if temp:
            slug+=1
            products[slug] = temp
    return products

def get_saree_data():
    url="https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=sarees&_sacat=0"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')
    products = {}
    container = soup.find_all('li')
    slug = 0
    for li in container:
        temp = {}
        for h3 in li.find_all('h3', 's-item__title'):
            temp['title'] = h3.text
        for a in li.find_all('a','s-item__link'):
            temp['ref'] = a["href"]
        for img in li.find_all('img','s-item__image-img'):
            temp['img'] = img["src"]
        for price in li.find_all('span', 's-item__price'):
            temp['price'] =  price.text
        if temp:
            slug+=1
            products[slug] = temp
    return products

def get_y_data():
    response="What type of shirts are you looking for? Please specify the color or the size of the shirts..."
    return response
def get_ebay_data(color):
    url="https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=shirt+"
    url1=url+color
    response = requests.get(url1)
    soup = BeautifulSoup(response.text,'lxml')
    products = {}
    container = soup.find_all('li')
    slug = 0
    for li in container:
        temp = {}
        for h3 in li.find_all('h3', 's-item__title'):
            temp['title'] = h3.text
        for a in li.find_all('a','s-item__link'):
            temp['ref'] = a["href"]
        for img in li.find_all('img','s-item__image-img'):
            temp['img'] = img["src"]
        for price in li.find_all('span', 's-item__price'):
            temp['price'] =  price.text
        if temp:
            slug+=1
            products[slug] = temp
    return products

def get_shoe_data():
    url="https://www.ebay.com/sch/i.html?_from=R40&_nkw=shoes"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')
    products = {}
    container = soup.find_all('li')
    slug = 0
    for li in container:
        temp = {}
        for h3 in li.find_all('h3', 's-item__title'):
            temp['title'] = h3.text
        for a in li.find_all('a','s-item__link'):
            temp['ref'] = a["href"]
        for img in li.find_all('img','s-item__image-img'):
            temp['img'] = img["src"]
        for price in li.find_all('span', 's-item__price'):
            temp['price'] =  price.text
        if temp:
            slug+=1
            products[slug] = temp
    return products

def get_size_data(size):
    url="https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=shirt+"
    url1=url+size
    response = requests.get(url1)
    soup = BeautifulSoup(response.text,'lxml')
    products = {}
    container = soup.find_all('li')
    slug = 0
    for li in container:
        temp = {}
        for h3 in li.find_all('h3', 's-item__title'):
            temp['title'] = h3.text
        for a in li.find_all('a','s-item__link'):
            temp['ref'] = a["href"]
        for img in li.find_all('img','s-item__image-img'):
            temp['img'] = img["src"]
        for price in li.find_all('span', 's-item__price'):
            temp['price'] =  price.text
        if temp:
            slug+=1
            products[slug] = temp
    return products


def get_speaker_data():
    url="https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=speakers&_sacat=0"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')
    products = {}
    container = soup.find_all('li')
    slug = 0
    for li in container:
        temp = {}
        for h3 in li.find_all('h3', 's-item__title'):
            temp['title'] = h3.text
        for a in li.find_all('a','s-item__link'):
            temp['ref'] = a["href"]
        for img in li.find_all('img','s-item__image-img'):
            temp['img'] = img["src"]
        for price in li.find_all('span', 's-item__price'):
            temp['price'] =  price.text
        if temp:
            slug+=1
            products[slug] = temp
    return products

def get_sunglass_data():
    url="https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=sunglasses&_sacat=0"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')
    products = {}
    container = soup.find_all('li')
    slug = 0
    for li in container:
        temp = {}
        for h3 in li.find_all('h3', 's-item__title'):
            temp['title'] = h3.text
        for a in li.find_all('a','s-item__link'):
            temp['ref'] = a["href"]
        for img in li.find_all('img','s-item__image-img'):
            temp['img'] = img["src"]
        for price in li.find_all('span', 's-item__price'):
            temp['price'] =  price.text
        if temp:
            slug+=1
            products[slug] = temp
    return products

