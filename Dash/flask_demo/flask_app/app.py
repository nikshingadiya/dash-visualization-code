import pickle

import numpy as np
from flask import Flask, render_template, request, url_for, redirect

from database import create_tabel

app = Flask(__name__)
from encoding_input_data import enc_dict

create_tabel()
np.random.seed(25)
'''['Age',
 'Ease and convenient',
 'Time saving',
 'More restaurant choices',
 'Easy Payment option',
 'More Offers and Discount',
 'Good Food quality',
 'Good Tracking system',
 'Unaffordable',
 'Maximum wait time']'''


def encoding_data(enc_dict={}, dec_dict={}):
    list_enc = []
    convert_age = [20, 24, 22, 27, 23, 21, 28, 25, 32, 30, 31, 26, 18, 19, 33, 29]
    for i in dec_dict.keys():
        if (i == 'Age'):
            x = int(dec_dict[i])
            if x in convert_age:
                y = enc_dict[i][str(x)]
                list_enc.append(y)
            else:
                absolute_difference_function = lambda list_value: abs(list_value - x)
                closest_value = min(convert_age, key=absolute_difference_function)
                y = enc_dict[i][str(closest_value)]
                list_enc.append(y)

        else:
            y = enc_dict[i][dec_dict[i]]
            list_enc.append(y)

    return np.array(list_enc).reshape(1, -1)


def random():
    return np.random.randint(0, 235633)


def predction(pred_values):
    model = pickle.load(open('model.pkl', 'rb'))
    output = model.predict(pred_values)
    print(output)
    if (output == 1):
        return "Yes"
    else:
        return "No"


@app.route('/', methods=['POST', 'GET'])
def form_submit():
    y = 0
    x = 0
    if request.method == 'POST':

        values = request.form.to_dict()

        pre_array = encoding_data(enc_dict, values)

        values['Output'] = predction(pre_array)

        from database import insert_values
        x = insert_values(values.values())
        y = random()
        return redirect(url_for('submission', flag=f"{x},{y}"))
    else:
        return render_template('index.html')


@app.route('/submit_sucess/<flag>')
def submission(flag):
    print(flag)
    flag = flag.split(",")
    results = list(map(int, flag))
    print(results)

    if (results[0] == 1):
        return render_template('submit_success.html')
    else:
        return render_template('unsuccessful.html')


@app.route('/about')
def about():
    return "<h2>hi im nikhil</h2>"


@app.route('/html_login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':

        values = request.form.to_dict()
        get_username = values['u']
        get_password = values['p']

        from database import get_admin_data
        x = get_admin_data()
        if (x[0][0] == get_username and x[0][1] == get_password):
            return redirect(url_for('fetch_data'))
        else:
            return render_template('invalid.html')
    return render_template('html_login.html')


@app.route("/admin/fetch_data")
def fetch_data():
    from database import get_data
    field_names, data = get_data()
    print(field_names, data)

    return render_template('database_show.html', filed_names=field_names, data=data)


if __name__ == '__main__':
    app.run(host='localhost', port=8078, debug=True)
