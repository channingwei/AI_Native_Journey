# Step 1: Greet the user
name = input("Welcome! What's your name? ")
print(f"Hi {name}, great to see you! 😊")

# Step 2: Ask if they built something today
answer = input("Did you build anything today? (yes/no): ").strip().lower()

# Step 3: Respond based on their answer
if answer == "yes":
    print("Awesome! Keep building and growing! 💪")
elif answer == "no":
    print("No worries — go build something right now! 🚀")
else:
    print("Hmm, I didn't understand that. Let's build something anyway! 🔧")
