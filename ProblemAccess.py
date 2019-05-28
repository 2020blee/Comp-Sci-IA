import random

problems_hash = {}

def start():
    directory = int(input("Welcome to Math Test Creator Beta version. What do you want to do? 1. Create a test. 2. View the history of created tests. 3. How to use this program. 4. Quit\n"))
    if directory == 1:
        create_a_test()
    elif directory == 2:
        print("History of tests not available yet")
        quit()
    elif directory == 3:
        print("Directions not available yet")
        quit()
    elif directory == 4:
        print("Quitting")
        quit()
    else:
        print("Invalid input")
        start()

def select_a_topic():
    #Only option 2 works for now; others can be coded later
    topic_picker = int(input("Select a topic: 1. Proportions. 2. Geometry. 3. Systems of equations. 4. Transformations.\n"))
    if topic_picker == 2:
        geometry_subtopic()
    else:
        print("Invalid input")
        select_a_topic()

def geometry_subtopic():
    #Only subtopic 3 works for now; others can be coded later
    subtopic_picker = int(input("Select a subtopic: 1. Circles. 2. Squares. 3. Triangles.\n"))
    if subtopic_picker == 3:
        freq_q_1 = int(input("How frequent to do you want questions about area to be in terms of percentage (it should be as a decimal)?\n"))
        freq_q_2 = int(input("How frequent to do you want questions about angles to be in terms of percentage (it should be as a decimal)?\n"))
        freq_q_3 = int(input("How frequent to do you want questions about classfying triangles to be in terms of percentage (it should be as a decimal)?\n"))
        questions_per_test = int(input("How many questions do you wish per test?\n"))
        tests_number = int(input("How many tests do you wish to be generated?\n"))
        questions_1 = int(round(freq_q_1 * questions_per_test))
        questions_2 = int(round(freq_q_2 * questions_per_test))
        questions_3 = int(round(freq_q_3 * questions_per_test))
        create_tests()

def create_tests():
    for x in range(tests_number):
        create_problems()

def create_problems():
    for a in range(freq_q_1):
        base = str(random.randint(1,11))
        height = str(random.randint(1,11))
        question = "A triangle has a base of " + base + " and a height of " + height ". What is the area of the triangle?"
        problems_hash[str(len(problems_hash) + 1)] = question
    for b in range(freq_q_2):
        base = str(random.randint(1,11))
        height = str(random.randint(1,11))
        question = "A triangle has a base of " + base + " and a height of " + height ". What is the area of the triangle?"
        problems_hash[str(len(problems_hash) + 1)] = question

start()
