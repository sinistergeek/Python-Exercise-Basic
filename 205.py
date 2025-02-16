objects = set()
print(objects)

objects.add('Mars')
print(objects)

objects.add('Mars')
print(objects)

objects.add('Neptun')
print(objects)

from survey import AnonymousSurvey

def test_store_single_response():
    question = "What language did you first learn to speak?"
    language_survey.store_response("English")
    assert 'English' in language_survey.responses
