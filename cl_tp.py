import csv
import pandas as pd
import os

def load_csv(filename):
    data_tmp = []
    data_out = []

    data_tmp = pd.read_csv(filename)
    for i in range(len(data_tmp)):
        tdict = {}
        if data_tmp["spot_s"][i] == "01F0584N" and data_tmp["spot_g"][i] == "01F0557N":
            tdict.update({"time":data_tmp["time"][i]})
            tdict.update({"spot_s":data_tmp["spot_s"][i]})
            tdict.update({"spot_g":data_tmp["spot_g"][i]})
            tdict.update({"cate":data_tmp["cate"][i]})
            tdict.update({"spd":data_tmp["spd"][i]})
            tdict.update({"num":data_tmp["num"][i]})
            data_out.append(tdict)

        elif data_tmp["spot_s"][i] == "01F0532N" and data_tmp["spot_g"][i] == "01F0509N":
            tdict.update({"time":data_tmp["time"][i]})
            tdict.update({"spot_s":data_tmp["spot_s"][i]})
            tdict.update({"spot_g":data_tmp["spot_g"][i]})
            tdict.update({"cate":data_tmp["cate"][i]})
            tdict.update({"spd":data_tmp["spd"][i]})
            tdict.update({"num":data_tmp["num"][i]})
            data_out.append(tdict)

        elif data_tmp["spot_s"][i] == "01F0509N" and data_tmp["spot_g"][i] == "01F0467N":
            tdict.update({"time":data_tmp["time"][i]})
            tdict.update({"spot_s":data_tmp["spot_s"][i]})
            tdict.update({"spot_g":data_tmp["spot_g"][i]})
            tdict.update({"cate":data_tmp["cate"][i]})
            tdict.update({"spd":data_tmp["spd"][i]})
            tdict.update({"num":data_tmp["num"][i]})
            data_out.append(tdict)

        elif data_tmp["spot_s"][i] == "01F0413N" and data_tmp["spot_g"][i] == "01F0376N":
            tdict.update({"time":data_tmp["time"][i]})
            tdict.update({"spot_s":data_tmp["spot_s"][i]})
            tdict.update({"spot_g":data_tmp["spot_g"][i]})
            tdict.update({"cate":data_tmp["cate"][i]})
            tdict.update({"spd":data_tmp["spd"][i]})
            tdict.update({"num":data_tmp["num"][i]})
            data_out.append(tdict)

        elif data_tmp["spot_s"][i] == "01F0339N" and data_tmp["spot_g"][i] == "01F0293N":
            tdict.update({"time":data_tmp["time"][i]})
            tdict.update({"spot_s":data_tmp["spot_s"][i]})
            tdict.update({"spot_g":data_tmp["spot_g"][i]})
            tdict.update({"cate":data_tmp["cate"][i]})
            tdict.update({"spd":data_tmp["spd"][i]})
            tdict.update({"num":data_tmp["num"][i]})
            data_out.append(tdict)

        elif data_tmp["spot_s"][i] == "01F0256N" and data_tmp["spot_g"][i] == "01F0233N":
            tdict.update({"time":data_tmp["time"][i]})
            tdict.update({"spot_s":data_tmp["spot_s"][i]})
            tdict.update({"spot_g":data_tmp["spot_g"][i]})
            tdict.update({"cate":data_tmp["cate"][i]})
            tdict.update({"spd":data_tmp["spd"][i]})
            tdict.update({"num":data_tmp["num"][i]})
            data_out.append(tdict)

        else:
            pass

    return data_out


def main():
    #variable
    data = []
    file_list = []
    title = ["time", "spot_s", "spot_g", "cate", "spd", "num"]

    #main
    for item in os.listdir("./"):
        if str(item).find(".csv") != -1:
            file_list.append(item)

    file_list.sort()

    for name in file_list:
        data = load_csv(name)

        file_name = name[10:]

        with open("cl_tp_" + file_name, "w") as fout:

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
