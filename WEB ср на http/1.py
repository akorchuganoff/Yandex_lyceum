from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def do():
    return jsonify({
    "organic": [
        {
            "respiration": 3,
            "growth": 9,
            "metabolism": 4,
            "synthesis": 7
        },
        {
            "cleavage": 11,
            "digestion": 5,
            "division": 8,
            "response to stimuli": 1
        }
    ],
    "inorganic": [
        {
            "assimilation": 12,
            "dissimilation": 6
        }
    ]
})


if __name__ == '__main__':
    app.run(host='localhost', port=8080)