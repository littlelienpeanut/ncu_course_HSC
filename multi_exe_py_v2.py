import multiprocessing as mp
import numpy as np
import final_pred
from multiprocessing import Queue
import os
import time
import matplotlib.pyplot as plt

def run_final_pred(q, j):
    a = final_pred.Run()
    tdict = {}

    if j == 0:
        s1_1_result, s1_2_result, s1_3_result, s1_4_result = a.main(j)
        tdict.update({"s1t1":s1_1_result})
        tdict.update({"s1t2":s1_2_result})
        tdict.update({"s1t3":s1_3_result})
        tdict.update({"s1t4":s1_4_result})
        q.put(tdict)

    elif j == 2:
        s2_1_result, s2_2_result, s2_3_result, s2_4_result = a.main(j)
        tdict.update({"s2t1":s2_1_result})
        tdict.update({"s2t2":s2_2_result})
        tdict.update({"s2t3":s2_3_result})
        tdict.update({"s2t4":s2_4_result})
        q.put(tdict)

    elif j == 4:
        s3_1_result, s3_2_result, s3_3_result, s3_4_result = a.main(j)
        tdict.update({"s3t1":s3_1_result})
        tdict.update({"s3t2":s3_2_result})
        tdict.update({"s3t3":s3_3_result})
        tdict.update({"s3t4":s3_4_result})
        q.put(tdict)

    elif j == 6:
        s4_1_result, s4_2_result, s4_3_result, s4_4_result = a.main(j)
        tdict.update({"s4t1":s4_1_result})
        tdict.update({"s4t2":s4_2_result})
        tdict.update({"s4t3":s4_3_result})
        tdict.update({"s4t4":s4_4_result})
        q.put(tdict)

    elif j == 8:
        s5_1_result, s5_2_result, s5_3_result, s5_4_result = a.main(j)
        tdict.update({"s5t1":s5_1_result})
        tdict.update({"s5t2":s5_2_result})
        tdict.update({"s5t3":s5_3_result})
        tdict.update({"s5t4":s5_4_result})
        q.put(tdict)

    elif j == 10:
        s6_1_result, s6_2_result, s6_3_result, s6_4_result = a.main(j)
        tdict.update({"s6t1":s6_1_result})
        tdict.update({"s6t2":s6_2_result})
        tdict.update({"s6t3":s6_3_result})
        tdict.update({"s6t4":s6_4_result})
        q.put(tdict)

    else:
        pass

if __name__ == '__main__':
    list = []
    data = {}
    q = mp.Queue()

    p1 = mp.Process(target=run_final_pred, args=(q, 0))
    p2 = mp.Process(target=run_final_pred, args=(q, 2))
    p3 = mp.Process(target=run_final_pred, args=(q, 4))
    p4 = mp.Process(target=run_final_pred, args=(q, 6))
    p5 = mp.Process(target=run_final_pred, args=(q, 8))
    p6 = mp.Process(target=run_final_pred, args=(q, 10))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()

    #get element in Queue
    while not q.empty():
        list.append(q.get())

    for d in list:
        data.update(d)

    #print accuracy
    print("spot1 00:00 - 06:00_accuracy:" + str(data["s1t1"]))
    print("spot1 06:00 - 12:00_accuracy:" + str(data["s1t2"]))
    print("spot1 12:00 - 18:00_accuracy:" + str(data["s1t3"]))
    print("spot1 18:00 - 24:00_accuracy:" + str(data["s1t4"]))
    print("")
    print("spot2 00:00 - 06:00_accuracy:" + str(data["s2t1"]))
    print("spot2 06:00 - 12:00_accuracy:" + str(data["s2t2"]))
    print("spot2 12:00 - 18:00_accuracy:" + str(data["s2t3"]))
    print("spot2 18:00 - 24:00_accuracy:" + str(data["s2t4"]))
    print("")
    print("spot3 00:00 - 06:00_accuracy:" + str(data["s3t1"]))
    print("spot3 06:00 - 12:00_accuracy:" + str(data["s3t2"]))
    print("spot3 12:00 - 18:00_accuracy:" + str(data["s3t3"]))
    print("spot3 18:00 - 24:00_accuracy:" + str(data["s3t4"]))
    print("")
    print("spot4 00:00 - 06:00_accuracy:" + str(data["s4t1"]))
    print("spot4 06:00 - 12:00_accuracy:" + str(data["s4t2"]))
    print("spot4 12:00 - 18:00_accuracy:" + str(data["s4t3"]))
    print("spot4 18:00 - 24:00_accuracy:" + str(data["s4t4"]))
    print("")
    print("spot5 00:00 - 06:00_accuracy:" + str(data["s5t1"]))
    print("spot5 06:00 - 12:00_accuracy:" + str(data["s5t2"]))
    print("spot5 12:00 - 18:00_accuracy:" + str(data["s5t3"]))
    print("spot5 18:00 - 24:00_accuracy:" + str(data["s5t4"]))
    print("")
    print("spot6 00:00 - 06:00_accuracy:" + str(data["s6t1"]))
    print("spot6 06:00 - 12:00_accuracy:" + str(data["s6t2"]))
    print("spot6 12:00 - 18:00_accuracy:" + str(data["s6t3"]))
    print("spot6 18:00 - 24:00_accuracy:" + str(data["s6t4"]))
    print("")

    #plot
    order_list = []
    x_label = []

    for i in range(1, 7, 1):
        tmp_list = []
        for j in range(1, 5, 1):
            name = "s" + str(i) + "t" + str(j)
            tmp_list.append(float(data[name]))
        order_list.append(tmp_list)

    x_label = ["time1", "time2", "time3", "time4"]
    x = np.arange(1, 5, 1)

    plt.figure(figsize=(16,9))
    fig, arr = plt.subplots(2, 3)
    arr[0, 0].plot(x, order_list[0], "b-",lw=2, alpha=0.7)
    arr[0, 0].set_title("spot_1")
    arr[0, 1].plot(x, order_list[1], "b-",lw=2, alpha=0.7)
    arr[0, 1].set_title("spot_2")
    arr[0, 2].plot(x, order_list[2], "b-",lw=2, alpha=0.7)
    arr[0, 2].set_title("spot_3")
    arr[1, 0].plot(x, order_list[3], "b-",lw=2, alpha=0.7)
    arr[1, 0].set_title("spot_4")
    arr[1, 1].plot(x, order_list[4], "b-",lw=2, alpha=0.7)
    arr[1, 1].set_title("spot_5")
    arr[1, 2].plot(x, order_list[5], "b-",lw=2, alpha=0.7)
    arr[1, 2].set_title("spot_6")
    plt.setp(arr, xticks= x , xticklabels = x_label, ylim = ([0.3, 1.0]))
    plt.show()
