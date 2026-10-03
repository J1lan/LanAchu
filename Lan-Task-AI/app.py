from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/api/analyze")
def analyze():
    data = request.get_json(silent=True) or {}
    name = data.get("name","").strip()
    kelas = data.get("kelas","").strip()
    email = data.get("email","").strip()
    url = data.get("url","").strip()
    if not all([name, kelas, email, url]):
        return jsonify({"ok":False,"error":"Lengkapi Nama, Kelas, Gmail, dan Link Tugas."}), 400
    return jsonify({"ok":True,"name":name,"kelas":kelas,"email":email,"url":url})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
