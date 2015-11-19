#!/usr/bin/env python3

""" Graded Lab #4 for Inf1340, Fall 2015

    This program computes federal and provincial sales tax.
    Assume that the provincial sales tax is 5 percent and
    the federal sales tax is 2.5 percent. It displays the
    amount of the purchase, the provincial sales tax, the
    federal sales tax, the total tax, and the total of the
    sale.
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# Rewrite this code to use global constants, local variables and functions
# Output the text to a file instead of printing it

provincial_tax = 0.05
federal_tax = 0.025
total_tax = provincial_tax + federal_tax
total_sale = total_tax + 1


def bill_of_sale(purchase):

    file_name = "sales.txt"

    with open(file_name, 'w') as sales_file:
        sales_file.write("Amount of purchase: {0:.2f}\n".format(purchase))
        sales_file.write("Provincial tax: {0:.2f}\n".format(purchase * .05))
        sales_file.write("Federal tax: {0:.2f}\n".format(purchase * .025))
        sales_file.write("Total tax: {0:.2f}\n".format(purchase * .075))
        sales_file.write("Total sale: {0:.2f}\n".format(purchase * 1.075))


bill_of_sale(50)