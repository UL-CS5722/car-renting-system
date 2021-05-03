from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table, DateTime, create_engine, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
import datetime

engine = create_engine('sqlite:////tmp/test.db', convert_unicode=True)
metadata = MetaData(bind=engine)


Base = declarative_base()

vehicles = Table(
    "vehicles",
    Base.metadata,
    Column("id", String, primary_key=True),
    Column("no_of_seats", Integer),
    Column("engine", Float),
    Column("fuel_type", String),
    Column("gear_type", String),
    Column("company", String),
    Column('model', String),
    Column('build_year', Integer)
)

stations = Table(
    "stations",
    Base.metadata,
    Column("code", String, primary_key=True),
    Column("name", String),
    Column("address_id", Integer, ForeignKey("addresses.id")),
    Column("email", String),
    Column("phone", Integer)
)

addresses = Table(
    "addresses",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column('street_no', String),
    Column("street_name", String),
    Column("city", String),
    Column("postcode", String),
    Column("country", String)
)

customers = Table(
    "customers",
    Base.metadata,
    Column("username", String, primary_key=True),
    Column("name", String),
    Column("address_id", Integer, ForeignKey("addresses.id")),
    Column("email", String),
    Column("phone", Integer),
    Column("type", String),
    Column("password", String)
)

bookings = Table(
    "bookings",
    Base.metadata,
    Column("id", String, primary_key=True),
    Column("car_id", String, ForeignKey("vehicles.id")),
    Column("customer_uname", String, ForeignKey("customers.username")),
    Column("booked_on", DateTime, default=datetime.datetime.utcnow),
    Column("booked_for", DateTime),
    Column("station_code", String, ForeignKey("stations.code")),
    Column("return_on", DateTime)
)

trips = Table(
    "trips",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("booking_id", String, ForeignKey("bookings.id")),
    Column("distance", Float),
    Column("duration", Float),
    Column("cost", Float),
    Column("status", String)
)

payments = Table(
    "payments",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("trip_id", Integer, ForeignKey("trips.id")),
    Column("method", String),
    Column("status", String)
)



con = engine.connect()
# con.execute(addresses.insert(), id=1, street_no=1, street_name="Liffey Road", city="Lucan, Dublin", postcode="K78YV80", country="Ireland")

con.execute("INSERT INTO addresses (id, street_no, street_name, city, postcode, country) VALUES (1, 1, 'Liffey Road', 'Lucan, Dublin', 'K78YV80', 'Ireland')")
