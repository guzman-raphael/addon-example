print('-------------maz-------------')
import maz

print(maz.__version__)
print(maz.show_usr())
print(maz.msg())

print('-------------maz-user-------------')
import maz.user as u

print(u.usr())
print(u.show_usr())
print(u.test())
try:
    print(u.new())
except:
    print('## not found ##')
try:
    print(u.__version__)
except:
    print('## not found ##')
try:
    print(u.__certificate__)
except:
    print('## not found ##')



print('-------------maz_message-------------')
import maz.message as m

print(m.msg())
try:
    print(m.__version__)
except:
    print('## not found ##')
try:
    print(m.__certificate__)
except:
    print('## not found ##')
