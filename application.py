from flask import Flask, render_template, request, flash, redirect, sessions

app = Flask(__name__)

# this is because I'm using sessions to show a flash message
app.secret_key = 'some_secret'

# shows the home page
@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")

# shows the application form
@app.route("/application-form")
def show_application_form():
    """shows the application form"""

    # directs the user to the application form page. 
    return render_template("application-form.html")

# shows the applicaiton response after filling out the form. 
# if a number isn't entered for base salary, a flash message directs the user
# to enter a numerical value. I wanted flash practice. 
@app.route("/application-response", methods=["POST"])
def show_application_response():
    """takes information from the application form and 
    renders a response based on the input"""

    # gathers data from the form and stores it in variables
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    job_title = request.form.get("job_title")

    # if a minimum salary is entered as a number, format it. 
    # if a salary isn't entered, flashes a message to only use numerical values. 
    if request.form.get("salary").isdigit():
        # integerizes the input, then formats it to a string with commas
        # and a '$' symbol. I couldn't figure out how to format a string to 
        # money, so I intergerized it first, then re-cast it as a string. 
        salary = "${:,}".format(int(request.form.get("salary")))
        # passes the user to a response page verifying the info submitted. 
        return render_template("application-response.html", 
                            first_name=first_name,
                            last_name=last_name,
                            job_title=job_title,
                            salary=salary)
    else: 
        # flashes a message to input a salary value and redirects to the form. 
        flash("Pleae enter a numerical value only for your minimum salary requirement")
        return redirect("/application-form")
    


if __name__ == "__main__":
    app.run(debug=True)


    