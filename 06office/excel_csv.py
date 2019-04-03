# -*- coding: utf-8 -*-


import csv


def ReadCSV(path):
    dataList = []
    with open(path, "r") as fd:
        allFile = csv.reader(fd)
        for raw in allFile:
            dataList.append(raw)
        return dataList


# 覆盖
def writeCSV(path, data):
    with open(path, "w+") as fd:
        writer = csv.writer(fd)
        for i in data:
            writer.writerow(i)


csv_file = "/Users/jayce/Documents/test.csv"
csv1_file = "/Users/jayce/Documents/test1.csv"

data = [[1,2,3], [4,5,6]]

info = ReadCSV(csv_file)
print(info)

writeCSV(csv1_file, data)