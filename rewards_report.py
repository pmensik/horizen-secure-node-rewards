from get_data import get_lastmonth, get_total, get_usdprice

musd = round(get_lastmonth() * get_usdprice(), 2)
tusd = round(get_total() * get_usdprice(), 2)

print("Last month reward:".ljust(20), str(get_lastmonth()).rjust(6), "ZEN ...", str(musd).rjust(10), "USD")
print("Total reward:".ljust(20), str(get_total()).rjust(6), "ZEN ...", str(tusd).rjust(10), "USD")


