class Difference:
    def __init__(self, a):
        self.__elements = a

    # maximumDifference = 0

	# Add your code here
    def computeDifference(self):
        result = []

        for i in self.__elements:
            for j in self.__elements:
                if abs(i - j) not in result:
                    result.append(abs(i - j))
        
        self.maximumDifference = sorted(result, reverse=True)[0]

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]
# a = [8, 8, 8]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)