import requests
import urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings()

url=input('url: ')
rutasf=input('fichero con rutas: ')
with open(rutasf) as f:
        for linea in f:
                site=url+'/'+linea[:-1]
                resq=requests.get(site,verify=False)
                print (resq.status_code)
                if resq.status_code==200:
                        print ('hackeado')
                        print (url)
                        print (linea)
