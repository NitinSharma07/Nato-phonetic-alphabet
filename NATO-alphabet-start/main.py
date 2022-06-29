import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

phonetic_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dictionary)
legal_char = True
while legal_char:
    word = input('Enter a word: ').upper()
    try:
        output_list = [phonetic_dictionary[i] for i in word]


    except KeyError as file_error:
        print('Sorry only letter in the alphabet please.')
    else:
        print(output_list)
        legal_char = False





