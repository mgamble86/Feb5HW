from __future__ import division

#defines function
def get_at_content(dna):
	length = len(dna)
	#.upper changes lowercase to capitals so function can count them
	a_count = dna.upper().count('A')
	t_count = dna.upper().count('T')
	at_content = (a_count + t_count) / length
	#round to 2 decimal places
	return round (at_content, 2)

#Defines new variable to measure function content	
my_at_content = get_at_content("ATTTGGGCCCCCTTTCCC")
#print code
print(str(my_at_content))
#print AT content
print(get_at_content("ATTTGGGCCCCCTTTAAAGG"))
#print at content lowercase
print(get_at_content("aatttttcccccgggggga"))
#bonus count
print(get_at_content("tnnacgnnat"))
#other bonus count
my_at_content = get_at_contentC("TTCGNNN")
