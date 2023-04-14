#!/usr/bin/env python
import cgi

# Read the contents of the tasks.txt file
with open('tasks.txt', 'r') as file:
    tasks = file.read()

# Split the contents of the file into an array of tasks
task_list = tasks.split('\n')

# Generate HTML to display the tasks
html = '<ul>'
for task in task_list:
    html += '<li>' + cgi.escape(task) + '</li>'
html += '</ul>'

# If the form has been submitted, append the new task to the file
form = cgi.FieldStorage()
if 'task' in form:
    new_task = form['task'].value.strip()
    if new_task:
        with open('tasks.txt', 'a') as file:
            file.write(new_task + '\n')

# Generate HTML for the task form
html += '<form method="post">'
html += '<input type="text" name="task">'
html += '<button type="submit">Add</button>'
html += '</form>'

print('Content-type: text/html\n')
print(html)
