class Vehicle:
    vid = None
    seat  = 0
    company = None
    build_year = None
    mileage = 0

    def __init__(self, vid=vid, seat=seat, company=company, build_year=build_year, mileage=mileage):
        self.vid = vid
        self.seat = seat
        self.company = company
        self.build_year = build_year
        self.mileage = mileage

    def __str__(self):
        return f"This is Vehicle Class of Company: {self.company}!"