"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #
        tags = soup.find_all('td')
        lst = []
        male = 0
        female = 0
        for i in range(1, len(tags)-2):
            if not tags[i].text.isdigit() and not tags[i].text.isalpha():
                if tags[i].text.find(",") != -1:
                    num = tags[i].text.split(",")
                    lst.append(int(num[0]) * 1000 + int(num[1]))
                else:
                    lst.append(int(tags[i].text))
        for i in range(len(lst)):
            if i % 2 == 0:
                male += lst[i]
            else:
                female += lst[i]
        print('Male Number:', male)
        print('Female Number:', female)


if __name__ == '__main__':
    main()
