#Tutoring Service File

#Define Function 
def get_tutoring_service():
    #Instantiates list to store student's information 
    student_info_list = []
    #Prompt user to input student's name
    student_name = input("Input student's name: ")
    #Append student's name to list
    student_info_list.append(student_name)

    #Prompt user to input student's academic goals
    student_goals = input("Input student's academic goals: ")
    #Append student's academic goals to list 
    student_info_list.append(student_goals)

    #Prompt user to input student's subject of interest
    student_subjects = input("Input student's subject of interest: ")
    #Append student's subject of interest to list 
    student_info_list.append(student_subjects)

      #Prompt user to input student's academic level
    student_level = input("Input student's academic level: ")
    #Append student's academic level to list 
    student_info_list.append(student_level)

    #Return student's information as a list
    return student_info_list

  #Define Function 
def provide_instruction(student_info_list):
    #Retrieve student's information from the list 
    student_name = student_info_list[0]
    student_goals = student_info_list[1]
    student_subjects = student_info_list[2]
    student_level = student_info_list[3]

    #Print personalized instruction 
    print("Welcome {0}! To fulfill your academic goals of {1}, here are some tips for your {2} classes. At your level of {3}, it is important to focus on developing your critical thinking and problem solving skills. This is fundamental to understanding difficult concepts and applying them to new problems. Be sure to practice solving problems, review fundamental concepts, and be willing to take risks with new ideas. All the best!".format(student_name, student_goals, student_subjects, student_level))

#Call Function 
student_info_list = get_tutoring_service()
provide_instruction(student_info_list)