import csv
import pandas as pd
import numpy as np
import os

def load_csv(file_name):
    data_out = []
    with open(file_name, "r") as f:
        content = f.readlines()
        #print("load " + file_name)
        for item in content:
            data = []
            tdict = {}
            data = item.split(",")
            tdict.update({"time":data[0]})
            tdict.update({"spot_s":data[1]})
            tdict.update({"spot_g":data[2]})
            tdict.update({"cate":data[3]})
            tdict.update({"spd":int(data[4])})
            tdict.update({"num":int(data[5][:-1])})
            data_out.append(tdict)

        return data_out

def data_combine(data, csv):
    for i in range(len(data)):
        data[i]["spd"] = (data[i]["spd"] + csv[i]["spd"])
        data[i]["num"] = data[i]["num"] + csv[i]["num"]

    return data


def main():
    #variable
    data = []
    next_data = []
    file_list = []
    file_count = 0
    out_file_count = 0
    filename_count = 1

    #main

    for item in os.listdir("./"):
        if str(item).find(".csv") != -1:
            file_list.append(item)

    file_list.sort()

    #print(file_list)
    for file in file_list:
        if file_count < 71:
            if file_count == 0:
                data = load_csv(file)

            if file_list.index(file)+1 < len(file_list):
                next_data = load_csv(file_list[file_list.index(file)+1])
                data = data_combine(data, next_data)
                file_count += 1

        else:
            file_count = 0
            out_file_count += 1
            filename_1 = data[0]["time"][0:4]
            filename_2 = data[0]["time"][5:7]
            filename_3 = data[0]["time"][8:10]
            filename = filename_1 + "-" + filename_2 + "-" + filename_3
            print(filename)

            with open("M05_" + filename + "_" + str(filename_count) + ".csv", "w") as fout:
                print("writing " + filename)
                wr = csv.writer(fout)
                #title = ["time", "spot_s", "spot_g", "cate", "spd", "num"]
                #wr.writerow(title)
                for i in range(len(data)):
                    value = []
                    value.append(data[i]["time"])
                    value.append(data[i]["spot_s"])
                    value.append(data[i]["spot_g"])
                    value.append(data[i]["cate"])
                    value.append(data[i]["spd"]/72)
                    value.append(data[i]["num"])
                    wr.writerow(value)


            if filename_count < 4:
                filename_count += 1
            else:
                filename_count = 1




if __name__ == '__main__':
    main()
