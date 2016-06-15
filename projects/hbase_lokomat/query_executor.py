import datetime
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math

def get_info_patients(connection, dataset):
    time = datetime.datetime.now()
    patients_table = connection.table('patient')
    patients_table.scan(columns=
                        ['analysis:width',
                         'analysis:lokomat_shank',
                         'analysis:lokomat_thigh',
                         'analysis:lwalk_distance',
                         'analysis:height',
                         'analysis:id',
                         'analysis:legtype',
                         'analysis:lwalk_training_duration',
                         'analysis:name',
                         'analysis:l_shank',
                         'analysis:l_thigh',
                         'analysis:lokomat_recorded',
                         'analysis:step_datas'])
    save_time(str(datetime.datetime.now() - time),"get_info_patients","stat",dataset)
    return datetime.datetime.now() - time

def get_patient_with_name(connection,dataset):
    time = datetime.datetime.now()
    patients_table = connection.table('patient')
    patients_table.scan(filter="SingleColumnValueFilter ('analysis','name',=,'regexstring:^KRVYRSKX7')")
    save_time(str(datetime.datetime.now() - time),"get_patient_with_name","stat",dataset)
    return datetime.datetime.now() - time

def get_misuration__patient(connection,dataset):
    time = datetime.datetime.now()
    patients_table = connection.table('patient')
    patients_table.scan(filter="SingleColumnValueFilter ('analysis','lwalk_training_duration',<,2400) AND ('analysis','width',!=,0.80) AND ('analysis','step_datas',>,5)")
    save_time(str(datetime.datetime.now() - time),"get_misuration__patient","stat",dataset)
    return datetime.datetime.now() - time


def create_graph(first_time,all_media,array_all_time,q):
    lenght = len(array_all_time[0])
    eConf = {'ecolor': '0.3'}

    avg_all_time = []
    std_array = []
    confidence_interval = []

    for avg_array in array_all_time:
        avg_all_time.append(calculate_avg(avg_array))

    j=0
    for media in avg_all_time:
        std_array.append(calculate_std(media,array_all_time[j]))
        j = j + 1

    for std in std_array:
        confidence_interval.append(calculate_confidence_interval(std,lenght))

    count = 0
    for firstTime in first_time:
        plt.bar(count,firstTime, width = 0.5, color='b')
        count = count + 2

    count = 0
    i = 0
    for allTime in all_media:
        plt.bar(count + 0.5, allTime, width = 0.5,yerr=confidence_interval[i], error_kw=eConf, color='r')
        count = count + 2
        i = i + 1

    plt.xticks([0.5,2.5,4.5,6.5], ['10','100','1000','10000'], rotation = 'horizontal')
    plt.xlabel('Record')
    plt.ylabel('Time')
    plt.title('statistic Hbase ' + str(q))
    plt.savefig(str(q))
    plt.clf()


def calculate_avg(array):
    sum = 0
    for x in array:
        sum = sum + x
    return sum/(len(array))


def calculate_std(media,array_time):
    sum = 0
    for time in array_time:
        sum = sum + (pow((time - media),2))
    std = math.sqrt(sum/len(array_time))
    return std


def calculate_confidence_interval(std,lenght):
    return (1.96 * (std /(math.sqrt(lenght))))



def save_time(time,name_query,filename,dataset):
    out_file = open(filename,"a")
    out_file.write(str(dataset) + " --> ")
    out_file.write(str(name_query) + ":  ")
    out_file.write("  "+str(time))
    out_file.write("\n")
    out_file.close()