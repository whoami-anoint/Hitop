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

def get_inactive_services():
    # Run the 'systemctl' command to list inactive services
    inactive_services_output = subprocess.check_output(['systemctl', '--no-pager', 'list-units', '--state', 'inactive', '--plain'])
    return inactive_services_output.decode('utf-8')

@app.route('/')
def index():
    # Get top command output, current time, and running/inactive services
    top_output = get_top_output()
    current_time = get_current_time()
    running_services = get_running_services()
    inactive_services = get_inactive_services()

    # Split the top output into lines
    top_lines = top_output.split('\n')

    # Split the running and inactive services into lists
    running_services_list = [line.split() for line in running_services.split('\n') if line]
    inactive_services_list = [line.split() for line in inactive_services.split('\n') if line]

    # Pass the information to the template
    return render_template('index.html', top_lines=top_lines, current_time=current_time,
                           running_services=running_services_list, inactive_services=inactive_services_list)

@app.route('/running-services')
def running_services():
    # Get running services
    running_services = get_running_services()

    # Split the running services into a list
    running_services_list = [line.split() for line in running_services.split('\n') if line]

    # Pass the information to the template
    return render_template('running_services.html', running_services=running_services_list)

if __name__ == '__main__':
    app.run(debug=True)
