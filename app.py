from flask import Flask, render_template, request
import caesar_cipher

app = Flask(__name__)


@app.route("/") # If someone opens our application
def index():    # Run this function
    return render_template("index.html") # load the HTML file.

@app.route("/results", methods=["POST"]) # When form is submitted
def result():                            # Run this function
    message = request.form["message"] # Get the message from the form and store in message
    shift = int(request.form["shift"]) # Get shift value from form and convert to int and store in shift
    choice = request.form["choice"] # Get choice of encode or decode and store in choice

    if choice == "encode": # If encode
        # Call enocde(msg, shift) from our logic file and store in output
        output = caesar_cipher.encode(message, shift) 
    else: # If decode
        # Call decode(msg, shift) from our logic file and store in output
        output = caesar_cipher.decode(message, shift)

    # Load results.html and pass in the result, choice, original message, and shift value.
    return render_template("results.html", result = output,
                           choice = choice,
                           original = message,
                           shift = shift)

if __name__ == "__main__":
    # Auto reloads the server when changes are saved 
    app.run(debug=True) 