'''
Real time example: downloading
'''
import threading
# import time
# def download_file(file):
#     print("downloading ",file)
#     time.sleep(2)
#     print(file,"finished")
# file=["movie.mp4",
#       "song.mp3",
#       "image.jpg"
#       ]
# threads=[]
# for f in file:
#   t=threading.Thread(target=download_file,args=(f,))
#   threads.append(t)
#   t.start()
# for t in threads:
#    t.join()
# print("all downloads finished")

import time
def student(name):
   print(name,"start exam")
   time.sleep(3)
   print(name,"submitted paper")
