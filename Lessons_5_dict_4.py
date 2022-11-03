rec = {'name': {'first': 'Bob', 'last': 'Smith'},           #словник з вложеностями
       'jobs':['dev', 'mgr'],
       'age': 40.5}
print(rec)

print(rec['name'])                        #'name' - вложений словник
print(rec['name']['last'])                #індексація в вложеному словнику 'Smith'

print(rec['jobs'])                        #'jobs' - вложений словний
print(rec['jobs'][-1])                    #індексація в вложеному словнику 'mgr'

print(rec['jobs'].append('janitor'))      #розширення списку назв посад
print(rec)