"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, monthly, commission, *args):
        self.name = name
        self.monthly = monthly
        self.commission = commission
        self.args = args

    def get_pay(self):
        total_pay = 0
        index_to_use = 0

        if self.monthly == True: #monthly
            total_pay += self.args[index_to_use]
            index_to_use += 1
        else: #hourly
            total_pay += self.args[index_to_use] * self.args[index_to_use + 1]
            index_to_use += 2

        if self.commission == 'b': #bonus commission
            total_pay += self.args[index_to_use]
        elif self.commission == 'c': #contract comission
            total_pay += self.args[index_to_use] * self.args[index_to_use + 1]
        #do nothing if no comission

        return total_pay

    def __str__(self):
        employee_string = ''
        index_to_use = 0
        employee_string += self.name
        employee_string += ' '

        if self.monthly == True: #monthly
            employee_string += 'works on a monthly salary of '
            employee_string += str(self.args[index_to_use])
            index_to_use += 1
        else: #hourly
            employee_string += 'works on a contract of '
            employee_string += str(self.args[index_to_use])
            index_to_use += 1
            employee_string += ' hours at '
            employee_string += str(self.args[index_to_use])
            index_to_use += 1
            employee_string += '/hour'

        if self.commission == 'b': #bonus commission
            employee_string += ' and receives a bonus commission of '
            employee_string += str(self.args[index_to_use])
        elif self.commission == 'c': #contract comission
            employee_string += ' and recieves a commission for '
            employee_string += str(self.args[index_to_use])
            index_to_use += 1
            employee_string += ' contract(s) at '
            employee_string += str(self.args[index_to_use])
            employee_string += '/contract'
        #do nothing if no comission

        employee_string += '. Their total pay is '
        employee_string += str(self.get_pay())
        employee_string += '.'

        return employee_string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', True, 'n', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', False, 'n', 100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', True, 'c', 3000, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', False, 'c', 150, 25, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', True, 'b', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', False, 'b', 120, 30, 600)