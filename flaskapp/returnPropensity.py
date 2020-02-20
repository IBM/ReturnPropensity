#!/usr/bin/python3

# -*- coding: utf-8 -*-
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import json
import os
import requests
from dotenv import load_dotenv
from flask import Flask, request, session, render_template, flash

app = Flask(__name__)

app.config.update(dict(
    DEBUG=True,
    SECRET_KEY=os.environ.get('SECRET_KEY', 'development key')
))

# the values for each key indicate the following:
# 1. type = number, float, string or category
# if type = number, the remaining values are:
# 2. default value
# 3. min value
# 4. max value
# if type = category, the remaining values are all the valid values for that field.

input_fields = {
    "BASKET_SIZE": ["number", 0, 0, 1000000],
    "EXTN_COMPOSITION": ["string"],
    "CARRIER_SERVICE_CODE_OL": ["string"],
    "CATEGORY": ["string"],
    "COUNTRY_OF_ORIGIN_OI": ["string"],
    "DAY_OF_MONTH": ["number", 1, 1, 31],
    "DAY_OF_WEEK": ["category", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
    "DAY_OF_YEAR": ["number", 1, 1, 366],
    "EXTN_BRAND": ["string"],
    "EXTN_DISCOUNT_ID": ["string"],
    "EXTN_IS_GIFT": ["category","N","Y"],
    "EXTN_IS_PREORDER": ["category","N","Y"],
    "EXTN_SHIP_TO_CITY": ["string"],
    "EXTN_SHIP_TO_COUNTRY": ["string"],
    "EXTN_SEASON": ["string"],
    "LIST_PRICE": ["number", 0, 0, 1000000],
    "MONTH_OF_YEAR": ["number", 1, 1, 12],
    "OTHER_CHARGES": ["float", 0, -1000000, 1000000],
    "OTHER_CHARGES_OL": ["float", 0, -1000000, 1000000],
    "REQ_DELIVERY_DATE": ["number", 0, 0, 1],
    "TOTAL_AMOUNT_USD": ["float", 0, -1000000.0, 1000000.0],
    "WEEKEND": ["number", 0, 0, 1],
    "ZIP_CODE": ["string"],
    "MTS_CTS": ["number", 0, 0, 100],
    "HOUR_OF_DAY": ["number", 0, 0, 23],
    "LOCKID": ["number", 0, 0, 1000]
}

labels = ["Order will not be returned", "Order will be returned"]


def generate_input_lines():
    result = f'<table>'

    counter = 0
    for k in input_fields.keys():
        fields = input_fields[k]
        if (counter % 2 == 0):
            result += f'<tr>'
        result += f'<td>{k}'
        if (fields[0] == "number" or fields[0] == "float"):
            if len(fields) > 2:
                min = fields[2]
                max = fields[3]
                if fields[0] == "number":
                    step = 1
                else:
                    step = 0.01
                result += f'<input type="number" class="form-control" name="{k}" min="{min}" max="{max}" step="{step}" id="{k}" value="{fields[1]}" required (this.value)">'
            else:
                result += f'<input type="number" class="form-control" name="{k}" id="{k}" value="{fields[1]}" required (this.value)">'
        elif (fields[0] == "string"):
            result += f'<input type="string" class="form-control" name="{k}" id="{k}" required (this.value)">'
        elif (fields[0] == "category"):
            options = fields[1:]
            result += f'<select class="form-control" name="{k}">'
            for value in options:
                result += f'<option value="{value}" selected>{value}</option>'
            result += f'</select>'
        result += f'</td>'
        if (counter % 2 == 1):
            result += f'</tr>'
        counter = counter + 1

    result += f'</table>'

    return result


app.jinja_env.globals.update(generate_input_lines=generate_input_lines)


class churnForm():

    @app.route('/', methods=['GET', 'POST'])
    def index():

        if request.method == 'POST':
            ID = 999

            session['ID'] = ID
            data = {}

            for k, v in request.form.items():
                data[k] = v
                session[k] = v

            scoring_href = os.environ.get('URL')
            mltoken = os.environ.get('TOKEN')

            if not (scoring_href and mltoken):
                raise EnvironmentError('Env vars URL and TOKEN are required.')

            for field in input_fields.keys():
                if input_fields[field][0] == "number":
                    data[field] = int(data[field])
                if input_fields[field][0] == "float":
                    data[field] = float(data[field])

            input_data = list(data.keys())
            input_values = list(data.values())

            payload_scoring = {"input_data": [
                {"fields": input_data, "values": [input_values]} 
            ]}
            print("Payload is: ")
            print(payload_scoring)
            header_online = {
                'Cache-Control': 'no-cache',
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + mltoken}
            response_scoring = requests.post(
                scoring_href,
                verify=False,
                json=payload_scoring,
                headers=header_online)
            result = response_scoring.text
            print("Result is ", result)
            result_json = json.loads(result)

            result_keys = result_json['predictions'][0]['fields']
            result_vals = result_json['predictions'][0]['values']

            result_dict = dict(zip(result_keys, result_vals[0]))
            churn_risk = result_dict["prediction"]
            no_percent = result_dict["probability"][0] * 100
            yes_percent = result_dict["probability"][1] * 100
            flash('Percentage of this customer returning the order is: %.0f%%'
                  % yes_percent)
            return render_template(
                'score.html',
                result=result_dict,
                churn_risk=churn_risk,
                yes_percent=yes_percent,
                no_percent=no_percent,
                response_scoring=response_scoring,
                labels=labels)

        else:
            return render_template('input.html')


load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
port = os.environ.get('PORT', '5000')
host = os.environ.get('HOST', '0.0.0.0')
if __name__ == "__main__":
    app.run(host=host, port=int(port))
