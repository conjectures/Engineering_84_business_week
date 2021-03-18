import csv
import matplotlib.pyplot as plt

# Graph first plot - Open first file
with open('ex3p2.csv', newline='') as ex3csv:
    # Read as dictionary
    ex3reader = csv.DictReader(ex3csv)
    suppliers = []
    sales = []
    # Get values for each row
    for row in ex3reader:
        suppliers.append(row['CompanyName'])
        sales.append(float(row['Sales'].replace(',', '')))
    # Make plot
    fig, ax = plt.subplots()
    ax.invert_yaxis()
    plt.grid(b=True, axis='x', alpha=0.2)
    plt.title('Supplier Total')
    plt.barh(suppliers, sales)
    plt.gcf().subplots_adjust(left=0.2)
    plt.show()

# Graph second plot
with open('ex3p4.csv', newline='') as ex3csv:
    # Read as dict
    ex3reader = csv.DictReader(ex3csv)
    month = []
    days_to_ship = []
    # Get values for each row
    for row in ex3reader:
        print(row)
        month.append(row['Shipment month'])
        days_to_ship.append(float(row['Days to Ship'].replace(',', '')))

    fig, ax = plt.subplots()
    plt.grid(b=True, axis='y', alpha=0.2)
    plt.title('Average Ship Time By Month')
    plt.plot(month, days_to_ship)
    plt.gcf().subplots_adjust(left=0.2)
    plt.show()

