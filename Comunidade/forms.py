from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from Comunidade.models import Usuario
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed
class Formcriarconta(FlaskForm):
    username = StringField('Nome de Usuario', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação de senha', validators=[DataRequired(), EqualTo('senha')])
    botao_criarconta = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado. Cadastre-se com outro e-mail ou faça login pra continuar')
class Formlogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Dados de acesso')
    botao_login = SubmitField('Fazer Login')

class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuario', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar Foto de Perfil', validators=[FileAllowed(['jpg', 'png'])])
    curso_excel = BooleanField('Curso Excel')
    curso_vba = BooleanField('Curso VBA')
    curso_powerbi = BooleanField('Curso Power BI')
    curso_python = BooleanField('Curso Python')
    curso_ppt = BooleanField('Curso PPT')
    curso_sql = BooleanField('Curso SQL')
    botao_editarperfil = SubmitField('Confirmar Edição')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('E-mail já cadastrado. Cadastre-se com outro e-mail ou faça login pra continuar')

class FormCriarPost(FlaskForm):
    titulo = StringField('Titulo Do Post', validators=[DataRequired(), Length(2, 150)])
    corpo = TextAreaField('Escreva Seu Post Aqui', validators=[DataRequired()])
    botao_submit = SubmitField('Criar Post')


class Formeditar_post(FlaskForm):
    titulo = StringField('Titulo Do Post', validators=[DataRequired(), Length(2, 150)])
    corpo = TextAreaField('Escreva Seu Post Aqui', validators=[DataRequired()])
    botao_submit = SubmitField('Editar Post')