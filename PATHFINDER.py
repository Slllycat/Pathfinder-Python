#simple pathfinder hahaha forschadowing ???
import tkinter as tk
import random,time

delay=1
biggnes=15
fullness=15
size = 25
size2 = size**2
tt=0

#bot
bx=0
by=0
ziel=0
dirb=[]
path=[]
distb=[]
for i in range(size2):
    distb.append(-1)




#window setup
window = tk.Tk()
window.title("BLEH")
window.geometry(str(size * biggnes) + "x" + str(size * biggnes))
canvas = tk.Canvas(window, width=(size * biggnes), height=(size * biggnes), bg="white")
canvas.pack()



#resets
def reset():
    global size,size2,blocks,near,fullness,bx,by,distb,dirb
    blocks = []
    near = []
    for i in range(size):
        blocks.append(1)
    for i in range(size-2):
        blocks.append(1)
        for i in range(size-2):
            if random.randint(1,100)<=fullness:
                blocks.append(1)
            else:
                blocks.append(0)
        blocks.append(1)
    for i in range(size):
        blocks.append(1)
    for i in range(1000):
        bx=random.randint(1,size-1)
        by=random.randint(1,size-1)
        if blocks[bx+(by*size)]==0:
            return






#bro i cant its 3 in the morning  >:]
def newdest():
    global path,dirb,distb,bx,by,size,size2,blocks,ziel
    ib=bx+by*size
    dirb=[]
    distb=[]
    for i in range(size2):
        distb.append(-1)

    for i in range(size2):
        dirb.append(0)

    distb[ib]=0
    dirb[ib]=-1

    #optimal path for everywhere
    for i in range(30):
        weg=0
        for i in range(size2):
            if blocks[weg]==0 and distb[weg]!=-1:
                if blocks[weg+1]==0 and not(distb[weg+1]>=0):
                    distb[weg+1]=distb[weg]+1
                    dirb[weg+1]=weg

                if blocks[weg-1]==0 and not(distb[weg-1]>=0):
                    distb[weg-1]=distb[weg]+1
                    dirb[weg-1]=weg

                if blocks[weg+size]==0 and not(distb[weg+size]>=0):
                    distb[weg+size]=distb[weg]+1
                    dirb[weg+size]=weg

                if blocks[weg-size]==0 and not(distb[weg-size]>=0):
                    distb[weg-size]=distb[weg]+1
                    dirb[weg-size]=weg



            weg=weg+1
    ziel=0
    while distb[ziel]<=5:
        ziel=random.randint(1,size2)

    weg=ziel
    while dirb[weg]>=0:
        path.append(weg)
        weg=dirb[weg]
reset()




def render():
    global cube,blocks,bx,by,size,path,ziel,delay,tt
    tick()
    tt=time.time()
    x = 0
    y = biggnes*size
    weg = 0
    canvas.delete("all")
    # RENDER BLOCKS
    for i in range(size):
        for i in range(size):
            if blocks[weg] == 1:
                cube = canvas.create_rectangle(x, y, x + biggnes, y - biggnes, fill="black")
            else:

                if bx+by*size==weg:
                    cube = canvas.create_rectangle(x, y, x + biggnes, y - biggnes, fill="red", outline="red")

                elif weg==ziel:
                    cube = canvas.create_rectangle(x, y, x + biggnes, y - biggnes, fill="orange", outline="orange")

                elif weg in path:
                    cube = canvas.create_rectangle(x, y, x + biggnes, y - biggnes, fill="lightgreen", outline="lightgreen")

                else:
                    cube = canvas.create_rectangle(x, y, x + biggnes, y - biggnes, fill="white", outline="white")


            weg = weg + 1
            x = x + biggnes
        x = 0
        y = y - biggnes
    window.after(delay, render)


def tick():
    global path,dirb,distb,bx,by,size,tt
    if len(path)==0:
        tt=time.time()
        newdest()
        print("LOADING ALLLLLL",time.time()-tt)
    else:
        bx=path[len(path)-1]%size
        by=path[len(path)-1]//size
        path.pop()
        print("run:",time.time()-tt)




render()
window.mainloop()
