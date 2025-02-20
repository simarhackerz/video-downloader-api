import os
import yt_dlp
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/download', methods=['GET'])
def download_video():
    url = request.args.get('url')
    
    if not url:
        return jsonify({"success": False, "message": "URL is required"}), 400

    ydl_opts = {
        'cookies': 'cookies.txt',  # Yeh line add karein
        'format': 'best',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return jsonify({"success": True, "info": info})
    
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
