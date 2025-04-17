from pet import Pet

# Create Fluffy with custom attributes
fluffy = Pet(
    name="Fluffy",
    hunger=3,
    energy=5,
    happiness=10,
    tricks=["rolling over", "jumping high"]
)

# Initial status

fluffy.get_status()
fluffy.show_tricks()

# Perform actions
fluffy.eat()    # Reduces hunger, increases happiness
fluffy.play()   # Changes energy, happiness, hunger
fluffy.sleep()  # Restores energy
fluffy.train("fetch")  # Teaches a new trick

# Final status after activities

fluffy.get_status()
fluffy.show_tricks()