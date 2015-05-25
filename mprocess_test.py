import os.path
from multiprocessing import Pool
import time

def process_file(name):
    ''' Process a file: count number of lines and words '''
    linecount=0
    wordcount=0
    with open(name, 'r') as inp:
        for line in inp:
            linecount+=1
            wordcount+=len(line.split(' '))

    return name, linecount, wordcount


class Initialiser(object):
    '''
    show PID of process (to verify number and reuse of processes is as expected
    '''
    def __call__(self):
        print "inside process ", os.getpid()
        

def process_files_parallel(thePool, dirname, names):
    ''' Process each file in parallel via Poll.map() '''
    paths = [os.path.join(dirname, name) for name in names]
    results=thePool.map(process_file,  [p for p in paths if os.path.isfile(p)])
    for cnt,r in enumerate(results, 0):
        print cnt, r


if __name__ == '__main__':
    start=time.time()
    dirPath = '/home/eoin/Documents/3rdparty/'
    pool=Pool( initializer=Initialiser())
    os.path.walk(dirPath, process_files_parallel, pool)
    print "finished!"