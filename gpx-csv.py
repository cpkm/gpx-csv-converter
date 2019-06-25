#gpx-csv

from bs4 import BeautifulSoup

file = 'data/run_ex.gpx'

with infile as open(file,'r'):
    soup = BeautifulSoup(infile.read(),'xml')

    title = soup.find_all('name')[0].get_text()

    for tp in soup.find_all('trkpt'):
        print(tp.time.get_text(),tp['lat'],tp['lon'])