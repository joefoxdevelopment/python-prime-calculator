from .result import Result

class ResultCollection :
    results        = []
    primes         = 0
    totalTestTime  = 0
    testsPerformed = 0

    def registerResult(self, result: Result) -> None :
        self.results.append(result)

        self.primes         += 1 if result.getIsPrime() else 0
        self.totalTestTime  += result.getTimeUs()
        self.testsPerformed += result.getTestsNeeded()

    def getSummary(self) -> dict :
        return {
            'results'        : self.results,
            'primes'         : str(self.primes),
            'testsPerformed' : str(self.testsPerformed),
            'totalTestTime'  : str(self.totalTestTime),
        }
