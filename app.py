from flask import Flask, request, render_template
import csv
import os
import random
import pandas as pd
app = Flask(__name__)


if os.path.exists('results/results.csv'):
    pass


else:
    print('Creating csv....')
    with open('results/results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['FILE_NAME', 'Ventricles', 'LV', 'Atria',
                         'MV_TV', 'Centered', 'Depth', 'Gain', 'Zoom', 'Segments', 'Border'])


data = pd.read_csv('results/results.csv')
names = data['FILE_NAME'].values

image_directory = 'static/data'
image_paths = []


for i in os.listdir(image_directory):
    if i not in names:

        image_paths.append(os.path.join(image_directory, i))


app.config['IMAGE_PATHS'] = image_paths
CURRENT_IMAGE = random.choice(image_paths)
app.config['CURRENT_IMAGE'] = CURRENT_IMAGE


@app.route("/")
def index():
    random_video = app.config["CURRENT_IMAGE"]

    return render_template("index.html", user_image=random_video)


@app.route("/examples")
def examples():
    return render_template("examples.html")


@app.route('/form', methods=["GET", "POST"])
def get_form():

    ventricle = request.form.get('ventricles', 'NA')
    lv = request.form.get('lv', 'NA')
    atria = request.form.get('atria', 'NA')
    centering = request.form.get('centering', 'NA')
    mv_tv = request.form.get('mv_tv', 'NA')
    mv_tv_optimal = request.form.get('mv_tv_optimal', 'NA')
    gain = request.form.get('gain', 'NA')
    depth = request.form.get('depth', 'NA')
    zoom = request.form.get('zoom', 'NA')
    seg = request.form.get('seg', 'NA')
    border = request.form.get('border', 'NA')

    with open('results/results.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            [app.config['CURRENT_IMAGE'][12:], ventricle, lv, atria, mv_tv, centering, depth, gain, zoom, seg, border])

    app.config['CURRENT_IMAGE'] = random.choice(app.config["IMAGE_PATHS"])

    app.config['IMAGE_PATHS'].remove(app.config['CURRENT_IMAGE'])

    return render_template("index.html", user_image=app.config['CURRENT_IMAGE'])


if __name__ == '__main__':
    app.run(debug=True)
