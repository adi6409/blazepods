from bleak import BleakClient
from tkinter import *
import time
import asyncio
address = "C5:02:0A:BD:EF:E3"
touchuuid = "50c9727e-4cb8-4c84-b745-0e58a0280cd6"
sheeesh = 1

class StopWatch(Frame):  
    """ Implements a stop watch frame widget. """                                                                
    def __init__(self, parent=None, **kw):        
        Frame.__init__(self, parent, kw)
        self._start = 0.0        
        self._elapsedtime = 0.0
        self._running = 0
        self.timestr = StringVar()               
        self.makeWidgets()      

    def makeWidgets(self):                         
        """ Make the time label. """
        l = Label(self, textvariable=self.timestr)
        self._setTime(self._elapsedtime)
        l.pack(fill=X, expand=NO, pady=2, padx=2)                      
    
    def _update(self): 
        """ Update the label with elapsed time. """
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)
    
    def _setTime(self, elap):
        """ Set the time string to Minutes:Seconds:Hundreths """
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds)*100)                
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, hseconds))
        
    def Start(self):                                                     
        """ Start the stopwatch, ignore if running. """
        if not self._running:            
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1        
    
    def Stop(self):                                    
        """ Stop the stopwatch, ignore if stopped. """
        if self._running:
            self.after_cancel(self._timer)            
            self._elapsedtime = time.time() - self._start    
            self._setTime(self._elapsedtime)
            self._running = 0
    
    def Reset(self):                                  
        """ Reset the stopwatch. """
        self._start = time.time()         
        self._elapsedtime = 0.0    
        self._setTime(self._elapsedtime)
        
        
def main():
    root = Tk()
    sw = StopWatch(root)
    sw.pack(side=TOP)
    Button(root, text='Start', command=sw.Start).pack(side=LEFT)
    Button(root, text='Stop', command=sw.Stop).pack(side=LEFT)
    Button(root, text='Reset', command=sw.Reset).pack(side=LEFT)
    Button(root, text='Quit', command=root.quit).pack(side=LEFT)

    root.mainloop()


async def run(address):
    async with BleakClient(address) as client:
        while sheeesh > 0:
            model_number = await client.read_gatt_char(touchuuid)
            pressedfile = open("pressed.txt","rb")
            pressedvalue = pressedfile.read()
            if model_number != pressedvalue:
                pressedwrite = open("pressed.txt","w")
                pressedwrite.close()
                pressedfile.close()
                writebytes = open("pressed.txt","wb")
                writebytes.write(model_number)
                print(model_number)
                if sheeesh==1 :
                    sw.Start
                    sheeesh = sheeesh + 1
                else:
                    sw.Stop
                    sheeesh = sheeesh - 1
                writebytes.close()

def looping():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(address))
if __name__ == '__main__':
    looping()
    main()
