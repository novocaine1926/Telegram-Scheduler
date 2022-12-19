from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def schedule():
    if request.method == 'POST':
        # Get the form data
        group = request.form['group']
        message = request.form['message']
        interval = request.form['interval']

        # Run the Python script with the form data
        # You can call a function in your script and pass the form data as arguments
        run_scheduler(group, message, interval)

    # Render the HTML template
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
