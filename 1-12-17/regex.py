import re

def get_matching_words(regex):
    words = ["aca","aeiou","aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

    return [word for word in words if re.search(regex, word)]
result = get_matching_words('v+')
print result,'\n'
result = get_matching_words('s{2}')
print result,'\n'
result = get_matching_words('e$')
print result,'\n'
result=get_matching_words('b.b')
print result,'\n'
result=get_matching_words('b.+b')
print result,'\n'
result=get_matching_words('b.*b')
print result,'\n'
result=get_matching_words('aeiou')
print result, '\n'
result=get_matching_words('[regularexpression]')
print result,'\n'
result=get_matching_words('a.*a|b.*b|c.*c')
print result,'\n'
