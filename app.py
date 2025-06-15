from flask import Flask, request, render_template_string

visitor_count = 0  # Tracks how many times the page is loaded

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    global visitor_count
    visitor_count += 1

    if request.method == "POST":
        name = request.form["name"].title()
        goal = request.form.get("goal", "(no goal entered)")

        # Save name and goal to a file
        with open("user_log.txt", "a") as file:
            file.write(f"{name} - {goal}\n")

        return render_template_string("""
            <style>
                body { font-family: Arial, sans-serif; text-align: center; margin-top: 60px; }
                h1 { color: #333; }
                p { font-size: 1.2em; }
                a { text-decoration: none; color: #0077cc; }
            </style>
            <h1>Welcome, {{ name }}! 🎉</h1>
            <p>Your goal today: <strong>{{ goal }}</strong></p>
            <p>This is your personal AI learning journey portal.</p>
            <p>👥 Total visitors: {{ count }}</p>
            <a href="/">Back</a>
        """, name=name, goal=goal, count=visitor_count)

    return '''
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 80px; }
            input[type="text"] { padding: 8px; margin: 10px 0; width: 250px; }
            input[type="submit"] { padding: 8px 20px; }
        </style>
        <form method="post">
            <label>What's your name?</label><br>
            <input type="text" name="name"><br><br>
            <label>What is your goal today?</label><br>
            <input type="text" name="goal"><br><br>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == "__main__":
    print("🚀 Flask app is starting...")
    app.run(debug=True)
