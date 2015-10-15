#!python
from datetime import date
from PyQt4 import QtGui




# ---------------------------Starting Variables-----------------------------
arrest = date(2011, 11, 20)
sobriety = date(2012, 4, 16)
conviction = date(2012, 6, 25)
relapses = 0


# --------------------------Set Up GUI Environment--------------------------------------
class TimeFromApp(QtGui.QWidget):
    def __init__(self, parent=None):
        super(TimeFromApp, self).__init__(parent)

        self.button = QtGui.QPushButton('Yes', self)

        mainLayout = QtGui.QGridLayout()
        mainLayout.addWidget(self.button, 0, 0)

        self.setLayout(mainLayout)
        self.setWindowTitle("Sobriety App")

        def check_relapse_number(var):
            global relapses
            while relapses == 0:
                  try:
                      relapse_count = raw_input("Have you had any more relapses since the last time you used this app? Y or N ")
                      if relapse_count == "N" or relapse_count == "n":
                          relapse_count = 4
                      elif relapse_count != "N" or relapse_count != "n":
                          relapse_count = int(raw_input("Enter number of total times relapsed: "))
                          if not relapse_count >= 1:
                              raise ValueError()
                  except ValueError:
                      print('')
                      print('Error: Invalid Option, a number value above zero is required. Program now restarting...')
                      print('')
                      relapses = 0
                  else:
                      relapses = relapse_count

            return relapses

        #self.button.clicked.connect(self.handle)

if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)

    soberWidget = TimeFromApp()
    soberWidget.show()

# -------------------------Determine if the relapse count has stayed the same---------------


    sys.exit(app.exec_())


# -------------------------Calculated Variables--------------------------------

# Calculated From Date of Arrest
timeFromArrest = (date.today() - arrest).days
monthsFromArrest = timeFromArrest / 30

# Calculated from Sobriety Date
daysFromLastDrink = (date.today() - sobriety).days
daysFromConviction = (date.today() - conviction).days
monthsFromLastDrink = daysFromLastDrink / 30.0
yearsFromLastDrink = daysFromLastDrink / 365.0
totalNightsSober = (daysFromLastDrink - relapses)
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
