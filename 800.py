def session(headers,request,forms):
    pre-process: determine session 
    content = csrf(headers,request,forms)
    post-processes the content
    return the content 
def csrf(headers,request,forms):
    pre-process: validate csrf tokens
    content = authenticate(headers,request,forms)
    post-processes the content 
    return the content
