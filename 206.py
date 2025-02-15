set(['Neptun','Mars'])
objects = set(['Mars','Jupiter','Saturn'])
internal = set(['Mercury','Venus','Earth','Mars'])

objects.update(internal)
print(objects)
print(internal)

from survey import AnonymousSurvey 

question  = "What language did you first learn to speak?"
language_survey = AnonymousSurvey(question)

language_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Lanugage:")
    if response == 'q':
        break
    language_survey.store_response(response)

print("\n Thank you to everyone who participated in the survey!")
lanugage_survvey.show_result()
