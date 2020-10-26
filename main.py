from flask import Flask, render_template, request, url_for, flash, redirect, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/nlp")
def hello():
    #return request.args.get("query")
    return jsonify(
        message = request.args.get("query"),
        category1 = "Category1",
        category2 = "Category2",
        category3 = "Category3",
    )

if __name__ == "__main__":
    app.run(debug=True)
