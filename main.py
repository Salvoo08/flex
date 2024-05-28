from flask import Flask
import random
app = Flask(__name__)
lista_fatti=["Elon Musk sostiene che i social network sono progettati per tenerci all'interno della piattaforma, in modo che trascorriamo il maggior tempo possibile a guardare contenuti.", 
            "Secondo uno studio condotto nel 2018, più del 50'%' delle persone di età compresa tra i 18 e i 34 anni si considera dipendente dal proprio smartphone.", 
            "I social network hanno aspetti positivi e negativi e dobbiamo essere consapevoli di entrambi quando usiamo queste piattaforme.", 
            "Lo studio della dipendenza tecnologica è una delle aree più rilevanti della ricerca scientifica moderna."]

@app.route("/")
def ciao_mondo():
    #return f'<p>{random.choice(lista_fatti)}</p>'
    return '<h1>Ciao questa è la home pagi trami il link puoi scoprire un fatto sulle dipendenze</h1> <a href ="/fatto_causuale">vedi dei fatti causuali</a>'
@app.route("/fatto_causuale")
def fatti():
    return f'<p>{random.choice(lista_fatti)}</p>'
app.run(debug=True)