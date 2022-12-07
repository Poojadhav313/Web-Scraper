from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
headings = ['title','price','discount','rating']
ws.append(headings)

url = 'https://www.flipkart.com/cameras/dslr-mirrorless/pr?sid=jek%2Cp31%2Ctrv&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p%5B%5D=facets.type%255B%255D%3DMirrorless&param=179&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJTaG9wIE5vdyEiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19LCJ0aXRsZSI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ0aXRsZSIsImluZmVyZW5jZVR5cGUiOiJUSVRMRSIsInZhbHVlcyI6WyJUb3AgTWlycm9ybGVzcyBDYW1lcmFzIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fSwiaGVyb1BpZCI6eyJzaW5nbGVWYWx1ZUF0dHJpYnV0ZSI6eyJrZXkiOiJoZXJvUGlkIiwiaW5mZXJlbmNlVHlwZSI6IlBJRCIsInZhbHVlIjoiRExMR0ZZN1hZRzhZRk1RVCIsInZhbHVlVHlwZSI6IlNJTkdMRV9WQUxVRUQifX19fX0%3D&fm=neo%2Fmerchandising&iid=M_e8cab033-a68b-4e74-8746-5b8bf13ae893_3.Q5LU1U8PHMK6&ssid=wtvn23c2yo0000001667478375602&otracker=hp_omu_Best%2Bof%2BElectronics_2_3.dealCard.OMU_Q5LU1U8PHMK6_3&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Best%2Bof%2BElectronics_NA_dealCard_cc_2_NA_view-all_3&cid=Q5LU1U8PHMK6'
page = requests.get(url)
HTML = BeautifulSoup(page.content, 'html.parser')
lists = HTML.find_all('div', attrs={'class' : '_2kHMtA'})

for cam in lists:
  title = cam.find('div', class_ = '_4rR01T').text
  price = cam.find('div', class_ = '_30jeq3 _1_WHN1').text
  discount = cam.find('div', class_ = '_3Ay6Sb')
  rating = cam.find('div', class_ = '_3LWZlK')

  # print(title)
  try:
    ws.append([title,price,discount.text,rating.text])
  except:
    pass

print('data added successfuly')

wb.save('camera.xlsx')
