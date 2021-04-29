from flask import Flask, redirect, url_for, render_template, request, flash, Blueprint
from ola_rent.vehicles import Director, ToyotaBuilder, FordBuilder, HyundaiBuilder
from ola_rent.station import Dublin, Cork, Limerick, Galway
from ola_rent.customer import Prototype, Address
from ola_rent import logger
from ola_rent.booking import Facade

app = Flask(__name__, template_folder="templates", root_path='ola_rent', static_folder='ola_rent') #root_path='ola_rent'
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
# bp = Blueprint('auth', __name__)

###defining data structures
customer_dict = dict()
car_dict = dict()
station_dict = dict()
booking_dict = dict()

#customer prototype
c1 = Prototype()

#Home route
@app.route('/')
def index():
    print("******WELCOME TO OLA RENT*******") 
    return render_template('index.html')

#admin route
@app.route('/admin')
def admin():
    logger.info('Admin log in initiated')
    return redirect(url_for('login'))

@app.route('/car')
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

@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        if not username:
            error = 'Username is required'

        elif not password:
            error = 'Password is required'

        elif username in customer_dict:
            error = f"User {username} already exists. Please Login Instead."
            logger.error(f"customer with {username} already exists")
        
        if error is None:
            print("**********CUSTOMER CREATION***********")
            c2 = c1.clone()
            c2.create('Aman Niyaz', Address('1 Liffey Road', 'Dublin', 'K78 V80', 'Ireland'), 'aniyaz@gmail.com', '083 015 2772', 'Premium')
            customer_dict[username] = c2

            return redirect(url_for('login'))
        flash(error)
        
    return render_template('auth/register.html')

@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        user = request.form['username']
        pswd = request.form['password']

        if user == 'aman' and pswd == '2020':
            print(f"Welcome! {user}")
            logger.info(f"user {user} successfully logged in.")
            return redirect('/')
        error = 'Username and Password mismatch, Try again!'
        logger.warning(error)
        flash(error)
        return redirect('login')
    return render_template('auth/login.html')
    
########station creation
@app.route('/station')
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
@app.route('/booking', methods=('GET', 'POST'))
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
            print
            return redirect('booking')

        booking_obj = Facade()
        b_id = booking_obj.operations(s_code, bookingdate)
        booking_dict[b_id] = booking_obj

        return render_template('booking/success.html', msg=f"Success! Your booking ID: {b_id}")

    return render_template('booking/new.html', cars=cars)

