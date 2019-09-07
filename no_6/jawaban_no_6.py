hint = input("Enter Your The Hint : ")
secret_word = input("Enter the answer : ")
secret_word1 = list(secret_word)
x = input("are u ready?")
if x == "":
    print("\n"*25)

guess = []
guess_count = 0
guess_limit = len(secret_word1)*1.5
out_of_guesses = False

for i in range(len(secret_word1)):
    guess.append("_")
print("The hint is : ",hint)
print(guess)
while guess != secret_word1 and not (out_of_guesses):
    if guess_count < guess_limit:
        guess1 = input("enter a word : ")
        a = len(secret_word1)
        for i in range(a):
            if guess1 == secret_word1[i]:
                guess[i] = guess1
                guess_count -= 1
        c = guess_limit - guess_count
        print(guess,"you have ",c," more guesses.")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("you are out of guesses, You Lose!")
else:
    print("You Win!")