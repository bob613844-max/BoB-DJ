import os
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# --- المحرك المنطقي ---
class SovereignLogic:
    @staticmethod
    def analyze(text):
        bias_keywords = {'مؤكد': 15, 'خائن': 20, 'عدو': 20, 'مؤامرة': 20}
        score = 100
        found = []
        for word, penalty in bias_keywords.items():
            if word in text:
                score -= penalty
                found.append(word)
        return {"score": max(0, score), "warnings": found}

# --- الواجهة مع أكواد الدمج الاجتماعي ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <meta property="og:title" content="BoB-DJ ثقة | الحارس الرقمي">
    <meta property="og:description" content="أداة فيدرالية لتحليل الأخبار وحماية سيادتك المنطقية. مجانية للجميع.">
    <meta property="og:image" content="https://bo-b-dj.vercel.app/static/logo.png">
    <meta property="og:url" content="https://bo-b-dj.vercel.app/">
    <meta name="twitter:card" content="summary_large_image">

    <title>BoB-DJ ثقة</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background-color: #0a192f; color: white; font-family: sans-serif; }
        .card { background-color: #112240; border-radius: 20px; padding: 25px; margin-top: 50px; border: 1px solid #233554; }
        .btn-share { background-color: #25d366; color: white; margin-top: 10px; border: none; padding: 10px; border-radius: 10px; width: 100%; }
        .btn-fb { background-color: #1877f2; color: white; margin-top: 10px; border: none; padding: 10px; border-radius: 10px; width: 100%; }
    </style>
</head>
<body class="container d-flex justify-content-center">
    <div class="card shadow text-center" style="max-width: 450px; width: 100%;">
        <h2>🛡️ BoB-DJ ثقة</h2>
        <textarea id="inp" class="form-control bg-dark text-white mb-3" rows="4" placeholder="انسخ الخبر هنا للتحقق..."></textarea>
        <button onclick="check()" class="btn btn-info w-100">تحليل المنطق</button>
        
        <div id="resBox" style="display:none;" class="mt-4 p-3 bg-secondary rounded">
            <h3 id="scr"></h3>
            <hr>
            <p>شارك النتيجة لحماية الآخرين:</p>
            <button onclick="shareWA()" class="btn-share">إرسال عبر واتساب ✅</button>
            <button onclick="shareFB()" class="btn-fb">نشر على فيسبوك 💙</button>
        </div>
    </div>

    <script>
        let lastScore = 0;
        async function check() {
            const text = document.getElementById('inp').value;
            const response = await fetch('/analyze', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({content: text})
            });
            const data = await response.json();
            lastScore = data.score;
            document.getElementById('resBox').style.display = 'block';
            document.getElementById('scr').innerText = "درجة الثقة: " + data.score + "%";
        }

        function shareWA() {
            const msg = `استخدمت حارس BoB-DJ الرقمي لتحليل خبر، وكانت درجة الموضوعية ${lastScore}%. تحقق بنفسك هنا: https://bo-b-dj.vercel.app/`;
            window.open(`https://wa.me/?text=${encodeURIComponent(msg)}`);
        }

        function shareFB() {
            const url = "https://bo-b-dj.vercel.app/";
            window.open(`https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`);
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    return jsonify(SovereignLogic.analyze(data.get('content', '')))

if __name__ == '__main__':
    app.run()
