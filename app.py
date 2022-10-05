from datetime import date
from urllib import request
from flask import Flask, render_template, request
import datetime

app = Flask(__name__)
global studentOrganisationDetails
# Assign default 5 values to studentOrganisationDetails for Application  3.


@app.get('/')
def index():
    # Complete this function to get current date and time assign this value to currentDate, display this data on index.html
    currentDate = datetime.datetime.now()
    return render_template('index.html', currentDate=currentDate)


@app.get('/calculate')
def displayNumberPage():
    # Complete this function to display form.html page
    return render_template('form.html')


@app.route('/calculate', methods=['POST'])
def checkNumber():
    # Get Number from form and display message according to number
    # Display "Number {Number} is even" if given number is even on result.html page
    # Display "Number {Number} is odd" if given number is odd on result.html page
    # Display "No number provided" if value is null or blank on result.html page
    # Display "Provided input is not an integer!" if value is not a number on result.html page
    global number
    number = request.form['number']

    # Write your to code here to check whether number is even or odd and render result.html page
    global outcome
    outcome = ''
    if (number.isdecimal()):
        number = int(number)
        if(number % 2 == 0):
            outcome = str(number) + ' is even'
        else:
            outcome = str(number) + ' is odd'
    else:
        outcome = "Not an integer"
    
    return render_template('result.html', outcome=outcome)



@app.get('/addStudentOrganisation')
def displayStudentForm():
    # Complete this function to display studentForm.html page
    return render_template('studentForm.html')


@app.route('/addStudentOrganisation', methods=['POST'])
def displayRegistrationPage():
    # Get student name and organisation from form.
    organizations = [
    "Charlotte Hack",
    "Code9",
    "CompSci Club",
    "Cool Coders",
    "Pragmatic Programmers",
    ]

    studentName = request.form['name']
    organization = request.form['organization']

    # Append this value to studentOrganisationDetails
    studentOrganisationDetails = {'Tom':'Charlotte Hack', 'Hunter':'Code9'}
    if studentName != "" and organization != "" and organization in organizations:
        studentOrganisationDetails[studentName] = organization

    # Display studentDetails.html with all students and organisations
    return render_template('StudentDetails.html', studentOrganisationDetails = studentOrganisationDetails)
