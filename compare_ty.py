import plotly.plotly as py
import csv
import matplotlib.pyplot as plt
import numpy as np

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
            tdict.update({"num":float(data[4][:-1])})
            data_out.append(tdict)

        return data_out

def add_all(data):
    data_out = {}
    data_out.update({"31":0})
    data_out.update({"32":0})
    data_out.update({"41":0})
    data_out.update({"42":0})
    data_out.update({"5":0})


    for i in range(0, len(data)-5, 5):
        data_out["31"] += data[i]["num"]
        data_out["32"] += data[i+1]["num"]
        data_out["41"] += data[i+2]["num"]
        data_out["42"] += data[i+3]["num"]
        data_out["5"] += data[i+4]["num"]

    data_out["31"] = "%.1f" % (data_out["31"] / 329.0)
    data_out["32"] = "%.1f" % (data_out["32"] / 329.0)
    data_out["41"] = "%.1f" % (data_out["41"] / 329.0)
    data_out["42"] = "%.1f" % (data_out["42"] / 329.0)
    data_out["5"] = "%.1f" % (data_out["5"] / 329.0)

    return data_out

def main():
    #variable
    M03_8H = []
    M03_8N = []
    M03_8H_2 = {}
    M03_8N_2 = {}
    ty_76 = []
    ty_916 = []
    ty_926 = []
    ty_76_2 = {}
    ty_916_2 = {}
    ty_926_2 = {}
    cate = []
    day = []

    #main
    M03_8H = load_csv("M03_8H.csv")
    M03_8N = load_csv("M03_8N.csv")
    ty_76 = load_csv("76.csv")

    ty_926 = load_csv("926.csv")
    M03_8H_2 = add_all(M03_8H)
    M03_8N_2 = add_all(M03_8N)
    ty_76_2 = add_all(ty_76)

    ty_926_2 = add_all(ty_926)

    print(M03_8N_2)
    print(M03_8H_2)
    print(ty_76_2)
    print(ty_926_2)

    #plt
    cate.append(M03_8H_2["31"])
    cate.append(M03_8H_2["32"])
    cate.append(M03_8H_2["41"])
    cate.append(M03_8H_2["42"])
    cate.append(M03_8H_2["5"])
    day.append(cate)
    cate = []
    cate.append(M03_8N_2["31"])
    cate.append(M03_8N_2["32"])
    cate.append(M03_8N_2["41"])
    cate.append(M03_8N_2["42"])
    cate.append(M03_8N_2["5"])
    day.append(cate)
    cate = []
    cate.append(ty_76_2["31"])
    cate.append(ty_76_2["32"])
    cate.append(ty_76_2["41"])
    cate.append(ty_76_2["42"])
    cate.append(ty_76_2["5"])
    day.append(cate)
    cate = []
    cate.append(ty_926_2["31"])
    cate.append(ty_926_2["32"])
    cate.append(ty_926_2["41"])
    cate.append(ty_926_2["42"])
    cate.append(ty_926_2["5"])
    day.append(cate)

    plt.ylabel("Traffic_flow")
    plt.xlabel("Cate")



    X = np.arange(5)+1
    plt.bar(X+0.1,day[0],width = 0.15,facecolor = 'yellowgreen',edgecolor = 'white')
    plt.bar(X+0.25,day[2],width = 0.15,facecolor = 'lightskyblue',edgecolor = 'white')
    plt.bar(X+0.6,day[1],width = 0.15,facecolor = 'yellowgreen',edgecolor = 'white')
    plt.bar(X+0.75,day[3],width = 0.15,facecolor = 'lightskyblue',edgecolor = 'white')

    #plt.ylim(0,+1.25)
    plt.show()



if __name__ == '__main__':
    main()
