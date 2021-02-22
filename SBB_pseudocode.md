*import math library*

<!-- ##H2 -->
<h3><u>VARIABLE DECLARATION: </u></h3>

Get input BOX, box, book_height, no_of_books (all in inches)

Set BOOKS_FIT = BOX / book_height   
Set books_fit = box / book_height

Round down both (BOOKS_FIT and books_fit)

Set no_of_BOXES = math.ceil((no_of_books / BOOKS_FIT))

Set no_of_boxes = math.ceil((no_of_books % BOOKS_FIT) / books_fit) 

<hr>

<h3><u>PROGRAM START: </u></h3><b>
try {

    Calculate no_of_BOXES and no_of_boxes:
        no_of_BOXES = math.ceil((no_of_books / BOOKS_FIT))
        no_of_boxes = math.ceil((no_of_books % BOOKS_FIT) / books_fit) 
} <br>

except (ZeroDivisionError as e) {

    print e 
    print "Book height cannot be greater than the boxes. Please try again!"
}
<hr>

if (BOX is equal to 0) && (box is greater than 0) {

    if (BOOKS_FIT is less than no_of_books) & (books_fit is greater than or equal to no_of_books)

        {
            if no_of_books % books_fit == 0 {
                print "Shipping " + no_of_boxes + " small box(es)"
            }

            else {
                print "Shipping " + no_of_boxes + " box(es)"
                print no_of_BOXES + " small"
            }
        }

}


if box is greater than BOX

    {
        print "Height of the large box cannot be inferior to the smaller box. Please try again!"
        terminate program
    }


else {

    if BOOKS_FIT is greater than or equal to no_of_books

        {
            print "Shipping 1 large box"
        }

    else if BOOKS_FIT is less than or equal to no_of_books {

        if no_of_books % BOOKS_FIT is equal to 0
        
            {
                print "Shipping " + no_of_BOXES + " boxes"
                print no_of_BOXES + " large"
            }

        else if (no_of_books % BOOKS_FIT) is not equal to 0:

            {

                if (box is less than book_height) && (no_of_books % BOOKS_FIT >= BOOKS_FIT/2)

                    {
                        print "Shipping " + no_of_BOXES + " boxes"
                        print no_of_BOXES + " large"
                    }

                else if box is greater than or equal to book_height:

                    {
                        no_of_BOXES = no_of_BOXES -1

                        print "Shipping " + (no_of_BOXES + no_of_boxes) + " boxes"
                        print no_of_BOXES + " large"
                        print no_of_boxes + " small"
                    }
            }
        }
    }

    else {

        print "Something went wrong. Please try again."
    }
}



N.B:
- All inputs are in inches except for the number of books input.
- Uppercase variables are variables related to the larger box, NOT NECESSARILY constants.
- 'and' operator is represented as &&.
- 'modulus' operator is represented as %.