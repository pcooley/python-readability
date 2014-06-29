from bottle import post, route, run, template, request, BaseResponse, response
import sys
import os
import barrister

sys.path.append('./')      # import the root directory
class ReadabilityService(object):

    def readability(self, req):
        stringlength = len(req["text"])
        response = { "length":"%s" %(stringlength)}
        return response

@route('/hello2/<name>')
def index(name):
        return template('<b>Hello {{name}}</b>!', name=name)

@post('/readability')
def read():
    resp_data = server.call_json(request.body.getvalue())
    response.content_type="application/json"
    return resp_data

@post('/hello')
def hello():
    print request.json
    return "Hello World!"


fn = os.path.join(os.path.dirname(__file__), './idl/readability.json')
contract = barrister.contract_from_file(fn)
server = barrister.Server(contract)
server.add_handler("ReadabilityService", ReadabilityService())


if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True)
