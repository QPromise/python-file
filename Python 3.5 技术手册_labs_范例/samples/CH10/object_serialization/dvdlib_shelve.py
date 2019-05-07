import shelve

class DVD:
    def __init__(self, title, year=None, duration=None, director_id=None):
        self.title = title
        self.year = year
        self.duration = duration
        self.director_id = director_id

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return ("DVD('{title}', {year}, {duration}, '{director_id}')"
                    .format(**vars(self)))

class DvdDao:
    def __init__(self, dbname):
        self.dbname = dbname

    def save(self, dvd):
        with shelve.open(self.dbname) as shelve_db:
            shelve_db[dvd.title] = dvd

    def all(self):
        with shelve.open(self.dbname) as shelve_db:
            shelve_db = shelve.open(self.dbname)
            return (shelve_db[title]
                        for title in sorted(shelve_db, key = str.lower))

    def load(self, title):
        with shelve.open(self.dbname) as shelve_db:
            if title in shelve_db:
                return shelve_db[title]
        return None

    def remove(self, title):
        with shelve.open(self.dbname) as shelve_db:
            del shelve_db[title]


dao = DvdDao('dvdlib.shelve')
dvd1 = DVD('Birds', 2016, 1, 'Justin Lin')
dvd2 = DVD('Dogs', 2016, 7, 'Monica Huang')

dao.save(dvd1)
dao.save(dvd2)
print(list(dao.all()))
print(dao.load('Birds'))
dao.remove('Birds')
print(list(dao.all()))
