from pyscript import document,display


nonmetals= {"H": ("Hydrogen", 1, 1.008),
            "He": ("Helium", 2, 4.003),
            "C": ("Carbon", 6, 12.011),
            "N": ("Nitrogen", 7, 14.007),
            "O": ("Oxygen", 8, 15.999),
            "F": ("Fluorine", 9, 18.998),
            "Ne": ("Neon", 10, 20.180),
            "P": ("Phosphorus", 15, 30.974),
            "S": ("Sulfur", 16, 32.06),
            "Cl": ("Chlorine", 17, 35.45),
            "Ar": ("Argon", 18, 39.948),
            "Se": ("Selenium", 34, 78.971),
            "Br": ("Bromine", 35, 79.904),
            "Kr": ("Krypton", 36, 83.798),
            "I": ("Iodine", 53, 126.90),
            "Xe": ("Xenon", 54, 131.29),
            "Rn": ("Radon", 86, 222.02)
            
            }
# assigning the element symbol, atomic number, and atomic mass for

# function to search for a non-metal
def search_nonmetal(e):  
    # Get the value from the input field
    Planet2 = document.getElementById("nonmetal1").value
    # Retrieve information from dictionary
    result = nonmetals.get(Planet2, ("Non-metal not found", "-", "-"))
    # Display the result in HTML
    # Non-metal code, Name, Atomic Number, Atomic Mass
    document.getElementById("name").innerText = result[0]
    document.getElementById("number").innerText = result[1]
    document.getElementById("mass").innerText = result[2]