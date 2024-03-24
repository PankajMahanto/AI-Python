
def findSum(n):
      sum=0
      # i=1
      # while(i<=10):
      #       sum+=i
      sum=(n+1)*n/2
      #       i+=1
      return sum


def main():
      n=int(input("Enter The number: "))
      print("Sum of",n,"number: ",findSum(n))
      print("Finished!!")


# if __name__== "__main__":
main()
print("Coding Start")