tupl = 1,2,3,34,4,5,5,["anton", "hello"]
tupl1 =  23,45,3,45,43,23,5,42,["siggi", "dsf"]
tupl2 = []
tupl2.append(tupl)
tupl2.append(tupl1)
#print(tupl2)
siggi = tupl2
print(str(siggi)[1:-1])

ze_tuple = ("tuple", "list")
" ".join(ze_tuple)
'tuple list'
ze_tuple = ("tuple", "list", ["francais", "deutschland"])
list(ze_tuple)
['tuple', 'list', ['francais', 'deutschland']]
string = " ".join(ze_tuple[:-1]) + " " + " ".join(ze_tuple[-1])
'tuple listfrancais deutschland'
print(string.split())
