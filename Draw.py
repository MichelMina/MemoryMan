import numpy as np
from matplotlib import pyplot as plt
from stackedBarGraph import StackedBarGrapher
import Hole
import Process


def draw_graph(Holes_Objects,Processes_Objects, Block_List):
    SBG = StackedBarGrapher()

    Memory_List = []
    for each in Holes_Objects:
        Memory_List.append([float(each.address),float(each.size),1])
    
    if (Block_List==[]):
        for x in range(len(Holes_Objects)):
            Block_List.append([float(Holes_Objects[x].address+Holes_Objects[x].size), float(Holes_Objects[x+1].address- Holes_Objects[x].address-Holes_Objects[x].size) if x<len(Holes_Objects)-1 else 0, 0] )

    for each in Block_List:
        Memory_List.append(each)

    for each in Processes_Objects:
        if (each.allocated_to!=-1):
            Memory_List.append([float(each.allocated_to.address), float(each.size), 2])
    
    print Memory_List
    
    Memory_List.sort(key = lambda x:x[0])
    
    print Memory_List

    np_array = []
    d_colors = []

    for each in Memory_List:
        np_array.append(each[1])
        if (each[2]==0):
            d_colors.append('#aaaaaa')
        elif (each[2]==1):
            d_colors.append('#0000bb')
        elif (each[2]==2):
            d_colors.append('#bb0000')

        
    d = np.array([np_array])
    
    print d
    
    d_widths = [1]
    d_labels = ["Memory"]
    fig = plt.figure()

    ax = fig.add_subplot(111)
    SBG.stackedBarPlot(ax,
                       d,
                       d_colors,
                       xLabels=d_labels,
                       yTicks=7,
                       widths=d_widths,
                      )
    plt.title("Memory Allocation")

    fig.subplots_adjust(bottom=0.4)
    plt.tight_layout()
    plt.show()
    plt.close(fig)
    del fig