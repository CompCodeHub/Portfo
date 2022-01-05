from flask import Flask, render_template, request, redirect, url_for
import csv

#Create an instance of flask framework
app = Flask(__name__, template_folder='templates', static_folder='static')


#Routes for our web app
@app.route("/")
def default():
    return render_template("index.html")

#For any additional pages if needed
# @app.route("/<string:page_name>")
# def html_page(page_name='index.html'):
#     return render_template(page_name)

#Send form data if we have a post request
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
      try:
        #Getting a dictionary of the data
        data = request.form.to_dict()
        write_to_csv(data)
        #Redirect to top
        return redirect('/')
      except:
        return 'Did not save to database'
    else:
      return 'Something went wrong. Try again!'



#Write data to txt file
# def write_to_file(data):
#   with open('WebServer/database.txt', 'a') as database:
#     name = data['name']
#     email = data['email']
#     subject = data['subject']
#     message = data['message']
#     file = database.write(f'\nName: {name}\nEmail:{email}\nSubject: {subject}\nMessage: {message} ')

def write_to_csv(data):
  with open('WebServer/database.csv','a', newline = '') as database2:
    name = data['name']
    email = data['email']
    subject = data['subject']
    message = data['message']
    #Get a csv writer object
    csv_writer = csv.writer(database2, delimiter = ',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
    #Write a row to database2
    csv_writer.writerow([name,email,subject,message])


#Needed to run on repl
app.run(host='0.0.0.0', debug=True)