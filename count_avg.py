import csv
import pandas as pd
import numpy as np
import os

def load_csv(file_name):
    data_out = []
    with open(file_name, "r") as f:
        content = f.readlines()
        for item in content:
            data = []
            tdict = {}
            data = item.split(",")
            tdict.update({"time":data[0]})
            tdict.update({"spot":data[1]})
            tdict.update({"ns":data[2]})
            tdict.update({"cate":data[3]})
            tdict.update({"num":int(data[4][:-1])})
            data_out.append(tdict)

        return data_out

def data_combine(data, csv):
    for i in range(len(data)):
        data[i]["num"] = data[i]["num"] + csv[i]["num"]

    return data


def main():
    #variable
    data = []
    next_data = []
    file_list = []
    file_count = 0


    #main
    for item in os.listdir("./"):
        if str(item).find(".csv") != -1:
            file_list.append(item)

    file_list.sort()
    data_num = len(file_list) * 1.0


    for file in file_list:

            if file_count == 0:
                data = load_csv(file)

            if file_list.index(file)+1 < len(file_list):
                next_data = load_csv(file_list[file_list.index(file)+1])
                data = data_combine(data, next_data)
                file_count += 1


    with open("926.csv", "w") as fout:
        wr = csv.writer(fout)

        for i in range(len(data)):
            value = []
            value.append(data[i]["time"])
            value.append(data[i]["spot"])
            value.append(data[i]["ns"])
            value.append(data[i]["cate"])
            value.append(data[i]["num"]/data_num)
            wr.writerow(value)





if __name__ == '__main__':
    main()
