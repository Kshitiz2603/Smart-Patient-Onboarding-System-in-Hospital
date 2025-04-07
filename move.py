#importing necessary libraries/modules
import os
import shutil

#extracting the full name of the new user and saving it as image's file name in the database
with open('PersonDetails.csv', "r", encoding="utf-8", errors="ignore") as scraped:
    final_line = scraped.readlines()[-1]
    fname = final_line.split(',')[0]
fn = fname + '.png'
print(fn)
os.rename('/Users/kshitiz2000/desktop/pythonpro/imageCap.png',fn)
new_name = os.path.join('/Users/kshitiz2000/desktop/pythonpro/Image/',fn)
shutil.move(fn, new_name)






