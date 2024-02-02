from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route('/weather')
def weather():
  return render_template('weather.html')

@app.route('/bmi_calculator', methods=['GET', 'POST'])
#
def bmi_calculator():
  if request.method == 'POST':
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    bmi = calculate_bmi(height, weight)
    # Log BMI to JSON or TXT file
    log_bmi_result({'height': height, 'weight': weight, 'bmi': bmi})
    return render_template('bmi_calculator.html', bmi=bmi)
  return render_template('bmi_calculator.html')

#Function to calculate BMI
def calculate_bmi(height, weight):
  return weight / (height**2)

def log_bmi_result(data):
    import json

    result = {'bmi': data}

    # Read existing data if the file already exists
    try:
        with open('data/bmi_results.json', 'r') as file:
            existing_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []

    # Append the new result to the array
    existing_data.append(result)

    # Write the updated array back to the file
    with open('data/bmi_results.json', 'w') as file:
        json.dump(existing_data, file, indent=2)


if __name__ == '__main__':
  app.run(debug=False)
