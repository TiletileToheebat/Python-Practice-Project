import streamlit as st

#title of the app
st.title('🎓 My Grading App')
st.subheader('Enter your student details below ⬇️')

#etting columns for details
col1, col2 = st.columns(2)

#student details in two columns
with col1:
	name = st.text_input('Name', placeholder= 'First Name and Last Name')
	name_split = name.split(' ')
	age = st.number_input('Age', step=1)

with col2:
	gender = st.selectbox('select your gender', ['Male', 'Female'])
	student_score = int(st.number_input('Enter your average score', step = 1))


#defining functions for grade
def my_grade_and_remark(student_score):
	if student_score >100:
		grade = 'Input a number betweem 0 and 100'
		remark = 'invalid'
	elif student_score >=80:
		grade = 'A'
		remark = 'Excellent'
	elif student_score >=70:
		grade = 'B'
		remark = 'Very Good'
	elif student_score >=50:
         grade = 'C'
         remark = 'Good'
	elif student_score >=45:
         grade = 'D'
         remark = 'Pass'
	elif student_score >=0:
         grade = 'F'
         remark = 'Fail'
	else:
		grade = 'Input a number betweem 0 and 100'
		remark = 'Invalid'
	return grade, remark

grade = ''
remark = ''
#creating submit button
submit_button = st.button('Click to submit')

#result display
if submit_button:
	grade, remark = my_grade_and_remark(student_score)
	st.success(f'Welcome, {name_split[0]}')
	st.info(f'Full Name: {name}')
	st.info(f'Age: {age}')
	st.info(f'Gender: {gender}')
	st.write(f'Grade: {grade}')
	st.write(f'Remark: {remark}')

# Display balloons for high scores
if grade == 'A' or grade == 'B':
	st.balloons()  
