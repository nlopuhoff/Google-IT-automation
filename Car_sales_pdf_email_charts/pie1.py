#!/usr/bin/env python3
import cars
from operator import itemgetter
from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics import shapes
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.charts.axes import XValueAxis
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart

data = cars.load_data("car_sales.json")
summary = cars.process_data(data)
optional_challenge_1_raw = cars.cars_dict_to_table(data)
optional_challenge_1 = optional_challenge_1_raw[1:]
car_name_lst = []
car_sales_lst = []
car_price_lst = []
optional_challenge_1 = sorted(optional_challenge_1, key=itemgetter(3), reverse=True)
for i in optional_challenge_1:
    car_name = i[1]
    car_name_lst.append(car_name)
    car_sales = i[3]
    car_sales_lst.append(car_sales)
    car_price = float(i[2].strip("$")) #by default all the prices are in '', for example '18731.76
    car_price_lst.append(car_price)



d = Drawing(400,400)
pc = Pie()
pc.x = 100
pc.y = 240
pc.width = 130
pc.height = 130
pc.sideLabels = True
pc.sideLabelsOffset = 0.05
pc.data = car_sales_lst[:10]
pc.labels = list(set(car_name_lst[:10]))
d.add(pc, '')

revenue_calculation_1 = car_sales_lst[:10]
revenue_calculation_2 = car_price_lst[:10]
car_revenue_list = []
for i in range(len(car_price_lst[:10])):
    reven = revenue_calculation_1[i] * revenue_calculation_2[i]
    car_revenue_list.append(int(reven)) #using int because its many digits after ","

#print(car_revenue_list)


bc = VerticalBarChart()
data = [tuple(car_revenue_list)]
bc.x = 50
bc.y = 75
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

renderPDF.drawToFile(d, 'example2.pdf', 'My 2nd Drawing')






#lab = Label()
#lab.setOrigin(100,90)
#lab.boxAnchor = 'ne'
#lab.angle = 45
#lab.dx = 0
#lab.dy = -20
#lab.boxStrokeColor = colors.green
#lab.setText('Some Multi-Line Label')
#d.add(lab)

#data = [(0, 45)]
#xAxis = XValueAxis()
#xAxis.setPosition(15, 150, 180)
#xAxis.valueSteps = [10, 15, 20, 30, 35, 40]
#xAxis.configure(data)
#xAxis.labels.boxAnchor = 'n'
#d.add(xAxis)
