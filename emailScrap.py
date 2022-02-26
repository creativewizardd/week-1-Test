import pandas as pd
import re

#non_human regular expression
regex = '[a-z]{1,8}@[a-z]+[.][a-z]+'
#Reading the textfile
with open('websiteData.txt', encoding='utf8') as f:
    lines = f.read()


#extracting all the valid emails using regular expression
findEmail = re.findall('[\w\.-]+@[\w\.-]+\.\w+', lines)

#classifying type of email
type = []
for word in findEmail:
    if(re.match(regex, word)):
        type.append('nonhuman')
    else:
        type.append('human')

#counting occurence
d = {}
for word in findEmail:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1

#Creating dataframe
data_items = d.items()
data_list = list(data_items)
df = pd.DataFrame(data_list, columns = ['email','occurences'] )

#adding type column
df['type'] = type

#setting index
df.set_index('email', inplace= True)


#Converting to json format
Out = df.to_json(orient = 'index')

#Writing to json file
with open('result.json','w') as outfile:
	outfile.write((Out))