class Movie:
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDRENS = 2

    def __init__(self, title, price_code):
        self.title = title
        self.price_code = price_code


class Rental:
    def __init__(self, movie, days_rented):
        self.movie = movie
        self.days_rented = days_rented

    def get_charge(self):
        this_amount = 0
        price_code = self.movie.price_code
        if price_code == Movie.REGULAR:
            this_amount += 2
            if self.days_rented > 2:
                this_amount += (self.days_rented - 2) * 1.5
        elif price_code == Movie.NEW_RELEASE:
            this_amount += (self.days_rented * 3)
        elif price_code == Movie.CHILDRENS:
            this_amount += 1.5
            if self.days_rented > 3:
                this_amount += (self.days_rented - 3) * 1.5
        return this_amount

    def get_freq_renter_points(self):
        return 2 if self.movie.price_code == Movie.NEW_RELEASE and self.days_rented > 1 else 1


class Customer:
    def __init__(self, name):
        self.name = name
        self.rentals = []

    def add_rental(self, rental):
        self.rentals.append(rental)

    def statement(self):
        freq_renter_points = 0
        result = 'Rental Record for ' + self.name + '\n'
        for rental in self.rentals:
            result += '\t' + rental.movie.title + '\t' + str(rental.get_charge() ) + '\n'

        result += 'Amount owed is ' + str(self.get_total_charge()) + '\n'
        result += 'You earned ' + str(self.get_total_freq_renter_points()) + ' frequent renter points'
        return result

    def get_total_charge(self):
        total_amount = 0
        for rental in self.rentals:
            total_amount += rental.get_charge()
        return total_amount

    def get_total_freq_renter_points(self):
        freq_renter_points = 0
        for rental in self.rentals:
            freq_renter_points += rental.get_freq_renter_points()
        return freq_renter_points


if __name__ == '__main__':
     customer = Customer('test')
     movies = [Movie('ABC', Movie.NEW_RELEASE), Movie('XYZ', Movie.REGULAR), Movie('123', Movie.CHILDRENS)]
     for movie in movies:
         customer.add_rental(Rental(movie, 7))
     print(customer.statement())