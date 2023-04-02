# 04 Hands-on Activity 1 - ARG    Natanauan, Carlos

# para po macompute ang kinetic energy
def kinetic_energy(m, v):
    ke = 0.5 * m * v**2
    return ke

# loop para itanong na magtatanong sa user ng new input hangang sa mag exit sya huhuhu
while True:
    try:
        # hingin ang masas at velocity 
        mass = float(input("\nEnter mass in kilograms: "))
        velocity = float(input("Enter velocity in meters per second: "))

        # kalkulahin ang kinetic energy gamit ang function
        kin_energy = kinetic_energy(mass, velocity)
        print(f"The object's kinetic energy is: {kin_energy:.2f} J.\n")

    except ValueError:
        # harapin ang error kung maglagay ang user ng hindi tamang input
       print("Invalid input. Mass and velocity must be numbers.")
    finally:
        # hingin sa user kung gusto pa ba niyang enter ulit
        choice = input("Do you want to calculate again? (y/n): ")
        if choice.lower() != 'y':
            print("\n❤------------------------------------------------❤")
            print("❤        Salamat sa paggamit nitong program      ❤")
            print("❤    Your smile is warmer than hydrogen plasma   ❤")
            print("❤                                       - Carlos ❤")
            print("❤------------------------------------------------❤")
            break










