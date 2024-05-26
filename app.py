from flask import Flask, request, render_template
from name_suggestions import suggest_names

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name_input = request.form["name_input"]
        suggestions = suggest_names(name_input)
        return render_template("index.html", suggestions=suggestions)
    return render_template("index.html", suggestions=[])


if __name__ == "__main__":
    app.run(debug=True)
