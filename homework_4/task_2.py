first = input()

func = first.split('*')
name = func[0]
dateb = func[1].split('-')
dated = func[2].split('-')

datebb = (int(dateb[0]))
datedd = (int(dated[0]))

age = str(datedd - datebb)

print('Name: ' + name ,'\nAge: ' + age +' years')