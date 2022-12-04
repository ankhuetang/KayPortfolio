from flask import Flask, render_template, request
import smtplib

EMAIL = "ankhuetang03@gmail.com"
PASSWORD="Ankhuetang_03"

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.form
        # send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("index.html", msg_sent=True)
    return render_template("index.html", msg_sent=False)

# def send_email(name, email, phone, message):
#     email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(EMAIL, PASSWORD)
#         connection.sendmail(EMAIL, EMAIL , email_message)

if __name__ == "__main__":
    app.run(debug=True)


