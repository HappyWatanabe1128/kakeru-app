from flask import Flask, render_template, request

app = Flask(__name__)

# お題を固定で用意（例）
question = "I ___ to Tokai junior high school every day."

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        answer = request.form.get("answer", "")
        # 簡単な正誤判定（正解は "go" とする例）
        if answer.strip().lower() == "go":
            result = "Correct!"
        else:
            result = "Try again."
    return render_template("index.html", question=question, result=result)

if __name__ == "__main__":
    app.run(debug=True)

