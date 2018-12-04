from populate import base
from tutorial.models import PythonTopic
 
 
 
 
 
def populate():
    print('Creating PythonTopic ... ', end='')
    PythonTopic.objects.all().delete()
    for i in range(1,60):
        PythonTopic.objects.create(num=i, title='title', example='example', topic='topic', answer='answer', difficult=1)
    print('done')
     
 
 
if __name__ == '__main__':
    populate()