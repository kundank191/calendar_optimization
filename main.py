from flask import Flask, render_template, request, send_from_directory
from app.calendar_api import add_alarm_to_calender_events

app = Flask(__name__, static_folder='static', static_url_path='', template_folder='templates')

@app.route('/')
def index():
    """
    This function will render the index page
    """

    return render_template('index.html')

@app.route('/update_calendar', methods=['POST'])
def update_calendar():
    """
    This function will update the calendar events with the alarm
    """
    file_name = request.files['file']

    print(file_name)

    send_from_directory('./logs/',file_name, as_attachment=True)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
