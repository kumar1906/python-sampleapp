from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        print(f"First Name: {first_name}, Last Name: {last_name}")
        return render_template('submit.html', first_name=first_name, last_name=last_name)

if __name__ == '__main__':
    app.run(debug=True)
