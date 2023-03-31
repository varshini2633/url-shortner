import pyshorteners
link=input("Enter the link :")
shortner=pyshorteners.Shortener()
x=shortner.tinyurl.short(link)
print(x)