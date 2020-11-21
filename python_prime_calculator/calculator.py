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
        primes    = 0
        notPrimes = 0
        for i in range(self.min, self.max) :
            if self.testIsPrime(i) :
                print(str(i) + ' is prime')
                primes += 1
            else :
                print(str(i) + ' is not prime')
                notPrimes += 1

        print('')
        print('Found ' + str(primes) + ' primes')
        print('Found ' + str(notPrimes) + ' not primes')

    def testIsPrime(self, test: int):
        for i in range(2, test - 1) :
            if (float(test)/i) == int(test/i) :
                return False

        return True
