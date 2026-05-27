from flask import Flask, render_template, request
import time

app = Flask(__name__)

def function(txt, pat, n, m):
    for i in range(n - m + 1):
        if txt[i:m+i] == pat:
            return i
    return -1

@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    time_taken = None

    if request.method == "POST":

        txt = request.form["txt"]
        pat = request.form["pat"]

        stime = time.time()

        result = function(txt, pat, len(txt), len(pat))

        etime = time.time()

        time_taken = etime - stime

    return render_template(
        "index.html",
        result=result,
        time_taken=time_taken
    )

app = app
