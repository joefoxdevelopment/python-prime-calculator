from .results.result import Result
from .results.result_collection import ResultCollection
from .tests.tester import Tester

class Calculator :
    # final properties
    min     = None
    max     = None
    threads = None
    showAll = False

    def __init__(self, min: int, max: int, threads: int, showAll: bool = False) -> None:
        self.validateArgs(min, max, threads)

        self.min     = min
        self.max     = max
        self.threads = threads
        self.showAll = showAll

    def validateArgs(self, min: int, max: int, threads: int) -> None :
        if min < 2 :
            raise ValueError('min is not integer greater than 1')

        if max <= min :
            raise ValueError('max is not integer greater than min')

        if 1 > threads:
            raise ValueError('threads is not a positive integer')

    def run(self) -> None :
        results = ResultCollection()
        test    = Tester()

        for i in range(self.min, self.max) :
            result = test.testValue(i)
            results.registerResult(result)

            if result.getIsPrime() or self.showAll :
                print(result.getResultString())

        summary = results.getSummary()

        print('')
        print('Found ' + summary['primes'] + ' prime numbers between ' + str(self.min) + ' and ' + str(self.max))
        print('Performed ' + summary['testsPerformed'] + ' tests in ' + summary['totalTestTime'] + ' microseconds')
