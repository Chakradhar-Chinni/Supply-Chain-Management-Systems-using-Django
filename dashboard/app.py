import os

from flask import Flask

from flask import render_template

from flask import request

from flask sqlalchemy import SQLALchemy
from flask import redirect

project_dir = os.path.dirname(os.path.abspath( file })
database file = "sglite:///{}"
.format(oa.path.join(project dir, “medidatabase.db"}}

app = Flask({ name}
app.config[ "SQLALCHEMY DATABASE_URI"] = database file

db = SQLAlchemy (app)

class Medicine{db.Model):
name = db.Column(db.String(#0), unique=True, nullable="False, primary_key=
True)

def repr (self):
return “<Name: {}>".format(self.name}

@app. routes ”"/", methods=["GET", "FOST"])
def home():
if request.form:
medicine = Medicine(name=request.form.get("name™))
dbesession.add{medicine)
db.session.commit{ )
medicines = Medicine.query.all()
raturn render _template(“home.html", medicines=medicines)