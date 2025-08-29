
employee_file = open("FernandoEx", "r")

for employee in employee_file.readlines():

    print(employee)


employee_file.close()