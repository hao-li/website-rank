import requests
from bs4 import BeautifulSoup


def fetch_chinaz(page):
    target = 'https://top.chinaz.com/hangye/index_shenghuo_fangchang_br'
    if page > 1:
        target += '_' + str(page)

    target += '.html'

    res = requests.get(url=target)
    res.encoding = res.apparent_encoding
    bf = BeautifulSoup(res.text, 'html.parser')
    items = bf.select('ul.listCentent li')
    for item in items:
        item_bf = BeautifulSoup(str(item), 'html.parser')
        h3_bf = item_bf.find('h3')

        title = h3_bf.find('a').text
        domain = h3_bf.find('span').text

        rtc_datas = item_bf.find_all('p', class_='RtCData')

        ranks = ''
        for rtc_data in rtc_datas:
            rtc_data_bf = BeautifulSoup(str(rtc_data), 'html.parser')
            a_bf = rtc_data_bf.find('a')
            number = a_bf.text
            if number == '':
                img_bf = a_bf.find('img')
                src = str(img_bf.attrs['src'])
                suffix_removed_src = src.replace('.gif', '')
                segments = suffix_removed_src.split('/')
                last_segment = segments[len(segments) - 1]
                segment_parts = last_segment.split('_')
                number = segment_parts[len(segment_parts) - 1]

            ranks += ',' + number

        print(title + ',' + domain + ranks)
    return


for page in range(1, 44):
    fetch_chinaz(page)
