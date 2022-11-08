from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

@app.route('/')
def index():
   return render_template("index.html")

# Crud del Area
@app.route('/area')
def area():
   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh' )
   cursor = conn.cursor()
   cursor.execute('select idArea, descripcion from area order by idArea')
   datos = cursor.fetchall()
   return render_template("area.html", area = datos)

@app.route('/a_editar/<string:id>')
def area_editar(id):
   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
   cursor = conn.cursor()
   cursor.execute('select idArea, descripcion from area where idArea = %s', (id))
   dato = cursor.fetchall()
   return render_template("area_edi.html", area=dato[0])

@app.route('/area_fed/<string:id>',methods=['POST'])
def area_fedita(id):
   if request.method == 'POST':
       desc=request.form['descripcion']
       conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
       cursor = conn.cursor()
       cursor.execute('update area set descripcion=%s where idArea=%s', (desc,id))
       conn.commit()
       return redirect(url_for('area'))

@app.route('/a_borrar/<string:id>')
def area_borrar(id):
   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
   cursor = conn.cursor()
   cursor.execute('delete from area where idArea = {0}'.format(id))
   conn.commit()
   return redirect(url_for('area'))

@app.route('/area_agregar')
def area_agregar():
   return render_template("area_agr.html")

@app.route('/area_fagr', methods=['POST'])
def area_fagrega():
   if request.method == 'POST':
       desc = request.form['descripcion']
       conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh' )
       cursor = conn.cursor()
       cursor.execute('insert into area (descripcion) values (%s)',(desc))
       conn.commit()
       return redirect(url_for('area'))

# Crud del Carrera
@app.route('/carrera')
def carrera():
   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh' )
   cursor = conn.cursor()
   cursor.execute('select idCarrera, descripcion from carrera order by idCarrera')
   datos = cursor.fetchall()
   return render_template("carrera.html", area = datos)

@app.route('/c_editar/<string:id>')
def carrera_editar(id):
   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
   cursor = conn.cursor()
   cursor.execute('select idCarrera, descripcion from carrera where idCarrera = %s', (id))
   dato = cursor.fetchall()
   return render_template("carrera_edi.html", carrera=dato[0])

@app.route('/carrera_fed/<string:id>',methods=['POST'])
def carrera_fedita(id):
   if request.method == 'POST':
       desc=request.form['descripcion']
       conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
       cursor = conn.cursor()
       cursor.execute('update carrera set descripcion=%s where idCarrera=%s', (desc,id))
       conn.commit()
       return redirect(url_for('carrera'))

@app.route('/c_borrar/<string:id>')
def carrera_borrar(id):
   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
   cursor = conn.cursor()
   cursor.execute('delete from carrera where idCarrera = {0}'.format(id))
   conn.commit()
   return redirect(url_for('carrera'))

@app.route('/carrera_agregar')
def carrera_agregar():
   return render_template("carrera_agr.html")

@app.route('/carrera_fagr', methods=['POST'])
def carrera_fagrega():
   if request.method == 'POST':
       desc = request.form['descripcion']
       conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh' )
       cursor = conn.cursor()
       cursor.execute('insert into carrera (descripcion) values (%s)',(desc))
       conn.commit()
       return redirect(url_for('carrera'))

# Crud del Escolaridad
@app.route('/escolaridad')
def escolaridad():
   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh' )
   cursor = conn.cursor()
   cursor.execute('select idEscolaridad, descripcion from escolaridad order by idEscolaridad')
   datos = cursor.fetchall()
   return render_template("escolaridad.html", escolaridad = datos)

@app.route('/e_editar/<string:id>')
def escolaridad_editar(id):
   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
   cursor = conn.cursor()
   cursor.execute('select idEscolaridad, descripcion from escolaridad where idEscolaridad = %s', (id))
   dato = cursor.fetchall()
   return render_template("escolaridad_edi.html", escolaridad=dato[0])

@app.route('/escolaridad_fed/<string:id>',methods=['POST'])
def escolaridad_fedita(id):
   if request.method == 'POST':
       desc=request.form['descripcion']
       conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
       cursor = conn.cursor()
       cursor.execute('update escolaridad set descripcion=%s where idEscolaridad=%s', (desc,id))
       conn.commit()
       return redirect(url_for('escolaridad'))

@app.route('/e_borrar/<string:id>')
def escolaridad_borrar(id):
   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
   cursor = conn.cursor()
   cursor.execute('delete from escolaridad where idEscolaridad = {0}'.format(id))
   conn.commit()
   return redirect(url_for('escolaridad'))

@app.route('/escolaridad_agregar')
def escolaridad_agregar():
   return render_template("escolaridad_agr.html")

@app.route('/escolaridad_fagr', methods=['POST'])
def escolaridad_fagrega():
   if request.method == 'POST':
       desc = request.form['descripcion']
       conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh' )
       cursor = conn.cursor()
       cursor.execute('insert into escolaridad (descripcion) values (%s)',(desc))
       conn.commit()
       return redirect(url_for('escolaridad'))

# Crud del Estado Civil
@app.route('/estadoCivil')
def EstadoCivil():
   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh' )
   cursor = conn.cursor()
   cursor.execute('select idEstado, descripcion from estadocivil order by idEstado')
   datos = cursor.fetchall()
   return render_template("EstadoCivil.html", EstadoCivil = datos)

@app.route('/eC_editar/<string:id>')
def EstadoCivil_editar(id):
   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
   cursor = conn.cursor()
   cursor.execute('select idEstado, descripcion from estadocivil where idEstado = %s', (id))
   dato = cursor.fetchall()
   return render_template("EstadoCivil_edi.html", estadocivil=dato[0])

@app.route('/estadoCivil_fed/<string:id>',methods=['POST'])
def EstadoCivil_fedita(id):
   if request.method == 'POST':
       desc=request.form['descripcion']
       conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
       cursor = conn.cursor()
       cursor.execute('update estadocivil set descripcion=%s where idEstado=%s', (desc,id))
       conn.commit()
       return redirect(url_for('EstadoCivil'))

@app.route('/eC_borrar/<string:id>')
def EstadoCivil_borrar(id):
   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
   cursor = conn.cursor()
   cursor.execute('delete from estadocivil where idEstado = {0}'.format(id))
   conn.commit()
   return redirect(url_for('EstadoCivil'))

@app.route('/EstadoCivil_agregar')
def EstadoCivil_agregar():
   return render_template("EstadoCivil_agr.html")

@app.route('/EstadoCivil_fagr', methods=['POST'])
def EstadoCivil_fagrega():
   if request.method == 'POST':
       desc = request.form['descripcion']
       conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh' )
       cursor = conn.cursor()
       cursor.execute('insert into estadocivil (descripcion) values (%s)',(desc))
       conn.commit()
       return redirect(url_for('EstadoCivil'))

# Crud del Grado de Avance
@app.route('/gradoAvance')
def gradoAvance():
   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh' )
   cursor = conn.cursor()
   cursor.execute('select idAvance, descripcion from gradoavance order by idAvance')
   datos = cursor.fetchall()
   return render_template("gradoAvance.html", gradoavance = datos)

@app.route('/gA_editar/<string:id>')
def gradoAvance_editar(id):
   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
   cursor = conn.cursor()
   cursor.execute('select idAvance, descripcion from gradoavance where idAvance = %s', (id))
   dato = cursor.fetchall()
   return render_template("gradoA_edi.html", gradoavance=dato[0])

@app.route('/gradoA_fed/<string:id>',methods=['POST'])
def gradoAvance_fedita(id):
   if request.method == 'POST':
       desc=request.form['descripcion']
       conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
       cursor = conn.cursor()
       cursor.execute('update gradoavance set descripcion=%s where idAvance=%s', (desc,id))
       conn.commit()
       return redirect(url_for('gradoAvance'))

@app.route('/gA_borrar/<string:id>')
def gradoAvance_borrar(id):
   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
   cursor = conn.cursor()
   cursor.execute('delete from gradoavance where idAvance = {0}'.format(id))
   conn.commit()
   return redirect(url_for('gradoAvance'))

@app.route('/gradoA_agregar')
def gradoAvance_agregar():
   return render_template("gradoA_agr.html")

@app.route('/gradoA_fagr', methods=['POST'])
def gradoAvance_fagrega():
   if request.method == 'POST':
       desc = request.form['descripcion']
       conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh' )
       cursor = conn.cursor()
       cursor.execute('insert into gradoavance (descripcion) values (%s)',(desc))
       conn.commit()
       return redirect(url_for('gradoAvance'))

# Crud de Habilidades
@app.route('/habilidad')
def habilidad():
   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh' )
   cursor = conn.cursor()
   cursor.execute('select idHabilidad, descripcion from habilidad order by idHabilidad')
   datos = cursor.fetchall()
   return render_template("habilidad.html", habilidades = datos)

@app.route('/h_editar/<string:id>')
def habilidad_editar(id):
   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
   cursor = conn.cursor()
   cursor.execute('select idHabilidad, descripcion from habilidad where idHabilidad = %s', (id))
   dato = cursor.fetchall()
   return render_template("habilidades_edi.html", habilidades=dato[0])

@app.route('/habilidades_fed/<string:id>',methods=['POST'])
def habilidad_fedita(id):
   if request.method == 'POST':
       desc=request.form['descripcion']
       conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
       cursor = conn.cursor()
       cursor.execute('update habilidad set descripcion=%s where idHabilidad=%s', (desc,id))
       conn.commit()
       return redirect(url_for('habilidad'))

@app.route('/h_borrar/<string:id>')
def habilidad_borrar(id):
   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
   cursor = conn.cursor()
   cursor.execute('delete from habilidad where idHabilidad = {0}'.format(id))
   conn.commit()
   return redirect(url_for('habilidad'))

@app.route('/habilidades_agregar')
def habilidad_agregar():
   return render_template("habilidad_agr.html")

@app.route('/habilidad_fagr', methods=['POST'])
def habilidad_fagrega():
   if request.method == 'POST':
       desc = request.form['descripcion']
       conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh' )
       cursor = conn.cursor()
       cursor.execute('insert into habilidad (descripcion) values (%s)',(desc))
       conn.commit()
       return redirect(url_for('habilidad'))


# Crud de Idiomas
@app.route('/idioma')
def idioma():
   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh' )
   cursor = conn.cursor()
   cursor.execute('select idIdioma, descripcion from idiomas order by idIdioma')
   datos = cursor.fetchall()
   return render_template("idioma.html", idioma = datos)

@app.route('/id_editar/<string:id>')
def idioma_editar(id):
   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
   cursor = conn.cursor()
   cursor.execute('select idIdioma, descripcion from idiomas where idIdioma = %s', (id))
   dato = cursor.fetchall()
   return render_template("idiomas_edi.html", idioma=dato[0])

@app.route('/idioma_fed/<string:id>',methods=['POST'])
def idioma_fedita(id):
   if request.method == 'POST':
       desc=request.form['descripcion']
       conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
       cursor = conn.cursor()
       cursor.execute('update idiomas set descripcion=%s where idIdioma =%s', (desc,id))
       conn.commit()
       return redirect(url_for('idioma'))

@app.route('/id_borrar/<string:id>')
def idioma_borrar(id):
   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
   cursor = conn.cursor()
   cursor.execute('delete from idiomas where idIdioma = {0}'.format(id))
   conn.commit()
   return redirect(url_for('idioma'))

@app.route('/idioma_agregar')
def idioma_agregar():
   return render_template("idiomas_agr.html")

@app.route('/idioma_fagr', methods=['POST'])
def idioma_fagrega():
   if request.method == 'POST':
       desc = request.form['descripcion']
       conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh' )
       cursor = conn.cursor()
       cursor.execute('insert into idiomas (descripcion) values (%s)',(desc))
       conn.commit()
       return redirect(url_for('idioma'))

# Crud de Medio de Publicidad
@app.route('/medioPublic')
def medioPublic():
   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh' )
   cursor = conn.cursor()
   cursor.execute('select idMedioP, descripcion from mediopublicidad order by idMedioP')
   datos = cursor.fetchall()
   return render_template("medioPublic.html", mediopublicidad = datos)

@app.route('/mp_editar/<string:id>')
def medioPublic_editar(id):
   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
   cursor = conn.cursor()
   cursor.execute('select idMedioP, descripcion from mediopublicidad where idMedioP = %s', (id))
   dato = cursor.fetchall()
   return render_template("medioP_edi.html", mediopublicidad =dato[0])

@app.route('/mp_fed/<string:id>',methods=['POST'])
def medioPublic_fedita(id):
   if request.method == 'POST':
       desc=request.form['descripcion']
       conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
       cursor = conn.cursor()
       cursor.execute('update mediopublicidad set descripcion=%s where idMedioP=%s', (desc,id))
       conn.commit()
       return redirect(url_for('medioPublic'))

@app.route('/mp_borrar/<string:id>')
def medioPublic_borrar(id):
   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
   cursor = conn.cursor()
   cursor.execute('delete from mediopublicidad where idMedioP = {0}'.format(id))
   conn.commit()
   return redirect(url_for('medioPublic'))

@app.route('/medioPu_agregar')
def medioPublic_agregar():
   return render_template("medioP_agr.html")

@app.route('/mp_fagr', methods=['POST'])
def medioPublic_fagrega():
   if request.method == 'POST':
       desc = request.form['descripcion']
       conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh' )
       cursor = conn.cursor()
       cursor.execute('insert into mediopublicidad (descripcion) values (%s)',(desc))
       conn.commit()
       return redirect(url_for('medioPublic'))

# Crud del Puesto

@app.route('/puesto')
def puesto():
   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh' )
   cursor = conn.cursor()
   cursor.execute('select idPuesto, nomPuesto from puesto order by idPuesto')
   datos = cursor.fetchall()
   return render_template("puesto.html", pue=datos, dat=' ', catArea=' ', catEdoCivil=' ', catEscolaridad=' ', catGradoAvance=' ', catCarrera=' ', catIdioma=' ', catHabilidad=' ')

@app.route('/puesto_fdetalle/<string:idP>', methods=['GET'])
def puesto_fdetalle(idP):
   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
   cursor = conn.cursor()
   cursor.execute('select idPuesto, nomPuesto from puesto order by idPuesto')
   datos = cursor.fetchall()
   cursor.execute('select idPuesto,codPuesto,idArea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,''funciones,edad,sexo,idEstadoCivil,idEscolaridad,idGradoAvance,idCarrera,experiencia,conocimientos,manejoEquipo,''reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo from puesto where idPuesto = %s', (idP))
   dato = cursor.fetchall()

   cursor.execute('select a.idArea, a.descripcion from area a, puesto b where a.idArea = b.idArea and b.idPuesto = %s', (idP))

   datos1 = cursor.fetchall()
   cursor.execute('select a.idEstado, a.descripcion from estadocivil a, puesto b where a.idEstado = b.idEstadoCivil and b.idPuesto = %s', (idP))
   datos2 = cursor.fetchall()
   cursor.execute('select a.idEscolaridad, a.descripcion from escolaridad a, puesto b where a.idEscolaridad = b.idEscolaridad and b.idPuesto = %s', (idP))
   datos3 = cursor.fetchall()
   cursor.execute('select a.idAvance, a.descripcion from gradoavance a, puesto b where a.idAvance = b.idGradoAvance and b.idPuesto = %s', (idP))
   datos4 = cursor.fetchall()
   cursor.execute('select a.idCarrera, a.descripcion from carrera a, puesto b where a.idCarrera = b.idCarrera and b.idPuesto = %s', (idP))
   datos5 = cursor.fetchall()
   cursor.execute('select a.idPuesto, b.idIdioma, b.descripcion from puesto a, idiomas b, puesto_has_idiomas c ''where a.idPuesto = c.idPuesto and b.idIdioma = c.idIdioma and a.idPuesto = %s',(idP))
   datos6 = cursor.fetchall()
   cursor.execute('select a.idPuesto, b.idHabilidad, b.descripcion from puesto a, habilidad b, puesto_has_habilidad c ''where a.idPuesto = c.idPuesto and b.idHabilidad = c.idHabilidad and a.idPuesto = %s', (idP))
   datos7 = cursor.fetchall()
   print(datos)
   return render_template("puesto.html", pue=datos , dat=dato[0], catArea=datos1[0],catEdoCivil=datos2[0], catEscolaridad=datos3[0],catGradoAvance=datos4[0], catCarrera=datos5[0], catIdioma=datos6,catHabilidad=datos7)

@app.route('/puesto_borrar/<string:idP>')
def puesto_borrar(idP):
   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
   cursor = conn.cursor()
   cursor.execute('delete from puesto where idPuesto = %s',(idP))
   conn.commit()
   cursor.execute('delete from puesto_has_habilidad where idPuesto =%s ', (idP))
   conn.commit()
   cursor.execute('delete from puesto_has_idiomas where idPuesto =%s ', (idP))
   conn.commit()
   return redirect(url_for('puesto'))

@app.route('/puesto_agregar')
def puesto_agregar():
   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
   cursor = conn.cursor()

   cursor.execute('select idArea, descripcion from area ')
   datos1 = cursor.fetchall()
   cursor.execute('select idEstado, descripcion from estadocivil ')
   datos2 = cursor.fetchall()
   cursor.execute('select idEscolaridad, descripcion from escolaridad ')
   datos3 = cursor.fetchall()
   cursor.execute('select idAvance, descripcion from gradoavance ')
   datos4 = cursor.fetchall()
   cursor.execute('select idCarrera, descripcion from carrera ')
   datos5 = cursor.fetchall()
   cursor.execute('select idIdioma, descripcion from idiomas ')
   datos6 = cursor.fetchall()
   cursor.execute('select idHabilidad, descripcion from habilidad ')
   datos7 = cursor.fetchall()
   return render_template("puesto_agr.html", catArea=datos1, catEdoCivil=datos2,
   catEscolaridad=datos3, catGradoAvance=datos4, catCarrera=datos5, catIdioma=datos6,
   catHabilidad=datos7)

@app.route('/puesto_fagrega', methods=['POST'])
def puesto_fagrega():
   if request.method == 'POST':
       if 'idArea' in request.form:
           idAr = request.form['idArea']
       else:
           idAr = '1'
       if 'idEstado' in request.form:
           idEC = request.form['idEstado']
       else:
           idEC = '1'
       if 'idEscolaridad' in request.form:
           idEs = request.form['idEscolaridad']
       else:
           idEs = '1'
       if 'idAvance' in request.form:
           idGA = request.form['idAvance']
       else:
           idGA = '1'
       if 'idCarrera' in request.form:
           idCa = request.form['idCarrera']
       else:
           idCa = '1'
       if 'sexo' in request.form:
           sex = request.form['sexo']
       else:
           sex = '1'
       codP = request.form['codPuesto']

       nomP = request.form['nomPuesto']
       pueJ = request.form['puestoJefeSup']
       jorn = request.form['jornada']
       remu = request.form['remunMensual']
       pres = request.form['prestaciones']
       desc = request.form['descripcionGeneral']
       func = request.form['funciones']
       eda = request.form['edad']
       expe = request.form['experiencia']
       cono = request.form['conocimientos']
       manE = request.form['manejoEquipo']
       reqF = request.form['reqFisicos']
       reqP = request.form['reqPsicologicos']
       resp = request.form['responsabilidades']
       conT = request.form['condicionesTrabajo']

   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
   cursor = conn.cursor()
   cursor.execute('insert into puesto (codPuesto,idArea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,''funciones,edad,sexo,idEstadoCivil,idEscolaridad,idGradoAvance,idCarrera,experiencia,conocimientos,manejoEquipo,''reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(codP, idAr, nomP, pueJ, jorn, remu, pres, desc, func, eda, sex, idEC, idEs, idGA, idCa, expe, cono, manE, reqF, reqP, resp, conT))
   conn.commit()
   cursor.execute('select idPuesto, nomPuesto from puesto where idPuesto=(select max(idPuesto) frompuesto) ')
   dato=cursor.fetchall()

   idpue = dato[0]
   idP = idpue[0]
   cursor.execute('select count(*) from idiomas ')
   dato = cursor.fetchall()
   nidio = dato[0]
   ni = nidio[0] + 1
   for i in range(1, ni):
       idio = 'i' + str(i)
       if idio in request.form:
           cursor.execute('insert into puesto_has_idiomas(idPuesto,idIdioma) values (%s,%s)', (idP,i))
           conn.commit()
   cursor.execute('select count(*) from habilidad ')
   dato = cursor.fetchall()
   nhab = dato[0]
   nh = nhab[0] + 1

   for i in range(1, nh):
       habi = 'h' + str(i)
       if habi in request.form:
           cursor.execute('insert into puesto_has_habilidad(idPuesto,idHabilidad) values (%s,%s)',(idP, i))
           conn.commit()
   return redirect(url_for('puesto'))

# Puesto_Editar

@app.route('/puesto_editar/<string:idP>')
def puesto_editar(idP):
   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
   cursor = conn.cursor()
   cursor.execute('select idPuesto,codPuesto,idArea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,'
       'funciones,edad,sexo,idEstadoCivil,idEscolaridad,idGradoAvance,idCarrera,experiencia,conocimientos,manejoEquipo,'
       'reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo from puesto where idPuesto = %s', (idP))
   dato = cursor.fetchall()

   cursor.execute('select idArea, descripcion from area ')
   datos1 = cursor.fetchall()

   cursor.execute('select idEstado, descripcion from estadocivil ')
   datos2 = cursor.fetchall()

   cursor.execute('select idEscolaridad, descripcion from escolaridad ')
   datos3 = cursor.fetchall()

   cursor.execute('select idAvance, descripcion from gradoavance ')
   datos4 = cursor.fetchall()

   cursor.execute('select idCarrera, descripcion from carrera ')
   datos5 = cursor.fetchall()

   cursor.execute('select idIdioma, descripcion from idiomas ')
   datos6 = cursor.fetchall()

   cursor.execute('select idHabilidad, descripcion from habilidad ')
   datos7 = cursor.fetchall()

   cursor.execute('select a.idArea, a.descripcion from area a, puesto b where a.idArea = b.idArea and b.idPuesto = %s',(idP))
   datos11 = cursor.fetchall()

   cursor.execute('select a.idEstado, a.descripcion from estadocivil a, puesto b where a.idEstado = b.idEstadoCivil and b.idPuesto = %s',(idP))
   datos12 = cursor.fetchall()

   cursor.execute(
       'select a.idEscolaridad, a.descripcion from escolaridad a, puesto b where a.idEscolaridad = b.idEscolaridad and b.idPuesto = %s',(idP))
   datos13 = cursor.fetchall()

   cursor.execute(
       'select a.idAvance, a.descripcion from gradoavance a, puesto b where a.idAvance = b.idGradoAvance and b.idPuesto = %s',(idP))
   datos14 = cursor.fetchall()

   cursor.execute(
       'select a.idCarrera, a.descripcion from carrera a, puesto b where a.idCarrera = b.idCarrera and b.idPuesto = %s',(idP))
   datos15 = cursor.fetchall()

   cursor.execute('select a.idPuesto, b.idIdioma, b.descripcion from puesto a, idiomas b, puesto_has_idiomas c '
                  'where a.idPuesto = c.idPuesto and b.idIdioma = c.idIdioma and a.idPuesto = %s', (idP))
   datos16 = cursor.fetchall()

   cursor.execute('select a.idPuesto, b.idHabilidad, b.descripcion from puesto a, habilidad b, puesto_has_habilidad c ''where a.idPuesto = c.idPuesto and b.idHabilidad = c.idHabilidad and a.idPuesto = %s', (idP))
   datos17 = cursor.fetchall()

   return render_template("puesto_edi.html", dat=dato[0], catArea=datos1, catEdoCivil=datos2, catEscolaridad=datos3,
                          catGradoAvance=datos4, catCarrera=datos5, catIdioma=datos6, catHabilidad=datos7,
                          Area=datos11[0], EdoCivil=datos12[0], Escolaridad=datos13[0], GradoAvance=datos14[0],
                          Carrera=datos15[0], Idioma=datos16, Habilidad=datos17)


@app.route('/puesto_fedita/<string:idP>', methods=['POST'])
def puesto_fedita(idP):
   if request.method == 'POST':
       if 'idAvance' in request.form:
           idGA = request.form['idAvance']
       else:
           idGA = '1'
       if 'idCarrera' in request.form:
           idCa = request.form['idCarrera']
       else:
           idCa = '1'
       codP = request.form['codPuesto']
       idAr = request.form['idArea']
       nomP = request.form['nomPuesto']
       pueJ = request.form['puestoJefeSup']
       jorn = request.form['jornada']
       remu = request.form['remunMensual']
       pres = request.form['prestaciones']
       desc = request.form['descripcionGeneral']
       func = request.form['funciones']
       eda = request.form['edad']
       sex = request.form['sexo']
       idEC = request.form['idEstadoCivil']
       idEs = request.form['idEscolaridad']
       expe = request.form['experiencia']
       cono = request.form['conocimientos']
       manE = request.form['manejoEquipo']
       reqF = request.form['reqFisicos']
       reqP = request.form['reqPsicologicos']
       resp = request.form['responsabilidades']
       conT = request.form['condicionesTrabajo']

   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
   cursor = conn.cursor()
   cursor.execute('update puesto set codPuesto = %s, idArea = %s, nomPuesto = %s, puestoJefeSup = %s, jornada = %s, '
                  'remunMensual = %s, prestaciones = %s, descripcionGeneral = %s, funciones = %s, edad = %s, sexo = %s, '
                  'idEstadoCivil = %s, idEscolaridad = %s, idGradoAvance = %s, idCarrera = %s, experiencia = %s, '
                  'conocimientos = %s, manejoEquipo = %s, reqFisicos = %s, reqPsicologicos = %s, responsabilidades = %s, '
                  'condicionesTrabajo = %s where idPuesto = %s', (codP, idAr, nomP, pueJ, jorn, remu, pres, desc, func, eda,
                  sex, idEC, idEs, idGA, idCa, expe, cono, manE, reqF, reqP, resp, conT, idP))
   conn.commit()
   cursor.execute('DELETE FROM puesto_has_idiomas WHERE idPuesto=%s', (idP))
   conn.commit()
   cursor.execute('DELETE FROM puesto_has_habilidad WHERE idPuesto=%s', (idP))
   conn.commit()
   cursor.execute('select idPuesto, nomPuesto from puesto where idPuesto=(select max(idPuesto) frompuesto) ')
   dato = cursor.fetchall()

   idpue = dato[0]
   idP = idpue[0]
   cursor.execute('select count(*) from idiomas ')
   dato = cursor.fetchall()
   nidio = dato[0]
   ni = nidio[0] + 1
   for i in range(1, ni):
       idio = 'i' + str(i)
       if idio in request.form:
           cursor.execute('insert into puesto_has_idiomas(idPuesto,idIdioma) values (%s,%s)', (idP, i))
           conn.commit()
   cursor.execute('select count(*) from habilidad ')
   dato = cursor.fetchall()
   nhab = dato[0]
   nh = nhab[0] + 1

   for i in range(1, nh):
       habi = 'h' + str(i)
       if habi in request.form:
           cursor.execute('insert into puesto_has_habilidad(idPuesto,idHabilidad) values (%s,%s)', (idP, i))
           conn.commit()
   return redirect(url_for('puesto'))



# Crud de Requisicion

@app.route('/requisicion_agr')
def requisicion_agr():
   conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh' )
   cursor = conn.cursor()
   cursor.execute('select idArea, descripcion from area')
   datos1 = cursor.fetchall()

   cursor.execute('select idPuesto, nomPuesto from puesto ')
   datos2 = cursor.fetchall()

   return render_template("requisicion_agr.html" , catArea=datos1, puesto=datos2)

@app.route('/requisicion_fagrega', methods=['POST'])
def requisicion_fagrega():
    if request.method == 'POST':
        fol = request.form['folio']
        feElab = request.form['fechaElaborac']
        feRecl = request.form['fechaRecluta']
        feIniV = request.form['fechaInicVacante']
        motR = request.form['motReq']
        motE = request.form['motReqEsp']
        tiVa = request.form['tipoVac']
        nomS = request.form['nomSoli']
        idPu = request.form['idPuesto']
        idAr = request.form['idArea']

    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('insert into requisicion (folio,fechaElab, fechaRecluta, fechaInicVac, motivoRequisicion, '
                   'motivoEspecifique, tipoVacante, nomSolicita,idPuesto, idArea) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                   (fol, feElab, feRecl, feIniV, motR, motE, tiVa,nomS, idPu,idAr))
    conn.commit()

    return redirect(url_for('requisicion_pend'))

@app.route('/requisicion_pend')
def requisicion_pend():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('select a.idRequisicion, a.folio, b.nomPuesto from requisicion  a, puesto b where a.idPuesto = b.idPuesto and a.autorizada =0  ')
    datos =cursor.fetchall()

    return render_template("requisicion_pend.html", requi = datos, dat = '', areaReq='', edoCiv= '', esco='', areaPue='')

@app.route('/requisicion_fdetalle/<string:idR>', methods=['GET'])
def requisicion_fdetalle(idR):
    conn= pymysql.connect(host='localhost', user='root', passwd= '', db='rh')
    cursor = conn.cursor()
    cursor.execute(
        'select a.idRequisicion, a.folio, b.nomPuesto from requisicion  a, puesto b where a.idPuesto = b.idPuesto and a.autorizada =0  ')
    datos = cursor.fetchall()

@app.route('/Borrar_requisicion_pend/<string:idP>')
def Borrar_Requisicion(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('delete from requisicion where idRequisicion = %s', (idP))
    conn.commit()
    return redirect(url_for('requisicion_pend'))

if __name__ == "__main__":
   app.run(debug=True)
