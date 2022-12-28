from flask import Flask, render_template, request

from logic import *

app = Flask(__name__)

if __name__ == '__main__':
    app.run()


@app.route('/', methods=['GET', 'POST'])
def home():
    show_breakdown = False
    ssnit_inclusive = False
    if request.method == 'POST':
        monthly_income = request.form.get('monthlyIncome', type=float)
        tier_3 = request.form.get('tier_3', type=float)
        mortgage_interest = request.form.get('mortgage_interest', type=float)
        bonus = request.form.get('bonus', type=float)
        car = request.form.get('Car', type=bool)
        car_driver = request.form.get('Car + Driver', type=bool)
        accommodation = request.form.get('Accommodation', type=bool)
        furnished_accommodation = request.form.get('Furnished Accommodation', type=bool)
        allowance = sum_allowance(car, car_driver, accommodation, furnished_accommodation)
        married = request.form.get('Married', type=bool)
        unmarried = request.form.get('Unmarried', type=bool)
        one = request.form.get('1', type=bool)
        two = request.form.get('2', type=bool)
        three = request.form.get('3', type=bool)
        relief = sum_reliefs(married, unmarried, one, two, three)
        ssnit_inclusive = request.form.get('ssnit_inclusive', type=bool)
        income_tax, take_home, snnit_rate, breakdown_table, tiers = calculate_tax(monthly_income,
                                                                                  ssnit_inclusive,
                                                                                  allowance,
                                                                                  relief,
                                                                                  tier_3,
                                                                                  mortgage_interest,
                                                                                  bonus)
        # print(allowance,relief)
    else:
        take_home = 0
        income_tax = 0
        snnit_rate = 0
        breakdown_table = []
        tiers = ()

    return render_template('index.html',
                           net_income=take_home,
                           income_tax=income_tax,
                           snnit_rate=snnit_rate,
                           ssnit_inclusive=ssnit_inclusive,
                           breakdown_table=breakdown_table,
                           tiers=tiers,
                           show_breakdown=show_breakdown)
