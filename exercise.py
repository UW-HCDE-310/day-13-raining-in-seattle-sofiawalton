from flask import Flask
import urllib.request
app= Flask(__name__)
@app.route('/')
def index():
    try:
        with urllib.request.urlopen('https://depts.washington.edu/ledlab/teaching/is-it-raining-in-seattle/') as response:
            is_it_raining_in_seattle = response.read().decode()

        if is_it_raining_in_seattle == "true":
            return"Yes"
        else:
            return"No"
    except Exception as e:
        return "e"
if __name__ == '__main__':
    app.run(debug=True)
