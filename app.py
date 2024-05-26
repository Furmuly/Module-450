from flask import Flask, request, render_template
from name_suggestions import suggest_names

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    suggestions = []
    if request.method == "POST":
        user_input = request.form["name_input"]
        suggestions = suggest_names(user_input)
    return render_template("index.html", suggestions=suggestions)

if __name__ == "__main__":
    app.run(debug=True)
