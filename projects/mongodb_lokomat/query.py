#PAZIENTE
def queryInserisciDati(db,id,name,width,height,l_shank,l_thigh,lokomat_shank,lokomat_thigh,
                       lokomat_recorded,version,legtype,lwalk_training_duration,lwalk_distance,step_datas):
    collection = db.Patients
    collection.insert({
        "id" : id,
		"name" : name,
		"width" : width,
		"height": height,
		"l_shank" : l_shank,
		"l_thigh" : l_thigh,
		"lokomat_shank" : lokomat_shank,
        "lokomat_thigh" : lokomat_thigh,
        "lokomat_recorded" : lokomat_recorded,
        "version" : version,
        "legtype" : legtype,
        "lwalk_training_duration" : lwalk_training_duration,
        "lwalk_distance" : lwalk_distance,
        "step_datas" : step_datas
   })

def queryEliminaCollection(db):
    db.Patients.drop()

def primaQuery(db):
    collection = db.Patients
    patients = collection.find({})
    return patients

def secondaQuery(db):
    collection = db.Patients
    patients = collection.find({'name' : 'KBN96H9'})
    return patients

def terzaQuery(db):
    collection = db.Patients
    patients = collection.find({'lwalk_training_duration' : { $lt : 5} , : 'KBN96H9'})
    return patients
