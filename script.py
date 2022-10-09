import sys
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dotnot.settings')
django.setup()

from bench.models import Bench1, Bench2, Bench3

def main():
    for i in range(5):
        b1 = Bench1(name='Bench1 %d' % i)
        b1.save()
        for j in range(10):
            b2 = Bench2(name='Bench2 %d' % j, parent=b1)
            b2.save()
            for k in range(400):
                b3 = Bench3(name='Bench3 %d' % k, parent=b2)
                b3.save()

if __name__ == '__main__':
    main()