import wikipedia
 
# nExtracting Summary Of An Article

print(wikipedia.summary("google"))

# if you want to get the search title of a page

print(wikipedia.search("facebook"))

# Changing Language Of An Article

print(wikipedia.set_lang("ar"))
 
print(wikipedia.summary("facebook"))
 

#if you want to get suggestion for what you are searching

print(wikipedia.suggest("faceook"))

# If you want to get complete content from a page on wikipedia 

complete_content = wikipedia.page("facebook")
print(complete_content.content)

# Getting URL Of A Page

complete_url = wikipedia.page("facebook")
print(complete_url.url)

# Extracting Images Included In A Page 

page_image = wikipedia.page("India")
print(page_image.images[0])

# Downloading Images From A Page

page_image = wikipedia.page("facebook")
image_down_link = page_image.images[1]

#Extracting The Title Of Page

page_Title = wikipedia.page("Indian Demographic")
print(page_Title.title)

# 