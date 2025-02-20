from flask import Flask, request, jsonify
import yt_dlp
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Multi-Platform Video Downloader API!"

@app.route('/download', methods=['GET'])
def download_video():
    url = request.args.get('url')
    if not url:
        return jsonify({"success": False, "message": "Invalid request, URL required"}), 400

    # yt-dlp options
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'outtmpl': 'downloads/%(title)s.%(ext)s'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            video_url = info_dict.get("url", None)
            if video_url:
                return jsonify({"success": True, "downloadUrl": video_url})
            else:
                return jsonify({"success": False, "message": "Failed to fetch video"}), 500
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
