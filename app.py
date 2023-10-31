from flask import Flask, render_template, request,redirect, url_for
import pickle

app = Flask(__name__)

# Load the trained machine learning model 
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET'])
def predict():

    # Extract form data from query parameters
    marital_status = request.args.get('marital_status')
    application_mode = request.args.get('application_mode')
    application_order = request.args.get('application_order')
    course = request.args.get('course')
    daytime_evening_attendance = request.args.get('attendance')
    previous_qualification = request.args.get('previous_qualification')
    mother_qualification = request.args.get('mother_qualification')
    father_qualification = request.args.get('father_qualification')
    father_occupation = request.args.get('father_occupation')
    displaced = request.args.get('displaced')
    debtor = request.args.get('debtor')
    tuition_fees = request.args.get('tuition_fees')
    gender = request.args.get('gender')
    scholarship = request.args.get('scholarship')
    age_at_enrollment = request.args.get('age_at_enrollment')

    # Check for missing input fields
    if any(field is None or field == '' for field in [marital_status, application_mode, application_order, course,
                                      daytime_evening_attendance, previous_qualification,
                                      mother_qualification, father_qualification, father_occupation,
                                      displaced, debtor, tuition_fees, gender, scholarship,
                                      age_at_enrollment]):
        return render_template('out1.html', prediction_result='Error,Missing Fields', message="Please fill out all required fields.")

    
    # Convert values to integers
    marital_status = int(marital_status)
    application_mode = int(application_mode)
    application_order = int(application_order)
    course = int(course)
    daytime_evening_attendance = int(daytime_evening_attendance)
    previous_qualification = int(previous_qualification)
    mother_qualification = int(mother_qualification)
    father_qualification = int(father_qualification)
    father_occupation = int(father_occupation)
    displaced = int(displaced)
    debtor = int(debtor)
    tuition_fees = int(tuition_fees)
    gender = int(gender)
    scholarship = int(scholarship)
    age_at_enrollment = int(age_at_enrollment)

    #printing just to debug
    print("Feature Values:")
    print(f"Marital Status: {marital_status}")
    print(f"Application Mode: {application_mode}")
    print(f"Application Order: {application_order}")
    print(f"Course: {course}")
    print(f"Attendance: {daytime_evening_attendance}")
    print(f"Previous Qualification: {previous_qualification}")
    print(f"Mother's Qualification: {mother_qualification}")
    print(f"Father's Qualification: {father_qualification}")
    print(f"Father's Occupation: {father_occupation}")
    print(f"Displaced: {displaced}")
    print(f"Debtor: {debtor}")
    print(f"Tuition Fees: {tuition_fees}")
    print(f"Gender: {gender}")
    print(f"Scholarship: {scholarship}")
    print(f"Age at Enrollment: {age_at_enrollment}")
    # Make predictions using the model
    prediction = model.predict([[marital_status, application_mode, application_order, course,
                                 daytime_evening_attendance, previous_qualification,
                                 mother_qualification, father_qualification, father_occupation,
                                 displaced, debtor, tuition_fees, gender, scholarship,
                                 age_at_enrollment]])
    print(prediction)
    if prediction[0] == 'Dropout':
        result = "Based on our analysis, there are higher chances that the student may face difficulties and dropout. Here are some preventive measures:"
    elif prediction[0] == 'Enrolled':
        result = "Congratulations! Based on our analysis, the student is likely to continue their education and stay enrolled."
    elif prediction[0] == 'Graduate':
        result = "Congratulations! Based on our analysis, the student is likely to successfully graduate."
    return render_template('out1.html',prediction_result=prediction[0], message=result)
@app.route('/dropout_preventive')
def dropout_preventive():
    # Render the dropout preventive measures page (create a 'dropout_preventive.html' template for this page)
    return render_template('dropout_preventive.html')

@app.route('/enrollment')
def enrollment():
    # Render the enrollment measures page (create an 'enrollment.html' template for this page)
    return render_template('enrollment_info.html')

@app.route('/graduation')
def graduation():
    # Render the graduation success message (create a 'graduation.html' template for this page)
    return render_template('graduation_message.html')
@app.route('/about')
def about():
    # Render the About Us page (create an 'about.html' template for this page)
    return render_template('about.html')

@app.route('/explore')
def explore():
    # Render the Explore page (create an 'explore.html' template for this page)s
    return render_template('explore.html')
@app.route('/blog')
def blog():
    # Render the Explore page (create an 'explore.html' template for this page)
    return render_template('blog.html')



if __name__ == '__main__':
    app.run(debug=True)
