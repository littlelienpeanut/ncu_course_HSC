import csv
import numpy as np
import pandas as pd
import os
import random
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from datetime import datetime,date

global acc_result_1
global acc_result_2
global acc_result_3
global acc_result_4

def load_csv(filename):
    data_tmp = []
    data_out = []

    data_tmp = pd.read_csv(filename)
    for i in range(len(data_tmp)):
        tdict = {}
        tdict.update({"time":data_tmp["time"][i][:10]})
        tdict.update({"spot_s":data_tmp["spot_s"][i]})
        tdict.update({"spot_g":data_tmp["spot_g"][i]})
        tdict.update({"cate":data_tmp["cate"][i]})
        tdict.update({"spd":data_tmp["spd"][i]})
        tdict.update({"num":data_tmp["num"][i]})
        s = date(year = int(data_tmp["time"][i][0:4]), month = int(data_tmp["time"][i][5:7]), day = int(data_tmp["time"][i][8:10]))
        week = s.weekday()
        tdict.update({"week":week})
        data_out.append(tdict)

    return data_out

def get_feature(j):
    #variable
    file_list_1 = []
    file_list_2 = []
    file_list_3 = []
    file_list_4 = []
    feature_1_s1 = []
    feature_2_s1 = []
    feature_3_s1 = []
    feature_4_s1 = []
    label_1_s1 = []
    label_2_s1 = []
    label_3_s1 = []
    label_4_s1 = []
    rn_day = {"2016/05/01":1, "2016/05/03":1, "2016/05/10":2, "2016/05/11":2, "2016/05/16":3, "2016/05/21":1, "2016/05/22":1, "2016/05/23":1, "2016/05/24":1, "2016/05/27":1, "2016/07/02":1, "2016/07/03":1, "2016/07/07":1, '2016/07/08':1, "2016/07/09":1, "2016/07/10":1, "2016/07/19":1,  "2016/08/01":1, "2016/08/02":1, "2016/08/11":3, "2016/08/13":1, "2016/08/27":1, "2016/08/28":1, "2016/09/02":2, "2016/09/03":3, "2016/09/06":4, "2016/09/07":1, "2016/09/09":1, "2016/09/12":1, "2016/09/13":1, "2016/09/14":1, "2016/09/16":1, "2016/09/17":2, "2016/09/18":1, "2016/09/26":2, "2016/09/27":3, "2016/09/29":1, "2016/09/30":1, "2016/10/06":1, "2016/10/07":1, "2016/10/08":2, "2016/10/09":1, "2016/10/10":1, "2016/10/11": 1, "2016/10/12":1, "2016/10/14":1, "2016/10/15":1, "2016/10/29":1, "2016/06/02":3, "2016/06/03":2, "2016/06/06":2, "2016/06/07":1, "2016/06/09":1, "2016/06/10":1, "2016/06/11":1, "2016/06/12":1, "2016/06/13":2, "2016/06/14":4, "2016/06/17":1, "2016/06/28":2, "2016/06/29":2, "2016/11/01":1, "2016/11/08":2, "2016/11/09":1, "2016/11/10":2,"2016/11/18":1,"2016/11/20":2,"2016/11/21":2,"2016/11/22":2,"2016/11/23":3,"2016/11/26":1,"2016/11/27":2}


    #get file list
    for item in os.listdir("./"):
        if str(item).find("1.csv") != -1:
            file_list_1.append(item)

    file_list_1.sort()

    for item in os.listdir("./"):
        if str(item).find("2.csv") != -1:
            file_list_2.append(item)

    file_list_2.sort()

    for item in os.listdir("./"):
        if str(item).find("3.csv") != -1:
            file_list_3.append(item)

    file_list_3.sort()

    for item in os.listdir("./"):
        if str(item).find("4.csv") != -1:
            file_list_4.append(item)

    file_list_4.sort()

    for i in range(len(file_list_1)):

        #feature1
        data = []
        data = load_csv(file_list_1[i])
        feature_tmp = []
        label_tmp = []


        if any(date in data[j]["time"] for date in rn_day):
            feature_tmp.append(int(rn_day[data[j]["time"]]))

        else:
            feature_tmp.append(0)

        feature_tmp.append(data[j]["week"])
        label_tmp.append(data[j]["spd"])
        #label_tmp.append(data[j+1]["spd"])

        feature_1_s1.append(feature_tmp)
        label_1_s1.append(label_tmp)

    for i in range(len(file_list_2)):
        #feature2
        data = []
        data = load_csv(file_list_2[i])
        feature_tmp = []
        label_tmp = []

        if any(date in data[j]["time"] for date in rn_day):
            feature_tmp.append(int(rn_day[data[j]["time"]]))

        else:
            feature_tmp.append(0)

        feature_tmp.append(data[j]["week"])
        label_tmp.append(data[j]["spd"])
        #label_tmp.append(data[j+1]["spd"])

        feature_2_s1.append(feature_tmp)
        label_2_s1.append(label_tmp)

    for i in range(len(file_list_1)):
        #feature3
        data = []
        data = load_csv(file_list_3[i])

        feature_tmp = []
        label_tmp = []

        if any(date in data[j]["time"] for date in rn_day):
            feature_tmp.append(int(rn_day[data[j]["time"]]))

        else:
            feature_tmp.append(0)

        feature_tmp.append(data[j]["week"])
        label_tmp.append(data[j]["spd"])
        #label_tmp.append(data[j+1]["spd"])

        feature_3_s1.append(feature_tmp)
        label_3_s1.append(label_tmp)

    for i in range(len(file_list_1)):
        #feature4
        data = []
        data = load_csv(file_list_4[i])
        feature_tmp = []
        label_tmp = []


        if any(date in data[j]["time"] for date in rn_day):
            feature_tmp.append(int(rn_day[data[j]["time"]]))

        else:
            feature_tmp.append(0)

        feature_tmp.append(data[j]["week"])
        label_tmp.append(data[j]["spd"])
        #label_tmp.append(data[j+1]["spd"])

        feature_4_s1.append(feature_tmp)
        label_4_s1.append(label_tmp)


    return feature_1_s1, label_1_s1, feature_2_s1, label_2_s1, feature_3_s1, label_3_s1, feature_4_s1, label_4_s1

def data_split(feature, label, size):
    tmp = []
    tr_x = []
    tr_y = []
    te_x = []
    te_y = []
    tmp = list(zip(feature, label))
    random.shuffle(tmp)
    feature, label = zip(*tmp)

    for i in range(len(feature)):
        if i <= len(feature)*size:
            tr_x.append(feature[i])
            tr_y.append(label[i])

        else:
            te_x.append(feature[i])
            te_y.append(label[i])

    tr_x = np.array(tr_x).reshape((len(tr_x),-1))
    tr_y = np.array(tr_y).reshape((len(tr_y),-1)).ravel()


    return tr_x, tr_y, te_x, te_y

def change_to_level_s1(input, j):
        list_out = []
        for i in range(len(input)):
            tmp_list = []

            if j == 0:

                if input[i][0] < 60:
                    list_out.append("slow")
                elif input[i][0] > 72:
                    list_out.append("fast")
                else:
                    list_out.append("normal")

            elif j == 2:
                if input[i][0] < 63:
                    list_out.append("slow")
                elif input[i][0] > 77:
                    list_out.append("fast")
                else:
                    list_out.append("normal")

            elif j == 4:
                if input[i][0] < 80:
                    list_out.append("slow")
                elif input[i][0] > 90:
                    list_out.append("fast")
                else:
                    list_out.append("normal")

            elif j == 6 or j == 8:
                if input[i][0] < 77:
                    list_out.append("slow")
                elif input[i][0] > 93:
                    list_out.append("fast")
                else:
                    list_out.append("normal")

            elif j == 10:
                if input[i][0] < 78:
                    list_out.append("slow")
                elif input[i][0] > 94:
                    list_out.append("fast")
                else:
                    list_out.append("normal")

            else:
                pass

        return list_out

class Run:
    def main(self, j):
        #variable

        feature_1_s1 = []
        feature_2_s1 = []
        feature_3_s1 = []
        feature_4_s1 = []
        label_1_s1 = []
        label_2_s1 = []
        label_3_s1 = []
        label_4_s1 = []
        knn_tr_pred_1 = []
        knn_tr_pred_2 = []
        knn_tr_pred_3 = []
        knn_tr_pred_4 = []
        tr_x = []
        tr_y = []
        te_x = []
        te_y = []
        acc_count_1 = 0
        acc_count_2 = 0
        acc_count_3 = 0
        acc_count_4 = 0
        acc_result_1 = 0
        acc_result_2 = 0
        acc_result_3 = 0
        acc_result_4 = 0

        #main
        feature_1_s1, label_1_s1, feature_2_s1, label_2_s1, feature_3_s1, label_3_s1, feature_4_s1, label_4_s1 = get_feature(j)

        knn = KNeighborsClassifier(n_neighbors=7)

        #time_1
        tr_x, tr_y, te_x, te_y = data_split(feature_1_s1, label_1_s1, 0.9)
        knn = knn.fit(tr_x, tr_y)

        for i in range(len(te_x)):
            knn_tr_pred_1.append(knn.predict([te_x[i]]))


        knn_tr_pred_1 = change_to_level_s1(knn_tr_pred_1, j)
        te_y = change_to_level_s1(te_y, j)

        for i in range(len(te_x)):
            if knn_tr_pred_1[i] == te_y[i]:
                acc_count_1 += 1.0
            else:
                pass

        #time_2
        tr_x, tr_y, te_x, te_y = data_split(feature_2_s1, label_2_s1, 0.9)
        knn = knn.fit(tr_x, tr_y)

        for i in range(len(te_x)):
            knn_tr_pred_2.append(knn.predict([te_x[i]]))


        knn_tr_pred_2 = change_to_level_s1(knn_tr_pred_2, j)
        te_y = change_to_level_s1(te_y, j)

        for i in range(len(te_x)):
            if knn_tr_pred_2[i] == te_y[i]:
                acc_count_2 += 1.0
            else:
                pass

        #time_3
        tr_x, tr_y, te_x, te_y = data_split(feature_3_s1, label_3_s1, 0.9)
        knn = knn.fit(tr_x, tr_y)

        for i in range(len(te_x)):
            knn_tr_pred_3.append(knn.predict([te_x[i]]))


        knn_tr_pred_3 = change_to_level_s1(knn_tr_pred_3, j)
        te_y = change_to_level_s1(te_y, j)

        for i in range(len(te_x)):
            if knn_tr_pred_3[i] == te_y[i]:
                acc_count_3 += 1.0
            else:
                pass

        #time_4
        tr_x, tr_y, te_x, te_y = data_split(feature_4_s1, label_4_s1, 0.9)
        knn = knn.fit(tr_x, tr_y)

        for i in range(len(te_x)):
            knn_tr_pred_4.append(knn.predict([te_x[i]]))


        knn_tr_pred_4 = change_to_level_s1(knn_tr_pred_4, j)
        te_y = change_to_level_s1(te_y, j)

        for i in range(len(te_x)):
            if knn_tr_pred_4[i] == te_y[i]:
                acc_count_4 += 1.0
            else:
                pass

        acc_result_1 = "%.3F" % (acc_count_1/len(knn_tr_pred_1))
        acc_result_2 = "%.3F" % (acc_count_2/len(knn_tr_pred_2))
        acc_result_3 = "%.3F" % (acc_count_3/len(knn_tr_pred_3))
        acc_result_4 = "%.3F" % (acc_count_4/len(knn_tr_pred_4))

        return acc_result_1, acc_result_2, acc_result_3, acc_result_4
