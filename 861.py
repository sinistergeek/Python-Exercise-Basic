from string import Template 
t = Template('Hey, $name!')
t.substitute(name=name)
