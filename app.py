from flask import Flask, render_template, request, redirect, url_for, flash
import openpyxl

app = Flask(__name__)
app.secret_key = "super-secret-key"  # Chave para gerenciar mensagens flash

# Página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "CAOA" and password == "CAOA1885":
            flash("Bem-vindo ao sistema!", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Usuário ou senha incorretos!", "danger")
    return render_template('login.html')

# Página principal
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        # Captura os dados do formulário
        nome = request.form['nome']
        idade = request.form['idade']
        genero = request.form['genero']
        estado_civil = request.form['estado_civil']

        # Abre ou cria o arquivo Excel
        workbook = openpyxl.load_workbook("Membros.xlsx")
        sheet = workbook.active
        sheet.append([nome, idade, genero, estado_civil])
        workbook.save("Membros.xlsx")
        flash("Cadastro realizado com sucesso!", "success")

    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
