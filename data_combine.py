import numpy as np
import matplotlib.pyplot as plt


csv_com = np.array([])
first_pt_1 = []
first_pt_2 = []
first_pt_3 = []
first_pt_4 = []
first_pt_5 = []


for c in range(0, 24, 1):
        for m in range(0, 60, 5):
            print("loding" + str(c).zfill(2) + str(m).zfill(2) + "00.csv")
            train = np.genfromtxt("TDCS_M03A_20170418_" + str(c).zfill(2) + str(m).zfill(2) + "00.csv", delimiter=",")
            train = train[:,4]
            csv_com = np.concatenate((csv_com, train))


for i in range(0, len(csv_com), 1655):
    first_pt_1.append(csv_com[i])
    first_pt_2.append(csv_com[i+1])
    first_pt_3.append(csv_com[i+2])
    first_pt_4.append(csv_com[i+3])
    first_pt_5.append(csv_com[i+4])


plt.ylabel("Traffic_flow")
plt.xlabel("Time")
x1 = np.arange(0, 288 ,1)
plt.plot(x1, first_pt_1, "r-")
plt.plot(x1, first_pt_2, "g-")
plt.plot(x1, first_pt_3, "b-")
plt.plot(x1, first_pt_4, "y-")
plt.plot(x1, first_pt_5, "b-")
plt.title("Total traffic flow")

plt.show()
