receipt_header = """
    ABC Book Store

    Main street

    City Center
"""
print(receipt_header.upper())
book_title_1 = "Python Basics"
price_1 = 450
book_title_2 = "Data Science Intro"
price_2 = 600

stack = "The price of the book {} is {} and price of the book {} is {}"
print(stack.format(book_title_1, price_1, book_title_2, price_2).upper())

total = price_1 + price_2

print(("Total is:" +str(total)).upper())

str1 = "Thank you"
str2 = "Visit Again"

print((str1 + " " + str2).upper())
