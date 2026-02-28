from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template("base.html", title="Заготовка")


@app.route("/training/<prof>")
def profession(prof):
    return render_template("prof.html", title="Тренировки", profession=prof)


@app.route("/list_prof/<list>")
def prof_list(list):
    professions_list = [
        "инженер-исследователь",
        "пилот",
        "строитель",
        "экзобиолог",
        "врач",
        "инженер по терраформированию",
        "климатолог",
        "специалист по радиационной защите",
        "астрогеолог",
        "гляциолог",
        "инженер жизнеобеспечения",
        "метеоролог",
        "оператор марсохода",
        "киберинженер",
        "штурман",
        "пилот дронов",
    ]
    return render_template(
        "all_professions.html",
        title="Профессии",
        professions=professions_list,
        list_type=list,
    )


@app.route("/answer", methods=["POST", "GET"])
@app.route("/auto_answer", methods=["POST", "GET"])
def astronaut_selection():
    if request.method == "GET":
        return render_template("answer.html", title="Анкета")
    elif request.method == "POST":
        data = {}
        data["surname"] = request.form["surname"]
        data["name"] = request.form["name"]
        data["education"] = request.form["education"]
        data["motivation"] = request.form["about"]

        all_professions = [
            "Инженер-исследователь",
            "Инженер-строитель",
            "Пилот",
            "Метеоролог",
            "Инженер по жизнеобеспечению",
            "Инженер по радиационной защите",
            "Врач",
            "Экзобиолог",
        ]
        professions = []
        for i in range(1, 9):
            prof = request.form.get(f"profession{i}", "")
            if prof == "on":
                professions.append(all_professions[i - 1])
        data["professions"] = ", ".join(professions)

        data["sex"] = request.form["sex"]
        accept = request.form.get("accept", "")
        if accept == "on":
            accept = True
        else:
            accept = False
        data["stay"] = accept

        return render_template("auto_answer.html", title="Анкета", data=data)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")