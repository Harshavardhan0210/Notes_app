from flask import Flask, render_template , redirect ,request
app = Flask(__name__)
@app.route('/')
def home():
    try:
        with open('notes.txt','r') as f:
            notes = f.readlines()
    except:
        notes = []

    return render_template('index.html',notes=notes)

@app.route('/add',methods=['POST'])
def add():
    note =request.form['note']

    with open('notes.txt','a') as f:
        f.write(note+"\n")

    return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
    with open('notes.txt','r') as f:
        notes = f.readlines()

    notes.pop(index)

    with open('notes.txt','w') as f:
        f.writelines(notes)
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)        