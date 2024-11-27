from flask import Flask, request, jsonify
from web_crawler import crawl 
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://10.96.0.101:27017")
db = client['mongodb-service-cluster']

@app.route('/crawl', methods=['GET'])
def crawl_url():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL parameter is required"}), 400

    content = crawl(url)
    if content:
        db.content.insert_one(content)
        return jsonify({"Crawled content added to database"}), 200
    else:
        return jsonify({"error": "Failed to retrieve content"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
