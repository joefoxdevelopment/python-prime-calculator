from ..results.result import Result
from datetime import datetime, timedelta

class Tester :
    def testValue(self, value: int) -> Result :
        isPrime   = True
        startTime = datetime.now()
        tests     = 0
        halfValue = value / 2

        for i in range(2, value - 1) :
            tests += 1

            # if we're already further than halfway, we aren't finding a factor, so quit and move onto the next
            if (i > halfValue) :
                break

            if (float(value)/i) == int(value/i) :
                isPrime = False
                break

        return Result(value, isPrime, int((datetime.now() - startTime).total_seconds() * 1000000), tests)
