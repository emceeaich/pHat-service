#!/usr/bin/env python

import subprocess
from flask import Flask, request, jsonify
try:
    import http.client as http_status
except ImportError:
    import httplib as http_status

print("""
Control the pHat HD via a web service
""")

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "PUT to / to change display\n {\"script\": script} where script is one of " +  ", ".join(scriptController.list())

class ScriptController():
    _running  = False
    _proc     = None
    _scripts  = {
        "plasma": "/home/pi/Pimoroni/scrollphathd/examples/plasma.py",
        "life": "/home/pi/Pimoroni/scrollphathd/examples/gameoflife.py",
        "fire": "/home/pi/Pimoroni/scrollphathd/examples/forest-fire.py",
        "swirl": "/home/pi/Pimoroni/scrollphathd/examples/swirl.py",
        "none": "/home/pi/clear.py"
    }

    def list(self):
        return self._scripts.keys()

    def update(self, script):

        # which script to run next 
        to_run = self._scripts.get(script, "/home/pi/clear.py")

        print("next script is:", to_run)
        print("state is:", self._running)

        if not self._running: 
            self._proc = subprocess.Popen(["python3", to_run])
            self._running = True
        elif self._running:
            self._proc.kill()
            self._proc = subprocess.Popen(["python3", to_run])
            if to_run == '/home/pi/clear.py':
                self._running = False # clean up

scriptController = ScriptController()

@app.route('/', methods=['PUT'])
def updateDisplay():
    data = request.get_json()

    if data is None:
        script = 'none'
    else:
        try:
            script = data['script']
        except KeyError:
            script = 'none'

    scriptController.update(script)

    return jsonify({"next script": script}), http_status.OK

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
