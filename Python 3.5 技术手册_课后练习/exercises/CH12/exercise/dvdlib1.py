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


class Customer:
    def __init__(self, name):
        self.name = name
        self.rentals = []

    def add_rental(self, rental):
        self.rentals.append(rental)

    def statement(self):
        total_amount = 0
        freq_renter_points = 0
        result = 'Rental Record for ' + self.name + '\n'
        for rental in self.rentals:
            this_amount = 0
            # determine amounts for each line
            price_code = rental.movie.price_code
            if price_code == Movie.REGULAR:
                this_amount += 2
                if rental.days_rented > 2:
                    this_amount += (rental.days_rented - 2) * 1.5
            elif price_code == Movie.NEW_RELEASE:
                this_amount += (rental.days_rented * 3)
            elif price_code == Movie.CHILDRENS:
                this_amount += 1.5
                if rental.days_rented > 3:
                    this_amount += (rental.days_rented - 3) * 1.5

            # add frequent renter points
            freq_renter_points += 1

            # add bonus for a two day new release rental
            if price_code == Movie.NEW_RELEASE and rental.days_rented > 1:
                freq_renter_points += 1

            # show figures for this rental
            result += '\t' + rental.movie.title + '\t' + str(this_amount) + '\n'
            total_amount += this_amount

        # add footer lines
        result += 'Amount owed is ' + str(total_amount) + '\n'
        result += 'You earned ' + str(freq_renter_points) + ' frequent renter points'
        return result

if __name__ == '__main__':
     customer = Customer('test')
     movies = [Movie('ABC', Movie.NEW_RELEASE), Movie('XYZ', Movie.REGULAR), Movie('123', Movie.CHILDRENS)]
     for movie in movies:
         customer.add_rental(Rental(movie, 7))
     print(customer.statement())