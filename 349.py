fname = ['Graham','Eric','Terry','Terry','John','Michael']
lname = ['Champman','Idle','Gilliam','Jones','Cleese','Palin']
born = ['8 January 1941','29 March 1943','22 November 1940','1 February 1940','27 October 1939','5 May 1943']

for f_name,l_name,b_date in zip(fname,lname,born):
    print("{:10} {:10} was born {}".format(f_name,l_name,b_date))

