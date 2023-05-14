import pygame
import time
import _thread
import tkinter
from tkinter.colorchooser import *
class main(object):
    def __init__(self):
        pygame.init()
        self.version = '0.0.1 Alpha'
        self.height = 700
        self.width = 600
        self.stringWidth = 5
        self.eraser = False
        self.draw = False
        self.posList = []
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.screen.fill([255,255,255])
        self.stringColor = [0,0,0]
        self.bgColor = [255,255,255]
        self.font = pygame.font.Font(
            "default.ttf", 70)
        self.running = True
        pygame.display.set_caption("Draw Board")
        _thread.start_new_thread(graphics.graphic,(self,1))
        _thread.start_new_thread(dock.dock,(self,0))
        main.main(self)
        
    def main(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.draw = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.draw:
                        self.draw = False
                        self.posList = []
                if self.draw:
                    try:
                        x,y = pygame.mouse.get_pos()
                    except:
                        continue
                    self.posList.append((x,y))
        pygame.quit()
        quit()
class graphics(main):
    def graphic(self,a):
        tools.startScreen(self)
        self.screen.fill(self.bgColor)
        while self.running:
            
            if self.posList != []:
                posBefore = self.posList[0]
                for i in self.posList:
                    add = int(self.stringWidth//2)
                    if not self.eraser:
                        pygame.draw.line(self.screen,self.stringColor,posBefore,i,width=self.stringWidth)
                        pygame.draw.circle(self.screen,self.stringColor,[i[0],i[1]],add)
                    else:
                        pygame.draw.line(self.screen,self.bgColor,posBefore,i,width=self.stringWidth)
                        pygame.draw.circle(self.screen,self.bgColor,[i[0],i[1]],add)
                    posBefore = i
            pygame.display.update()
class tools(main):
    def startScreen(self):
        self.screen.blit(self.font.render("Draw Board",True,'black'),(100,300))
        pygame.display.update()
        time.sleep(0.3)
    
class dock(main):
    def dock(self,arg):
        screen = tkinter.Tk()
        screen.title("Dock")
        self.sgButton = tkinter.Button(screen,text="画笔颜色",relief="flat",command=lambda:dock.stringColor_callback(self))
        self.swLabel=tkinter.Label(text="画笔粗细:")
        self.swLabel.grid(column=1,row=0)
        self.sgWidth = tkinter.Button(screen,text="5",relief="flat",command=lambda:dock.string_callback(self))
        self.bgButton = tkinter.Button(screen,text="背景颜色",relief="flat",command=lambda:dock.bgColor_callback(self))
        self.modeButton = tkinter.Button(screen,text="画笔",relief="flat",command= lambda:dock.mode_callback(self))
        clear = tkinter.Button(screen,text="清除",relief="flat",command=lambda:dock.clear(self) )
        self.sgButton.grid(column=0,row=0)
        self.sgWidth.grid(column=2,row=0)
        self.bgButton.grid(column=3,row=0)
        self.modeButton.grid(column=4,row=0)
        clear.grid(column=5,row=0)
        tkinter.mainloop()
    def clear(self):
        self.screen.fill(self.bgColor)
    def mode_callback(self):
        if self.eraser == False:
            self.eraser = True
            self.modeButton["text"] = '橡皮'
            return ""
        if self.eraser == True:
            self.eraser = False
            self.modeButton["text"] = '画笔'
    def stringColor_callback(self):
        self.stringColor = dock.choose_color(self)
    def bgColor_callback(self):
        self.bgColor = dock.choose_color(self)
        self.screen.fill(self.bgColor)
    def choose_color(self):
        color = askcolor()[0]
        return color
    def string_callback(self):
        window = tkinter.Tk()
        window.title("线条宽度")
        scaleBar = tkinter.Scale(window,relief="flat",from_=1,to=110,orient="horizontal",command= lambda pos:dock.scale_callback(self,scaleBar,))
        scaleBar.pack(side="top")
        saveButton = tkinter.Button(window,text="确定",relief="flat",command=lambda:quit)
        saveButton.pack(side="bottom")
        tkinter.mainloop()
    def scale_callback(self,scale):
        width = scale.get()
        self.stringWidth = width
        self.sgWidth["text"] = width
    

class test():
    pass
main()