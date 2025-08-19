from flask import Flask, render_template
import random

app = Flask(__name__)

vada_pav_quotes = [
    "😋 Mumbai's famous Vada Pav - A true street food king!",
    "🌶 Spicy chutney + crispy vada + soft pav = ❤️",
    "🥔 Potatoes wrapped in gram flour fried to perfection!",
    "🚋 Nothing beats eating Vada Pav at a Mumbai station!",
    "🍋 Squeeze a little lemon, add some chilies… Heaven!"
]

@app.route("/")
def home():
    quote = random.choice(vada_pav_quotes)
    return render_template("index.html", quote=quote)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
