class Result :

    # final variables
    value   = None
    isPrime = None
    timeUs  = None

    def __init__(self, value: int, isPrime: bool, timeUs: int) -> None :
        self.value   = value
        self.isPrime = isPrime
        self.timeUs  = timeUs

    def getIsPrime(self) -> bool :
        return self.isPrime

    def getResultString(self) -> str :
        if None == self.value or None == self.isPrime or None == self.timeUs :
            raise ValueError('Not all required result properties set')

        return str('Value: ' + str(self.value) + ' is ' +
            str('' if self.isPrime else 'not ') + 'prime. ' +
            'Duration ' + str(self.timeUs) + 'us')
