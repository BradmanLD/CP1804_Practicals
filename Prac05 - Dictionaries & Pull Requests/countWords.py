"""
Write a program to count the occurrences of words in a string. The program should ask the user for a string,
then print the counts of how many of each word are in the file.
"""


def main():
    dictionary = {}
    words = input("Enter a sentence: ").split()
    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    for word in sorted(dictionary):
        print("{:{}} : {:2}".format(word, len(max(words, key=len)), dictionary[word]))
main()
