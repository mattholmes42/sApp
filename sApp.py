#!python
from datetime import date




# ---------------------------Starting Variables-----------------------------
arrest = date(2011, 11, 20)
sobriety = date(2012, 4, 16)
conviction = date(2012, 6, 25)


# -----Prompts user for relapse update---------------
def determine_relapse_number():
    count = 0

    def no_change():
        with open('relapse_data.txt', 'r') as read_file:
            relapses = int(read_file.readline())
            return relapses

    def has_changed():
        with open('relapse_data.txt', 'w') as write_file:
            get_new_count = int(raw_input("Enter number of total times relapsed: "))
            write_file.write('%d' % get_new_count)
            return get_new_count

    while count == 0:
        try:
            has_count_changed = raw_input("Have you had any more relapses since the last time you used this app? Y or N ")
            if has_count_changed == "N" or has_count_changed == "n":
                count = no_change()
            elif has_count_changed != "N" or has_count_changed != "n":
                count = has_changed()
                if not count >= 1:
                    raise ValueError()
        except ValueError:
            print('')
            print('Error: Invalid Option, a number value above zero is required. Program now restarting...')
            print('')
            count = 0

    return count


# -------------------------Calculated Variables--------------------------------
times_relapsed = determine_relapse_number() # Sets variable for number of times the user has relapsed

# Calculated From Date of Arrest
timeFromArrest = (date.today() - arrest).days
monthsFromArrest = timeFromArrest / 30

# Calculated from Sobriety Date
daysFromLastDrink = (date.today() - sobriety).days
daysFromConviction = (date.today() - conviction).days
monthsFromLastDrink = daysFromLastDrink / 30.0
yearsFromLastDrink = daysFromLastDrink / 365.0
totalNightsSober = (daysFromLastDrink - times_relapsed)

# Calculated from Date of Conviction
monthsFromConviction = daysFromConviction / 30


# ----------------------------------Output displayed to user--------------------------------
def data_outputs():
    print ("------------------------------")
    print "Today's date is:", date.today()
    print "Arrested:", arrest
    print "Convicted:", conviction
    print "Sobriety started:", sobriety
    print ("------------------------------")
    print ""
#---------------------------------Output in secondary form----------------------------------
    print ("---------------------------------------------")
    print ("(1). %s            | months since arrest." % monthsFromArrest)
    print ("---------------------------------------------")
    print ("(2). %s            | months since conviction." % monthsFromConviction)
    print ("---------------------------------------------")
    print ("(3). %s          | nights sober." % totalNightsSober)
    print ("---------------------------------------------")
    print ("(4). %s | months sober." %monthsFromLastDrink)
    print ("---------------------------------------------")
    print ("(5). %s | years sober." % yearsFromLastDrink)
    print ("---------------------------------------------")
    print ("")

data_outputs()

raw_input = "press end"
