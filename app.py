from flask import Flask, jsonify

app = Flask(__name__)

# Mock data with VVIP field
npwp_data = [
    {"npwp": "01.234.567.8-123.000", "name": "Budi Santoso", "address": "Jl. Sudirman No. 123, Jakarta", "vvip": False},
    {"npwp": "98.765.432.1-456.000", "name": "Siti Rahayu", "address": "Jl. Thamrin No. 456, Jakarta", "vvip": True},
    {"npwp": "45.678.901.2-789.000", "name": "Ahmad Hidayat", "address": "Jl. Gatot Subroto No. 789, Jakarta", "vvip": False},
]

citizen_data = [
    {"nik": "3101012345678901", "name": "Dewi Lestari", "dob": "1990-05-15", "vvip": False},
    {"nik": "3202023456789012", "name": "Agus Prakoso", "dob": "1985-11-22", "vvip": True},
    {"nik": "3303034567890123", "name": "Rina Wulandari", "dob": "1995-03-30", "vvip": False},
]

@app.route('/api/npwp', methods=['GET'])
def get_npwp_data():
    return jsonify(npwp_data)

@app.route('/api/npwp/<npwp>', methods=['GET'])
def get_npwp_info(npwp):
    for data in npwp_data:
        if data['npwp'] == npwp:
            return jsonify(data)
    return jsonify({"error": "NPWP not found"}), 404

@app.route('/api/citizens', methods=['GET'])
def get_citizen_data():
    return jsonify(citizen_data)

@app.route('/api/citizens/<nik>', methods=['GET'])
def get_citizen_info(nik):
    for data in citizen_data:
        if data['nik'] == nik:
            return jsonify(data)
    return jsonify({"error": "NIK not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)