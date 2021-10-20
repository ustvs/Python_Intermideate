"""
Calculate frequencies of unique words in test variable

1. remove symbols like .,:'!, convert string to lower or uppercase, split text to words
2. create a dictionary where key is a unique word and value is number of time this word appeared in test
3. print each unique word togeather with it's frequency

"""

text = """
Alice caught the baby with some difficulty, as it was a queer-shaped
little creature, and held out its arms and legs in all directions, 'just
like a star-fish,' thought Alice. The poor little thing was snorting
like a steam-engine when she caught it, and kept doubling itself up and
straightening itself out again, so that altogether, for the first minute
or two, it was as much as she could do to hold it.

As soon as she had made out the proper way of nursing it, (which was to
twist it up into a sort of knot, and then keep tight hold of its right
ear and left foot, so as to prevent its undoing itself,) she carried
it out into the open air. 'IF I don't take this child away with me,'
thought Alice, 'they're sure to kill it in a day or two: wouldn't it be
murder to leave it behind?' She said the last words out loud, and the
little thing grunted in reply (it had left off sneezing by this time).
'Don't grunt,' said Alice; 'that's not at all a proper way of expressing
yourself.'

The baby grunted again, and Alice looked very anxiously into its face to
see what was the matter with it. There could be no doubt that it had
a VERY turn-up nose, much more like a snout than a real nose; also its
eyes were getting extremely small for a baby: altogether Alice did not
like the look of the thing at all. 'But perhaps it was only sobbing,'
she thought, and looked into its eyes again, to see if there were any
tears.

No, there were no tears. 'If you're going to turn into a pig, my dear,'
said Alice, seriously, 'I'll have nothing more to do with you. Mind
now!' The poor little thing sobbed again (or grunted, it was impossible
to say which), and they went on for some while in silence.

Alice was just beginning to think to herself, 'Now, what am I to do with
this creature when I get it home?' when it grunted again, so violently,
that she looked down into its face in some alarm. This time there could
be NO mistake about it: it was neither more nor less than a pig, and she
felt that it would be quite absurd for her to carry it further.
"""
# 1. remove symbols like .,:'!, convert string to lower or uppercase, split text to words
words=''.join((s if s.isalpha() else ' ') for s in text).lower().split()

#2. create a dictionary where key is a unique word and value is number of time this word appeared in test
occurences={}
for word in words:
    occurences[word] = occurences[word]+1 if (word in occurences) else 1

#3. print each unique word togeather with it's frequency

for word,frequency in list(occurences.items()):
    print(f"The word {word} was found {frequency} times")
 
