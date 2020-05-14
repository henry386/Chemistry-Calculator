# !/usr/bin/env
# -*- coding: utf-8 -*-

from __future__ import print_function
import os
from click._compat import raw_input
from clint.textui import puts, colored
from pyfiglet import Figlet

os.system("clear")  # Linux - OSX
os.system("cls")  # Windows
f = Figlet(font='big')
print(f.renderText("Scientific Calculator"))
a = """


 |-|    *
 |-|   _    *  __
 |-|   |  *    |/'
 |-|   |~*~~~o~|
 |-|   |  O o *|
/___\  |o___O__|
"""

b = """


   1A   2A                                         3A  4A  5A  6A  7A  8A
  -----                                                               -----
1 | H |                                                               |He |
  |---+----                                       --------------------+---|
2 |Li |Be |                                       | B | C | N | O | F |Ne |
  |---+---|                                       |---+---+---+---+---+---|
3 |Na |Mg |3B  4B  5B  6B  7B |    8B     |1B  2B |Al |Si | P | S |Cl |Ar |
  |---+---+---------------------------------------+---+---+---+---+---+---|
4 | K |Ca |Sc |Ti | V |Cr |Mn |Fe |Co |Ni |Cu |Zn |Ga |Ge |As |Se |Br |Kr |
  |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
5 |Rb |Sr | Y |Zr |Nb |Mo |Tc |Ru |Rh |Pd |Ag |Cd |In |Sn |Sb |Te | I |Xe |
  |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
6 |Cs |Ba |LAN|Hf |Ta | W |Re |Os |Ir |Pt |Au |Hg |Tl |Pb |Bi |Po |At |Rn |
  |---+---+---+------------------------------------------------------------
7 |Fr |Ra |ACT|
  ===--------------------------------------------------------------------===
   Lanthanide |La |Ce |Pr |Nd |Pm |Sm |Eu |Gd |Tb |Dy |Ho |Er |Tm |Yb |Lu |
              |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
   Actinide   |Ac |Th |Pa | U |Np |Pu |Am |Cm |Bk |Cf |Es |Fm |Md |No |Lw |
              -------------------------------------------------------------

"""

print(a)
print(b)
puts(colored.red("1. Chemistry"))
puts(colored.red("2. Physics "))
puts(colored.red("3. Biology "))
puts(colored.red("4. Computer Science "))
selection = raw_input("").upper()
if selection == "1":
    os.system("clear")  # Linux - OSX
    os.system("cls")  # Windows
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
elif selection == "2":
    os.system("clear")  # Linux - OSX
    os.system("cls")  # Windows
    f = Figlet(font='big')
    print(f.renderText("Physics Calculator"))
    puts(colored.yellow("1. Power"))
    puts(colored.yellow("2. Voltage"))
    puts(colored.yellow("3. Charge"))
    puts(colored.yellow("4. Energy  VxC"))
    puts(colored.yellow("5. Energy  VxIxt"))
    puts(colored.yellow("6. Total Cost"))
    puts(colored.yellow("7. Efficiency"))
    answer = raw_input("").upper()

    if answer == "1":
        current = raw_input("Enter Current:").upper()
        voltage = raw_input("Enter Voltage:").upper()
        power = float(voltage) * float(current)
        print("Power: ", power, " Watts")

    if answer == "2":
        resistance = raw_input("Enter Resistance:").upper()
        current = raw_input("Enter Current:").upper()
        voltage = float(current) * float(resistance)
        print("Voltage: ", voltage, " Volts")

    if answer == "3":
        time = raw_input("Enter Time:").upper()
        current = raw_input("Enter Current:").upper()
        voltage = float(current) * float(time)
        print("Charge: ", voltage, " Coulombs ")

    if answer == "4":
        voltage = raw_input("Enter Voltage:").upper()
        charge = raw_input("Enter Charge:").upper()
        energy = float(voltage) * float(charge)
        print("Energy: ", energy, " J ")

    if answer == "5":
        voltage = raw_input("Enter Voltage:").upper()
        current = raw_input("Enter Current:").upper()
        time = raw_input("Enter Time:").upper()
        energy = float(voltage) * float(current) * float(time)
        print("Energy: ", energy, " J ")

    if answer == "6":
        num = raw_input("Enter Number of Units:").upper()
        cost = raw_input("Enter Cost of Unit:").upper()
        totcost = float(num) * float(cost)
        print("Total Cost: £", totcost,)

    if answer == "7":
        num = raw_input("Enter Useful Energy Out:").upper()
        cost = raw_input("Enter Total Energy In:").upper()
        efficiency = (float(num) / float(cost)) * 100
        print("Efficiency: ", efficiency, "%")

elif selection == "3":
    os.system("clear")  # Linux - OSX
    os.system("cls")  # Windows
    f = Figlet(font='big')
    print(f.renderText("Biology Calculator"))
    puts(colored.yellow("1. Bit Rate"))
    puts(colored.yellow("2. Voltage"))
    puts(colored.yellow("3. Charge"))
    puts(colored.yellow("4. Energy  VxC"))
    puts(colored.yellow("5. Energy  VxIxt"))
    puts(colored.yellow("6. Total Cost"))
    puts(colored.yellow("7. Efficiency"))
    answer = raw_input("").upper()

elif selection == "4":
    os.system("clear")  # Linux - OSX
    os.system("cls")  # Windows
    f = Figlet(font='big')
    print(f.renderText("Computer Science Calculator"))
