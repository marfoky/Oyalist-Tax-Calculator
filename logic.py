breakdown_array = []


def is_taxable(monthly_income: float) -> tuple:
    non_taxable_amount = 365
    if monthly_income > non_taxable_amount:

        breakdown_array.append({
            'taxable_amount': non_taxable_amount,
            'rate': 0,
            'paid': 0,
        })
        taxable_amount = monthly_income - non_taxable_amount
        return True, taxable_amount
    else:

        breakdown_array.append({
            'taxable_amount': monthly_income,
            'rate': 0,
            'paid': 0,
        })
        return False, non_taxable_amount


def next_110(taxable_amount: float) -> tuple:
    if taxable_amount <= 110:
        rate = (5 / 100) * taxable_amount
        breakdown_array.append({
            'taxable_amount': taxable_amount,
            'paid': rate,
            'rate': 5
        })
        return None, rate
    else:
        rate = (5 / 100) * 110
        next_to_tax = taxable_amount - 110
        breakdown_array.append({
            'taxable_amount': 110,
            'paid': rate,
            'rate': 5
        })
        return next_to_tax, rate


def next_130(next_to_tax: float) -> tuple:
    if next_to_tax <= 130:
        rate = (10 / 100) * next_to_tax
        breakdown_array.append({
            'taxable_amount': next_to_tax,
            'paid': rate,
            'rate': 10
        })
        return None, rate
    else:
        rate = (10 / 100) * 130
        next_to_tax = next_to_tax - 130
        breakdown_array.append({
            'taxable_amount': 130,
            'paid': rate,
            'rate': 10
        })
        return next_to_tax, rate


def next_3000(next_to_tax: float) -> tuple:
    if next_to_tax <= 3000:
        rate = (17.5 / 100) * next_to_tax
        breakdown_array.append({
            'taxable_amount': next_to_tax,
            'paid': rate,
            'rate': 17.50
        })
        return None, rate
    else:
        rate = (17.5 / 100) * 3000
        next_to_tax = next_to_tax - 3000
        breakdown_array.append({
            'taxable_amount': 3000,
            'paid': rate,
            'rate': 17.50
        })
        return next_to_tax, rate


def next_16395(next_to_tax: float) -> tuple:
    if next_to_tax <= 16395:
        rate = (25 / 100) * next_to_tax
        breakdown_array.append({
            'taxable_amount': next_to_tax,
            'paid': rate,
            'rate': 25
        })
        return None, rate
    else:
        rate = (25 / 100) * 16395
        next_to_tax = next_to_tax - 16395
        breakdown_array.append({
            'taxable_amount': 16395,
            'paid': rate,
            'rate': 25
        })
        return next_to_tax, rate


def sum_allowance(car, car_driver, accommodation, furnished_accommodation):
    sum_of_allowances = 0
    if car is not None and True:
        sum_of_allowances += 100
    if car_driver is not None and True:
        sum_of_allowances += 100
    if accommodation is not None and True:
        sum_of_allowances += 100
    if furnished_accommodation is not None and True:
        sum_of_allowances += 100
    return sum_of_allowances


def sum_reliefs(married, unmarried, one, two, three, ):
    sum_of_reliefs = 0
    if married is not None and married:
        sum_of_reliefs += 100
    if unmarried is not None and unmarried:
        sum_of_reliefs += 100
    if one is not None and one:
        sum_of_reliefs += 100
    if two is not None and two:
        sum_of_reliefs += 200
    if three is not None and three:
        sum_of_reliefs += 300
    return sum_of_reliefs


def exceeding_20000(next_to_tax: float) -> float():
    if next_to_tax > 20000:
        rate = (30 / 100) * next_to_tax
        breakdown_array.append({
            'taxable_amount': next_to_tax,
            'paid': rate,
            'rate': 30
        })
        return next_to_tax, rate


def calculate_tax(monthly_income: float, ssnit_inclusive: bool, allowance: float, relief: float, tier_three: float,
                  mortgage_interest: float, bonus: float):
    breakdown_array.clear()
    # SSNIT calculations
    tier_two = (5.5 / 100) * monthly_income
    tier_3 = 0
    if tier_three is not None:
        tier_3 = (tier_three / 100) * monthly_income
        relief += tier_3
    if ssnit_inclusive is not None and ssnit_inclusive:
        monthly_income = monthly_income - tier_two
    if mortgage_interest is not None:
        relief += mortgage_interest
    # Allowance computations
    if allowance is not None:
        allowance_value = (allowance / 100) * monthly_income
        monthly_income = monthly_income + allowance_value
    # Tiers calculation
    tier_1 = monthly_income * 0.135
    tier_2 = monthly_income * 0.05

    tiers = (tier_1, tier_2, tier_3)
    # Reliefs computations
    if relief is not None:
        monthly_income = monthly_income - relief
    # Checking monthly salary and computing tax accordingly
    taxable, tax = is_taxable(monthly_income)
    if taxable is False:
        amount_to_tax = 0
        return amount_to_tax, monthly_income, tier_two, breakdown_array, tiers
    else:
        next_to_tax, rate_110 = next_110(tax)
        take_home = monthly_income - rate_110 - allowance + relief
        if next_to_tax is None:
            return rate_110, take_home, tier_two, breakdown_array, tiers
        else:
            next_to_tax1, rate_130 = next_130(next_to_tax)
            cumulative_rate = rate_110 + rate_130
            take_home = monthly_income - cumulative_rate - allowance + relief
            if next_to_tax1 is None:
                return cumulative_rate, take_home, tier_two, breakdown_array, tiers
            else:
                next_to_tax2, rate_3000 = next_3000(next_to_tax1)
                cumulative_rate = rate_110 + rate_130 + rate_3000
                take_home = monthly_income - cumulative_rate - allowance + relief
                if next_to_tax2 is None:
                    return cumulative_rate, take_home, tier_two, breakdown_array, tiers
                else:
                    next_to_tax3, rate_16395 = next_16395(next_to_tax2)
                    cumulative_rate = rate_110 + rate_130 + rate_3000 + rate_16395
                    take_home = monthly_income - cumulative_rate - allowance + relief
                    if next_to_tax3 is None:
                        return cumulative_rate, take_home, tier_two, breakdown_array, tiers
                    else:
                        next_to_tax4, rate_20000 = exceeding_20000(next_to_tax3)
                        cumulative_rate = rate_110 + rate_130 + rate_3000 + rate_20000
                        take_home = monthly_income - cumulative_rate - allowance + relief
                        return cumulative_rate, take_home, tier_two, breakdown_array, tiers
