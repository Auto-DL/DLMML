from flask import Flask, request
from flask import jsonify, make_response
import json
import os
import importlib
import sys

sys.path.append("..")


from utils import json_to_dict

from parser import *

app = Flask(__name__)

@app.route('/generate/', methods=['GET', 'POST'])
def generate(): 
    inputs = request.get_json()
    inputs = json_to_dict.MakeDict(inputs).parse()
    lib = inputs.get('lib', 'keras')
    lang = inputs.get('lang', 'python')
    parser_path ='parser.'+lang+'.'+lib+'.main'
    
    parser = importlib.import_module(parser_path)

    status, error = parser.generate_code(inputs)
    if status:
        print("Error", error)
        msg = error
        path = ''
    else:
        print("File generated") 
        msg = 'File Generated Successfully'
        path = 'file:///'+os.getcwd()+os.sep+'test.py'

    response = {
                    'message': msg, 
                    'path': path
                            }
    res = make_response(jsonify(response))

    return res
    

    


if __name__ == '__main__':
    app.run(port=5000, debug=True)