class NumberGuess:
    def __init__(self, guess_count, min_num = 0,max_num= 100):
        self.guess_count = guess_count
        self.min_num = min_num
        self.max_num = max_num

    def get_guess(self):
        number = input(f"please enter number between {self.min_num} to {self.max_num}: ")
        if self.valid_number(number):
            return int(number)
        print("please enter valid number")
        return self.get_guess()

    def valid_number(self, number):
        try:
            number = int(number)
        except ValueError:
            return False
        return self.min_num <= int(number) <=self.max_num

    def get_random_number(self):
        import random
        return random.randint(self.min_num, self.max_num)

    def play(self):
        random_number = self.get_random_number()
        number_count = 1
        while True:
            number = self.get_guess()
            if number_count >= self.guess_count:
                print("your guess was over")
                self.try_again()
                break
            elif number > random_number:
                print("your guess is greate than number")
                print(f"you have {self.guess_count - number_count} left")
                number_count +=1
            elif number < random_number:
                print("your guess is smaller than number")
                print(f"you have {self.guess_count - number_count} left")
                number_count +=1
            else:
                print("You guessed right")
                break
    
    def try_again(self):
        input_val = input(f"please enter yes if you want play again: ")
        if input_val == "yes":
            return self.play()
        return
obj = NumberGuess(guess_count=4)
obj.play()