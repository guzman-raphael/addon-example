print('-------------maz-------------')
import maz

print(maz.__version__)
print(maz.show_usr())
try:
    print(str(maz.student1))
except:
    print('## `{}` not found ##'.format('student1'))

print('-------------maz-user-------------')
import maz.user as u

print(u.usr())
print(u.show_usr())
print(u.test())
try:
    print(u.new())
except:
    print('## `{}` not found ##'.format('new'))
try:
    print(u.__version__)
except:
    print('## `{}` not found ##'.format('__version__'))
try:
    print(u.__certificate__)
except:
    print('## `{}` not found ##'.format('__certificate__'))



print('-------------maz_message-------------')
import maz.type as t

try:
    print(str(t.student1))
except:
    print('## `{}` not found ##'.format('student1'))
try:
    print(str(t.Student))
except:
    print('## `{}` not found ##'.format('Student'))
try:
    print(t.__version__)
except:
    print('## `{}` not found ##'.format('__version__'))
try:
    print(t.__certificate__)
except:
    print('## `{}` not found ##'.format('__certificate__'))
