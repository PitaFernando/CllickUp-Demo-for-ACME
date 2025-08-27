# quick Flask server just to test webhook calls
# nothing fancy, just prints data

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json(silent=True) or {}
    print('✅ Webhook received:', data)
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(port=3000)