from flask import Flask, request, render_template
import re

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# 1. ОТОБРАЖЕНИЕ ДАННЫХ ЗАПРОСА
@app.route("/request")
def request_info():
    return render_template(
        "request_info.html",
        args=request.args,
        headers=request.headers,
        cookies=request.cookies
    )


# 2. ФОРМА АВТОРИЗАЦИИ
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        return render_template(
            "login_result.html",
            username=username,
            password=password
        )

    return render_template("login.html")


# 3. ПРОВЕРКА ТЕЛЕФОНА
@app.route("/phone", methods=["GET", "POST"])
def phone():
    error = None
    formatted = None
    phone_input = ""

  
    pattern = r"^(\+7|8)?\s*\(?\d{3}\)?[\s\-\.]?\d{3}[\s\-\.]?\d{2}[\s\-\.]?\d{2}$"

    if request.method == "POST":
        phone_input = request.form.get("phone", "")


        if not re.fullmatch(r"[0-9\+\-\(\)\.\s]+", phone_input):
            error = "Недопустимый ввод. В номере телефона встречаются недопустимые символы."
        else:
            digits = re.sub(r"\D", "", phone_input)

            if phone_input.startswith("+7") or phone_input.startswith("8"):
                if len(digits) != 11:
                    error = "Недопустимый ввод. Неверное количество цифр."
            else:
                if len(digits) != 10:
                    error = "Недопустимый ввод. Неверное количество цифр."

          
            if not error and not re.fullmatch(pattern, phone_input):
                error = "Недопустимый ввод. Некорректный формат номера."

        
            if not error:
                if len(digits) == 11:
                    digits = digits[1:] 

                formatted = f"8-{digits[0:3]}-{digits[3:6]}-{digits[6:8]}-{digits[8:10]}"

    return render_template(
        "phone.html",
        error=error,
        formatted=formatted,
        phone=phone_input
    )

if __name__ == "__main__":
    app.run(debug=True)