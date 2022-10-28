from flask import Flask, render_template, request  # Importa Flask para permitirnos crear nuestra aplicación

app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"


# El decorador "@" asocia esta ruta con la función inmediatamente siguiente
@app.route('/')          
def hola_mundo():
    return 'Hola Mundo!'  #Localhost:5000/: haz que diga "¡Hola Mundo!"

@app.route('/dojo')       #Localhost:5000/dojo: haz que diga "¡Dojo!"
def dojo():
    return 'Dojo!'

@app.route('/say/<username>')                           #localhost:5000/say/flask: haz que diga "¡Hola, Flask!"
def say(username):                                      #localhost:5000/say/ Michael: haz que diga "¡Hola, Michael!"
    return f'Hola, {username.capitalize()}!'            #localhost:5000/say/john: haz que diga "¡Hola, John!"

@app.route('/repeat/<int:num>/<string:word>')       #localhost:5000/repeat/35/hello: haz que diga "hola" 35 veces
def repetir(num, word):                             #localhost:5000/repeat/80/bye: haz que diga "adiós" 80 veces
    out = ''                                     #localhost:5000/repeat/99/dogs: haz que diga "perros" 99 veces
    for _ in range(num):
        out += f'<h1>{word}</h1>'
    return out                    
                        
@app.errorhandler(404)              #si escribe otra ruta diferente y el servidor muestra un error 404 muestra un mensaje de error
def page_not_found(error): 
    print(error)     
    return render_template('404.html'), 404


if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)     