inputFile="casanova.txt"
N=int(input("Enter N value: "))
with open (inputFile, 'r')as filedata:
    linesList=filedata.readlines()
    print("The following are the first",N,"lines of a text file:")
    for textline in(linesList[:N]):
        print(textline, end="")
        filedata.close()
        word=input("Enter word to be searched: ")
        k=0
        with open(inputFile, 'r')as f:
              for line in f:
                words=line.split()
              if(i==word):
                k=k+1
              print(f"Occurances of the word{word} is:", k)