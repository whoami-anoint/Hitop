from flask import Flask, render_template
import subprocess
from datetime import datetime

app = Flask(__name__)

def get_top_output():
    # Run the 'top' command and capture its output
    top_output = subprocess.check_output(['top', '-n', '1', '-b'])
    return top_output.decode('utf-8')

def get_current_time():
    # Get the current time in a readable format
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def get_running_services():
    # Run the 'systemctl' command to list running services
    services_output = subprocess.check_output(['systemctl', '--no-pager', 'list-units', '--state', 'running', '--plain'])
    return services_output.decode('utf-8')

@app.route('/')
def index():
    # Get top command output, current time, and running services
    top_output = get_top_output()
    current_time = get_current_time()
    running_services = get_running_services()

    # Split the top output into lines
    top_lines = top_output.split('\n')

    # Pass the information to the template
    return render_template('index.html', top_lines=top_lines, current_time=current_time, running_services=running_services)

if __name__ == '__main__':
    app.run(debug=True)
