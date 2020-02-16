words = []
with open('words.txt') as input:
    for line in input:
        words.extend(line.strip().split(','))
#Split each word into separate entry in list

sums = [None] * len(words)
for i in range (0, len(words)):
    sum = 60
    # first letter in ascii is 65, so I subtract 64 bron each ascii code
    # since " is 34, and 34-64 is -30, i add 60 for both parethenses in each word
    for character in words[i]:
        number = ord(character) - 64
        sum = sum + number
    sums[i]= sum
#Give each word its value (sums of each letter)

nums=[]
i=0
while True:
    nums.append(((i+1)/2)*(i+2))
    if (nums[i]>max(sums)):
        break
        #max(sums) is the "most valued word", we don't have
        #to check triangle numbers above that
    i=i+1
print ("Triangle numbers:")
print (nums)
#Create list of traingle numbers

count=0
for i in range(0, len(words)):
    if (sums[i] in (nums)):
        count=count+1
        #print (words[i]+ " checks out")
        #I was double-checking some words
#Compare word values with tr. numbers
print("Triangle words: "+str(count))

#finished