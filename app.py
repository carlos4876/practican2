from flask import Flask, render_template, request
app = Flask(__name__)

# Ruta principal que renderiza la página principal (index)
@app.route("/")
def index():
    return render_template("index.html")

# Ruta para el formulario de inscripción a cursos
@app.route("/inscripcion_curso", methods=['GET', 'POST'])
def inscripcion_curso():
    if request.method == 'POST':
        # Recibimos los datos del formulario
        nombre = request.form.get('nombre')
        apellidos = request.form.get('apellidos')
        curso = request.form.get('curso')

        # Renderizamos la página de salida con los datos ingresados
        return render_template("salida.html", nombre=nombre, apellidos=apellidos, curso=curso)
    
    # Si el método es GET, mostramos el formulario
    return render_template("inscripcion_curso.html")
##ruta para el formulario de registro de usuario
@app.route("/registro_usuario", methods=['GET','POST'])
def registro_usuario():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        correo_electronico = request.form.get('correo_electronico')
        contraseña = request.form.get('contraseña')
        return render_template("salida_usuario.html",nombre=nombre,apellido=apellido,correo_electronico=correo_electronico,contraseña=contraseña)
    return render_template("registro_usuario.html")

# Ruta para el formulario de registro de producto
@app.route("/registro_productos", methods=['GET', 'POST'])
def registro_productos():
    if request.method == 'POST':
        producto = request.form.get('producto')
        categoria = request.form.get('categoria')
        existencia = request.form.get('existencia') 
        precio = request.form.get('precio')
        return render_template("salida_producto.html", producto=producto, categoria=categoria, existencia=existencia, precio=precio)
    return render_template("registro_productos.html")


#registro para formulario registro libro
@app.route("/registro_libro", methods=['POST', 'GET'])
def registro_libro():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        autor = request.form.get('autor')  
        resumen = request.form.get('resumen')
        medio = request.form.get('medio')
        return render_template("/salida_libro.html", titulo=titulo, autor=autor, resumen=resumen, medio=medio)  # Corregido aquí
    return render_template("registro_libro.html")



if __name__ == "__main__":
    app.run(debug=True)
    
    
