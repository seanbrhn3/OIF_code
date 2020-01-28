from flask import Flask, render_template, url_for, request, jsonify
import json
import requests

app = Flask(__name__)

actuator_list = {
    # actautor name: [externalip address, port actuator is listening on
    "Drone Surveillance Radar": "35.245.211.246",
    "Long Range Surveillance System": "35.221.57.117",
    "RF Tracking System": "35.245.228.136"
}


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if request.get_json() is not None:
            if "ipv4_net" in request.get_json().get("target",{}):
                oif = request.get_json().get("target",{})
                if oif is None:
                    return jsonify(message="message does not work")
                else:
                    actuator_name = oif.get("ipv4_net",{})
                    if str(actuator_name) in actuator_list.values():
                        headers = {"Content-Type": "application/json"}
                        data = {"action":"query", "target":{"features":[]}}
                        #data = request.get_json()
                        response = requests.post("http://"+actuator_name, json=data, headers=headers)
                        print(response.json())
                        res = requests.post("http://35.245.30.172/", headers=headers, json=data)
                        return jsonify(message=response.json())
            else:
                actuator_name = ""
                headers = {"Content-Type": "application/json"}
                data = request.get_json()
                actuator_name = actuator_list["Drone Surveillance Radar"]
                response = requests.post("http://"+actuator_name,json=data,headers=headers)
                print(response.json())
                return jsonify(message=response.json())
        else:
            return jsonify(message="invalid  input")
    else:
        return jsonify(message="you can only post to this url")


if __name__ == '__main__':
    app.run(debug=True)
