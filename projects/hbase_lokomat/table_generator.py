def generate_patient(connection):
    connection.create_table \
            (
            'patient',
            {
                'analysis': {},
                'step_datas':{}
            }
        )

def degenerate_patient(connection):
    connection.delete_table('patient', disable='true')


