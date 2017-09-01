# -*- coding: utf-8 -*-
import datetime
import json
import urllib
import re
import sys

default_encoding = 'utf-8'
reload(sys)
sys.setdefaultencoding(default_encoding)

def getdate(startdate, enddate):
    url = 'https://sjipiao.alitrip.com/search/cheapFlight.htm?startDate=%s&endDate=%s&' \
         'routes=BJS-&_ksTS=1469412627640_2361&callback=jsonp1815&ruleId=99&flag=1' % (startdate, enddate)
    price_html = urllib.urlopen(url).read().strip()

    pattern = r'jsonp1815\(\s+(.+)\)'
    re_rule = re.compile(pattern)
    json_data = re.findall(pattern, price_html)[0]

    price_json = json.loads(json_data)

    flights = price_json['data']['flights']  # flights Info
    return flights
# 输出所有航班信息
def print_all_trip(flights):
    for province in flights:
        print_trip(flights[province], province)


# 输出目的地航班信息
def print_trip(flight, province):
        print '===============Province:%s===============' % province
        for f in flight:
            source = '从：%s-' % f['depName']
            dest = '到：%s\t' % f['arrName']
            price = '\t价格：%s%s(折扣:%s)\t' % ((f['price']), f['priceDesc'], f['discount'])
            depart_date = '\t日期：%s' % f['depDate']
            print source + dest + price + depart_date
delay = int(raw_input('Enter the Day after: '))
today = datetime.date.today()
enddate = today + datetime.timedelta(delay)
endstr = str(enddate)
print str(today) + ' To ' + endstr

flights = getdate(today, enddate=endstr)
print_all_trip(flights)