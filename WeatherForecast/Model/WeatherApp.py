from flask import Flask, render_template, request, jsonify
import os

app = Flask(
    __name__,
    static_folder=os.path.join(os.path.pardir, 'Frontend/static'),
    template_folder=os.path.join(os.path.pardir, 'Frontend')
)


# Index oldal (időjárás lekérdezés)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/weather', methods=['POST'])
def weather():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Nincs adat küldve'}), 400

        city = data.get('city')
        start_date = data.get('start_date')
        end_date = data.get('end_date')

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
