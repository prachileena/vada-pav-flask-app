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
            margin: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #f9d976, #f39c12);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
          }}
          .container {{
            background: #fff;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.2);
            text-align: center;
            width: 500px;
            animation: fadeIn 1s ease-in-out;
          }}
          h1 {{
            color: #e67e22;
            font-size: 32px;
            margin-bottom: 20px;
          }}
          p {{
            font-size: 22px;
            color: #2c3e50;
            margin-top: 15px;
          }}
          .quote {{
            background: #fef5e7;
            padding: 20px;
            border-radius: 12px;
            font-style: italic;
            box-shadow: inset 0 2px 5px rgba(0,0,0,0.1);
          }}
          @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
          }}
        </style>
      </head>
      <body>
        <div class="container">
          <h1>🥪 Welcome to Vada Pav App 🥪</h1>
          <div class="quote">
            <p><b>Special:</b> {quote}</p>
          </div>
        </div>
      </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
