#Both are examples of loop structures which means that they cause the same code to repeat (iterate) several times in a program. The difference is that a definite loop structure iterates a specific number of times that is known (or can be figured out) before the code is run. An indefinite loop will just continue iterating until its condition expression is false. This is often used to get an unknown number of inputs from the user.

#Both are examples of how Python implements loop structures. \texttt{for}for is the usual loop used for a definite loop structure and \texttt{while}while is the usual loop used for an indefinite loop structure. Note though that technically, any program you can write using a \texttt{for}for loop you can rewrite using a \texttt{while}while loop instead and vice versa. This doesn't mean that you should only ever use one or the other, however, as your code is much easier to read if you use the one that fits best with what you're trying to accomplish.

#Both of these are examples of indefinite loop structures. An interactive will ask if the user wants to continue after getting each input while a sentinel loop will only repeatedly prompt the user for input but will allow the loop to end when a specific value (or set of values) called the sentinel value is input.

#Sentinel loops are described in part (c). An end-of-file loop is an indefinite loop that will continue getting input \textit{from a file}from a file until the end of the file is reached. This basically works the same way as a sentinel loop except that now you're getting input from a file instead of the user and the sentinel value is some signal that the end of the file has been reached (usually when the input is the empty string).


#A) F,T,T,T
#B) F,F,T,F
#C) F,T,T,T
#D) T,T,T,F,T,F,T,F
#E) T,T,T,F,T,F,T,F


n = int(input("Enter value for n: "))
i = 1
total = 0
while(i<=n):
    total += i
    i += 1
print(total)
print()


n = int(input("Enter value for n: "))
i = 1
k = 0
total = 0
while(k<=n):
    total += i
    i += 2
    k += 1
print(total)
print()


n = int(input("Enter value for n: "))
total = 0
while(n!=999):
    total += n
    n = int(input("Enter value for n: "))
print(total)
print()


n = int(input("Enter value for n: "))
total = 0
while(n>0):
    total += 1
    n //= 2
print(total)
print()

def Syracuse():
    m = int(input('Enter starting integer: '))
    seq = [m]
    while m != 1:
        if m % 2 == 0:
            m = m / 2
        else:
            m = 3 * m + 1
        seq.append(int(m))

    print(seq)

Syracuse()