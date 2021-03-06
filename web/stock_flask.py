from flask import Flask, request, render_template
app = Flask(__name__)
app.config['APPLICATION_ROOT'] = "."

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)