def greeting(name, timeofday="morning"):
    """This function generates a user greeting
    including the user name. The user can enter
    the time of day."""
    print("Good"+timeofday,name+"!")
    return

greeting(name="Arthur",timeofday="afternoon")
greeting(name="Moses")
greeting(name="Hawk",timeofday="night")
