from flask import Flask, render_template, request, redirect, flash, url_for, abort
from builtins import enumerate

app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    # Read the contents of the tasks.txt file
    with open('tasks.txt', 'r') as file:
        tasks = file.read()

    # Split the contents of the file into an array of tasks
    task_list = tasks.split('\n')

    # Render the HTML template with the task list
    return render_template('home.html', tasks=task_list, enumerate=enumerate)

# Define the route for adding a new task
@app.route('/add_task', methods=['POST'])
def add_task():
    # Get the task from the form data
    task = request.form['task']

    # If the task is not empty, append it to the tasks.txt file
    if task:
        with open('tasks.txt', 'a') as file:
            file.write(task + '\n')

    # Redirect back to the home page
    return redirect('/')

@app.route('/delete_task/<int:id>', methods=['POST'])
def delete_task(id):
    # Read the contents of the tasks.txt file
    with open('tasks.txt', 'r') as file:
        tasks = file.readlines()

    # Find the task with the specified ID and remove it from the list
    task_found = False
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            if not task.startswith(f'{id}\t'):
                file.write(task)
            else:
                task_found = True

    # If the task is not found, abort with a 404 error
    if not task_found:
        abort(404)

    # Redirect back to the home page
    return redirect('/')




if __name__ == '__main__':
    app.run(debug=True)
