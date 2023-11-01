#Q4
#def query_lab_time(F L S)
#No return
#condition:if "CSIT110" or "CSIT810" -->Thu 15:30 - 17:30;
#            "CSIT881"-->Thu 10:30 - 12:30
#           else--> mystery day

def query_lab_time(first_name, last_name, subject_code):
    if (subject_code == "CSIT110" or subject_code == "CSIT810" ):
        print("Hello, {0} {1}!".format(first_name, last_name))
        print("        The subject you query is {0}.".format(subject_code))
        print("        Its online lab is on Thu 15:30 - 17:30.")
    elif (subject_code == "CSIT881"):
        print("Hello, {0} {1}!".format(first_name, last_name))
        print("        The subject you query is {0}.".format(subject_code))
        print("        Its online lab is on Thu 10:30 - 12:30.")
    else:
        print("Hello, {0} {1}!".format(first_name, last_name))
        print("        The subject you query is not in our database.")
        print("        Its online lab is on mystery day.")

print(query_lab_time("Dan", "Murphys'", "CSIT110"))
