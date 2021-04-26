from datetime import date
from time import gmtime, strftime
from scheduler.controller import Controller

from flask import Flask, jsonify, request


app = Flask(__name__)

controller = Controller()


@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'GET':

        user_id = request.args.get('user_id')
        response = controller.getAppointments(user_id)
        return jsonify(response)

    elif request.method == 'POST':

        date_time = request.args.get('date_time')
        user_id = request.args.get('user_id')

        response = controller.addAppointment(date_time, user_id)
        return jsonify(response)



if __name__ == '__main__':
  app.run(host='0.0.0.0', port = 5001, debug=True)