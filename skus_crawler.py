import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import sys




def main():


    # url = 'https://www.zalando.es/collections/2NcExSbAQzi/?p='
    url=sys.argv[1] + '?p='
    print('URL:',url)
    path_to_csv=sys.argv[2]
    print('path_to_csv:',path_to_csv)

    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'

    response = requests.get(url, headers={'User-Agent': user_agent})
    soup = BeautifulSoup(response.text, 'html.parser')
    soup.find('script',attrs={"id":"z-nvg-cognac-props","type":"application/json"})
    textContent = []
    for i in range(0,1):
        paragraphs = soup.find_all('script',attrs={"id":"z-nvg-cognac-props","type":"application/json"})[i].text
        textContent.append(paragraphs)
        a=json.loads(textContent[0][9:-3])

    l=[]

    for i in a['articles']:
        data=dict()
        data['sku'] =i['sku']
        data['price'] =i['price']['promotional']
        data['brand_name'] =i['brand_name']
        data['url'] =url
        l.append(data)


    df=pd.DataFrame(l)


    if a['pagination']['page_count']>1:
        for page in range(2,a['pagination']['page_count']+1):

            next_url= url + str(page)
            print(next_url)
            user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'

            response = requests.get(next_url, headers={'User-Agent': user_agent})
            soup = BeautifulSoup(response.text, 'html.parser')
            soup.find('script',attrs={"id":"z-nvg-cognac-props","type":"application/json"})
            textContent = []
            for i in range(0,1):
                paragraphs = soup.find_all('script',attrs={"id":"z-nvg-cognac-props","type":"application/json"})[i].text
                textContent.append(paragraphs)
                a=json.loads(textContent[0][9:-3])


            l=[]

            for i in a['articles']:
                data=dict()
                data['sku'] =i['sku']
                data['price'] =i['price']['promotional']
                data['brand_name'] =i['brand_name']
                data['url'] =next_url
                l.append(data)

            df1=pd.DataFrame(l)

            df=df.append(df1, ignore_index = True)



    df.to_csv(path_to_csv,header=True)




if __name__ == '__main__':

    main()