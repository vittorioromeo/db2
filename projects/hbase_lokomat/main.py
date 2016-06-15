import connection_db
import import_dataset
import table_pusher
import table_generator
import query_executor
import datetime

dsr =['ds10.json','ds100.json','ds1000.json','ds10000.json']
aqr=[query_executor.get_info_patients,query_executor.get_patient_with_name,query_executor.get_misuration__patient]
connection = connection_db.database_connection()
all_media = []
first_time = []
array_all_time = []
time = datetime.datetime.now()

for q in aqr:

    for ds in dsr:
        data_set = import_dataset.import_data_set(ds)
        table_generator.degenerate_patient(connection)
        table_generator.generate_patient(connection)
        table_pusher.push_patients(connection, data_set)

        media = 0
        all_time = []
        for _ in range(0,31):
            single_time = q(connection, str(ds))
            t = single_time.total_seconds()
            if(_ == 0):
                first_time.append(t)
            else:
                media = media + t
                all_time.append(t)
        array_all_time.append(all_time)
        all_media.append(media/30)


    query_executor.create_graph(first_time,all_media,array_all_time,q)
    print("completed" + str(q))
    del all_media[:]
    del first_time[:]

print("TEMPO TOTALE")
print(datetime.datetime.now() - time)
