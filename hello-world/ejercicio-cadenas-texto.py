# Start by storing the following paragraph in a variable named text:

text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

# Separate the paragraph into sentences
# In English each sentence ends with a period. 
# You will use this to break the paragraph into difference sentences. 
# Using the split method to split the text into sentences by looking for the string . 
# (a period followed by a space). 
# Store the result in a variable named sentences. Print the result.

sentences = text.split(".")
print(sentences)

#Find keywords
#You will finish your program by adding the code to find any sentences which mention temperature. 
# Add code to loop through the sentences variable.
# For each sentence, search for the word temperature. 
# If the word is found, print the sentence.

for sentence in sentences:
# Se crea el for de 'oracion', pasando por cada una de las 'oraciones'
    if 'temperature' in sentence:
    # Evalua cada una de las oraciones con la palabra 'temperature'
        print(sentence)
        # Imprime la oracion que necesitamos


