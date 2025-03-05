from compare_credit_period import Credit_Parameters, Rate_Calculator

uploaded_data = Credit_Parameters()
uploaded_data.credit_input_data()
uploaded_data.credit_parameters()

credit_amount = uploaded_data.investment - uploaded_data.contribution
annual_interest_rate = uploaded_data.interest_rate
credit_period = uploaded_data.credit_period


calculate_uploaded_data = Rate_Calculator(credit_amount, annual_interest_rate, credit_period)
monthly_rate = calculate_uploaded_data.calculate_rate()

print(f"Twoja miesięczna rata wynosi: {monthly_rate:.2f} PLN.")

class Compare_rates:
    
    def __init__(self, credit_amount, annual_interest_rate, credit_period, monthly_rate):
        self.credit_amount = credit_amount
        self.annual_interest_rate = annual_interest_rate
        self.credit_period = credit_period
        self.monthly_rate = monthly_rate
    
    def compare_credit_rates(self):
        while True:
            try:
                self.new_interest_rate = float(input("Podaj inną stopę procentową do porównania: ").replace(",","."))
                break
            except ValueError:
                print("Błąd: wprowadź poprawne wartości liczbowe.")
        
        new_calculator = Rate_Calculator(self.credit_amount, self.new_interest_rate, self.credit_period)
        self.new_monthly_rate = new_calculator.calculate_rate()
        print(f"Twoja miesięczna rata przy stopie procentowej {self.new_interest_rate:.2f}% wynosi: {self.new_monthly_rate:.2f} PLN.")
        return self.new_interest_rate, self.new_monthly_rate
    
class Summary:
    
    def __init__(self, annual_interest_rate, monthly_rate, new_interest_rate, new_monthly_rate, credit_period):
        self.annual_interest_rate= annual_interest_rate
        self.monthly_rate = monthly_rate
        self.new_interest_rate=new_interest_rate
        self.new_monthly_rate = new_monthly_rate
        self.credit_period = credit_period
    
    def rates_summary(self):
        interest_rate_difference = abs(self.annual_interest_rate - self.new_interest_rate) 
        rate_ammount_diff = abs(self.monthly_rate - self.new_monthly_rate)
        overall_cost_diff = abs(self.monthly_rate*12*self.credit_period - self.new_monthly_rate*12*self.credit_period)
        if self.new_interest_rate < self.annual_interest_rate:
            print(f"Przy nowej stopie procentowej {self.new_interest_rate:.2f}% miesięczna rata zmniejszy się o {rate_ammount_diff:.2f} PLN.")
            print(f"Spadek wysokości raty wynika z obniżenia stopy procentowej o {interest_rate_difference:.2f} punktów procentowych.")
            print(f"Dzięki temu oszczędzasz {overall_cost_diff:.2f} PLN na odsetkach")
        else:
            print(f"Przy nowej stopie procentowej {self.new_interest_rate:.2f}% miesięczna rata wzrośnie o {rate_ammount_diff:.2f} PLN.")
            print(f"Wzrost wysokości raty wynika z podniesienia się stopy procentowej o {interest_rate_difference:.2f} punktów procentowych.")
            print(f"Skutkuje to wzrostem kosztów o {overall_cost_diff:.2f} PLN na odsetkach w całym okresie kredytowania.")
            
compare_results = Compare_rates(credit_amount, annual_interest_rate, credit_period, monthly_rate)
compare_results.compare_credit_rates()
rate_results_summary = Summary(
    annual_interest_rate, 
    monthly_rate, 
    compare_results.new_interest_rate, 
    compare_results.new_monthly_rate, 
    credit_period
    )
rate_results_summary.rates_summary()