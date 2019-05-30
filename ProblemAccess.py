import random

#Hash to store all the tests created
tests_hash = {}

#Hash that stores the problems created
problems_hash = {}

def start():
    directory = int(input("Welcome to Math Test Creator Beta version. What do you want to do? 1. Create a test. 2. View the history of created tests. 3. How to use this program. 4. Quit\n"))
    if directory == 1:
        select_a_topic()
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
        freq_q_1 = int(input("How frequent to do you want questions about area to be in terms of percentage?\n"))
        freq_q_2 = int(input("How frequent to do you want questions about angles to be in terms of percentage?\n"))
        freq_q_3 = int(input("How frequent to do you want questions about classfying triangles to be in terms of percentage?\n"))
        questions_per_test = int(input("How many questions do you wish per test?\n"))
        tests_number = int(input("How many tests do you wish to be generated?\n"))
        questions_1 = int(round(freq_q_1 * questions_per_test/100))
        questions_2 = int(round(freq_q_2 * questions_per_test/100))
        questions_3 = int(round(freq_q_3 * questions_per_test/100))
        create_tests(tests_number, questions_1, questions_2, questions_3)

def create_tests(tests_number, questions_1, questions_2, questions_3):
    for x in range(tests_number):
        create_problems(questions_1, questions_2, questions_3)

def create_problems(questions_1, questions_2, questions_3):
    questions_array = []

    for a in range(questions_1):
        base = str(random.randint(1,11))
        height = str(random.randint(1,11))
        question = "A triangle has a base of " + base + " and a height of " + height + ". What is the area of the triangle?"
        questions_array.append(question)
    for b in range(questions_2):
        angle1 = 180
        angle2 = 180
        while angle1 + angle2 > 179:
            angle1 = random.randint(1,180)
            angle2 = random.randint(1,180)
        angle1 = str(angle1)
        angle2 = str(angle2)
        question = "A triangle has angles " + angle1 + " degrees and " + angle2 + " degrees. What is the degree measure of the third angle?"
        questions_array.append(question)

    for c in range(questions_3):
        side1 = 2
        side2 = 3
        side3 = 5
        while side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
            side1 = random.randint(2,6)
            side2 = random.randint(2,6)
            side3 = random.randint(2,6)
        side1 = str(side1)
        side2 = str(side2)
        side3 = str(side3)
        question = "A triangle has side lengths " + side1 + ", " + side2 + ", and " + side3 + ". Is the triangle scalene, isoceles, or equilateral?"
        questions_array.append(question)

    #https://stackoverflow.com/questions/473973/shuffle-an-array-with-python-randomize-array-item-order-with-python - This helped me with shuffling the elements in an array

    random.shuffle(questions_array)

    for l in range(len(questions_array)):
        problems_hash[l] = questions_array[l]

    #I used this site to help me solve a key error problem in my code: https://stackoverflow.com/questions/23297569/python-key-error-0-cant-find-dict-error-in-code
    tests_hash[str(len(tests_hash) + 1)] = problems_hash

    print(problems_hash)
    print(tests_hash)

start()
