name_for_userid = {
        382: 'Alice',
        950: 'Bob',
        590: 'Dilbert',

        }

def greeting(userid):
    return 'Hi %s!' %s name_for_userid[userid]

greeting(382)
greeting(33333)

def greeting(userid):
    if userid in name_for_userid:
        return 'Hi %s!' % name_for_userid[userid]
    else:
        return 'Hi there!'

greeting(382)
greeting(333)

def greeting(userid):
    try:
        return 'Hi %s!' % name_fro_userid[userid]
    except KeyError:
        return 'Hi there'
