# Import packages
import json


## Function to read input
def take_int_list_input(category_list, catergory_id_list, query_word):

    #initialize variables to take category input
    category_input_list = []
    break_category_loop = False

    while break_category_loop==False:
        #Print all the categories
        print("Please Choose A " + query_word)
        for category in category_list:
            print(category['option'])

        #Print instructions for category
        print("---------------------------------------------------------------------")
        print("Please write the "+ query_word + " numbers. You can choose multiple " + query_word + " at a time. Separate them with COMMA(,)")
        print("For example: 3,5,6 ")

        #Ask for category input from user
        user_category_input = input("Select " + query_word + ": ")
        #print(user_category_input)

        
        #------Handle category input here------------#
        try:
            category_input_list = list(map( int, user_category_input.split(',')))
            elements_to_remove= []
            for i in category_input_list:
                if i not in catergory_id_list:
                    elements_to_remove.append(i)
                    print(str(i), ' is not a valid category')
            category_input_list = set(category_input_list)
            elements_to_remove = set(elements_to_remove)
            category_input_list = list(category_input_list-elements_to_remove)

        except Exception as e:
            messeage = 'Enter valid '+ query_word +' numbers using comma seperation\n' + 'Exception : ' + str(e) + '\noccured while handling your input'  
            print(messeage)


        
        if len(category_input_list) == 0:
            print("You have not entered any valid "+query_word+"\nPlease enter a valid "+query_word+"!")
            print("Press ENTER to continue")
            input()
            
        else:
            break_category_loop = True
            
        #--------------------------------------------#
    return category_input_list



def print_list(my_list):
    for i,item in enumerate(my_list):
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

    catergory_id_list = [category['pk'] for category in category_dict]


    #Create muscles list
    muscle_list=[dict(id=x['pk'],option=str(x['pk'])+"_"+x['fields']['name']) 
                    for x in muscle_dict]

    muscle_id_list= [muscle['pk'] for muscle in muscle_dict]


    #Take exercise category input from user
    exercise_input_list = take_int_list_input(category_list, catergory_id_list,'exercise category')
    print(exercise_input_list)

    print()
    print("Press ENTER to continue")
    input()
    
    #Take muscle category input from user
    muscle_input_list = take_int_list_input(muscle_list, muscle_id_list, 'muscle category')
    print(muscle_input_list)


    print()
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

    # Print output 
    print("Here is your list of exercises")
    print()
    print_list(output_exercise_list)



