#Libs
import requests
import json
import pandas as pd

url = 'https://app.nanonets.com/api/v2/OCR/Model/4da819e1-4fa1-43a9-81a9-163125265bca/LabelFile/?async=false'
image_path = './ProjetKhouloud/images/facture2.png'
images_links=['./ProjetKhouloud/images/facture2.png','./ProjetKhouloud/images/facture1.png']
#############################
##### Declare tables ########
#############################

def Get_data_from_image(url,image_path):
    data = {'file': open(image_path, 'rb')}
    response = requests.post(url, auth=requests.auth.HTTPBasicAuth('51d0a0da-ba9d-11ed-a27e-22a1d9fde453', ''), files=data)
    data =response.text
    parse_json = json.loads(data)
    list_predictions = parse_json['result'][0]['prediction']
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
    return dataframe


dataframe_list = []
def Get_images(images_links):
    for image_path in images_links:
        print(Get_data_from_image(url,image_path))


        