from flask import Flask, request, jsonify

app = Flask(__name__)

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.',
    ')': '-.--.-', ' ': '/'
}

@app.route('/text-to-morse')
def text_to_morse():
    text = request.args.get('text', '')
    morse = ' '.join(MORSE_CODE_DICT.get(ch.upper(), '') for ch in text)
    return jsonify({
        "text": text,
        "morse": morse
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
