import csv
import sys
from decimal import Decimal
import operator

countries = set()
prices_2014 = {}

def csv_reader(csv_file):
    return csv.reader(csv_file, delimiter=",", dialect=csv.excel_tab)

def add_countries(csv_file):
    reader = csv_reader(csv_file)
    for row in reader:
        country_code = row[2]
        if "Country Code" not in country_code:
            countries.add(country_code)

# Precondition: CSV contains rows sorted in descending order of price
def get_cheapest_rates(csv_file):
    reader = csv_reader(csv_file)
    prices = {}
    for row in reader:
        country = row[0]
        price = row[1]
        country_code = row[2]
        if "Country Code" not in country_code:
            prices[country] = (country_code, price)
    return prices

def to_csv(cheapest_price_list, output):
    output = open(output, "w")
    output.write('Country,"Cost per GB, excl conn (US$ PPP)",Country Code\n')
    for item in cheapest_price_list:
        row = ""
        row += '"' + item + '",'
        row += cheapest_price_list[item][1] + ","
        row += cheapest_price_list[item][0] + "\n"
        output.write(row.encode("utf-8"))
    output.close()

data_2013 = open('2013_bb_mobile_merge.csv', 'rU')
data_2014 = open('2014_bb_mobile_merge.csv', 'rU')

cheapest_2013 = get_cheapest_rates(data_2013)
cheapest_2014 = get_cheapest_rates(data_2014)

to_csv(cheapest_2013, "2013_cheapest.csv")
to_csv(cheapest_2014, "2014_cheapest.csv")

#print sorted(countries)