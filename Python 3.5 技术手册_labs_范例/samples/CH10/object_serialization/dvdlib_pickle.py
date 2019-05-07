import pickle

class DVD:
    def __init__(self, title, year=None, duration=None, director_id=None):
        self.title = title
        self.year = year
        self.duration = duration
        self.director_id = director_id
        self.filename = self.title.replace(' ', '_') + '.pickle'

    def save(self, filename=None):
        with open(self.filename, 'wb') as fh:
            pickle.dump(self, fh)

    @staticmethod
    def load(filename):
        with open(filename, 'rb') as fh:
            return pickle.load(fh)

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return "DVD('{0}', {1}, {2}, '{3}')".format(
            self.title, self.year, self.duration, self.director_id)

dvd1 = DVD('Birds', 2016, 1, 'Justin Lin')
dvd1.save()
dvd2 = DVD.load('Birds.pickle')
print(dvd2)
