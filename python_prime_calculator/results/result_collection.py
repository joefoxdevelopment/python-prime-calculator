from .result import Result

class ResultCollection :
    results = []

    def registerResult(self, result: Result) -> None :
        self.results.append(result)

    def getList(self) -> list :
        return self.results
