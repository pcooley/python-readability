from bottle import route, run
import sys
import os
import barrister

sys.path.append('./')      # import the root directory
class ReadabilityService(object):

    def readability(self, request):
        return request

@route('/readability')
def read():
        resp_data = server.call_json(request.data)
        resp = make_response(resp_data)
        resp.headers['Content-Type'] = 'application/json'
        return resp

@route('/hello')
def hello():
    return "Hello World!"

fn = os.path.join(os.path.dirname(__file__), './idl/readability.json')
contract = barrister.contract_from_file(fn)
server = barrister.Server(contract)
server.add_handler("ReadabilityService", ReadabilityService())


if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True)
