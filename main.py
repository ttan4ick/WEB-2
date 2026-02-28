from flask import Flask, render_template

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


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")