from flask import Flask, request

app = Flask(__name__)

@app.route('/reverse', methods=['POST'])
def reverse_string():
    input_string = request.json['input']
    reversed_string = input_string[::-1]
    return {'output': reversed_string}

if __name__ == '__main__':
    app.run(debug=True)