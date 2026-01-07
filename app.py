import os
from flask import Flask, render_template_string, request, jsonify
from datetime import datetime

app = Flask(__name__)

# --- المحرك المنطقي لـ BoB-DJ (مجاني للأبد) ---
class SovereignLogic:
    @staticmethod
    def analyze(text):
        # بروتوكول SAP: البحث عن علامات الانحياز
        bias_keywords = {
            'مؤكد': 15, 'خائن': 20, 'عدو': 20, 'دائماً': 10, 
            'أبداً': 10, 'مؤامرة': 20, 'حقيقة مطلقة': 15
        }
        
        found_warnings = []
        score = 100
        
        for word, penalty in bias_keywords.items():
            if word in text:
                score -= penalty
                found_warnings.append(f"تنبيه انحياز: استخدام لغة قاطعة ({word})")
        
        # تجبير المنطق: التأكد من عدم نزول النتيجة تحت الصفر
        final_score = max(0, score)
        
        return {
            "score": final_score,
            "warnings": found_warnings if found_warnings else ["لم يتم رصد انحيازات لغوية واضحة."],
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

# --- الواجهة البصرية (HTML) مدمجة للسهولة ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BoB-DJ ثقة | الحارس الرقمي</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        :root { --main-bg: #0a192f; --card-bg: #112240; --accent: #64ffda; --text: #e6f1ff; }
        body { background-color: var(--main-bg); color: var(--text); font-family: 'Segoe UI', sans-serif; min-height: 100vh; display: flex; align-items: center; justify-content: center; }
        .card { background-color: var(--card-bg); border: 1px solid #233554; border-radius: 20px; width: 100%; max-width: 500px; padding: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
        .btn-primary { background-color: var(--accent); color: var(--main-bg); border: none; font-weight: bold; padding: 12px; border-radius: 10px; transition: 0.3s; }
        .btn-primary:hover { background-color: #45c7a9; transform: translateY(-2px); }
        textarea { background-color: #020c1b !important; border: 1px solid #233554 !important; color: white !important; border-radius: 10px !important; }
        .result-area { display: none; margin-top: 25px; padding: 20px; background: #1d3359; border-radius: 15px; border-right: 5px solid var(--accent); }
        .score-circle { font-size: 2rem; font-weight: bold; color: var(--accent); }
    </style>
</head>
<body>
    <div class="card text-center">
        <h2 class="mb-2">🛡️ BoB-DJ ثقة</h2>
        <p class="text-secondary small">الميثاق الفيدرالي المعرفي - الإصدار السيادي</p>
        <hr class="opacity-25">
        
        <div class="mb-3 text-start">
            <label class="form-label small">ضع الخبر أو النص هنا للتحليل:</label>
            <textarea id="userInput" class="form-control" rows="5" placeholder="انسخ النص الذي تريد التأكد منه..."></textarea>
        </div>
        
        <button onclick="startAnalysis()" id="btnAction" class="btn btn-primary w-100 shadow-sm">إطلاق التحليل الفيدرالي</button>
        
        <div id="resultBox" class="result-area text-start">
            <div class="d-flex justify-content-between align-items-center mb-3">
                <span class="small">درجة الموضوعية:</span>
                <span id="scoreVal" class="score-circle">0%</span>
            </div>
            <div id="warningList" class="small text-warning mb-3"></div>
            <p class="x-small text-info mt-3" style="font-size: 0.7rem;">بصمة الحقيقة: {hash_val}</p>
        </div>
    </div>

    <script>
        async function startAnalysis() {
            const text = document.getElementById('userInput').value;
            if(!text) return alert("الرجاء إدخال نص أولاً!");
            
            const btn = document.getElementById('btnAction');
            btn.innerText = "جاري تجبير المنطق...";
            btn.disabled = true;

            try {
                const response = await fetch('/analyze', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({content: text})
                });
                const data = await response.json();
                
                document.getElementById('resultBox').style.display = 'block';
                document.getElementById('scoreVal').innerText = data.score + "%";
                document.getElementById('warningList').innerHTML = data.warnings.map(w => `• ${w}`).join('<br>');
            } catch (e) {
                alert("حدث خطأ في الات
