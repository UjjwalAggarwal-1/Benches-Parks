import sys
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dotnot.settings')
django.setup()

from bench.models import Park, Bench1, Bench2, Bench3

def main():
    for i in range(5):
        b1 = Bench1.objects.get(id=i+1)
        for j in range(10):
            b2 = Bench2.objects.get(id=j+1)
            for k in range(400):
                b3 = Bench3.objects.get(id=k+1)
                t=Park.objects.create(bench1=b1,bench2=b2,bench3=b3)
                print(t)



if __name__ == '__main__':
    main()