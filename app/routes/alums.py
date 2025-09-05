from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Alumnos


alu_bp = Blueprint ('alumnos',__name__)



@alu_bp.route('/')
def index():
    alumnos = Alumnos.query.all()
    return render_template('index.html', alumnos = alumnos)



