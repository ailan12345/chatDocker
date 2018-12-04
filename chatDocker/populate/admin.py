from populate import base
from django.contrib.auth.models import User



def populate():
    print('Creating admin account ... ', end='')
    User.objects.all().delete()
    User.objects.create_superuser(first_name='admin', username='admin', password='admin', email='karta2599434@gmail.com')
    for i in range(1,5):
        User.objects.create_user(first_name='user'+str(i), username='user'+str(i), password='user'+str(i), email='karta2599434@gmail.com')
    print('done')
     
     
 
if __name__ == '__main__':
    populate()