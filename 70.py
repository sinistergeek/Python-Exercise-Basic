class StringListOnly(list):
    def append(self,string):
        if not isinstance(string, str):
            raise TypeError('Only objects fo tpe str can be added to the list.')
        super().append(string)


slo = StringListOnly()
slo.append('Data')
slo.append('Science')
print(slo)
