def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)

def word_count():
    with open("books/frankenstein.txt") as wc:
        words = wc.read().split()
    print(len(words))

def character_count():
    car_count = {}
    with open("books/frankenstein.txt") as cc:
        lower_case = cc.read().lower()
        for char in lower_case:
            if char not in car_count:
                car_count[char] = 1
            else:
                car_count[char] += 1
    
    #print(car_count)
    return car_count

def sortari(car_count):

    listi_af_gaurum = []
    for set in car_count:
        dict_of_char = {}
        if set.isalpha():
            dict_of_char[set] = car_count[set]
            listi_af_gaurum.append(dict_of_char)
    listi_af_gaurum.sort(key=lambda d: list(d.values())[0], reverse=True)
    print("--- Begin report of books/frankenstein.txt ---")
    print("77986 words found in the document")
    print("")
    for set in listi_af_gaurum:
        for key, value in set.items(): 
            print(f"The '{key}' character was found {value} times")
    print("--- End report ---")

#character_count()
sortari(character_count())
#main()
#word_count()
