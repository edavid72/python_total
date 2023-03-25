seller_name = input("Hello!, What's your name? : ")
sales_month = int(input(f"How much $ did you sell this month, {seller_name} ?"))
commission = sales_month * 13 / 100
print("Wow that's fantastic!")
print('###########################')
print(
    f"Ok,{seller_name} since your sales were ${sales_month} your commission will be ${commission} giving a total on your payment sheet of ${round(sales_month + commission, 2)}")
