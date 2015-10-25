#!python
from datetime import date
import easygui

# ---------------------------Starting Variables-----------------------------
arrest = date(2011, 11, 20)
sobriety = date(2012, 4, 16)
conviction = date(2012, 6, 25)
relapses = 0

def determine_relapse_number():
    global relapses
    read_file = open('relapse_data.txt', 'r')
    write_file = open('relapse_data.txt', 'w')

    while relapses == 0:
        try:
            relapse_count = raw_input("Have you had any more relapses since the last time you used this app? Y or N ")
            if relapse_count == "N" or relapse_count == "n":
                #read_file.read()
                #read_file.close()
                relapses =  4
            elif relapse_count != "N" or relapse_count != "n":
                relapse_count = int(raw_input("Enter number of total times relapsed: "))
                #relapse_write = open('relapse_data.txt', 'w')
                #relapse_write.write(relapse_count)
                #relapse_write.close()
                relapses = relapse_count
                if not relapse_count >= 1:
                    raise ValueError()
        except ValueError:
            print('')
            print('Error: Invalid Option, a number value above zero is required. Program now restarting...')
            print('')
            relapses = 0

    return relapses

times_relapsed = determine_relapse_number()


# -------------------------Calculated Variables--------------------------------

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



# ----------------------------------Outputs--------------------------------

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
print "(3). You have been sober for %s nights. This equals roughly %s months or %f years of total sobriety." \
      % (totalNightsSober, monthsFromLastDrink, yearsFromLastDrink)
print ("")
raw_input = "press end"