from datetime import datetime

current_year = datetime.now().year

student = {'name': ['Oliver','Omondi'],
'date_of_birth': 1995,
'phone_number': '0728450575'

}

last_name = student.get('name')

print last_name[1]
print last_name[0],last_name[1]
print student.get('phone_number')
print student.get('date_of_birth')
print current_year - student.get('date_of_birth')

