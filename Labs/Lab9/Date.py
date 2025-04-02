'''
Start to the Date class for Lab 9.  This code will not run in Python
until three methods are added:
    __init__,
    __str__
    same_day_in_year
'''

days_in_month = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
month_names = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 'July',\
                    'August','September', 'October', 'November', 'December' ]
class Date(object):
    def __init__(self, year = 1900, month = 1, day = 1):
        self.year = year
        self.month = month
        self.day = day
        
    def __str__(self):
        self.year = str(self.year)
        self.month = str(self.month).rjust(2, '0')
        self.day = str(self.day).rjust(2, '0')
        return self.year + '/' + self.month + '/' + self.day
    
    def same_day_in_year(self, o):
        if self.month == o.month and self.day == o.day:
            return True
        else:
            return False
    
    def is_leap_year(self):
        if (int(self.year) % 4 == 0 and int(self.year) % 100 != 0) or (int(self.year) % 400 == 0):
            return True
        else:
            return False
        
    def __lt__(self, o):
        y1, m1, d1 = int(self.year), int(self.month), int(self.day)
        y2, m2, d2 = int(o.year), int(o.month), int(o.day)
        
        if y1 < y2:
            return True
        elif y1 > y2:
            return False
        if m1 < m2:
            return True
        elif m1 > m2:
            return False    
        return d1 < d2

    
if __name__ == "__main__":
    d1 = Date(1972, 3, 27)
    d2 = Date(1998, 4, 13)
    d3 = Date(1998, 5, 13)
    d4 = Date(1998, 4, 11)
    print("d1: " + str(d1))
    print("d2: " + str(d2))
    print("d3: " + str(d3))
    print("d1.same_day_in_year(d2)", d1.same_day_in_year(d2))
    print("d2.same_day_in_year(d3)", d2.same_day_in_year(d3)) 
    print(d1.is_leap_year())
    print (d2.is_leap_year())
    print()
    print(d1 < d2)
    print(d2 < d3)
    print(d3 < d4)