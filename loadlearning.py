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
    item.pic=row[5]
    item.save()