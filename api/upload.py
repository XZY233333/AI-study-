from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({"success": False, "error": "No file provided"}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({"success": False, "error": "No file selected"}), 400
        
        file_ext = file.filename.split('.')[-1].lower()
        
        if file_ext not in ['pptx', 'pdf', 'txt']:
            return jsonify({"success": False, "error": "Unsupported file type"}), 400
        
        # 模拟提取知识点
        notes = [
            f"从{file_ext}文件中提取的知识点1",
            f"从{file_ext}文件中提取的知识点2",
            f"从{file_ext}文件中提取的知识点3"
        ]
        
        return jsonify({
            "success": True, 
            "notes": notes,
            "fileName": file.filename
        })
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"})

# Vercel需要这个导出
handler = app
