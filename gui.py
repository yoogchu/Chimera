import Tkinter as tk
import cv2
from PIL import Image, ImageTk
import facial

# Layout setup
width, height = 600, 600
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Important variables 
people = []
webcam=True
folder='faces'

def show_frame():
	global people	
	
	(frame, people) = facial.recog(people, cap)
	# frame = cv2.flip(frame, 1)
	cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
	img = Image.fromarray(frame)
	imgtk = ImageTk.PhotoImage(image=img)
	
	lmain.imgtk = imgtk
	lmain.configure(image=imgtk)
	lmain.after(10, show_frame)

def close_window(people):
	root.quit()
	print 'Exiting...'

	print 'Saving faces in: '+folder
	facial.save_faces(people,folder=folder,webcam=webcam,)


# Tkinkter
root = tk.Tk()
root.bind('<Escape>', lambda e: close_window(people))
root.title('Gotcha Bitch!')
root.geometry('1280x800')
lmain = tk.Label(root)
lmain2 = tk.Label(root)
lmain.pack(side=tk.LEFT)
lmain2.pack(side=tk.RIGHT)
person = 0 
for r in range(4):
	for c in range(4):
		tk.Label(lmain2, text='%s, %s'%('Person', str(person)), borderwidth=1 ).grid(row=r,column=c)
		person+=1


show_frame()
root.mainloop()

