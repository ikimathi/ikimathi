import math

BOX = float(input("Please enter the height of the large box (in inches): "))  #large box
box = float(input("Please enter the height of the small box (in inches): "))  #small box
book_height = float(input("Please enter the height of the books (in inches): "))    #thickness of books
print()
no_of_books = int(input("Please enter the number of books required: "))    #no of books
print()

BOOKS_FIT = math.floor(BOX / book_height)   #books that can fit in one large box
books_fit = math.floor(box / book_height)   #books that can fit in one small box

try:
    no_of_BOXES = math.ceil((no_of_books / BOOKS_FIT))   #no of large boxes required
    no_of_boxes = math.ceil((no_of_books % BOOKS_FIT) / books_fit)  #no of small boxes needed
except ZeroDivisionError as e:  #a ZeroDivisionError is called when book height input is exaggerated
    print(e)
    print("Book height cannot be greater than the boxes. Please try again!")
    quit()

if BOX == 0 and box > 0:    #if the large box is equal to 0 we will package the small ones only

    if BOOKS_FIT < no_of_books and books_fit >= no_of_books:
        if no_of_books % books_fit == 0:
            print("Shipping " + str(no_of_boxes) + " small box(es)")
        else:
            print("Shipping " + str(no_of_boxes) + " box(es)")
            print(str(no_of_BOXES) + " small")

elif box > BOX:
    print("Height of the large box cannot be inferior to the smaller box. Please try again!")
    quit()

else:
    if BOOKS_FIT >= no_of_books:
        print("Shipping 1 large box")

    # elif BOOKS_FIT <= no_of_books: # and no_of_books % BOOKS_FIT <= books_fit and no_of_boxes <= books_fit:
    #     no_of_BOXES -= 1  #no of large boxes required (reverse the ceiling func on ln 20)

    elif BOOKS_FIT <= no_of_books:
        if no_of_books % BOOKS_FIT == 0:
            print("Shipping " + str(no_of_BOXES) + " boxes")
            print(str(no_of_BOXES) + " large")
            # print()
            # print("block 1")

        elif no_of_books % BOOKS_FIT != 0:
            if box < book_height and no_of_books % BOOKS_FIT >= BOOKS_FIT/2:
                print("Shipping " + str(no_of_BOXES) + " boxes")
                print(str(no_of_BOXES) + " large")
                # print()
                # print("block 2")

            elif box >= book_height:
                no_of_BOXES -= 1  #no of large boxes required (reverse the ceiling func)

                print("Shipping " + str(no_of_BOXES + no_of_boxes) + " boxes")
                print(str(no_of_BOXES) + " large")
                print(str(no_of_boxes) + " small")
                # print()
                # print("block 3")

    else:
        print("Something went wrong. Please try again.")
