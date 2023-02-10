from flask_cors import CORS
from flask_api import status
from flask import Flask, request,jsonify
import trainer

app = Flask(__name__)
CORS(app)


@app.route('/api',methods=["POST"])
def db_storage():
  user_input = request.json['Question']
  return jsonify({'data':{'Response':str(trainer.brain(user_input))},
                    'status':status.HTTP_201_CREATED
                  })

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)