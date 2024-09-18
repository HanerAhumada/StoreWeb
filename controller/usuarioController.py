from models.Usuarios import Usuarios
from werkzeug.security import generate_password_hash, check_password_hash
from flask import session, flash


class usuarioController:
    def POST(self, data):
        nombre = data.get('nombre')
        apellido = data.get('apellido')
        fecha = data.get('fecha')
        direccion = data.get('direccion')
        telefono = data.get('telefono')
        email = data.get('email')
        password = generate_password_hash(data.get('password'))
        estado = 'activo'

        if Usuarios.query.filter_by(email=email).first():
            return 'El usuario ya existe'

        nuevo_usuario = Usuarios(
            nombre=nombre,
            apellido=apellido,
            fecha=fecha,
            email=email,
            direccion=direccion,
            telefono=telefono,
            password=password,
            estado=estado,
        )
        nuevo_usuario.save()

    def login(self, data):
        usuario = Usuarios.query.filter_by(email=data.get('email')).first()

        # Validar si el usuario existe y si la contraseña es correcta
        if usuario and check_password_hash(usuario.password, data.get('password')):
            session['user_id'] = usuario.id  # Guardar el ID del usuario en la sesión
            flash('Inicio de sesión exitoso', 'success')
            return 'Login exitoso'
        else:
            flash('Email o contraseña incorrectos', 'danger')
            return 'Login fallido'

    def GET(self):
        pass

    def PUT(self):
        pass

    def DELETE(self):
        pass

    def PATCH(self):
        pass