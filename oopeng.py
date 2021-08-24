class Empyloyee:

    num_of_emps = 0
    raise_amount = 1.06

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Empyloyee.num_of_emps += 1

    def fullname(self):
        return (f'{self.first}{self.last}')

    def apply_raise(self):
        self.pay = int(self.pay * Empyloyee.raise_amount)


    @classmethod
    def set_raise_amt(cls, amount):
        pass 



emp_1 = Empyloyee('Yavuz', 'Molla', 4000)
emp_2 = Empyloyee('Kerim', 'Molla', 5000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)


'''emp_1 = Empyloyee('Yavuz', 'Molla', 4000)
emp_2 = Empyloyee('Kerim', 'Molla', 5000)

print(emp_1.fullname())
print(emp_2.fullname())
#print(emp_1)
#print(emp_2)


emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'Corey.5355@company.com'
emp_1.pay = 20000


emp_2.first = 'Kevin'
emp_2.last = 'Gates'
emp_2.email = 'kevin.gates@company.com'
emp_2.pay = 15000


print(emp_1.email)
print(emp_2.email)
'''