# !/usr/bin/env
from __future__ import print_function

from click._compat import raw_input
from clint.textui import puts, colored
from pyfiglet import Figlet

f = Figlet(font='big')
print(f.renderText("Chemistry Calculator"))
puts(colored.red("Select Function: "))
puts(colored.yellow("1. Moles"))
puts(colored.yellow("2. Mass"))
puts(colored.yellow("3. Relative Formula Mass"))
puts(colored.yellow("4. Show the equation that links Mass, Moles and RFM"))
puts(colored.yellow("5. Concentration (g/dm3)"))
puts(colored.yellow("6. Mass (c/v)"))
puts(colored.yellow("7. Volume (m/c)"))
puts(colored.yellow("8. Atom Economy"))
puts(colored.yellow("9. Percentage Yield"))
puts(colored.yellow("10. Gradient"))
puts(colored.yellow("11. Uncertainty"))
puts(colored.yellow("12. Gas Volume (dm3)"))
puts(colored.yellow("13. Rate of Reaction"))
puts(colored.yellow("14. RF Value"))

answer = raw_input("").upper()
if answer == "1":
    Mass = raw_input("Enter Mass:").upper()
    RelativeM = raw_input("Enter Relative Formula Mass:").upper()
    moles = float(Mass) / float(RelativeM)
    print("Moles: ", moles)

elif answer == "2":
    moles = raw_input("Enter Moles:").upper()
    RelativeM = raw_input("Enter Relative Formula Mass:").upper()
    mass = float(moles) * float(RelativeM)
    print("Mass: ", mass, "g")

elif answer == "3":
    mass = raw_input("Enter Mass:").upper()
    moles = raw_input("Enter Moles:").upper()
    rfm = float(moles) * float(mass)
    print("Relative Formula Mass: ", rfm)

elif answer == "4":
    print("MOLES * RFM = MASS")

elif answer == "5":
    mass = raw_input("Enter Mass:").upper()
    volume = raw_input("Enter Volume:").upper()
    concentration = float(mass) / float(volume)
    print("Concentration: ", concentration, "g/dm3")

elif answer == "6":
    concentration = raw_input("Enter Concentration:").upper()
    volume = raw_input("Enter Volume:").upper()
    mass = float(concentration) * float(volume)
    print("Mass: ", concentration, "g")

elif answer == "7":
    concentration = raw_input("Enter Concentration:").upper()
    mass = raw_input("Enter Mass:").upper()
    volume = float(concentration) * float(mass)
    print("Volume: ", volume, "dm3")

elif answer == "8":
    umass = raw_input("Enter Useful Mass:").upper()
    mass = raw_input("Enter Total Mass:").upper()
    aeconomy = (float(umass) / float(mass)) * 100
    print("Atom Economy: ", aeconomy, "%")

elif answer == "9":
    eyield = raw_input("Enter Expected Yield:").upper()
    actualyeild = raw_input("Enter Actual Yield:").upper()
    pyield = (float(actualyeild) / float(eyield)) * 100
    print("Percentage Yield: ", pyield, "%")

elif answer == "10":
    step = raw_input("Enter Step:").upper()
    rise = raw_input("Enter Rise:").upper()
    gradient = (float(rise) / float(step)) * 100
    print("Gradient: ", gradient)

elif answer == "11":
    range = raw_input("Enter Range:").upper()
    print("Range: ", float(range) / 2)

elif answer == "12":
    Mass = raw_input("Enter Mass:").upper()
    MolarMass = raw_input("Enter Molar Mass:").upper()
    volume = (float(Mass) / float(MolarMass)) * 24
    print("Volume: ", volume, "dm3")

elif answer == "13":
    Mass = raw_input("Enter Mass increase:").upper()
    time = raw_input("Enter time taken:").upper()
    rate = (float(Mass) / float(time))
    print("Rate of Reaction: ", rate, "g/s")

elif answer == "14":
    Mass = raw_input("Enter Distance traveled by compound:").upper()
    time = raw_input("Distance Traveled by solvent:").upper()
    rate = (float(Mass) / float(time))
    print("RF Value: ", rate)
else:
    print("Error: No Option Selected")

