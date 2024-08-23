def get_speak_func(text,volume):
    def whisper():
        return text.lower() + '...'
    def yell():
        return text.upper() + '!'
    if volume > 0.5:
        return yell 
    else:
        return whisper 

get_speak_func('Hello,World',0.7)()

add = lambda x,y: x + y
add(5,3)
