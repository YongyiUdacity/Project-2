def generate_concept_HTML(lesson_title, concept_title, concept_description):
    html_text_0 = '''
''' + '''
''' + lesson_title
    html_text_1 = '''
    <div class = "concept">
        <div class = "concept_title">
        ''' + concept_title
    html_text_2 = '''
        </div>
        <div class = "concept_description">
        ''' + concept_description
    html_text_3 = '''
        </div>
    </div>'''
    full_html_text = html_text_0 + html_text_1 + html_text_2 + html_text_3
    return full_html_text


def make_HTML(concept):
    lesson_title = concept[0]
    concept_title = concept[1]
    concept_description = concept[2]
    return generate_concept_HTML(lesson_title, concept_title, concept_description)

Example_list_of_concepts = [['Lesson 1: Introduction to "Serious" Programming', 'Computer and Computer Program', 'Unlike most machines, a computer can be programmed to do anything people want under a specific sequence of instructions. The sequence of steps that a computer can follow is a program.'],
                            ['', 'Programming language and Grammar', 'A Programming language is what programmers use to tell a computer what to do, such as Python. Programming language has to follow grammar. A grammar is a specification of what is "correct" and what is "incorrect".'],
                            ['', 'Python and Python Expressions', 'Python is a programming language. Python interpreter can convert python code people write as a set of instructions that the computer itself can understand and execute. A Python expression is a legal Pyhton statment. Python code has to follow the expressions.'],
                            ['Lesson 2: Variables and Strings', 'Variables in Python', 'Variables work as names for values. Programmer can assign a value to the variable by using "=". The "=" means "takes the value of". Programmer can change the value of a variable by re-assigning it to a different value later.'],
                            ['', 'String', 'In Python language, a string is expressed as "string". String index starts from 0. People can find strings in strings by using ".find()".'],
                            ['Lesson 3: Input -> Function -> Output', 'Function', 'A function takes input, does something to that input, and then produces output.'],
                            ['', 'How to Make and Use Functions', 'To make a function, start with a line of code with the keyword "def" and then give a function name followed by the function parameters in patentheses. These parameters will eventually be replaced by actual values when the function is called. To use a function, write the name of the function followed by the values people want to give it in parentheses.'],
                            ['', 'Return Statement', 'The "return" keyword tells Python exactly what the function should produce as output.'],
                            ['Lesson 4: Decisions and Repetition: If and While', '"if" Statement', '"if" statement is used to make decisions. The code in the "if" block can be execute only if the "if" condition is true. "else" statement is used to execute the followed code when the "if" condition is no longer true.'],
                            ['', '"while" Statement', 'A while loop repeatedly executes the body of the loop until the test condition is no longer true.'],
                            ['Lesson 5: Structured Data: lists and For Loops', 'List', 'List is the sequence of anything, such as numbers, strings, or even sub-lists.'],
                            ['', 'Mutation and Aliasing', 'Mutation means one can change the value of a list after it is created. Aliasing means there are two different ways to refer to the same object.'],
                            ['', 'List Operations', '"append" is not creating a new list. It is mutating the old list. "+" is creating a new list. "len" is for counting the outer elements in a list.'],
                            ['', '"for" Loop', '"for" loop: for each element in the list, we will assign the element to the name and evaluate the block. This process is done as the order of the list.']]


def make_HTML_for_many_concepts(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

print ('Stage 2: Automate Your page')
print (make_HTML_for_many_concepts(Example_list_of_concepts))