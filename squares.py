#import square from functions module
from functions import square

print("Import specific function from functions module: ")
for i in range(6):
    print(f"The square of {i} is {square(i)}")

#import entire functions module
import functions
print("==============================")
print("Import entire functions module: ")
for j in range(6):
    print(f"The square of {j} is {functions.square(j)}")