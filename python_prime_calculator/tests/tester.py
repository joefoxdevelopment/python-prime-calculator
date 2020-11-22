from ..results.result import Result
from datetime import datetime, timedelta

class Tester :
    def testValue(self, value: int) -> Result :
        isPrime   = True
        startTime = datetime.now()

        for i in range(2, value - 1) :
            if (float(value)/i) == int(value/i) :
                isPrime = False
                break

        return Result(value, isPrime, int((datetime.now() - startTime).total_seconds() * 1000000))
