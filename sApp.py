#!python

from datetime import date
import math


# ---------------------------Starting Variables-----------------------------
arrest = date(2011, 11, 20)
sobriety = date(2012, 4, 16)
conviction = date(2012, 6, 25)


# -----Prompts user for relapse update---------------
def determine_relapse_number():

    get_info = input("Have you relapsed?(INPUT: Y/N or y/n then press ENTER/RETURN):  ")

    def no_change():
        with open('relapse_data.txt', 'r') as read_file:
            count = int(read_file.readline())
            return count

    def has_changed():
        with open('relapse_data.txt', 'w') as write_file:
            count = int(input('Enter number of total times relapsed: '))  # If relapsed prompts user for a number.
            write_file.write(str(count))
            return count

    def relapse_number():
        if get_info == 'Y' or get_info == 'y':
            count = has_changed()
            if count >= 1:
                return count
            else:
                raise ValueError("Sorry Charlie! Try again.")
        else:
            count = no_change()
            return count

    relapses = relapse_number()

    return relapses


# Calculated From Date of Arrest
timeFromArrest = (date.today() - arrest).days
monthsFromArrest = timeFromArrest / 30

# Calculated from Sobriety Date
daysFromLastDrink = (date.today() - sobriety).days
daysFromConviction = (date.today() - conviction).days
monthsFromLastDrink = daysFromLastDrink / 30
yearsFromLastDrink = daysFromLastDrink / 365
totalNightsSober = (daysFromLastDrink - determine_relapse_number())

# Calculated from Date of Conviction
monthsFromConviction = daysFromConviction / 30


# ----------------------------------Output displayed to user--------------------------------
def data_outputs():
    print('------------------------------')
    print("Today's date is:", date.today())
    print('Arrested:', arrest)
    print('Sobriety started:', sobriety)
    print('Convicted:', conviction)
    print('------------------------------')
    print('')
    # ---------------------------------Output in secondary form----------------------------------
    print('----------------------------------------------------------------------------------')
    print('(1). %s           |  months since arrest.' % monthsFromArrest)
    print('---------------------------------|------------------------------------------------')
    print('(2). %s          |  months since conviction.' % monthsFromConviction)
    print('---------------------------------|------------------------------------------------')
    print('(3). %s                        |  nights sober.' % totalNightsSober)
    print('---------------------------------|------------------------------------------------')
    print('(4). %s                        |  months sober.' % monthsFromLastDrink)
    print('---------------------------------|------------------------------------------------')
    print('(5). %s           |  years sober.' % yearsFromLastDrink)
    print('----------------------------------------------------------------------------------')
    print('')
    print("pi =", math.pi)

data_outputs()

exit(0)
