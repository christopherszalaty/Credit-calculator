class Credit_Parameters:
    
    def credit_input_data(self):
        while True:
            try:
                self.investment = float(input("Jaka jest cena nieruchomości, która chcesz kupić? "))
                while True:
                    self.contribution = float(input("Jaki masz wkład własny w PLN? "))
                    if self.contribution < self.investment:
                        break
                    else:
                        print("Wielkość wkładu nie może być większa, niż cena nieruchomości.")
                break
            except ValueError:
                print("Błąd: wprowadź poprawne wartości liczbowe.")
            
    def credit_parameters(self):
        while True:
            try:
                self.interest_rate = float(input("Jaka jest wartość RRSO zaproponowana przez bank w procentach? ").replace(",","."))
                self.credit_period = int(input("Na jaki okres w latach planujesz wziąć kredyt? "))
                break
            except ValueError:
                print("Błąd: wprowadź poprawne wartości liczbowe.")
        
class Rate_Calculator: 
    
    def __init__(self, credit_amount, annual_interest_rate, number_of_years):
        self.credit_amount = credit_amount
        self.annual_interest_rate = annual_interest_rate
        self.number_of_years = number_of_years
        
    def calculate_rate(self):
        r = self.annual_interest_rate/100/12
        n = self.number_of_years * 12
        if r == 0:
            return self.credit_amount / n
        rate = (self.credit_amount * r * (1+r)**n) / ((1+r)**n - 1)
        return round (rate, 2)

class Compare_Period:
    
    def __init__(self, credit_amount, annual_interest_rate):
        self.credit_amount = credit_amount
        self.annual_interest_rate = annual_interest_rate
        
    def new_period(self):
        while True:
            try:
                self.new_credit_period = int(input("Podaj inną długość kredytowania do porównania w latach: "))
                break
            except ValueError:
                print("Błąd: wprowadź poprawne wartości liczbowe.")
        
    def compare_period(self):
        self.new_period()
        new_calculator = Rate_Calculator(self.credit_amount, self.annual_interest_rate, self.new_credit_period)
        self.new_monthly_rate = new_calculator.calculate_rate()
        print(f"Twoja miesięczna rata przy okresie kredytowania {self.new_credit_period} lat wynosi: {self.new_monthly_rate:.2f} PLN.")
        return self.new_credit_period, self.new_monthly_rate
        
class Compare_Interest:
    
    def __init__(self, credit_period, monthly_rate, new_credit_period, new_monthly_rate):
        self.credit_period = credit_period
        self.monthly_rate = monthly_rate
        self.new_credit_period = new_credit_period
        self.new_monthly_rate = new_monthly_rate
        
    def interest_comparasion(self):
        time_difference = abs(self.credit_period - self.new_credit_period)
        if self.new_credit_period < self.credit_period:
            month_profit = self.new_monthly_rate - self.monthly_rate
            overall_profit = self.monthly_rate*12*self.credit_period - self.new_monthly_rate*12*self.new_credit_period 
            print(f"Przy okresie kredytowania {self.new_credit_period} lat, rata kredytu jest wyższa o {month_profit:.2f} niż przy okresie {self.credit_period} lat.")
            print(f"Niemniej, dzięki skróceniu okresu kredytowania o {time_difference:.0f} lat, oszczędzasz {overall_profit:.2f} PLN na odsetkach.")
        else:
            month_loss = self.monthly_rate - self.new_monthly_rate
            overall_loss = self.new_monthly_rate*12*self.new_credit_period - self.monthly_rate*12*self.credit_period
            print(f"Przy okresie kredytowania {self.new_credit_period} lat, rata kredytu jest niższa o {month_loss:.0f} niż przy okresie {self.credit_period} lat.")
            print(f"Niestey, wydłużenie  okresu kredytowania o {time_difference:.0f} lat, do {self.new_credit_period} lat, zwiększa koszt odsetek o {overall_loss:.2f}.")

if __name__ == "__main__":
    param = Credit_Parameters()
    param.credit_input_data()
    param.credit_parameters()

    credit_amount = param.investment - param.contribution
    rate_calc = Rate_Calculator(credit_amount, param.interest_rate, param.credit_period)
    monthly_rate = rate_calc.calculate_rate()
    print(f"Twoja miesięczna rata przy okresie kredytowania {param.credit_period} lat wynosi: {monthly_rate:.2f} PLN.")

    comparison = Compare_Period(credit_amount, param.interest_rate)
    comparison.compare_period()

    profit_comparasion = Compare_Interest(param.credit_period, monthly_rate, comparison.new_credit_period, comparison.new_monthly_rate)
    profit_comparasion.interest_comparasion()

