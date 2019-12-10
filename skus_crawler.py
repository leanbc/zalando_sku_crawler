import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import configparser
import logging




def main():

    logging.basicConfig(level=logging.INFO)


    config = configparser.ConfigParser()
    config.read('config.ini')
    url=config.get('URL', 'url')
    path=config.get('PATH', 'path')

    logging.info('We will get data from :' + url)  # will print a message to the console



    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    response = requests.get(url, headers={'User-Agent': user_agent})
    soup = BeautifulSoup(response.text, 'html.parser')
    textContent = []
    paragraphs = soup.find_all('script',attrs={"id":"z-nvg-cognac-props","type":"application/json"})[0].text
    textContent.append(paragraphs)
    b=json.loads(textContent[0][9:-3])
    df=pd.DataFrame()


    for page in range(1,b['pagination']['page_count']+1):

        new_url=url+'?p=' + str(page)
        logging.info('paginatition : ' + new_url)
        l=[]

        for i in b['articles']:
            data=dict()
            data['sku'] =i['sku']
            data['price'] =i['price']['promotional']
            data['brand_name'] =i['brand_name']
            data['url'] =new_url
            l.append(data)

        df=df.append(pd.DataFrame(l), ignore_index = True)


    df.to_csv(path,header=True)

    logging.info('FINISH!!!!-- The file is in:' + str(path))
    logging.info('Number of Skus:' + str(df.brand_name.count()))

if __name__ == '__main__':
    main()
