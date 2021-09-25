'''
    2021/2022 Financial Year Australian income tax brackets and tax rates (As of 25/09/2021)
'''

bracket1 = (18200, 0.19)
bracket2 = (45000, 0.325)
bracket3 = (120000, 0.37)
bracket4 = (180000, 0.45)

def income_tax_calculator(x):
    '''
        Calculate income tax
    '''
    if x <= bracket1[0]:
        return 0 
    elif x <= bracket2[0]:
        return (x-bracket1[0])*bracket1[1]
    elif x <= bracket3[0]:
        return (x-bracket2[0])*bracket2[1]+income_tax_calculator(bracket2[0])
    elif x <= bracket4[0]:
        return (x-bracket3[0])*bracket3[1] + income_tax_calculator(bracket3[0])
    else:
        return (x-bracket4[0])*bracket4[1]+ income_tax_calculator(bracket4[0])

def main():
    income = input('Enter taxable income: ')
    while True:
        if income.isnumeric():
            income = int(income)
            break
        income = input('Please enter an valid income: ')

    tax_paid = income_tax_calculator(income)
    net_income = income - tax_paid
    effective_tax_rate = tax_paid/income
    print(f'Tax paid: {tax_paid}')
    print(f'Net income: {net_income}')
    print(f'Effective tax rate: {effective_tax_rate}')

if __name__ == '__main__':
	main()