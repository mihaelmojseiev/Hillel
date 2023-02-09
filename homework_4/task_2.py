first = input().split('*')

print('Name: ' + first[0],'\nAge: ',(int(first[2][:4])-int(first[1][:4])),' years')