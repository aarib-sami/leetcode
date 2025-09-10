class Solution:
    def bestClosingTime(self, customers: str) -> int:
        customerLen = len(customers)
        customerCount = [0] * (customerLen+1)
        noCustomerCount = [0] * (customerLen+1)

        for i in range(0, customerLen):
            if customers[i] == "N":
                noCustomerCount[i+1] = 1 + noCustomerCount[i]
            else:
                noCustomerCount[i+1] = noCustomerCount[i]

        for i in range(customerLen-1, -1, -1):
            if customers[i] == "Y":
                customerCount[i] = 1 + customerCount[i+1]
            else:
                customerCount[i] = customerCount[i+1]

        minPen = float('inf')
        res = 0

        print(noCustomerCount)
        print(customerCount)


        for i in range(customerLen + 1):
            if noCustomerCount[i] + customerCount[i] < minPen:
                res = i
                minPen = noCustomerCount[i] + customerCount[i]

        return res