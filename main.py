from flask import Flask
import random
app = Flask(__name__)
lista_fatti=["Elon Musk sostiene che i social network sono progettati per tenerci all'interno della piattaforma, in modo che trascorriamo il maggior tempo possibile a guardare contenuti.", 
            "Secondo uno studio condotto nel 2018, più del 50'%' delle persone di età compresa tra i 18 e i 34 anni si considera dipendente dal proprio smartphone.", 
            "I social network hanno aspetti positivi e negativi e dobbiamo essere consapevoli di entrambi quando usiamo queste piattaforme.", 
            "Lo studio della dipendenza tecnologica è una delle aree più rilevanti della ricerca scientifica moderna."]
lista_rischi=["UN problema di avere una dipendenza dai social newtork è la progressiva perdita di capacità o mancata creazione di competenze sociali, emozionali e relazional",
              "Il troppo utilizzodei degli strumenti tecnologici può alterale il ritmo del sonno",
              "Troppo tempo passato ha giocare hai videogichi puo farti credere di essere invicibile è cio può portarti ha mettere in pericolo la tua persona o altre persone",
              " il troppo utilizzo dei social newtork può cuasre nei giovani la comparsa di disturbi alimentari"]

@app.route("/")
def ciao_mondo():
    return '<h1>Ciao questa è la home pagi trami il link puoi scoprire un fatto sulle dipendenze</h1> <a href ="/fatto_causuale">vedi dei fatti causuali</a> <a href ="/risci_per_chi_ha_una_dipendenza_dalla_tecnologia"> vedi i problemi di avere una dipendenza dalla tecnologia</a>'
@app.route("/fatto_causuale")
def fatti():
    return f'<p>{random.choice(lista_fatti)}</p>'
@app.route("/risci_per_chi_ha_una_dipendenza_dalla_tecnologia")
def rischi():
    return f'<p>{random.choice(lista_rischi)}</p>

app.run(debug=True)