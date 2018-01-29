import string
import urllib2
from bs4 import BeautifulSoup
import sys
import datetime

reload(sys)
sys.setdefaultencoding('utf8')

global f

url_part1 = 'http://www.nasdaq.com/en/symbol/'

print("Starting")

f = open('/home/pi/stock_names.txt', 'r')
file_content = f.readlines()
count = 1;
print ("About %d tickers will be downloaded" % len(file_content))

for ticker in file_content:
    try:
    	ticker = ticker.strip()
    	url = url_part1 + ticker # + url_part2
    	print(url)
    	web_page = urllib2.urlopen(url)
    	soup = BeautifulSoup(web_page, 'html.parser')
    	print ("Downloading ticker %s (%d out of %d)" % (ticker, count, len(file_content)))
    	count = count + 1

    	a0 = "1_Year_Target "
    	a1 = soup.find("td", text="1 Year Target:").find_next_sibling("td").text
    	strA1 = str(a1)
    	#a2 = '\n'
    	b0 = "Today's_H/L "
    	b1 = soup.find("td", text="Today's High/Low:").find_next_sibling("td").text
    	strB1 = str(b1)
    	#b2 = '\n'
    	c0 = "Share_Vol "
    	c1 = soup.find("td", text="Share Volume:").find_next_sibling("td").text
    	strC1 = str(c1)
    	#c2 = '\n'
    	d0 = "Pre_Close "
    	d1 = soup.find("td", text="Previous Close:").find_next_sibling("td").text
    	strD1 = str(d1)
    	#d2 = '\n'
    	e0 = "52Week's_H/L "
    	e1 = soup.find("td", text="52 Week High /Low:").find_next_sibling("td").text
    	strE1 = str(e1)
    	#e2 = '\n'
    	f0 = "P/E_Ratio "
    	f1 = soup.find("td", text="P/E Ratio:").find_next_sibling("td").text
    	strF1 = str(f1)
    	#f2 = '\n'
    	#g0 = "Forward_P/E "
    	#g1 = soup.find("td", text="Forward P/E(1y)").find_next_sibling("td").text
    	#strG1 = str(g1)
    	#g2 = '\n'
    	#h0 = "EPS "
    	#h1 = soup.find("td", text="Earnings Per Share (EPS)").find_next_sibling("td").text
    	#strH1 = str(h1)
    	#h2 = '\n'
    	i0 = "Annualized_Dividend "
    	i1 = soup.find("td", text="Annualized dividend").find_next_sibling("td").text
    	strI1 = str(i1)
    	#i2 = '\n'
    	j0 = "Ex_Div_Rate "
    	j1 = soup.find("td", text="Ex Dividend Date").find_next_sibling("td").text
    	strJ1 = str(j1)
    	#j2 = '\n'
    	k0 = "Div_Payment_Data "
    	k1 = soup.find("td", text="Dividend Payment Date").find_next_sibling("td").text
    	strK1 = str(k1)
    	#k2 = '\n'
    	l0 = "Current_Yield "
    	l1 = soup.find("td", text="Current Yield").find_next_sibling("td").text
    	strL1 = str(l1)
    	#l2 = '\n'
    	m0 = "Beta "
    	m1 = soup.find("td", text="Beta").find_next_sibling("td").text
    	strM1 = str(m1)
    	#m2 = '\n'

    	now = datetime.datetime.now()

    	content = str(now) + '\n' + a0 + strA1 + '\n' + b0 + strB1 + '\n' + c0 + strC1 + '\n' + d0 + strD1 + '\n' + e0 + strE1 + '\n' + f0 + strF1 + '\n' +  i0 + strI1 + '\n' + j0 + strJ1 + '\n' + k0 + strK1 + '\n' + l0 + strL1 + '\n' + m0 + strM1 + '\n' + '\n' + "---" + '\n'
    	print(content)
    	# raw_input("...")

   	hisF = open('/home/pi/daily/dailyStocks/' + ticker + '.txt', 'w')
   	hisF.write(content)
    	hisF.close()
    	print("succeeded!")

    except Exception, e:
        pass


f.close()

