# Import utilities
import time
import sys
import numpy
import math
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def statistics(dataset_path, offset, count):
    with open(dataset_path, 'r') as f:
        values = [float(x) for x in f.readlines()]

    # Get first query time
    first = values[offset]

    # Other values
    other_values = values[offset+1:offset+count]

    # Get average time of remaining queries
    mean = numpy.mean(other_values)
    stddev = numpy.std(other_values)
    conf = 0.95 * (stddev / math.sqrt(len(other_values)))

    return (first, mean, conf)

def create_plot(plot_title, datasets, offset, count, output_path):
    x = 0

    for dataset_path in datasets:

        first,average,conf = statistics(dataset_path, offset, count)

        b_first = plt.bar(x, first, 0.5, color='b')
        x += 0.5

        b_average = plt.bar(x, average, 0.5, color='r', yerr=conf, ecolor='black')
        x += 1.5

    plt.title("benchmark: " + plot_title)

    plt.xlabel('Dataset', fontsize=12)
    plt.ylabel('Time', fontsize=12)

    plt.xticks([0.5, 2.5, 4.5, 6.5, 8.5], ['10', '100', '1000', '10000', '100000'], rotation='horizontal')

    # Create graph legend
    fontP = FontProperties()
    fontP.set_size('small')

    plt.legend([b_first, b_average], \
        ('first query time', 'average time of other queries'), \
        prop=fontP, loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=2)
    
    # Plot to file
    plt.savefig(output_path)
    plt.clf()

# Main function
if __name__ == "__main__":
    
    datasets = ["results/r10.txt", "results/r100.txt", "results/r1000.txt", "results/r10000.txt"]
    measurement_count = 30

    create_plot("query 0", datasets, 0, measurement_count, "plots/query0.png")
    create_plot("query 1", datasets, 30, measurement_count, "plots/query1.png")
    create_plot("query 2", datasets, 60, measurement_count, "plots/query2.png")