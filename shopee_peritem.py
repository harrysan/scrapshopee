# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 20:43:21 2019

@author: Harry
"""

import requests
from random import randint
#import csv

class Shopi:
    sellername = ""
    sellerid = ""
    productid = []
    images = []
    variasi = []
    path = ""
    itemid = ""
    keyword = ""
    harga = 0
    stok = 0
    catid = []
    itemid = []
    data = []
    
    def __init__(self, USERNAME):
        sellername = USERNAME
        print('Initalitation..')
        #1 GET USER ID
        print('Getting User ID..')
        self.sellerid = self.getSellerId(sellername)
        print('User ID = '+str(self.sellerid))
        if self.sellerid == False:
            print('User ID not found, try again..')
            return
        #2 GET ITEM ID
        print('Getting Search by Name..')
        self.keyword = input('Paste product name here: ')
        self.getResult(self.keyword)
        
        print('Complete..')
        
    def getSellerId(self,sellername):
        REQ = requests.Session()
        HEADERS = {
            "accept-encoding": "gzip, deflate, br",
            "content-type": "application/json",
            "if-none-match": "55b03-1ae7d4aa7c47753a96c0ade3a9ea8b35",
            "origin": "https://shopee.co.id",
            "referer": "https://shopee.co.id/asusofficialshop",
            "x-api-source": "pc",
            "x-csrftoken": "8XtQ7bHlv09rlx5U4NPN6rmavFn7MvTO",
            "x-requested-with": "XMLHttpRequest",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
            "cookie": 'SPC_IA=-1; SPC_EC=-; SPC_F=QpolQhTSikpnxRXO6T4RjIW8ZGHNBmBn; REC_T_ID=ac80cdde-0e7d-11e9-a8c2-3c15fb3af585; SPC_T_ID="e4t1VmH0VKB0NajA1BrHaDQlFRwWjTZT7o83rrHW+p16sTf1NJK7ksWWDicCTPq8CVO/S8sxnw25gNR0DLQz3cv7U3EQle9Z9ereUnPityQ="; SPC_SI=k2en4gw50emawx5fjaawd3fnb5o5gu0w; SPC_U=-; SPC_T_IV="in3vKQSBLhXzeTaGwMInvg=="; _gcl_au=1.1.557205539.1546426854; csrftoken=8XtQ7bHlv09rlx5U4NPN6rmavFn7MvTO; welcomePkgShown=true; bannerShown=true; _ga=GA1.3.472488305.1546426857; _gid=GA1.3.1348013297.1546426857; _fbp=fb.2.1546436170115.11466858'
        }
        URL = "https://shopee.co.id/api/v1/shop_ids_by_username/"
        DATA = {"usernames": [sellername]}
        GET_DATA = REQ.post(URL, headers=HEADERS, json=DATA)
        #RESULT = GET_DATA.json()
        res = GET_DATA.json()
        #USERID = RESULT[0][sellername]
        USERID = res[0][sellername]

        return USERID
    
    def getResult(self,keyword) :
        headers = {
            "accept-encoding": "gzip, deflate, br",
            "content-type": "application/json",
            "if-none-match": "55b03-1ae7d4aa7c47753a96c0ade3a9ea8b35",
            "origin": "https://shopee.co.id",
            "referer": "https://shopee.co.id/asusofficialshop",
            "x-api-source": "pc",
            "x-csrftoken": "8XtQ7bHlv09rlx5U4NPN6rmavFn7MvTO",
            "x-requested-with": "XMLHttpRequest",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
            "cookie": 'SPC_IA=-1; SPC_EC=-; SPC_F=QpolQhTSikpnxRXO6T4RjIW8ZGHNBmBn; REC_T_ID=ac80cdde-0e7d-11e9-a8c2-3c15fb3af585; SPC_T_ID="e4t1VmH0VKB0NajA1BrHaDQlFRwWjTZT7o83rrHW+p16sTf1NJK7ksWWDicCTPq8CVO/S8sxnw25gNR0DLQz3cv7U3EQle9Z9ereUnPityQ="; SPC_SI=k2en4gw50emawx5fjaawd3fnb5o5gu0w; SPC_U=-; SPC_T_IV="in3vKQSBLhXzeTaGwMInvg=="; _gcl_au=1.1.557205539.1546426854; csrftoken=8XtQ7bHlv09rlx5U4NPN6rmavFn7MvTO; welcomePkgShown=true; bannerShown=true; _ga=GA1.3.472488305.1546426857; _gid=GA1.3.1348013297.1546426857; _fbp=fb.2.1546436170115.11466858'
        }
        url = "https://shopee.co.id/api/v2/search_items/?by=relevancy&keyword={}&limit=100&order=desc&page_type=search".format(self.keyword)
        rest = requests.get(url, headers = headers)
        rest = rest.json()
        """rest = rest.text
        doc = pyquery.PyQuery(rest)
        items = doc('script[type="text/javascript"]').items()
        
        for item in items:
            js_data = json.loads(item.text()[21:-1], encoding='utf-8')
            print(js_data['items'])"""
        print(self.sellerid)
        
        for val in range(0,len(rest['items'])):
            if rest['items'][val]['shopid'] == self.sellerid: # and val['name'] == keyword:
                #kalau satu toko ada produk yang sama (lebih dari 1)
                print(rest['items'][val])
                print('--------------')
                print('Nama = '+rest['items'][val]['name'])
                print('Harga sebelum disc = '+str(rest['items'][val]['price_before_discount'])[:-5])
                print('Harga sesudah disc = '+str(rest['items'][val]['price'])[:-5])
                print('Brand = '+rest['items'][val]['brand'])
                print('Stock = '+str(rest['items'][val]['stock']))
                print('Lokasi = '+rest['items'][val]['shop_location'])
                #gambar
                for img in range(0,len(rest['items'][val]['images'])):
                    print('Gambar ke '+str(img)+' '+'https://cf.shopee.co.id/file/'+rest['items'][val]['images'][img])
                    self.images.append('https://cf.shopee.co.id/file/'+rest['items'][val]['images'][img])
                    
                #variasi
                for varss in range(0,len(rest['items'][val]['tier_variations'])):
                    for var in range(0,len(rest['items'][val]['tier_variations'][varss]['options'])):
                        print('Variasi ke '+str(var)+' '+rest['items'][val]['tier_variations'][varss]['options'][var])
                        self.variasi.append(rest['items'][val]['tier_variations'][varss]['options'][var])
                    
                self.getProductInfo(rest['items'][val]['itemid'])
                self.create_random_sleep(5,10)
                
    def create_random_sleep(self,min_time,max_time):
        
        time_sleep = randint(min_time, max_time)
        print("Wait "+str(time_sleep)+" sec for next search . . .")
        
        return time_sleep
                
    def getProductInfo(self,productid) :
        headers = {
            "accept-encoding": "gzip, deflate, br",
            "content-type": "application/json",
            "if-none-match": "55b03-1ae7d4aa7c47753a96c0ade3a9ea8b35",
            "origin": "https://shopee.co.id",
            "referer": "https://shopee.co.id/asusofficialshop",
            "x-api-source": "pc",
            "x-csrftoken": "8XtQ7bHlv09rlx5U4NPN6rmavFn7MvTO",
            "x-requested-with": "XMLHttpRequest",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
            "cookie": 'SPC_IA=-1; SPC_EC=-; SPC_F=QpolQhTSikpnxRXO6T4RjIW8ZGHNBmBn; REC_T_ID=ac80cdde-0e7d-11e9-a8c2-3c15fb3af585; SPC_T_ID="e4t1VmH0VKB0NajA1BrHaDQlFRwWjTZT7o83rrHW+p16sTf1NJK7ksWWDicCTPq8CVO/S8sxnw25gNR0DLQz3cv7U3EQle9Z9ereUnPityQ="; SPC_SI=k2en4gw50emawx5fjaawd3fnb5o5gu0w; SPC_U=-; SPC_T_IV="in3vKQSBLhXzeTaGwMInvg=="; _gcl_au=1.1.557205539.1546426854; csrftoken=8XtQ7bHlv09rlx5U4NPN6rmavFn7MvTO; welcomePkgShown=true; bannerShown=true; _ga=GA1.3.472488305.1546426857; _gid=GA1.3.1348013297.1546426857; _fbp=fb.2.1546436170115.11466858'
        }
        #get Detail Info Product
        page = "https://shopee.co.id/api/v1/item_detail/?item_id={}&shop_id={}".format(productid, self.sellerid)
        req = requests.get(page, headers=headers) #, verify=False)
        data = req.json()
        print('Description = ')
        print(data['description'])
        
    
URL = input('Paste the username here: ')
Shopi(URL)