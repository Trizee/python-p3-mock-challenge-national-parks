class NationalPark:

    all = []

    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if isinstance(name,str) and not hasattr(self,'name') and 3 <= len(name):
            self._name  = name
        else:
            raise Exception
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park is self]
    
    def visitors(self):
        return list({trip.visitor for trip in self.trips()})
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        visitors = [trip.visitor for trip in self.trips()]
        return max(set(visitors), key = visitors.count)
    
    @classmethod
    def most_visited(cls):
        return max(cls.all, key=lambda park: park.total_visits())

class Trip:
    
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self,date):
        if isinstance(date,str) and 7 <= len(date) and not hasattr(self, 'date'):
            self._start_date = date
        else:
            raise Exception
        
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self,date):
        if isinstance(date,str) and 7 <= len(date):
            self._end_date = date
        else:
            raise Exception

    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self,visitor):
        if isinstance(visitor,Visitor):
            self._visitor = visitor
        else:
            raise Exception
        
    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self,park):
        if isinstance(park,NationalPark):
            self._national_park = park
        else:
            raise Exception
        


class Visitor:

    all = []

    def __init__(self, name):
        self.name = name
        Visitor.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if isinstance(name,str) and 1<= len(name) <=15:
            self._name = name
        else:
            raise Exception
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor is self]
    
    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})
    
    def total_visits_at_park(self, park):
        if not self.trips():
            return 0
        return len([trip for trip in self.trips() if trip.national_park == park])
    
tri = Visitor('Tri')
park = NationalPark('Park')   
x = Trip(tri,park,'december 2','december 8th')
y = Trip(tri,park,'december 2','december 8th')

x.start_date = 'september 26'

print(tri.total_visits_at_park(park))

print(x)