import requests
import json
import pandas as pd

        
url = 'https://app.nanonets.com/api/v2/OCR/Model/b3b24599-459e-494e-88b1-ac6bf24047c8/LabelFile/?async=false'
image_path = './ProjetKhouloud/images/facture2.png'
data = {'file': open(image_path, 'rb')}

response = requests.post(url, auth=requests.auth.HTTPBasicAuth('a6e29951-c187-11ed-88ba-4eb78123d082', ''), files=data)

data =response.text
parse_json = json.loads(data)
list_predictions = parse_json['result'][0]['prediction']
#print(list_predictions)
buyer_name = []
invoice_number = []
invoice_date = []
subtotal= []
total_tax  = []
invoice_amount= []

for i in list_predictions:
    if (i['label']=='buyer_name'):
        buyer_name.append(i['ocr_text'])
    elif (i['label']=='invoice_number'):
        invoice_number.append(i['ocr_text'])
    elif(i['label']=='invoice_date'):
        invoice_date.append(i['ocr_text'])
    elif(i['label']=='subtotal'):
        subtotal.append(i['ocr_text'])
    elif(i['label']=='total_tax'):
        total_tax.append(i['ocr_text'])
    elif(i['label']=='invoice_amount'):
        invoice_amount.append(i['ocr_text'])

dataframe = pd.DataFrame(list(zip(buyer_name,invoice_number,invoice_date,subtotal,total_tax,invoice_amount)),columns=["Buyer Name","Invoice Number","Invoice Date","Subtotal","Total Tax","Invoice Amount"])

print(dataframe)