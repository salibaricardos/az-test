from flask import Flask, render_template_string, request

app = Flask(__name__)

# Simple homepage route
@app.route("/")
def home():
    return render_template_string("""
        <h1>Welcome to My Flask App 🚀</h1>
        <p>Enter your name below:</p>
        <form action="/greet" method="post">
            <input type="text" name="name" placeholder="Your name" required>
            <button type="submit">Say Hello</button>
        </form>
    """)

# Greeting route
@app.route("/greet", methods=["POST"])
def greet():
    name = request.form.get("name", "Guest")
    return render_template_string(f"""
        <h1>Hello, {name}! 👋</h1>
        <a href="/">Go Back</a>
    """)

if __name__ == "__main__":
    app.run(debug=True)
