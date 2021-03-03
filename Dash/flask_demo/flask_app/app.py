import pickle

import numpy as np
from flask import Flask, render_template, request, url_for, redirect

from database import create_tabel

app = Flask(__name__)
from encoding_input_data import enc_dict

create_tabel()

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


def predction(pred_values):
    model = pickle.load(open('model.pkl', 'rb'))
    output = model.predict(pred_values)
    if (output == 1):
        return "Yes"
    else:
        return "No"


@app.route('/', methods=['POST', 'GET'])
def form_submit():
    y = 0
    if request.method == 'POST':

        values = request.form.to_dict()

        pre_array = encoding_data(enc_dict, values)

        values['Output'] = predction(pre_array)

        from database import insert_values
        y = insert_values(values.values())
        return redirect(url_for('submission', flag=y))
    else:

        return render_template('index.html')


@app.route('/submit_sucess/<flag>')
def submission(flag):
    print(type(flag))
    if (flag == '1'):
        return render_template('submit_success.html')
    else:
        return render_template('unsuccessful.html')


@app.route('/about')
def about():
    return "<h2>hi im nikhil</h2>"


@app.route('/html_login')
def login():
    return render_template('html_login.html')


@app.route("/fetch_data")
def featch_data():
    from database import get_data
    field_names, data = get_data()
    print(field_names, data)

    return render_template('database_show.html', filed_names=field_names, data=data)


if __name__ == '__main__':
    app.run(host='localhost', port=8078, debug=True)
