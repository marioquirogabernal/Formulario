from datetime import date

from flask_wtf import FlaskForm
from wtforms.fields.choices import SelectField
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, Email, ValidationError, Regexp


class UsuarioForm(FlaskForm):
    usuario = StringField("Usuario", validators=[DataRequired(message="Este campo es obligatorio"),  Length(min=6, max=50, message="El usuario debe tener entre 6 y 50 caracteres"), Regexp(r'^[a-zA-Z0-9]+$', message="El usuario solo debe contener letras y números.")])
    email = StringField("Email", validators=[DataRequired(message="El email es obligatorio"), Email(message="Introduce un email válido")])
    contrasena = PasswordField("Contraseña", validators=[DataRequired(message="La contraseña es obligatoria"), Length(min=6, message="La contraseña debe tener al menos 6 caracteres")])
    confirmar_contrasena = PasswordField("Confirmar Contraseña", validators=[DataRequired(message="Debes confirmar la contraseña"), EqualTo("contrasena", message="Las contraseñas no coinciden")])
    fecha_nacimiento = DateField("Fecha de Nacimiento (YYYY-MM-DD)", format='%Y-%m-%d', validators=[DataRequired(message="La fecha de nacimiento es obligatoria")])
    sexo = SelectField("Sexo", choices=[('hombre', 'Hombre'), ('mujer', 'Mujer'), ('neutro', 'Neutro')], validators=[DataRequired(message="El campo de sexo es obligatorio")])
    confirmar = SubmitField('Enviar')

    # Validador personalizado para verificar que el usuario sea mayor de 18 años
    def validate_fecha_nacimiento(self, field):
        hoy = date.today()
        edad = hoy.year - field.data.year - ((hoy.month, hoy.day) < (field.data.month, field.data.day))
        if edad < 18:
            raise ValidationError("Debes tener al menos 18 años para registrarte.")