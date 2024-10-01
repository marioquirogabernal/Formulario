from flask import app, Flask, request, redirect, url_for, render_template, flash


from forms import UsuarioForm

app = Flask(__name__)

#Generar Secret_Key con: "python -c 'import secrets; print(secrets.token_hex()) y guardarla en una variable de entorno
app.config['SECRET_KEY'] = 'clave_ULTRA_secreta'

@app.route('/formulario', methods=['GET','POST'])
def formulario():
    usuarioForm = UsuarioForm()
    if request.method == "POST":
        if usuarioForm.validate_on_submit():
            # Aqui se llenaria el objeto usuario con los datos del formuladio
            # Aqui se guardaria el registro del usuario en la BD
            flash(f'Usuario {usuarioForm.usuario.data} registrado con éxito!', 'success')
            print("Usuario Guardado")
            return redirect(url_for("formulario"))
    return render_template('formulario.html', usuarioForm=usuarioForm)