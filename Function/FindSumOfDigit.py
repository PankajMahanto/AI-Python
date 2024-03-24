def find_sum_of_digit(n):
      sum = 0
      while n > 0:
            sum += n % 10
            n = n // 10
      return sum
def main():
      n = int(input("Enter a number: "))
      print("Sum of digits of", n, "is", find_sum_of_digit(n))


# if __name__ == "__main__":
if __name__=="__main__":
      main()