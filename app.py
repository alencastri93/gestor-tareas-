from flask import Flask,render_template,request

app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def inicio():
    if request.method == "POST":
        titulo = request.form.get("titulo")
        descripcion = request.form.get("descripcion")
        fecha = request.form.get("fecha")
        prioridad = request.form.get("prioridad")
        categoria = request.form.get("categoria")

        print("titulo:", titulo)
        print("Descripción:", descripcion)
        print("Fecha:", fecha)
        print("Prioridad:", prioridad)
        print("Categoría:", categoria)

        return "flask recibe los datos de tu tarea "

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)