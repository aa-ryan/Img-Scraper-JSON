import requests, json
from bs4 import BeautifulSoup
from os import path


def image_write_text(search, inum):

    topic = search.replace(' ', '+')
    data  = dict()
    list_link = []

    if (path.exists('data.json')):
        f = open('data.json', 'r')
        data = json.load(f)


    x = 0
    page_number = 0

    while True:
        url = 'https://imgur.com/search/score/all/page/' + str(page_number) + '?scrolled&q=' + topic + '&q_size_is_mpx=off'

        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        images = soup.find_all('img')
        page_number = page_number + 1
        if images:

            for image in images:
                img_source = image['src']

                if img_source == '//s.imgur.com/images/loaders/ddddd1_181817/48.gif':
                    continue

                lst = list(img_source)
                lst[-5] = 'h'
                img_source = "".join(lst)
                link = 'https:' + img_source
                list_link.append(link)
                x = int(x) + 1

                if x == inum:
                    data[topic] = list_link
                    with open('data.json', 'w+') as f:
                        json.dump(data, f, indent=4)
                    # f = open('data.json', 'a+')
                    # data = json.load(f)
                    exit(0)

if __name__ == "__main__":
    image_write_text(input('Search: '), int(input('Number of Images: ')))
