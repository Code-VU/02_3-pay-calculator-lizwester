def calculatePay():
    # Implement your solution in between the two comment blocks
    print("calculating pay")
    # This first line is provided for you
    hrs = int(input("Enter Hours:"))
    rate = float(input("Enter Rate:"))
    grosspay = float(hrs*rate)
    print(grosspay)


    # end assignment


## If you want to test locally before you try to sync
## Open your terminal and run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()
