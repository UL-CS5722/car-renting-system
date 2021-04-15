from flask import Flask
from ola_rent.builder import Director, ToyotaBuilder, FordBuilder, HyundaiBuilder
from ola_rent.station import Dublin, Cork, Limerick, Galway

app = Flask(__name__)

@app.route('/')
def index():
    print("******WELCOME TO OLA RENT*******")
    print("---------CARS AVAILABLE----------")
    #builder car executing 
    toyota_builder = Director(ToyotaBuilder())
    toyota_builder.build_car()
    toyota = toyota_builder.get_car()
    print(toyota)

    ford_builder = Director(FordBuilder())
    ford_builder.build_car()
    ford = ford_builder.get_car()
    print(ford)

    hyundai_builder = Director(HyundaiBuilder())
    hyundai_builder.build_car()
    hyundai = hyundai_builder.get_car()
    print(hyundai)

    print("*********STATIONS CREATION*********")
    d = Dublin()
    d.create_station()
    print(d)

    g = Galway()
    g.create_station()
    print(g)

    c = Cork()
    c.create_station()
    print(c)

    l = Limerick()
    l.create_station()
    print(l)

    
    return "<h1>Development in Progress</h1>"
