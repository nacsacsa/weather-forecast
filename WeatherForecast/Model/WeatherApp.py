from flask import Flask, render_template
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

if __name__ == '__main__':
    app.run(debug=True)