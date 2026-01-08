from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# --- المحرك المنطقي (الذي سيقوم بالتحليل فعلياً) ---
def logic_engine(text):
    # كلمات الاختبار: مؤامرة، خائن، عدو، مؤكد
    trigger_words = ['مؤامرة', 'خائن', 'عدو', 'مؤكد']
    found = [w for w in trigger_words if w in text]
    score = 100 - (len(found) * 25)
    return {"score": max(0, score), "warnings": found}

@app.route('/')
def index():
    return render_template_string('''
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BoB-DJ ثقة</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background-color: #0a192f; color: #64ffda; text-align: center; padding: 20px; }
        .card { background-color: #112240; border: 1px solid #64ffda; border-radius: 20px; padding: 20px; }
        textarea { background: #020c1b !important; color: white !important; border: 1px solid #233554 !important; }
    </style>
</head>
<body>
    <div class="card shadow-lg mx-auto" style="max-width: 500px;">
        <h2 class="mb-4">🛡️ BoB-DJ ثقة</h2>
        <textarea id="inp" class="form-control mb-3" rows="4" placeholder="انسخ النص المفخخ هنا..."></textarea>
        <button onclick="runAnalysis()" class="btn btn-info w-100 fw-bold">إطلاق التحليل الفيدرالي</button>
        <div id="resBox" class="mt-4" style="display:none; border-top: 1px solid #233554; padding-top: 20px;">
            <h1 id="scoreDisp" style="font-size: 3rem;">100%</h1>
            <p id="warnDisp" class="text-warning"></p>
        </div>
    </div>
    <script>
        async function runAnalysis() {
            const text = document.getElementById('inp').value;
            if(!text) return alert("الرجاء وضع نص!");
            
            const response = await fetch('/analyze', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({content: text})
            });
            const data = await response.json();
            
            document.getElementById('resBox').style.display = 'block';
            document.getElementById('scoreDisp').innerText = data.score + "%";
            document.getElementById('warnDisp').innerText = data.warnings.length ? 
                "⚠️ الكلمات المرصودة: " + data.warnings.join(' - ') : "✅ نص موضوعي";
        }
    </script>
</body>
</html>
''')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    return jsonify(logic_engine(data.get('content', '')))

if __name__ == "__main__":
    app.run()
