from flask import Flask, jsonify, request

app = Flask(__name__)

# Data for the units
units_data = {
    "Master Puppeteer": "800-1k",
    "Limitless Shadow": "1k",
    "Agonized Springtrap": "4.5k",
    "Fractured Bonnie": "1.5k-2k",
    "RWQFSFASXC": "4.5k",
    "Valkyrie Prime": "55k",
    "Nautic Crusher Mangle": "30k",
    "Animdude": "4k",
    "Bomber Boy": "2k",
    "Fortified Endo 02": "8k-10k",
    "Overclocked Puppeteer": "10k",
    "Deadeye Freddy": "21k-22k",
    "President Freddy": "2k-2.5k",
    "Overseer Foxy": "12k-12.5k",
    "Frostbite Freddy": "75k-80k",
    "Astral Bonnie": "60k+",
    "Old Man Consequences": "100k-120k",
    "Gravelord Foxy": "45k",
    "Kronos Endo Freddy": "50k+",
    "Dark Knight Puppet": "700k+",
    "Black Ice Freddy": "15k-16k",
    "Old Man Krampus": "200k"
}

@app.route("/api/values-api", methods=["GET"])
def get_value():
    unit_name = request.args.get("unit_name")
    if not unit_name:
        return jsonify({"error": "Please provide a unit name."}), 400

    value = units_data.get(unit_name)
    if not value:
        return jsonify({"error": "Unit not found."}), 404

    return jsonify({"unit_name": unit_name, "value": value})

if __name__ == "__main__":
    app.run(debug=True)
