from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Multi-Platform Video Downloader API!"

@app.route('/download', methods=['GET'])
def download_video():
    url = request.args.get('url')
    platform = request.args.get('platform')

    if not url or not platform:
        return jsonify({"success": False, "message": "Invalid request"}), 400

    # Example API for free video download (SaveFrom API or any other service)
    api_url = f"https://api.savefrom.net/?url={url}"
    response = requests.get(api_url).json()

    if "url" in response:
        return jsonify({"success": True, "downloadUrl": response["url"]})
    else:
        return jsonify({"success": False, "message": "Failed to fetch video"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
