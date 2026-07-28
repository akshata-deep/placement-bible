# ======== FEE RECEIPT ========

# Student Name :
# Course Fee :
# Scholarship :
# Final Fee :

# Type of Final Fee :

# =============================

student_name = "Akshata"
course_fee = "45000"
scholarship = "5000"


course_fee_int = int(course_fee)
scholarship_int = int(scholarship)
final_fee = course_fee_int + scholarship_int
print(f"======== FEE RECEIPT ========\n"
      f"Student Name : {student_name}\n"
      f"Course Fee : {course_fee_int}\n"
      f"Scholarship : {scholarship_int}\n"
      f"Final fee : {final_fee}\n\n"
      f"Type of Final Fee : {type(final_fee)}\n"
      f"=============================")