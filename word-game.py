madlib = """Today I went to the zoo. I saw a(n)
(adjective)
(Noun) jumping up and down in its tree.
He (verb, past tense) (adverb)
through the large tunnel that led to its (adjective2)
(noun). """

one = input("Tell me an adjective: ")
two = input("Tell me a noun: ")
three = input("Tell me a past tense verb: ")
four = input("Tell me an adverb: ")
five = input("Tell me an adjective: ")
six = input("Tell me a noun: ")

newMadlib = (madlib
.replace("(adjective)", one)
.replace("(Noun)", two)
.replace("(verb, past tense)", three)
.replace("(adverb)", four)
.replace("(adjective2)", five)
.replace("(noun)", six)
)
print (newMadlib)