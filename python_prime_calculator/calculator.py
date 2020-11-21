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
        if min < 1 :
            raise ValueError('min is not integer greater than 0')

        if max <= min :
            raise ValueError('max is not integer greater than min')

        if 1 > threads:
            raise ValueError('threads is not a positive integer')

    def run(self) :
        print('run called')
