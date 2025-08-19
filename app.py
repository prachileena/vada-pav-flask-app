from flask import Flask, render_template_string
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
    html = f"""
    <html>
      <head>
        <title>Vada Pav App</title>
        <style>
          body {{
            font-family: Arial, sans-serif;
            background: #fff3cd;
            text-align: center;
            padding: 50px;
          }}
          h1 {{ color: #d35400; }}
          p {{ font-size: 22px; color: #2c3e50; }}
        </style>
      </head>
      <body>
        <h1>🥪 Welcome to Vada Pav App 🥪</h1>
        <p><b>Special:</b> {quote}</p>
      </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
