string = 'hello'

substring = string[1:4]
print(substring)


nubstring = string[:3]
print(nubstring)


tubstring = string[3:]
print(tubstring)

lubstring = string[:]
print(lubstring)

class AnonymousSurvey:

    """Collect anonymous answers to a survery question."""

    def __init__(self,question):
        """Store a question, and prepare to store responses."""

        self.question = question
        self.response=[]

    def show_question(self):
        """ Show the survey question."""
        print(self.question)

    def store_response(self,new_response):
        """Store a single response to the survey."""
        self.response.append(new_response)

    def show_results(self):
        """ Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"-{response}")
