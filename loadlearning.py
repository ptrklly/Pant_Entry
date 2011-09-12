project_home="/Users/jmoxon/Tutorial/Clothesliner/pant_entry/"
csv_home="/Users/jmoxon/Tutorial/Clothesliner/pant_entry/learning.csv"

import sys, os
sys.path.append(project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from pants.models import Item

import csv
dataReader = csv.reader(open(csv_home, "rU"), delimiter=',')

for row in dataReader:
    item=Item()
    item.brand=row[0]
    item.style=row[1]
    item.desc=row[2]
    item.waist=row[3]
    item.rise=row[4]
    item.cuff=row[5]
    item.thigh=row[6]
    item.pic=row[7]
    item.price=row[8]
    item.similarity=row[9]
    item.sale=row[10]
    item.color1=row[11]
    item.color2=row[12]
    item.color3=row[13]
    item.color4=row[14]
    item.save()
