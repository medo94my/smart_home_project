import os
import datetime
current_path= os.getcwd()
img_name='image-'+str(datetime.datetime.now())+'.jpg'
new_path=os.path.join(current_path,img_name)
print(new_path)
