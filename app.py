from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Multi-Platform Video Downloader API!"

@app.route('/download', methods=['GET'])
def download_video():
    url = request.args.get('url')

    if not url:
        return jsonify({"success": False, "message": "Invalid request, URL is required"}), 400

    ydl_opts = {
        'cookies': 'cookies.txt',  # Ensure this file is in the same directory
        'format': 'best',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            download_url = info.get("url", None)
            
            if download_url:
                return jsonify({"success": True, "downloadUrl": download_url})
            else:
                return jsonify({"success": False, "message": "Failed to get video URL"}), 500

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
