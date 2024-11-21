def main():
    fileName = input("Name of the file:   ")
    with open(f"books/{fileName}") as f:
        files_content = f.read()

        words = files_content.split()
        numOfwords = len(words)
        lowerCaseLetters = []
        for word in words: 
            lowerCaseLetters += word.lower()
        alpha = {
            "a":0,
            "b":0,
            "c":0,
            "d":0,
            "e":0,
            "f":0,
            "g":0,
            "h":0,
            "i":0,
            "j":0,
            "k":0,
            "l":0,
            "m":0,
            "n":0,
            "o":0,
            "p":0,
            "q":0,
            "r":0,
            "s":0,
            "t":0,
            "u":0,
            "v":0,
            "w":0,
            "x":0,
            "y":0,
            "z":0
        }
        
        for word in lowerCaseLetters:
            if word in alpha:
                alpha[word] += 1
        sortedAlpha = dict(sorted(alpha.items(),key=lambda item: item[1], reverse = True))
    return fileName, numOfwords, sortedAlpha
    
        

fileName, numOfwords, alpha = main()
print(f"--- Begin report of {fileName} ---")

print(f"{numOfwords} words found in the document")
for a in alpha:
    print(f"The '{a}' character was found {alpha[a]} times")
print("--- End report ---")