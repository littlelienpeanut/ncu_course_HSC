import csv
import os
import pandas as pd

def load_csv(filename):
    data_tmp = []
    data_out = []
    data_tmp = pd.read_csv(filename)
    for i in range(len(data_tmp)):
        tdict = {}
        tdict.update({"spot_s":data_tmp["spot_s"][i]})
        tdict.update({"spot_g":data_tmp["spot_g"][i]})
        tdict.update({"cate":data_tmp["cate"][i]})
        tdict.update({"spd":data_tmp["spd"][i]})
        tdict.update({"num":data_tmp["num"][i]})
        data_out.append(tdict)

    return data_out

def main():
    #variable
    file_list = []
    file_num = 0
    data = []
    data_sum = []
    title = ["spot_s", "spot_g", "cate", "avg_spd_up", "avg_spd_down", "avg_num_up", "avg_num_down"]

    #main
    for item in os.listdir("./"):
        if str(item).find(".csv") != -1:
            file_list.append(item)

    file_list.sort()
    file_num = len(file_list)

    for i in range(file_num):
        data = load_csv(file_list[i])

        if i == 0:
            data_sum = load_csv(file_list[i])
            for j in range(len(data_sum)):
                data_sum[j]["spd"] = 0
                data_sum[j]["num"] = 0


        for j in range(len(data)):
            data_sum[j]["spd"] += data[j]["spd"]
            data_sum[j]["num"] += data[j]["num"]

        data = []

    with open("avg_spdnum.csv", "w") as fout:
        wr = csv.writer(fout)
        wr.writerow(title)
        for i in range(len(data_sum)):
            value = []
            value.append(data_sum[i]["spot_s"])
            value.append(data_sum[i]["spot_g"])
            value.append(data_sum[i]["cate"])
            value.append(int(data_sum[i]["spd"])/file_num + int(data_sum[i]["spd"])/file_num*10/100) #spd_up
            value.append(int(data_sum[i]["spd"])/file_num - int(data_sum[i]["spd"])/file_num*10/100) #spd_down
            value.append(int(data_sum[i]["num"])/file_num + int(data_sum[i]["num"])/file_num*10/100) #num_up
            value.append(int(data_sum[i]["num"])/file_num - int(data_sum[i]["num"])/file_num*10/100) #num_down
            wr.writerow(value)


if __name__ == '__main__':
    main()
