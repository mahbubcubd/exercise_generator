# Import packages
import json

#Load data
category_dict=json.loads(open("fixtures/categories.json").read())

muscle_dict=json.loads(open("fixtures/muscles.json").read())

exercise_dict=json.loads(open("fixtures/exercises.json").read())

bodyweight_dict=json.loads(open("fixtures/bodyweight.json").read()) # made from https://www.stackhealthy.com/complete-list-of-crossfit-exercises/



# Getting Exercise where language=2
exercises_language_2_list = []

for exercise in exercise_dict:
    try:
        if exercise['fields']['language']==2:
            exercises_language_2_list.append(exercise)
    except Exception as e:
        msg="error in "+ str(exercise['pk']) + ' ' +str(e)

#Create catagories list
category_list=[dict(id=x['pk'],option=str(x['pk'])+"_"+x['fields']['name']) 
                for x in category_dict]

catergory_id_list = [category['pk'] for category in category_dict]


#Create muscles list
muscle_list=[dict(id=x['pk'],option=str(x['pk'])+"_"+x['fields']['name']) 
                for x in muscle_dict]

muscle_id_list= [muscle['pk'] for muscle in muscle_dict]


#initialize variables to take category input
category_input_list = []
break_category_loop = False

while break_category_loop==False:
    #Print all the categories
    print("Please Choose A exercise categories")
    for category in category_list:
        print(category['option'])

    #Print instructions for category
    print("---------------------------------------------------------------------")
    print("Please write the category numbers. You can choose multiple categories at a time. Separate them with COMMA(,)")
    print("For example: 3 5 6 ")

    #Ask for category input from user
    user_category_input = input("Select Categories: ")
    #print(user_category_input)

    
    #------Handle category input here------------#
    try:
        category_input_list = list(map( int, user_category_input.split(',')))
        elements_to_remove= []
        for input in category_input_list:
            if input not in catergory_id_list:
                elements_to_remove.append(input)
                print(str(input), ' is not a valid category')
        category_input_list = set(category_input_list)
        elements_to_remove = set(elements_to_remove)
        category_input_list = list(category_input_list-elements_to_remove)

    except Exception as e:
        messeage = 'Enter valid category numbers using comma seperation\n' + 'Exception : ' + str(e) + '\noccured while handling your input'  
        print(messeage)


    
    if len(category_input_list) == 0:
        print("You have not entered any valid category \n Please enter a valid category!\n")
        print("Press any key to continue")
        input()
        
    else:
        break_category_loop = True
        print()
        print('Below is a list of selected catagories')
        print(category_input_list)
    #--------------------------------------------#



