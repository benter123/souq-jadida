from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        item = request.form.get('item')
        phone = request.form.get('phone')
        with open("items.txt", "a") as f:
            f.write(f"{item} | {phone}\n")
    
    try:
        with open("items.txt", "r") as f:
            items = f.readlines()
    except:
        items = []

    return render_template_string("""
    <html>
    <head>
        <style>
            body { font-family: sans-serif; max-width: 500px; margin: auto; padding: 20px; background: #f0f2f5; }
            input, button { width: 100%; padding: 10px; margin: 5px 0; border-radius: 5px; border: 1px solid #ccc; }
            button { background: #007bff; color: white; font-weight: bold; cursor: pointer; }
            li { background: white; padding: 10px; margin-bottom: 10px; border-radius: 8px; list-style: none; border-left: 5px solid #007bff; }
        </style>
    </head>
    <body>
        <h1>سوق الحي المستعمل</h1>
        <form method="POST">
            <input name="item" placeholder="اسم السلعة" required>
            <input name="phone" placeholder="رقم الهاتف" required>
            <button type="submit">نشر الإعلان</button>
        </form>
        <hr>
        <h2>الإعلانات المتاحة:</h2>
        <ul>
            {% for i in items %}
                <li>{{ i }}</li>
            {% endfor %}
        </ul>
    </body>
    </html>
    """, items=items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
