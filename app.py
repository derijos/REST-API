'''
@author Dereck Jos
Rest Api Order
X = [[N, P, K, ph, ec, oc, S, fe, cu, Mn, B]]
'''

from flask import Flask, request, jsonify
import pickle
import json

app = Flask(__name__)

@app.route("/model_pred", methods=["POST"])
def model_pred():
    model = pickle.load(open("model.cpickle","rb"))
    data = json.loads(request.data)
    X = [i for i in data.values()]
    pred = model.predict(X)[0]
    return jsonify(int(pred))

if __name__ == "__main__":
    app.run(debug = True)
