# Updating scraped news data to remove unnecessary textual units

def replace_all(text, arr):
  for each in arr:
    text=text.replace(each,"")
  return text

to_replace= ["None", "Click here for your comments", "Comment via Facebook", "Don't have facebook account? Use this form to comment ", "Published: 02-07-2016"]
f = open('hellotxt.csv','r')
filedata = f.read()
f.close()
newdata = replace_all(filedata, to_replace)
f = open('hellotxt.csv','w')
f.write(newdata)
f.close()

