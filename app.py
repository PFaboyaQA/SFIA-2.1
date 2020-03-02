from random import randint
import string
import random
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/random_number', methods=['GET'])
def random_number(n=3):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return Response(range_start, range_end, mimetype='text/plain')


@app.route('/random_string', methods=['GET'])
def random_string(size=3, chars=string.ascii_uppercase):
    string=''.join(random.choice(chars) for _ in range(size))
    return Response(string, mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)


