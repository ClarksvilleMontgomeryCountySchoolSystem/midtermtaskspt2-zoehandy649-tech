# Halloween Candy Sharing

# Given Variables
people = 2  # friends who went trick-or-treating
bagA = 23
bagB = 17
bagC = 19

# Part 1: Combine the haul
total_candy = bagA + bagB + bagC
print(f"Total candy collected: {total_candy}")


# Part 2: Fair sharing (include yourself)
people += 1
share = total_candy // people
leftover = total_candy % people
print(f"Each person gets: {share}")
print(f"Leftover candy: {leftover}")


# Part 3: Include the sick friend
# Variable reassignment is fine - previous values were already printed
people += 1
share = total_candy // people
leftover = total_candy % people
print(f"Each person gets: {share}")
print(f"Leftover candy: {leftover}")
