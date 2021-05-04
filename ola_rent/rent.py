from flask import Flask, redirect, url_for, render_template, request, flash, Blueprint, g
from werkzeug.exceptions import abort

from ola_rent.auth import login_required
from ola_rent.db import get_db

from .vehicles import Director, ToyotaBuilder, FordBuilder, HyundaiBuilder
from .station import Dublin, Cork, Limerick, Galway
from .customer import Prototype, Address
from .utils import logger
from .booking import Facade
from .wishlist import Wishlist, Originator, Caretaker

# app = Flask(__name__, template_folder="templates", root_path='ola_rent', static_folder='ola_rent') #root_path='ola_rent'
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

bp = Blueprint('rent', __name__)

# ###defining data structures
customer_dict = dict()
car_dict = dict()
station_dict = dict()
booking_dict = dict()

#customer prototype
c1 = Prototype()

#Home route
@bp.route('/')
def index():
    print("******WELCOME TO OLA RENT*******") 
    return render_template('index.html')

#admin route
@bp.route('/admin')
def admin():
    logger.info('Admin log in initiated')
    return redirect(url_for('login'))

@bp.route('/car')
def car():
    print("---------CARS AVAILABLE----------")
    #builder car executing 
    toyota_builder = Director(ToyotaBuilder())
    toyota_builder.build_car()
    toyota = toyota_builder.get_car()
    car_dict[toyota._id] = toyota

    ford_builder = Director(FordBuilder())
    ford_builder.build_car()
    ford = ford_builder.get_car()
    car_dict[ford._id] = ford

    hyundai_builder = Director(HyundaiBuilder())
    hyundai_builder.build_car()
    hyundai = hyundai_builder.get_car()
    car_dict[hyundai._id] = hyundai

    cars = car_dict.values()
    car_count = len(car_dict)

    return render_template('car.html', cars=cars, car_count=car_count)
    
########station creation
@bp.route('/station')
def station():
    print("*********STATIONS CREATION*********")
    d = Dublin()
    d.create_station()
    station_dict[d.get_code()] = d

    g = Galway()
    g.create_station()
    station_dict[g.get_code()] = g

    c = Cork()
    c.create_station()
    station_dict[c.get_code()] = c

    l = Limerick()
    l.create_station()
    station_dict[l.get_code()] = l
    if not request.method == 'GET':
        return "<h4>Sorry! You can't create a new Station<h4>"
    
    stations = station_dict.values()
    return render_template('station.html', stations=stations)

###booking
@bp.route('/booking', methods=('GET', 'POST'))
def booking():
    '''Function to handle booking process'''
    cars = car_dict.values()
    if request.method == 'POST':
        error = None
        s_code = request.form['code']
        bookingdate = request.form['bookingdate']   
        c_id = request.form['car_id']

        if not s_code:
            error = "Please select a station!"
        elif not bookingdate:
            error = 'Booking date is missing :('
        elif not c_id:
            error = "Please choose a car!"
        if not error is None:
            print(error)
            return redirect('booking')

        booking_obj = Facade()
        b_id = booking_obj.operations(s_code, bookingdate)
        booking_dict[b_id] = booking_obj

        return render_template('booking/success.html', msg=f"Success! Your booking ID: {b_id}")

    return render_template('booking/new.html', cars=cars)

###Wishlist
@bp.route('/wishlist', methods=('GET', 'POST'))
def wishlist():
    #Create a new wishlist'''
    wishlist = Wishlist()

    '''Create an object for wishlist'''
    cars = wishlist.get_car()
    newstate = wishlist.to_str(cars) #Convert to list to string

    '''Create a memento object'''
    originator = Originator(newstate)
    caretaker = Caretaker(originator)
    caretaker.backup()   #Save state
    caretaker.show_history()  #Show history of saved states

    print(cars)
    if request.method == "POST":
        try:
            if request.form['delete']:
                '''Delete item from wishlist'''
                car_delete = request.form['delete_car']
                wishlist.remove(car_delete)   #remove an item from the list'''
                cars = wishlist.get_car()
                return render_template('wishlist/wishlist.html', cars=cars)
        except:
            pass
        model = request.form['model']
        year = request.form['year']
        error = None
        if not model:
            error = "Model is required"
        elif not year:
            error = "year is a required field"
        if not error == None:
            flash(error)
            return redirect(url_for('wishlist'))
        token = str(model) + "_" + str(year)
        wishlist.add_car(token)
        newstate = wishlist.to_str(cars)    #Convert to list to string
        originator.new_state(newstate)    #Create a new state
        
        caretaker.backup()   #Save state
        caretaker.show_history()  #Show history of saved states
        
        cars = wishlist.get_car()
        return render_template('wishlist/wishlist.html', cars=cars)
    return render_template('wishlist/wishlist.html', cars=cars)
    