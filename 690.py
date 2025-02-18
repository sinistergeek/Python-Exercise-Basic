def beats(x,y):
    if isinstance(x,Rock):
        if isinstance(y,Rock):
            return None
        elif isinstance(y,paper):
            return y
        elif isinstance(y, Scissors):
            return x
        else:
            raise TypeError("Unkown second thing")
    elif isinstance(x,Paper):
        if isinstance(y,Rock):
            return x
        elif isinstance(y, Paper):
            return None
        elif isinstance(y, Scissors):
            return y
        else:
            raise TypeError("Unknown second thing")
    elif isinstance(x, Scissors):
        if isinstance(y,Rock):
            return y
        elif isinstance(x,Paper):
            return x
        elif isinstance(y,Scissors):
            return None
        else:
            raise TypeError("Unknown second thing")
    else:
        raise TypeError("Unknown first thing")

rock,paper,scissors = Rock(),Paper(),Scissors()

def test_store_three_response():
    question="What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    responses = ['English','Spanish','Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
