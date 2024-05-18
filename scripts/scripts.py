import requests
import config as cf
import json
import pandas as pd
import re
import base64




class SendRequest:
    def __init__(self) -> None:
        pass
        
    def save_image(self):
        image_url = input('\tEnter your image url: ')

        try: 
            r = requests.post(cf.HOST + 'lvtest/save/', data={'image_url': image_url})
            r.raise_for_status() 
        except requests.exceptions.HTTPError as errh: 
            print("\n<!> HTTP Error") 
            print(errh.args[0])

        response = json.loads(r.content.decode('utf-8'))
        print('- RESPONSE:')
        for k,v in response.items():
            print('\t' + k + ': ' + v)
    
    def get_list_image(self):
        
        params = {}
        print('\tEnter the param values, press "ENTER" to leave it blank:')

        search = input('\tEnter search value: ')
        filetype = input('\tEnter filter value: ')
        ordering = input('\tEnter ordering value: ')
        page_size = input('\tEnter the Size of page: ')
        page = input('\tEnter page number: ')

        if search != '': params['search'] = search
        if filetype != '': params['filetype'] = filetype
        if ordering != '': params['ordering'] = ordering
        if page_size != '': params['page_size'] = page_size
        if page != '': params['page'] = page

        try: 
            r = requests.get(cf.HOST + 'lvtest/get-list/', params=params)
            r.raise_for_status() 
        except requests.exceptions.HTTPError as errh: 
            print("\n<!> HTTP Error") 
            print(errh.args[0])
        
        response = json.loads(r.content.decode('utf-8'))
        results = response['results']
        print('- RESPONSE:\n')
        print(f'Total: {response['count']}')
        print('List:\n')
        data = pd.DataFrame(results)
        print(data)

    def get_image(self):
        params = {}

        image_id = input('\tEnter image id that you want to download: ')
        params['image_id'] = image_id

        try: 
            r = requests.get(cf.HOST + 'lvtest/get/', params=params)
            r.raise_for_status() 
        except requests.exceptions.HTTPError as errh: 
            print("\n<!> HTTP Error") 
            print(errh.args[0])

        d = r.headers['content-disposition']
        file_name = re.findall("filename=(.+)", d)[0]
        file_name = file_name.replace('"', '')
        file_dir = cf.LOCAL_IMAGE + file_name

        with open(file_dir, "wb") as fp:
            fp.write(r.content)
        
        print("Image downloaded successfully! Find the image in /image_data/\n")

    def remove_image(self):

        image_id = input('\tEnter the id of the image that you want to remove: ')
        try: 
            r = requests.post(cf.HOST + 'lvtest/remove/', data={'image_id': image_id})
            r.raise_for_status() 
        except requests.exceptions.HTTPError as errh: 
            print("\n<!> HTTP Error") 
            print(errh.args[0])

        response = json.loads(r.content.decode('utf-8'))
        
        print('- RESPONSE:\n')
        for k,v in response.items():
            print('\t' + k + ': ' + v)

    def upload_image(self):

        image = input('\tEnter the path to the image that you want to upload: ')
        file_ext = image.split('.')[-1]  
        with open(image, 'rb') as f:
            image_data = f.read()
            headers = {'Content-Type': f'media/{file_ext}'}
            
            try: 
                r = requests.post(cf.HOST + 'lvtest/upload/', headers=headers, data=image_data)
                # r = requests.post(cf.HOST + 'lvtest/upload/', files=files)
                r.raise_for_status() 
            except requests.exceptions.HTTPError as errh: 
                print("<!> HTTP Error") 
                print(errh.args[0])

        response = json.loads(r.content.decode('utf-8'))

        print('- RESPONSE:\n')
        for k,v in response.items():
            print('\t' + k + ': ' + v)

class Instruction:
    host_name = cf.HOST
    keyword_instruction = 'Use the following keywords to call the API that you want:\n\
        \t- save: Save an image from the url that you add.\n\
        \t- upload: Upload an image from local.(*)\n\
        \t- multi_upload: Upload many images from local.(*)\n\
        \t- list: Get list of the images information that are stored in database\n\
        \t- get: Download an image from database\n\
        \t- del: Delete an image in database\n\
        Enter "x" to exit the program.\n'
    
    instruction = f'Use this program to interact with the server\n\
    Host name: {host_name}\n\
    \n\
    {keyword_instruction}\n\
    \n\
    (*): Have to download image data from TensorFlow Image classification and extract to image_data/ if you want to use this request\n\
    '
    def show_instruction(self):
        print('.')
        print('.')
        print(self.instruction)
        print('------------------')


if __name__ == '__main__':
    ins = Instruction()
    req = SendRequest()
    ins.show_instruction()
    
    while True:
        print()
        call = input('Enter your request: ')
        try:
            if call == 'save':
                req.save_image()
            elif call == 'list':
                req.get_list_image()
            elif call == 'get':
                req.get_image()
            elif call == 'remove':
                req.remove_image()
            elif call == 'upload':
                req.upload_image()
            elif call == 'x':
                exit()
            else:
                print('\n<!> INVALID KEYWORD. Try again!\n')
                print(ins.keyword_instruction)
        except Exception as e:
            print('\n<!> ERROR!')
            print(e)
