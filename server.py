from flask import Flask, request, jsonify
import sys
import os

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    filepath = data.get('filepath')
    
    if not filepath:
        return jsonify({'error': 'No filepath provided'}), 400
    
    try:
        # Import and run your main.py logic here
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        import main
        result = main.process_audio(filepath)  # You'll need to modify main.py to have this function
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 