import happybase.batch
import datetime
def push_patients(connection,dict_patients):

    patient_table = connection.table('patient', use_prefix='true')
    b = patient_table.batch()
    for patient in dict_patients:
        b.put('row-key'+str(patient['id']),
              {'analysis:id': str(patient['id']),
               'analysis:width': str(patient['width']),
               'analysis:lokomat_shank': str(patient['lokomat_shank']),
               'analysis:lokomat_thigh': str(patient['lokomat_thigh']),
               'analysis:lwalk_distance': str(patient['lwalk_distance']),
               'analysis:height': str(patient['height']),
               'analysis:version': str(patient['version']),
               'analysis:legtype': str(patient['legtype']),
               'analysis:lwalk_training_duration': str(patient['lwalk_training_duration']),
               'analysis:name': str(patient['name']),
               'analysis:l_shank': str(patient['l_shank']),
               'analysis:l_thigh': str(patient['l_thigh']),
               'analysis:lokomat_recorded': str(patient['lokomat_recorded'])
               })
        i=0
        for data in patient['step_datas']:

            for single_data in data:

                b.put('row-key' + str(patient['id']),
                      {
                            'step_datas:step_datas'+str(i) : str(single_data)
                      })
                i = i + 1

    b.send()


