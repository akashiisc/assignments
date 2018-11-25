from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.ticker import MaxNLocator
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

def parse_file(file_name):
    map_accuracies = {}
    for i in k_values:
        map_accuracies[i] = {}
        map_accuracies[i]['dimension'] = []
        map_accuracies[i]['accuracy'] = []

    f = open(file_name).readlines()
    for row in f:
        x = row.strip().split(",")
        map_accuracies[int(x[1])]['dimension'].append(int(x[0]))
        map_accuracies[int(x[1])]['accuracy'].append(float(x[2]))
    return map_accuracies


def generate_table_data_for_latex(file_name):
    map_accuracies = {}
    for i in k_values:
        map_accuracies[i] = {}
        map_accuracies[i]['dimension'] = []
        map_accuracies[i]['accuracy'] = []

    f = open(file_name).readlines()
    for row in f:
        x = row.strip().split(",")
        print(x[0] + " & " + x[1] + " & " + x[2] + " \\\\" )


file_name = "readings"


k_values = [1,3,5,10,15,20]
k_colours = {1:'b' , 3:'r' , 5:'g' , 10:'c' , 15:'m' , 20:'y' }
map_accuracies = parse_file(file_name)
# generate_table_data_for_latex(file_name)
ax = plt.figure().gca()
#plt.figure()
plt.xlabel('Dimension')
plt.ylabel('Accuracy')
#plt.title('Degree distribution')
ax.xaxis.set_major_locator(MaxNLocator(integer=True))

blue_patch = mpatches.Patch(color='blue', label='K=1')
red_patch = mpatches.Patch(color='red', label='K=3')
green_patch = mpatches.Patch(color='green', label='K=5')
# k_colours = {1:'b' , 3:'r' , 5:'g' , 10:'c' , 15:'m' , 20:'y' }
cyan_patch = mpatches.Patch(color='cyan', label='K=10')
magenta_patch = mpatches.Patch(color='magenta', label='K=15')
yellow_patch = mpatches.Patch(color='yellow', label='K=20')
plt.legend(handles=[blue_patch , red_patch , green_patch , cyan_patch , magenta_patch , yellow_patch])
for k in k_values:
    x_coordinates = map_accuracies[k]['dimension']
    y_coordinates = map_accuracies[k]['accuracy']
    # for key in sorted(apni_map):
    #     x_coordinates.append(key)
    #     y_coordinates.append(apni_map[key])
    # print(x_coordinates)
    # print(y_coordinates)
    # plt.figure()
    plt.plot(x_coordinates, y_coordinates ,  k_colours[k] + '-', label=' K = ' + str(k))
    # function to show the plot
    # if True == toFile:

    # else:
plt.savefig("./output_plots/k-n-accuracy.png")