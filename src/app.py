from flask import Flask, render_template, request
from main.decide import Decide
import numpy as np

app = Flask(__name__)

# Parameters dictionary
params = {
    "LENGTH1": None,
    "RADIUS1": None,
    "EPSILON": None,
    "AREA1": None,
    "Q_PTS": None,
    "QUADS": None,
    "DIST": None,
    "N_PTS": None,
    "K_PTS": None,
    "A_PTS": None,
    "B_PTS": None,
    "C_PTS": None,
    "D_PTS": None,
    "E_PTS": None,
    "F_PTS": None,
    "G_PTS": None,
    "LENGTH2": None,
    "RADIUS2": None,
    "AREA2": None
}

# Function to parse points from the input string
def parse_points(points_str):
    points = [[float(coord) for coord in point.split(',')] for point in points_str.split(';')]
    return np.array(points)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        points_str = request.form['points']
        lcm_path = request.form['lcm_path']
        puv_path = request.form['puv_path']
        parameters = {key: float(request.form[key]) if '.' in request.form[key] else int(request.form[key]) for key in params.keys()}

        points = parse_points(points_str)
        num_points = points.shape[0]

        # Update params dictionary with input values
        params.update(parameters)

        decide_instance = Decide(num_points, points, params, None, None)
        decide_instance.load_lcm_from_file(lcm_path)
        decide_instance.load_puv_from_file(puv_path)

        decide_instance.decide()
        decision = decide_instance.launch

        return render_template('result.html', decision=decision)
    return render_template('index.html', parameters=params)

if __name__ == '__main__':
    app.run(debug=True)
