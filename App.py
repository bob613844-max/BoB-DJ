from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# المحرك المنطقي المجاني
def simple_analyze(text):
    bias_words = ['مؤكد', 'خائن', 'عدو', 'مؤامرة', 'دائماً']
    warnings = [w for w in bias_words if w in text]
    score = max(0, 100 - (len(warnings) * 20))
    return {"score": score, "warnings": warnings}

@app.route('/')
def home():
    return render_template_string('''
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BoB-DJ ثقة</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background-color: #0a192f; color: white; text-align: center; padding-top: 50px; }
        .card { background-color: #112240; border: 1px solid #64ffda; border-radius: 15px; padding: 20px; }
        .btn-custom { background-color: #64ffda; color: #0a192f; font-weight: bold; }
    </style>
</head>
<body class="container">
    <div class="card shadow">
        <h2>🛡️ BoB-DJ ثقة</h2>
        <p>حارس السيادة المنطقية</p>
        <textarea id="inp" class="form-control mb-3" rows="4" placeholder="ضع النص هنا..."></textarea>
        <button onclick="check()" class="btn btn-custom w-100">إطلاق التحليل الفيدرالي</button>
        <div id="res" class="mt-4" style="display:none;">
            <h3 id="score"></h3>
            <div id="warn" class="text-warning"></div>
        </div>
    </div>
    <script>
        async function check() {
            const t = document.getElementById('inp').value;
            const r = await fetch('/analyze', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({content: t})
            });
            const d = await r.json();
            document.getElementById('res').style.display = 'block';
            document.getElementById('score').innerText = "درجة الموضوعية: " + d.score + "%";
            document.getElementById('warn').innerText = d.warnings.length ? "تنبيهات: " + d.warnings.join('، ') : "لم يتم رصد انحيازات.";
        }
    </script>
</body>
</html>
''')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    return jsonify(simple_analyze(data.get('content', '')))

if __name__ == "__main__":
    app.run()
