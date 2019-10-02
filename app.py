from flask import Flask, render_template, request,make_response, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z12221324\n\xec]/'


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/Mathe/Addition', methods=["GET", "POST"])
def additions_exercise():
    if request.method == "POST":
        result = request.form['result']
        stripped_result = result.strip()
        try:
            int_result = int(stripped_result)
        except ValueError:
            return redirect(url_for("additions_exercise"))
        if int_result == session["result"]:
            return render_template("result.html", result="richtig")
        else:
            return render_template("result.html", result="falsch")
    else:
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)
        session["result"] = num1 + num2
    return render_template("addition.html", aufgabe=f"{num1}+{num2}")


if __name__ == '__main__':
    app.run()
