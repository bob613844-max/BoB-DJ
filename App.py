import os
from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# ميثاق BoB-DJ المصغر (يعمل محلياً ومجانياً)
class SovereignLogic:
    @staticmethod
    def analyze(text):
        # بروتوكول SAP: تفكيك المنطق
        words = text.split()
        bias_score = 0
        warnings = []
        
        # كشف الانحيازات البلاغية (أمثلة)
        bias_keywords = ['دائماً', 'أبداً', 'مؤكد', 'خائن', 'بطل', 'عدو']
        for word in bias_keywords:
            if word in text:
                bias_score += 15
                warnings.append(f"كلمة انحياز محتملة: {word}")
        
        return {
            "score": max(0, 100 - bias_score),
            "warnings": warnings,
            "status": "تم التحليل وفق بروتوكول SAP",
            "sovereignty": "القرار النهائي لعقلك"
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def run_analysis():
    data = request.json
    content = data.get('content', '')
    result = SovereignLogic.analyze(content)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
    
