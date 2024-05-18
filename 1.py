
def isValidHtml(html):
    pile = [] 
    i = 0 
    while i < len(html):
        if html[i] == '<':
            j = html.find('>', i)
            if j == -1:
                return False  
            balise = html[i+1:j]
            if not balise.startswith('/'): 
                pile.append(balise)
            else:  # Closing tag
                if not balise or balise[-1] != balise[1:]:
                    return False
                pile.pop()
            i = j + 1
        else:
            i += 1

    return not pile

# Example
html1 = "<p></p>"
html2 = "<p><span></p>"
html3 = "<p><span></p></span>"
html4 = "<p><span></span></p>"
print(isValidHtml(html1))  # retourner True
print(isValidHtml(html2))  # retourner False
print(isValidHtml(html3))  #retourner False
print(isValidHtml(html4))  #retourer True
