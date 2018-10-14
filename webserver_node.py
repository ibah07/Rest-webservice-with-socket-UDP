from flask import Flask, abort
import json
import socket, sys
app = Flask(__name__)
PORT = 7555
MAX = 65535

temp= []
@app.route('/node', methods=['GET'])
def semua():
    return json.dumps(temp)

@app.route('/node/<int:node_id>', methods=['GET'])
def satu(node_id):
    node = None
    for n in temp :
        if n["id"] == node_id :
            node = n
    if node :
        return json.dumps(node)
    else :
        abort(404)

if __name__=='__main__':
    app.run(debug=True, port=7555)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', PORT))
    while True:
        datax, address = s.recvfrom(MAX)
        temp.append(datax)
        print 'The client says', datax
