from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data storage (for simplicity, use a database in production)
patients = []
doctors = []

@app.route('/')
def home():
    return render_template('home.html', patients=len(patients), doctors=len(doctors))

@app.route('/patients')
def view_patients():
    return render_template('patients.html', patients=patients)

@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        condition = request.form['condition']
        patients.append({'name': name, 'age': age, 'condition': condition})
        return redirect(url_for('view_patients'))
    return render_template('add_patient.html')

@app.route('/doctors')
def view_doctors():
    return render_template('doctors.html', doctors=doctors)

@app.route('/add_doctor', methods=['GET', 'POST'])
def add_doctor():
    if request.method == 'POST':
        name = request.form['name']
        specialty = request.form['specialty']
        doctors.append({'name': name, 'specialty': specialty})
        return redirect(url_for('view_doctors'))
    return render_template('add_doctor.html')

if __name__ == '__main__':
    app.run(debug=True)