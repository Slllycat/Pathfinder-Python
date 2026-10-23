#simple pathfinder hahaha forschadowing ???
import tkinter as tk
import random,time


gotocorsor=1
debug=1
delay=1
biggnes=15
fullness=15
size=25
size2=size**2
tt=0
mx=0
my=0

#bot
bx=0
by=0
ziel=0
ttt=50
mind=5
maxd=ttt
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



def mouse_pos(event):
    global mx, my
    mx, my = event.x, event.y
canvas.bind("<Motion>", mouse_pos)


#bro i cant its 3 in the morning  >:]
def newdest():
    global path,dirb,distb,bx,by,size,size2,blocks,ziel,mx,my
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
    for i in range(ttt):
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
    if gotocorsor and mx!=0:
        ziel=(mx//biggnes)+(my//biggnes)*size
        if distb[ziel]==-1:
            while distb[ziel]<=mind or distb[ziel]>=maxd:
                ziel=random.randint(1,size2)
    else:
        ziel=0
        while distb[ziel]<=mind or distb[ziel]>=maxd:
            ziel=random.randint(1,size2)

    weg=ziel
    while dirb[weg]>=0:
        path.append(weg)
        weg=dirb[weg]
reset()




def render():
    global cube,blocks,bx,by,size,path,ziel,delay,debug,dirb,distb,tt
    tick()
    tt=time.time()
    x = 0
    y = biggnes*size
    weg = 0
    canvas.delete("all")
    img=tk.PhotoImage(width=size,height=size)
    m=max(distb)
    for y in range(size):
        row=[]
        for x in range(size):
            weg=y*size+x
            if blocks[weg]==1:
                row.append("#000000")
            elif debug==1:
                if bx+by*size==weg:
                    row.append("#FF0000")
                elif weg==ziel:
                    row.append("#FFA500")
                elif weg in path:
                    row.append("#00FF00")
                else:
                    row.append("#FFFFFF")
            elif debug==2:
                if distb[weg]>-1:
                    g_b=int(255*(distb[weg]/m))  # 255 -> 0
                    color=f"#{g_b:02x}{g_b:02x}{g_b:02x}"
                    row.append(color)
                else:
                    row.append("#FF0000")
        img.put("{" + " ".join(row) + "}", to=(0, y))
    scaled = img.zoom(biggnes, biggnes)
    canvas.image = scaled
    canvas.delete("all")
    canvas.create_image(0, 0, image=scaled, anchor="nw")
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
