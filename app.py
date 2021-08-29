from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("form.html")

def main():
    app.run(debug=True)

if __name__=="__main__":
    main()