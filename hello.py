from datetime import datetime  # For timestamping

print("🧠 Welcome to your AI learning log!\n(Type 'exit' at any time to quit)\n")

while True:
    # Name input
    name = input("What's your name? (or type 'exit') ").strip()
    if name.lower() == "exit":
        print("👋 Goodbye! See you next time.")
        break
    if not name or len(name) < 2 or "python" in name.lower():
        print("❗ Invalid name. Please enter a valid name.\n")
        continue
    name = name.title()

    # Age input with validation
    age = input("How old are you? (or type 'exit') ").strip()
    if age.lower() == "exit":
        print("👋 Goodbye! See you next time.")
        break
    if not age.isdigit():
        print("❗ Age must be a number. Please try again.\n")
        continue

    # Goal input
    goal = input("What's your goal today? (or type 'exit') ").strip()
    if goal.lower() == "exit":
        print("👋 Goodbye! See you next time.")
        break
    if not goal or len(goal) < 3:
        print("❗ Please enter a meaningful goal.\n")
        continue

    # Timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save to file in clean format
    with open("user_data.txt", "a") as file:
        file.write(f"[{timestamp}] Name: {name}, Age: {age}, Goal: {goal}\n")

    # Confirm to user
    print("\n✅ Saved:")
    print(f"[{timestamp}] Name: {name}, Age: {age}, Goal: {goal}\n")
