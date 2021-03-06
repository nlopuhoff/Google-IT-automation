#!/usr/bin/env python3

import json
import locale
import sys
from operator import itemgetter
from reports import generate
import emails
import operator
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.graphics.charts.barcharts import VerticalBarChart


def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums. Returns a list of lines that summarize the information."""
  max_revenue = {"revenue": 0}
  max_sales = {"sold": 0}
  sales_leader = {}
  car_years = {}
  for item in data:
    # Calculate the revenue generated by this model (price * total_sales) We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    x = item["car"]["car_year"]
    y = item["total_sales"]
    if item_revenue > max_revenue["revenue"]:
        item["revenue"] = item_revenue
        max_revenue = item
    # TODO: also handle max sales
    if item["total_sales"] > max_sales["sold"]:
        max_sales["sold"] = item["total_sales"]
        sales_leader = item
    # TODO: also handle most popular car_year
    if x not in car_years.keys():
        car_years[x] = y
    else:
        car_years[x] += y

  car_years = sorted(car_years.items(), key=itemgetter(1), reverse=True)
  summary = [
    "The {} generated the most revenue: ${}".format(format_car(max_revenue["car"]), max_revenue["revenue"]),
    "The {} had the most sales: {}".format(format_car(sales_leader["car"]), sales_leader["total_sales"]),
    "The most popular year was {} with {} sales.".format(car_years[0][0], car_years[0][1])]

  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data


def pie_chart(data_for_pie):
    d = Drawing(400,400)
    pc = Pie()
    pc.x = 100
    pc.y = 210
    pc.width = 170
    pc.height = 170
    pc.sideLabels = True
    pc.sideLabelsOffset = 0.05
    car_name_lst = []
    car_sales_lst = []
    car_price_lst = []
    data_for_pie = data_for_pie[1:]
    data_for_pie = sorted(data_for_pie, key=itemgetter(3), reverse=True) # so i can show 10 most popular cars
    for i in data_for_pie:
        car_name = i[1]
        car_name_lst.append(car_name)
        car_sales = i[3]
        car_sales_lst.append(car_sales)
        car_price = float(i[2].strip("$")) #by default all the prices are in '', for example '18731.76'
        car_price_lst.append(car_price)
    pc.data = car_sales_lst[:10]
    pc.labels = list(set(car_name_lst[:10])) # by using set i wont have similar items in list
    d.add(pc, '')

    """have to done this because in task i have to calculate revenue on Xaxis and car name on Yaxis"""
    revenue_calculation_1 = car_sales_lst[:10]
    revenue_calculation_2 = car_price_lst[:10]
    car_revenue_list = []
    for i in range(len(car_price_lst[:10])):
        reven = revenue_calculation_1[i] * revenue_calculation_2[i]
        car_revenue_list.append(int(reven)) #using int because its many digits after ","

    """bar chart """
    data = [tuple(car_revenue_list)] #for some reason bar chart accepts only [[]] or [()]
    bc = VerticalBarChart()
    bc.x = 50
    bc.y = 0
    bc.height = 125
    bc.width = 300
    bc.data = data
    bc.strokeColor = colors.black
    bc.valueAxis.valueMin = 7000000
    bc.valueAxis.valueMax = 23000000
    bc.valueAxis.valueStep = 1000000
    bc.categoryAxis.labels.boxAnchor = 'ne'
    bc.categoryAxis.labels.dx = 8
    bc.categoryAxis.labels.dy = -2
    bc.categoryAxis.labels.angle = 30
    bc.categoryAxis.categoryNames = list(set(car_name_lst[:10]))
    d.add(bc)

    return d


def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("car_sales.json")
  summary = process_data(data)
  optional_challenge_1_raw = cars_dict_to_table(data)
  optional_challenge_1 = optional_challenge_1_raw[1:] # have to remove first row to be able to sort the list
  optional_challenge_1 = sorted(optional_challenge_1, key=itemgetter(3), reverse=True) # sorting the list
  optional_challenge_1.insert(0, ["ID", "Car", "Price", "Total Sales"])
  pie = pie_chart(optional_challenge_1_raw)
  # TODO: turn this into a PDF report
  generate("/home/alex/Lab/ssss.pdf", "Sales Summary for last month", '<br /> '.join(summary), optional_challenge_1, pie) #last item is a pie, will be added to the end of pdf(also corrected report.py file)
  # TODO: send the PDF report as an email attachment
  #x = emails.generate("automation@example.com", "student-01-0487a467ec76@", "Sales summary for last month", ", \n".join(summary), "/tmp/cars.pdf")
  #emails.send(x)


if __name__ == "__main__":
  main(sys.argv)
