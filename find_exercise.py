# Import packages
import json
from random import shuffle


## Function to read input
def take_int_list_input(category_list, catergory_id_list, query_word):

    #initialize variables to take category input
    category_input_list = []
    break_category_loop = False
    is_input_given = False

    while break_category_loop==False:
        #Print all the categories
        print("Please Choose A " + query_word)
        for category in category_list:
            print(category['option'])

        #Print instructions for category
        print("---------------------------------------------------------------------")
        print("Please write the "+ query_word + " numbers. You can choose multiple " + query_word + " at a time. Separate them with COMMA(,)")
        shuffle(catergory_id_list)
        
        print("For example: " + str(catergory_id_list[0:3])[1:-1])

        #Ask for category input from user
        user_category_input = input("Select " + query_word + "\nnumber from the above list\nor press ENTER to skip:\n")
        #print(user_category_input)
        
        #Check whether user gave an empty input
        if user_category_input:
            is_input_given = True
        else:
            is_input_given = False

        
        #------Handle category input here------------#
        try:
            if is_input_given:
                category_input_list = list(map( int, user_category_input.split(',')))

                elements_to_remove= []
                for i in category_input_list:
                    if i not in catergory_id_list:
                        elements_to_remove.append(i)
                        print(str(i), ' is not a valid category')
                category_input_list = set(category_input_list)
                elements_to_remove = set(elements_to_remove)
                category_input_list = list(category_input_list-elements_to_remove)
            else:
                pass

        except Exception as e:
            messeage = 'Enter valid '+ query_word +' numbers using comma seperation\n\n' + 'Exception : ' + str(e) + '\noccured while handling your input' 
            print()
            print()
            print(messeage)


        
        if (len(category_input_list) == 0) and (is_input_given):
            print("\nYou have not entered any valid "+query_word+"\nPlease enter a valid "+query_word+"!")
            print("Press ENTER to continue")
            input()

        elif (len(category_input_list) == 0) and (not is_input_given):
            print()
            print("You choose not a give a "+ query_word + " input")
            break_category_loop = True

        else:
            break_category_loop = True
            
        #--------------------------------------------#
    return category_input_list, is_input_given



def take_int_input(query_word):
    break_input_loop = False

    while not break_input_loop:
        number_string = input("Select " + query_word)
        is_input_given = False
        
        if number_string:
            is_input_given = True
        else:
            is_input_given = False

        try:
            if is_input_given:
                number = int(number_string)
                break_input_loop = True
            else:
                number = 10000
                break_input_loop = True
            
        except Exception as e:
            message = "While handling your input\n an exception " + e + "occured\n\nPlease enter a valid integer number\n\n"
            print(message)
            input()
            print('Press ENTER to continue\n')
    
    return number



def print_list(my_list,max_output_number):        
    for i,item in enumerate(my_list[:max_output_number]):
        print("{:02d}".format( i+1 ), '|  ', item)
        



## Main function
if __name__ == '__main__':
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
    
    # Sorting Category List
    category_list.sort(key=lambda x:x['id'])

    catergory_id_list = [category['pk'] for category in category_dict]


    #Create muscles list
    muscle_list=[dict(id=x['pk'],option=str(x['pk'])+"_"+x['fields']['name']) 
                    for x in muscle_dict]
    
    # Sorting the sequence
    muscle_list.sort(key=lambda x:x['id'])

    muscle_id_list= [muscle['pk'] for muscle in muscle_dict]


    #Take exercise category input from user
    exercise_input_list, _ = take_int_list_input(category_list, catergory_id_list,'exercise category')

    print(exercise_input_list)

    print()
    print("Press ENTER to continue")
    input()
    
    #Take muscle category input from user
    muscle_input_list, _ = take_int_list_input(muscle_list, muscle_id_list, 'muscle category')
    
    print(muscle_input_list)


    print()
    print("Press ENTER to continue")
    input()

    #Ask user to give maximum number of output 
    max_output_number = take_int_input("maximum number of exercises to show\nor press ENTER to skip:\n")
    if max_output_number < 10000:
        if max_output_number>1:
            print("You will be shown maximum "+ str(max_output_number) + " exercises\n\n")
        else:
            print("You will be shown maximum "+ str(max_output_number) + " exercise\n\n")
    else:
        print("You will be shown all exercises \nthat meet your search criteria\n\n")

    print("Press ENTER to continue")
    input()
    

    # Find out the exercises to show as output
    output_exercise_list= [] #list to hold outputs
    for exercise in exercises_language_2_list:
        is_in_category = False
        is_in_muscle = False

        if exercise['fields']['category'] in exercise_input_list:
            is_in_category = True
        
        for muscle in exercise['fields']['muscles']:
            if muscle in muscle_input_list:
                is_in_muscle = True

        if is_in_category or is_in_muscle:
            output_exercise_list.append(exercise['fields']['name'])
            #print('Added', exercise['fields']['name'],' to output list')
    
    #bodyweight=input("Number of bodyweight exercises from[0-{}] =  ".format#(str(len(bodyweight_dict))) )

    bodyweight = take_int_input( "number of bodyweight exercises from[0-{}] =  ".format(str(len(bodyweight_dict))) + "\n")

    try:
        tn=int(bodyweight)
        shuffle(bodyweight_dict)
        bdwt=bodyweight_dict[0:tn]
    except Exception as e:
        print("Error ", e)
        bdwt=[]
    
    output_exercise_list.extend(bdwt)
    # Print output 
    print("Here is your list of exercises")
    print()
    print_list(output_exercise_list, max_output_number)



