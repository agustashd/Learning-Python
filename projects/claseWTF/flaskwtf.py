from flask import Flask , render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class MiFormulario(FlaskForm):
    name = StringField('Ingrese cuenta bancaria', validators=[DataRequired()])

app = Flask(__name__)
app.config['SECRET_KEY'] = "un string muy dificil de adivinar"

@app.route('/')
      
    
@app.route('/formulario',methods=['GET' , 'POST'])
def formulario():
    mi_formulario = MiFormulario()
    if mi_formulario.validate_on_submit():
        return 'Usted ingreso {}'.format(mi_formulario.name.data)
    return render_template('formulario.html', form=mi_formulario)

if __name__ == "__main__":
    app.run(debug=True)
