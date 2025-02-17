import app

def test_app():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert '<form action ="/echo" method="GET" >' in rv.data.decode('utf-8')

    rv = web.get('/echo')
    assert rv.status == '200 OK'
    assert b"You said" == rv.data

    rv = web.get('/echo?text=foo+bar')
    assert rv.status == '200 OK'
    assert b"You said: foo bar" == rv.data

def test_store_three_response():
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    responses = ['English','Spanish','Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
