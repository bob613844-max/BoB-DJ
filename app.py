from flask import Flask, render_template_string
import hashlib

app = Flask(__name__)

# تطبيق مبدأ السيادة المنطقية عبر التشفير
def generate_truth_hash(content):
    return hashlib.sha256(content.encode()).hexdigest()

@app.route('/')
def home():
    truth_id = generate_truth_hash("Venezuela_Oil_Crisis_2026")
    return """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>BoB DJ ثقة | الحارس الرقمي</title>
        <style>
            body { background: #020617; color: white; text-align: center; font-family: sans-serif; padding: 50px; }
            .card { border: 2px solid #1e40af; border-radius: 20px; padding: 30px; max-width: 500px; margin: auto; background: #0f172a; box-shadow: 0 0 20px #1e3a8a; }
            .status { color: #fbbf24; font-weight: bold; }
            .btn { background: #2563eb; color: white; padding: 15px 30px; text-decoration: none; border-radius: 10px; display: inline-block; margin-top: 20px; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🛡️ BoB DJ ثقة</h1>
            <p>قضية الساعة: أزمة فنزويلا</p>
            <p class="status">الحالة: تحت التدقيق (اختبار المرآة المكسورة)</p>
            <p>بصمة الحقيقة: <code style="color:#60a5fa;">""" + truth_id[:16] + """</code></p>
            <a href="#" class="btn">وثق خبراً الآن (1 دولار)</a>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
