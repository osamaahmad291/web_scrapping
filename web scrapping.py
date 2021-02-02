# Importing Necessary dependencies
import requests
from bs4 import BeautifulSoup
import os 
from PIL import Image 

def imagedown(url, folder):

    #Identifying if the folder exists or not, else create one by name provided in function's second parameter
    if not os.path.exists(os.path.join(os.getcwd() , folder)):
        os.makedirs(os.path.join(os.getcwd() , folder))

    name = '' 
    link = ''

    # Required. The url of the request
    r = requests.get(url)

    #Parsing html file via BeautifulSoup
    soup = BeautifulSoup(r.text , 'html.parser')

    #Fetching required list of links(URL's) 
    images = soup.select('div.AnfrageZG > a')

    # Iteration over URL's
    for image in images:
        link = image['href']
        # Fetching the file name
        image_name = image['href'].split("/", 2)[2]

        # Concatination of URL in the responce body 
        img_response = requests.get('https://www.heisig.com/'+link, stream = True)
        # Opening image in raw form
        img = Image.open(img_response.raw)
        # Saving image
        img.save(image_name)
        # For console output, not to get bored :)
        print(img)       

# Function call, Signature is two parameters URL and folder name
imagedown('https://www.heisig.com/aktuelle-auftraege' , 'img')
