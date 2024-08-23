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

def make_adder(n):
    return lambda x: x + n 

plus_3 =make_adder(3) 
plus_5 =make_adder(5) 
plus_3(4)
plus_5(4)
