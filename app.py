from flask import Flask, request, jsonify
from web_crawler import crawl 

app = Flask(__name__)

@app.route('/crawl', methods=['GET'])
def crawl_url():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL parameter is required"}), 400

    content = crawl(url)
    if content:
        return jsonify({"content": content}), 200
    else:
        return jsonify({"error": "Failed to retrieve content"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
