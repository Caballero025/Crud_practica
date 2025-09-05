from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Alumnos


alu_bp = Blueprint ('alumnos',__name__)



@alu_bp.route('/')
def index():
    alumnos = Alumnos.query.all()
    return render_template('index.html', alumnos = alumnos)


@alu_bp.route('/new',methods=['GET','POST'])
def create_alumno():
     if request.method == 'POST':
         #Agregar Alumno 
         no_control = request.form['no_control']
         nombre = request.form['nombre']
         ap_paterno = request.form['ap_paterno']
         ap_materno = request.form['ap_materno']
         semestre = request.form['semestre']

         nvo_alumno = Alumnos(no_control = no_control, nombre = nombre,ap_paterno = ap_paterno, ap_materno = ap_materno, semestre = semestre)

         db.session.add(nvo_alumno)
         db.session.commit()
         return redirect(url_for('alumnos.index'))
     #Aqui sigue si es GET
     return render_template('create_alumno.html')
