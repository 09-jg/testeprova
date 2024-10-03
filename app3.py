from flask import Flask 
App= Flask(__name__)

@App.route("/")
def cadastro():
    return "Bem vindo ao cadastro"

if __name__=="__main__":
    App.run(debug="true")