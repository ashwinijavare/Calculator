from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            num1 = int(float(request.form["num1"]))
            num2 = int(float(request.form["num2"]))

            operation = request.form["operation"]

            if operation == "add":
                result = f"{num1} + {num2} = {num1 + num2}"
            elif operation == "subtract":
                result = f"{num1} - {num2} = {num1 - num2}"
            elif operation == "multiply":
                result = f"{num1} * {num2} = {num1 * num2}"
            elif operation == "divide":
                if num2 == 0:
                    result = "Error: Cannot divide by zero."
                else:
                    result = f"{num1} / {num2} = {num1 / num2}"
            else:
                result = "Invalid operation selected."

        except ValueError:
            result = "Please enter valid numbers."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
