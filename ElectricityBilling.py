def initialDisplay():
    print(f'''   
--------------------------------------------------------------
                Sunway Int'l Electricity Billing    
                        Mitidevi Kathmand
--------------------------------------------------------------
                            ''')


def inputInfo():
    name=input('Enter Customer Name')
    address=input('Enter the Customer address')
    unit = int(input('Enter unit consumed'))
    return name, address, unit


def calculationUnit(unit):
    discount = 0
    totalAmt = 0
    afterDisAmt = 0
    totalDis = 0
    if unit <= 20:
        totalAmt = unit * 4
    elif 20 < unit <= 50:
        totalAmt = (unit - 20) * 7.5 + 20 * 4
    elif 50 < unit <= 150:
        totalAmt = ((unit - 50) * 9.5) + 30 * 7.5 + 20 * 4
        discount = ((unit - 50) * 9.5) * 5 / 100
        totalDis = ((unit - 50) * 9.5) * 5 / 100
        afterDisAmt += totalAmt - discount
    elif 150 < unit <= 250:
        totalAmt = ((unit - 150) * 11.5) + 100 * 9.5 + 30 * 7.5 + 20 * 4
        discount = ((unit - 150) * 11.5) * 10 / 100
        totalDis = ((unit - 150) * 11.5) * 10 / 100 + (100 * 9.5) * 10 / 100
        afterDisAmt = totalAmt - totalDis
    elif 250 < unit:
        totalAmt = ((unit - 250) * 13.5) + 100 * 11.5 + 100 * 9.5 + 30 * 7.5 + 20 * 4
        discount = ((unit - 250) * 13.5) * 15 / 100
        totalDis = ((unit - 250) * 13.5) * 15 / 100 + (100 * 11.5) * 10 / 100 + (100 * 9.5) * 5 / 100
        afterDisAmt = totalAmt - totalDis

    return totalAmt, discount, totalDis, afterDisAmt

initialDisplay()
name, address, unit = inputInfo()
totalAmt, discount, totalDis, afterDisAmt = calculationUnit(unit)

def output(totalAmt, discount, totalDis, afterDisAmt, name, address, unit):
    print(f''' 
    Customer name: {name}                   Customer Address: {address}
    Consumed unit: {unit}
    Payable Amount: {totalAmt}              Total Discount: {totalDis}
    Payable Amount after discount: {afterDisAmt}
     ''')
initialDisplay()
output(totalAmt, discount, totalDis, afterDisAmt, name, address, unit)
