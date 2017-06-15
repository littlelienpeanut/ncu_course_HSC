import csv
import pandas as pd
import os

def load_csv(file_name):
    data_tmp = []
    data_out = []


    with open(file_name, "r") as f:
        content = f.readlines()
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
            data_tmp.append(tdict)


    for i in range(0, len(data_tmp)-5, 5):
        tdict = {}
        tdict.update({"time":data_tmp[i]["time"]})
        tdict.update({"spot_s":data_tmp[i]["spot_s"]})
        tdict.update({"spot_g":data_tmp[i]["spot_g"]})
        tdict.update({"cate":"passenger_31"})
        tdict.update({"spd":(data_tmp[i]["spd"] + data_tmp[i+2]["spd"])/2})
        tdict.update({"num":int(data_tmp[i]["num"]) + int(data_tmp[i+2]["num"])})
        data_out.append(tdict)
        tdict = {}
        tdict.update({"time":data_tmp[i]["time"]})
        tdict.update({"spot_s":data_tmp[i]["spot_s"]})
        tdict.update({"spot_g":data_tmp[i]["spot_g"]})
        tdict.update({"cate":"passenger_41"})
        tdict.update({"spd":data_tmp[i+2]["spd"]})
        tdict.update({"num":int(data_tmp[i+1]["num"]) + int(data_tmp[i+3]["num"]) + int(data_tmp[i+4]["num"])})
        data_out.append(tdict)

    return data_out

def main():
    #variable
    file_list = []
    data = []
    title = ["time", "spot_s", "spot_g", "cate", "spd", "num"]

    #main

    for item in os.listdir("./"):
        if str(item).find(".csv") != -1:
            file_list.append(item)

    file_list.sort()

    for name in file_list:
        print("loading" + name)
        data = load_csv(name)
        with open("2type_" + name, "w") as fout:
            wr = csv.writer(fout)
            wr.writerow(title)
            for i in range(len(data)):
                value = []
                value.append(data[i]["time"])
                value.append(data[i]["spot_s"])
                value.append(data[i]["spot_g"])
                value.append(data[i]["cate"])
                value.append(data[i]["spd"])
                value.append(data[i]["num"])
                wr.writerow(value)




if __name__ == '__main__':
    main()
