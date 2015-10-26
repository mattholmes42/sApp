#!python
from datetime import date


# ---------------------------Starting Variables-----------------------------
arrest = date(2011, 11, 20)
sobriety = date(2012, 4, 16)
conviction = date(2012, 6, 25)
relapses = 0
read_file = open('relapse_data.txt', 'r')
write_file = open('relapse_data.txt', 'w')


# -----Finds out if the user has relapsed since last use of this app---------------
def determine_relapse_number():
    global relapses
    global read_file
    global write_file

    while relapses == 0:
        relapse_count = 0
        try:
            has_count_changed = raw_input("Have you had any more relapses since the last time you used this app? Y or N ")
            if has_count_changed == "N" or has_count_changed == "n":
                relapse_count = read_file
                relapse_count
                read_file.read()
                read_file.close()

                relapses = relapse_count

            elif has_count_changed != "N" or relapse_count != "n":
                relapse_count = int(raw_input("Enter number of total times relapsed: "))
                write_file
                write_file.write('%d' % relapse_count)
                write_file.close()
                relapses = relapse_count
                if not relapse_count >= 1:
                    raise ValueError()
        except ValueError:
            print('')
            print('Error: Invalid Option, a number value above zero is required. Program now restarting...')
            print('')
            relapses = 0

    return relapses


# -------------------------Calculated Variables--------------------------------
# Sets variable for number of times the user has relapsed
times_relapsed = determine_relapse_number()

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


# ----------------------------------Output to display to user--------------------------------
def data_outputs():
    print ("------------------------------")
    print "Today's date is:", date.today()
    print "Arrested:", arrest
    print "Convicted:", conviction
    print "Sobriety started:", sobriety
    print ("------------------------------")
    print ""
    print "(1). You were arrested %s months ago." % monthsFromArrest
    print ("")
    print "(2). It has been %s months since you were convicted." % monthsFromConviction
    print ("")
    print "(3). You have been sober for %s nights. This equals, roughly, \n%s months or %f years of total sobriety." \
      % (totalNightsSober, monthsFromLastDrink, yearsFromLastDrink)
    print ("")


data_outputs()

raw_input = "press end"
