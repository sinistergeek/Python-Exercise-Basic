from string import Template 
t = Template('Hey, $name!')
t.substitute(name=name)

templ_string = 'Hey $name, there is a $error error!'
Template(templ_string).substitute(name=name,error=hex(errno))
