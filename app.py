from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/test'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbkomentar.sqlite3'
app.config['SECRET_KEY'] = 'SFSDFDLdfdjbfmewhebznmsnskdllw0909sd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS '] = False

dbku = SQLAlchemy(app)


class Tamu(dbku.Model):
    idTamu = dbku.Column(dbku.Integer, primary_key=True)
    namaTamu = dbku.Column(dbku.String(50), nullable=False)
    komentar = dbku.Column(dbku.String(255), nullable=False)
    tanggalKomen = dbku.Column(dbku.DateTime, default=datetime.utcnow)
    
    
@app.route('/')
def index():
    # if request.method == 'POST':
    #     komen = request.form['komentar']
    #     komentarbaru = Tamu(namaTamu='linknamaundangan', komentar=komen)
    #     dbku.session.add(komentarbaru)
    #     dbku.session.commit()
    #     return redirect('/')
    tampilkan = Tamu.query.all()
    return render_template('index.html', konten=tampilkan)

@app.route('/<linknamaundangan>/', methods=['GET', 'POST'])
def tamu_undangan(linknamaundangan):
    if request.method == 'POST':
        komen = request.form['komentar']
        komentarbaru = Tamu(namaTamu=linknamaundangan, komentar=komen)
        dbku.session.add(komentarbaru)
        dbku.session.commit()
        return redirect(url_for('index'))
    
    tampilkan = Tamu.query.all()
    return render_template('tamu.html', namaku=linknamaundangan, konten=tampilkan)

# @app.route('/simpan', methods=['GET','POST'])
# def simpan():
#     return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
    