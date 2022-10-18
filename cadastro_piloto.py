import os
from flask import Flask, request, render_template
from flaskext.mysql import MySQL
mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_DB'] = 'teste'
app.config['MYSQL_DATABASE_HOST'] = 'db'
mysql.init_app(app)


mysql.init_app(app)

@app.route('/')
def main():
    return render_template('cadastro_piloto.html')


@app.route('/gravar', methods=['POST', 'GET'])
def gravar():
    nome = request.form['nome']
    cpf = request.form['cpf']
    rg = request.form['rg']
    telefone = request.form['telefone']
    email = request.form['email']
    data_nascimento = request.form['data_nascimento']
    contato_emergencia = request.form['contato_emergencia']

    if nome and cpf and rg and telefone and email and contato_emergencia:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into cadastro_piloto (nome,cpf,rg, telefone, email, data_nascimento, contato_emergencia) VALUES (%s, %s, %s,  %s, %s, %s, %s)', (nome,cpf,rg, telefone, email, data_nascimento, contato_emergencia))
        conn.commit()
    return render_template('cadastro_piloto.html')


@app.route('/listar', methods=['POST', 'GET'])
def listar():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select nome,cpf,rg, telefone, email, data_nascimento, contato_emergencia from tbl_user')
    data = cursor.fetchall()
    conn.commit()
    return render_template('lista.html', datas=data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

