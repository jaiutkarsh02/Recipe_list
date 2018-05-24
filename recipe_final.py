
# coding: utf-8

# In[153]:


import json,os,sys,re


# In[32]:


# f= open('/home/nishant/Downloads/allRecipesInStructure.txt','r')


# In[154]:


with open('C:/Users/jaiu978/Desktop/allRecipesInStructure.txt','r') as myfile:
    data=myfile.read()


# In[155]:


flis=data.split('\n')


# In[156]:


flis = list(filter(None, flis))
# print(str_list)


# In[157]:


recipe=[]


# In[158]:


strt=re.compile('START RECIPE')
ing=re.compile('INGREDIENTS')
direc=re.compile('DIRECTIONS')


# In[159]:


unit=['cup','tbsp','tablespoon','teaspoon','ounce']


# In[160]:


for idx,i in enumerate(flis):
#     print(i)
    if strt.search(i):
        recipe.append(idx)


# In[161]:


a=[(x,y) for x,y in zip(recipe,recipe[1:])]
# print(lis[a[0][0]:a[0][1]])


# In[165]:


for j in a:
    lis=flis[j[0]:j[1]]
    out={}
    out['id']=''
    out['RecipeName']=''
    out['Ingredients']=[]
    out['instructions']=''
    for idx,i in enumerate(lis):
    #     print(i)
        if strt.search(i):
            s_id=idx
        elif ing.search(i):
            i_id=idx
        elif direc.search(i):
            d_id=idx
#     print(not i_id)
    for k in lis[s_id+1:i_id]:
        if re.search('([A-Z\s]){1,}$',k.strip()) and 'recipe by' not in k.lower():

            out['RecipeName']=k.strip()
    if not out['RecipeName']:
        try:
            out['RecipeName']=lis[s_id+1]
        except IndexError:
            continue

    for idx,k in enumerate(lis[i_id+1:d_id]):
        dic={}
        dic['i_id']=''
        try:
            dic['quantity']=re.match('([\d/.\- ]){1,}',k).group(0)
        except AttributeError:
            dic['quantity']=''

        try:
            dic['unit']=unit[[i for i, j in enumerate([re.search(x,k.lower()) for x in unit]) if j is not None][0]]
        except IndexError:
            dic['unit']=''
        if dic['unit']:
            re.search
    #     print(dic['quantity'])
        qty=re.compile(dic['quantity'])
        ingr=re.sub(dic['unit'],'',k)
        ingr=re.sub(dic['quantity'],'',ingr).strip()
        dic['ingredientName']=re.sub('^(s )','',ingr)
        out['Ingredients'].append(dic)
    out['instructions']=' '.join(lis[d_id+1:])

    print(json.dumps(out))

