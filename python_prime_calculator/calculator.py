from .results.result import Result
from datetime import datetime, timedelta

class Calculator :
    # final properties
    min = None
    max = None
    threads = None


    def __init__(self, min: int, max: int, threads: int) :
        self.validateArgs(min, max, threads)

        self.min     = min
        self.max     = max
        self.threads = threads

    def validateArgs(self, min: int, max: int, threads: int) :
        if min < 2 :
            raise ValueError('min is not integer greater than 1')

        if max <= min :
            raise ValueError('max is not integer greater than min')

        if 1 > threads:
            raise ValueError('threads is not a positive integer')

    def run(self) :
        results = []

        for i in range(self.min, self.max) :
            results.append(self.testIsPrime(i))

        for result in results :
            if result.getIsPrime() :
                print(result.getResultString())

    def testIsPrime(self, test: int) :
        isPrime   = True
        startTime = datetime.now()

        for i in range(2, test - 1) :
            if (float(test)/i) == int(test/i) :
                isPrime = False
                break

        return Result(test, isPrime, (startTime - datetime.now()).microseconds)
