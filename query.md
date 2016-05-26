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

# Algoritmo da implementare

```
# pseudocodice

# per ogni dataset
for d in datasets:

    # pulisci completamente il db e carica il dataset
    pulisci_database()
    carica_dataset(d)

    # per ogni query da fare
    for q in query_da_fare:
        
        # benchmark q, eseguita 100 vole di fila
        inizia_timer()
        for _ in range(0, 100):
            esegui_query(q)
        ris = termina_timer()

        # salva tempo impiegato su file
        salva(ris)
```