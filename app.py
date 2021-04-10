from flask import Flask
from ola_rent.builder import Director, ToyotaBuilder, FordBuilder, HyundaiBuilder

app = Flask(__name__)

@app.route('/')
def index():
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
    
    return "<h1>Development in Progress</h1>"
