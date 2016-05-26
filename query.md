>> IMPORTANTE:
Le query devono essere ripetute 100 volte di fila.
Il tempo della benchmark sarà calcolato così:

```
inizia_timer()
for _ in range(0, 100):
    esegui_query()
termina_timer()
```

* **Query 0**: SELECT * FROM patients

* **Query 1**: SELECT * FROM patients WHERE nome = 'SIVV33W0'

* **Query 2**: SELECT patients,healthstate FROM patients JOIN healthstate ON (healstate.id_patient = patient_id) Where timestamp > '5000'

* **Query 3**: seleziona le terapie dei pazienti che hanno installato un device con when > '5000'