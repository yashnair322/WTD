# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
import re
from markupsafe import escape

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv('SECRET_KEY', 'development-key')  # For flash messages

db = SQLAlchemy(app)

# Define Contact model
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<Contact {self.name}>'

# Create tables if they don't exist
with app.app_context():
    db.create_all()

# Validation functions
def validate_name(name):
    if not name or len(name) < 2:
        return False, "Name must be at least 2 characters long"
    if len(name) > 100:
        return False, "Name cannot exceed 100 characters"
    return True, ""

def validate_email(email):
    # Basic email validation using regex
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not email or not re.match(email_pattern, email):
        return False, "Please enter a valid email address"
    if len(email) > 100:
        return False, "Email cannot exceed 100 characters"
    return True, ""

def validate_subject(subject):
    if not subject:
        return False, "Subject is required"
    if len(subject) > 200:
        return False, "Subject cannot exceed 200 characters"
    return True, ""

def validate_message(message):
    if not message or len(message) < 10:
        return False, "Message must be at least 10 characters long"
    if len(message) > 5000:
        return False, "Message cannot exceed 5000 characters"
    return True, ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        subject = request.form.get('subject', '').strip()
        message = request.form.get('message', '').strip()
        
        # Validate input data
        validation_errors = []
        
        name_valid, name_error = validate_name(name)
        if not name_valid:
            validation_errors.append(name_error)
            
        email_valid, email_error = validate_email(email)
        if not email_valid:
            validation_errors.append(email_error)
            
        subject_valid, subject_error = validate_subject(subject)
        if not subject_valid:
            validation_errors.append(subject_error)
            
        message_valid, message_error = validate_message(message)
        if not message_valid:
            validation_errors.append(message_error)
        
        # If there are validation errors, return to form with error messages
        if validation_errors:
            for error in validation_errors:
                flash(error, 'error')
            return render_template('contact.html', 
                                  name=escape(name), 
                                  email=escape(email), 
                                  subject=escape(subject), 
                                  message=escape(message))
        
        # Create new contact entry
        new_contact = Contact(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # Add to database
        try:
            db.session.add(new_contact)
            db.session.commit()
            flash('Your message has been sent successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred: {str(e)}', 'error')
            return render_template('contact.html', 
                                  name=escape(name), 
                                  email=escape(email), 
                                  subject=escape(subject), 
                                  message=escape(message))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
