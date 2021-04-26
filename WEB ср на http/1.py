from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def do():
    return jsonify(
    {
        "operation mode": [
            108,
            93,
            83,
            115,
            103,
            46,
            120,
            51
        ],
        "slow cooling": [
            31,
            138,
            42,
            58,
            53,
            76,
            56,
            101
        ],
        "fast cooling": [
            41,
            84,
            46,
            8,
            30,
            43,
            89,
            116
        ],
        "extreme cooling": [
            40,
            97,
            125,
            129,
            87,
            33,
            109,
            30
        ],
        "medium cooling": [
            45,
            4,
            81,
            76,
            94,
            120,
            29,
            120
        ]
    })


if __name__ == '__main__':
    app.run(host='localhost', port=8080)
