"""Customers at Hackbright."""
with open('customers.txt') as f:
    for line in f:
        info = line.split("|")

class Customer(object):
    """Ubermelon customer."""
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        """Covenience method to show information about customer in console."""
        return "<Customer: {} {}: {} {}".format(self.first_name, self.last_name, self.email, self.password)

def read_customer_from_file(filepath):
        """
        Read customer data and populate directionary of customers.

        Dictionary will be {email: Customer object}.
        """
        customers = {}

        with open('customers.txt') as f:
            for line in f:
                (first_name, last_name, email, password) = line.strip().split("|")
                customers[email] = Customer(first_name, last_name, email, password)
        return customers

def get_by_email(email):
        """Get a customer object by email and returns it."""
        try: 
            return customers[email]
        except KeyError:
            return None

        

customers = read_customer_from_file('customers.txt')
