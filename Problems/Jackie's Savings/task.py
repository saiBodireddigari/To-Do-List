def final_deposit_amount(*interests, amount=1000):
    tot_amo = amount
    for interest in interests:
        tot_amo *= (1 + interest / 100)
    return round(tot_amo, 2)
