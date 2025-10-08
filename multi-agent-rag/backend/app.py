from flask import Flask, request, jsonify
from .controllers.controller import route_request, init_controllers
from db.init_db import init_db, get_recent_traces
import os

def create_app():
    app = Flask(__name__, static_folder='../frontend', static_url_path='/')
    init_db(app)
    init_controllers(app)

    @app.route('/upload_pdf', methods=['POST'])
    def upload_pdf():
        f = request.files.get('file')
        if not f or not f.filename.lower().endswith('.pdf'):
            return jsonify({'error':'invalid file'}), 400
        fname = f"uploaded_{int(__import__('time').time())}.pdf"
        save_path = app.config.get('UPLOAD_DIR', './uploads')
        os.makedirs(save_path, exist_ok=True)
        f.save(os.path.join(save_path, fname))
        return jsonify({'file_id': fname}), 201

    @app.route('/ask', methods=['POST'])
    def ask():
        payload = request.json or {}
        resp = route_request(payload)
        return jsonify(resp)

    @app.route('/logs', methods=['GET'])
    def logs():
        traces = get_recent_traces(limit=20)
        return jsonify(traces)

    @app.route('/')
    def index():
        return app.send_static_file('index.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=7860, debug=True)
