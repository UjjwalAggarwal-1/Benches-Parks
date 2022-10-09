import sys
import os
import django
import time
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dotnot.settings')
django.setup()

from bench.models import Bench1, Bench2, Bench3, Park

def main():
    t1 = time.time()
    b = Bench1.objects.filter(id=2).first()
    b2 = b.bench2_set.filter(id=2).first()
    b3 = b2.bench3_set.all()
    t2 = time.time()
    print('first ',t2 - t1)
    b = Bench1.objects.filter(id=2).first()
    b2 = b.bench2_set.filter(id=2).first()
    b3again = Bench3.objects.filter(parent__parent=b, parent=b2).all()
    t3 = time.time()
    print('second',t3 - t2)
    b = Bench1.objects.filter(id=2).first()
    b2 = b.bench2_set.filter(id=2).first()
    b4 = Bench3.objects.filter(parent__parent=b)
    b4 = b4.filter(parent=b2)
    print('third ',time.time() - t3)

def main2():
    tot1 = 0
    tot2 = 0
    tot3 = 0
    for b in Bench1.objects.all():
        t1 = time.time()
        b2 = b.bench2_set.first()
        b3 = b2.bench3_set.all()
        t2 = time.time()
        tot1 += t2 - t1
        b2 = b.bench2_set.first()
        b3again = Bench3.objects.filter(parent__parent=b, parent=b2)
        t3 = time.time()
        tot2 += t3 - t2
        b2 = b.bench2_set.first()
        b4 = Bench3.objects.filter(parent__parent=b)
        b4 = b4.filter(parent=b2)
        tot3 += time.time() - t3
    
    print('tot1', tot1)
    print('tot2', tot2)
    print('tot3', tot3)


def main2a():
    tot= 0
    for i in range (5):
        t1 = time.time()
        b1 = Bench1.objects.get(name='Bench1 %d' % i)
        print(b1)
        t2 = time.time()
        tot += t2 - t1
        for j in range(10):
            t3 = time.time()
            b2 = b1.bench2_set.get(name='Bench2 %d' % i)
            print(b2)
            t4 = time.time()
            tot += t4 - t3
            for k in range(400):
                t5=time.time()
                b3 = b2.bench3_set.get(name='Bench3 %d' % i)
                print(b3)
                tot+=time.time()-t5
    print('time in main2a: ',tot)
def main3():
    tot = 0
    
    for i in range (5):
        for j in range(10):
            for k in range(400):
                t1 = time.time()
                g=Park.objects.filter(bench1__name='Bench1 %d' % i)
                g=g.filter(bench3__name='Bench3 %d' % k)
                g=g.filter(bench2__name='Bench2 %d' % j) 
                tot += time.time() - t1
    print('time in main3: ',tot)

if __name__ == '__main__':
    main3()

