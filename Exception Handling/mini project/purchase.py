# You had saved the items and their pricedetails in a text file,which you purchased yesterday from a nearby super market. You need to know:
# 1.How many items did you purchase?
# 2.How many itemsarefree?
# 3.What is the total amount you had to pay?
# 4.What is the discount amount?
# 5.What is the final amount did you payafter the discount?
# Help yourself by writing a python code to do this.Include necessary code to handle the possible exceptions.Note:Data is stored in a text file Purchase-1.txt.
# Each line contains oneitem’s details.Item name and price isseparated by a space.You have to enter the file name during run time.
# Sample input1:Purchase-1.txtChocolate 50Biscuit 35 Icecream 50(blank line)Discount 5
# Sample output 1:Enter the file name:Purchase-1No of items purchased:3No of free items:0Amount to pay:135Discount given:5Final amount paid: 130
# Sample input2:Purchase-1.txtChocolate 50Biscuit 35Icecream 50Rice 100Chicken 250(blank line)Perfume FreeSoup Free(blank line)Discount 80 
# Sample output 2:Enter the file name:Purchase-1No of items purchased:5No of free items:2Amount to pay:485Discount given:80Final amount paid: 405



try:
    name=input('Enter file name : ')
    file=open(f'Exception Handling\mini project\{name}','r')
    items_purchased = 0
    free_items = 0
    total_amount = 0
    discount = 0

    for line in file:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) == 2:
            item, price = parts
            if price.lower() == 'free':
                free_items += 1
            elif item.lower() == 'discount':
                try:
                    discount = int(price)
                except ValueError:
                    print(f"Invalid discount value: {price}")
            else:
                try:
                    total_amount += int(price)
                    items_purchased += 1
                except ValueError:
                    print(f"Invalid price for item {item}: {price}")
        else:
            print(f"Invalid line format: {line}")

    file.close()
    print(f"No of items purchased:{items_purchased}")
    print(f"No of free items:{free_items}")
    print(f"Amount to pay:{total_amount}")
    print(f"Discount given:{discount}")
    print(f"Final amount paid: {total_amount - discount}")

except FileNotFoundError:
    print("File not found. Please check the file name and path.")
except Exception as e:
    print(f"An error occurred: {e}")