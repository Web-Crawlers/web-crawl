from flask import Flask, request, jsonify
from web_crawler import crawl 
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://10.96.0.101:27017")
db = client['mydb']

@app.route('/crawl', methods=['GET'])
def crawl_url():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL parameter is required"}), 400

    content = crawl(url)
    if content:
        try:
            db.Articles.insert_one(content)
            return jsonify({"Response": "Crawled content added to database"}), 200
        except Exception as e:
            return jsonify({"Response": f"{e}"})
    else:
        return jsonify({"error": "Failed to retrieve content"}), 500

@app.route('/reset', methods=['GET'])
def reset_db():
    try:
        db.Articles.delete_many({})
        return jsonify({"Response": "Articles collection has been reset."}), 200
    except Exception as e:
        return jsonify({"Response": f'Failed to reset "Articles" collection (Exception: {e})'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
