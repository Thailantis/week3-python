class RentalProperty:
    def __init__(self, rental_income, laundry_income, storage_income, misc_income, tax, insurance, utilities, electricity, water, sewer, garbage, gas, hoa, lawn_snow_care, vacancy, repair, capex, property_management, mortage, downpayment, closing_cost, rehab_budget, misc_cost):
        self.rental_income = rental_income
        self.laundry_income = laundry_income
        self.storage_income = storage_income
        self.misc_income = misc_income
        self.tax = tax
        self.insurance = insurance
        self.utilities = utilities
        self.electricity = electricity
        self.water = water
        self.sewer = sewer
        self.garbage = garbage
        self.gas = gas
        self.hoa = hoa
        self.lawn_snow_care = lawn_snow_care
        self.vacancy = vacancy
        self.repair = repair
        self.capex = capex
        self.property_management = property_management
        self.mortage = mortage
        self.downpayment = downpayment
        self.closing_cost = closing_cost
        self.rehab_budget = rehab_budget
        self.misc_cost = misc_cost
    
    def driver(self):
        rental_income = float(input("Enter monthly rental income: "))
        laundry_income = float(input("Enter monthly laundry income: "))
        storage_income = float(input("Enter monthly storage income: "))
        misc_income = float(input("Enter monthly misc income: "))
        tax = float(input("Enter monthly property tax: "))
        insurance = float(input("Enter monthly insurance cost: "))
        utilities = float(input("Enter monthly utilities cost: "))
        electricity = float(input("Enter monthly electricity cost: "))
        water = float(input("Enter monthly water cost: "))
        sewer = float(input("Enter monthly sewer cost: "))
        garbage = float(input("Enter monthly garbage cost: "))
        gas = float(input("Enter monthly gas cost: "))
        hoa = float(input("Enter monthly HOA fee: "))
        lawn_snow_care = float(input("Enter monthly lawn/snow care cost: "))
        vacancy = float(input("Enter monthly vacancy cost: "))
        repair = float(input("Enter monthly repair cost: "))
        capex = float(input("Enter monthly capital expenditures cost: "))
        property_management = float(input("Enter monthly property_management: "))
        mortage = float(input("Enter monthly mortage payment: "))
        downpayment = float(input("Enter down payment amount: "))
        closing_cost = float(input("Enter closing cost amount: "))
        rehab_budget = float(input("Enter rehab budget amount: "))
        misc_cost =  float(input("Enter miscellaneous cost amount: "))
        return self.driver(rental_income, laundry_income, storage_income, misc_income, tax, insurance, utilities, electricity, water, sewer, garbage, gas, hoa, lawn_snow_care, vacancy, repair, capex, property_management, mortage, downpayment, closing_cost, rehab_budget, misc_cost)
    
    def calculate_total_monthly_income(self):
        return self.rental_income + self.laundry_income + self.storage_income + self.misc_income
    
    def calculate_total_monthly_expenses(self):
        return self.tax + self.insurance + self.utilities + self.electricity + self.water + self.sewer + self.garbage + self.gas + self.hoa + self.lawn_snow_care + self.vacancy + self.repair + self.capex + self.property_management + self.mortage
    
    def calculate_total_monthly_cash_flow(self):
        return self.calculate_total_monthly_income() - self.calculate_total_monthly_expenses()
    
    def calculate_total_annual_cash_flow(self):
        return self.calculate_total_monthly_cash_flow() * 12
    
    def calculate_total_investment(self):
        return self.downpayment + self.closing_cost + self.rehab_budget + self.misc_cost
    
    def calculate_cash_on_cash_roi(self):
        return self.calculate_total_annual_cash_flow() / self.calculate_total_investment()
    
rp = RentalProperty(2000, 1000, 500, 200, 500, 200, 100, 50, 50, 50, 50, 50, 50, 50, 100, 200, 500, 100, 1000, 50000, 10000, 20000, 500)

total_monthly_income = rp.calculate_total_monthly_income()
total_monthly_expenses = rp.calculate_total_monthly_expenses()
total_monthly_cash_flow = rp.calculate_total_monthly_cash_flow()
total_annual_cash_flow = rp.calculate_total_annual_cash_flow()
total_investment = rp.calculate_total_investment()
cash_on_cash_roi = rp.calculate_cash_on_cash_roi()

print("Total Monthly Income: ${:.2f}".format(total_monthly_income))
print("Total Monthly Expenses: ${:.2f}".format(total_monthly_expenses))
print("Total Monthly Cash Flow: ${:,.2f}".format(total_monthly_cash_flow))
print("Total Annual Cash Flow: ${:,.2f}".format(total_annual_cash_flow))
print("Total Investment: ${:,.2f}".format(total_investment))
print("Cash on Cash ROI: {:.2%}".format(cash_on_cash_roi))
