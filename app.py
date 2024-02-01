from flask import Flask, render_template, request

app = Flask(__name__)


comments = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/monumentos_hispanos")
def hispano():
    return render_template("cultura_espanola.html")




@app.route("/monumentos_mexicanos")
def view_cultura_mexicana():
    return render_template("mexico.html")


@app.route("/monumentos_españoles")
def view_cultura_español():
    return render_template("españa.html")


@app.route("/monumentos_chilenos")
def view_cultura_chilena():
    return render_template("chile.html")

@app.route("/monumentos_cubanos")
def view_cultura_cubana():
    return render_template("cuba.html")

@app.route("/monumentos_argentinos")
def view_cultura_argentina():
    return render_template("argentina.html")

@app.route("/monumentos_venezuelanos")
def view_cultura_venezuelana():
    return render_template("venezuela.html")

@app.route("/monumentos_guatemaltecos")
def view_cultura_guatemalca():
    return render_template("guatemala.html")

@app.route("/monumentos_ecuatorianos")
def view_cultura_ecuatoriana():
    return render_template("ecuador.html")



@app.route('/monumentos_dominicanos')
def view_cultura_dominicana():
    return render_template("república_dominicana.html")

@app.route('/monumentos_bolivianos')
def view_cultura_boliviana():
    return render_template("bolivia.html")


@app.route('/monumentos_salvadoreños')
def view_cultura_salvadoreña():
    return render_template("salvador.html")


@app.route('/monumentos_nicaragüense')
def view_cultura_nicaragüensa():
    return render_template("nicaragua.html")



@app.route('/monumentos_columbianos')
def view_cultura_columbiana():
    return render_template("columbia.html")

@app.route('/monumentos_peruanos')
def view_cultura_peruana():
    return render_template("peru.html")

@app.route('/monumentos_hondureños')
def view_cultura_hondereña():
    return render_template("honduras.html")






@app.route("/forum", methods=["GET", "POST"])
def view_forum():
    
    if request.method == "POST":
        username = request.form["username"]
        content = request.form["content"]
        
        comments.append({"name" : username, "content" : content})
        
        if not username or not content:
            return render_template("forum.html")
        
        return render_template("forum.html", comments=comments)
            
        
    return render_template("forum.html", comments=comments)


if __name__ == "__main__":
    app.run(debug=True)