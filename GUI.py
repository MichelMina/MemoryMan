import wx
import pygame
import sys
"""
Opening the WIKI Video
"""
def Wiki_Question_Handler(Answer):
    if Answer == wx.ID_NO:
        FPS = 60
        pygame.init()
        clock = pygame.time.Clock()
        pygame.mixer.quit()
        movie = pygame.movie.Movie('icons/test.mpg')
        screen = pygame.display.set_mode(movie.get_size())
        movie_screen = pygame.Surface(movie.get_size()).convert()
        movie.set_display(movie_screen)
        movie.play()
        playing = True
        while playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    movie.stop()
                    playing = False

            screen.blit(movie_screen, (0, 0))
            pygame.display.update()
            clock.tick(FPS)

    pygame.quit()

class Mem(wx.Frame):

    holes=[]
    processes=[]
    holes_id=0
    processes_id=0
    def __init__(self, parent, id):

        # Single Choice Dialogue (Choose Management mode)
        select = wx.SingleChoiceDialog(None, 'Please choose the type of your desired scheduler', 'Scheduler Choice',['First fit', 'Best fit','Worst fit'])
        if select.ShowModal() == wx.ID_CANCEL:
            sys.exit()
        # Store the choice and destroy it
        self.Management_Mode = select.GetStringSelection()
        select.Destroy()

        def Holes_Init(self):
            # BMP Buttons
            ''' Add button and Done button .. this will take the Holes data from the user '''
            self.Add = wx.BitmapButton(panel, -1, wx.Image("icons/Add.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap(),
                                      pos=(350, 175), style=wx.BORDER_NONE)
            self.Done = wx.BitmapButton(panel, -1, wx.Image("icons/Done.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap(),
                                      pos=(350, 230), style=wx.BORDER_NONE)

            #binding buttons to events
            self.Bind(wx.EVT_BUTTON, Add_Hole_EVT, self.Add)
            self.Bind(wx.EVT_BUTTON, Done_Hole_EVT, self.Done)

            #Static Texts
            self.Starting_Address= wx.StaticText(panel,-1,"Starting Address",(10,170))
            self.Starting_Address.SetBackgroundColour("white")
            self.Starting_Address.SetFont(
            wx.Font(20, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_ITALIC, wx.BOLD, False, u'Tahoma'))
            self.Hole_Size_static= wx.StaticText(panel,-1,"Hole Size",(10,230))
            self.Hole_Size_static.SetBackgroundColour("white")
            self.Hole_Size_static.SetFont(
            wx.Font(20, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_ITALIC, wx.BOLD, False, u'Tahoma'))

            # Starting Address Input
            self.Starting_Address_Text = wx.TextCtrl(panel, pos=(250, 173), size=(100, 32), style=wx.BORDER_NONE)
            # Changing Starting Address Input font
            self.Starting_Address_Text.SetFont(
            wx.Font(20, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_ITALIC, wx.BOLD, False, u'Viner Hand ITC'))
            # Setting default Value
            self.Starting_Address_Text.Value = '0'
            # Hole Size text input
            self.Hole_Size = wx.TextCtrl(panel, pos=(250, 233), size=(100, 32), style=wx.BORDER_NONE)
            # Changing Hole Size font
            self.Hole_Size.SetFont(
            wx.Font(20, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_ITALIC, wx.BOLD, False, u'Viner Hand ITC'))
            # Setting default Value
            self.Hole_Size.Value = '0'
        def Add_Hole_EVT(event):
            #Appends the list with list of ID, Size, Starting address and increments the ID
            self.holes.append((self.holes_id,int(self.Hole_Size.GetValue()),int(self.Starting_Address_Text.GetValue())))
            self.holes_id += 1
            self.Hole_Size.Value='0'
            self.Starting_Address_Text.Value='0'
        def Done_Hole_EVT(event):
            #Destroys the previous layer, calls the add processes layer
            self.Starting_Address_Text.Destroy()
            self.Starting_Address.Destroy()
            self.Hole_Size_static.Destroy()
            self.Hole_Size.Destroy()
            Processes_Init(self)

        def Add_Process_EVT(event):
            #appends the list with ID, size and increments the PID
            self.processes.append((self.processes_id,int(self.Process_Size.GetValue())))
            self.Process_Size.Value='0'
            self.processes_id += 1
        def Done_Process_EVT(event):
            #destroys the previous layer and calls the backend with data
            self.Process_Size.Destroy()
            self.Process_Size_Static.Destroy()
            self.Add.Hide()
            self.Done.Hide()
            print self.processes
            Output(self)

        def Deallocate_EVT(event):
            #asks user which process to deallocate and sends it to the backend
            dummy = []
            for i in self.processes:
                dummy.append('ID '+str(i[0])+' , Size '+str(i[1]))
            pop = wx.SingleChoiceDialog(None, 'Please choose which process to deallocate', 'Scheduler Choice',dummy)
            if pop.ShowModal() == wx.ID_CANCEL:
                return
            # Store the choice and destroy it
            self.to_be_deallocated = pop.GetStringSelection()
            print self.to_be_deallocated[3]
            """TODO Call Backend"""
            pop.Destroy()

        def Add_More_Process_EVT(event):
            print 1
            """TODO Call Backend"""
        def Done_And_Return_To_Output_EVT(event):
            self.Add.Destroy()
            self.Done.Destroy()
            Output(self)
        def Add_More_EVT(event):
            self.Add_More.Destroy()
            self.Deallocate.Destroy()
            # BMP Buttons
            self.Add = wx.BitmapButton(panel, -1, wx.Image("icons/Add.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap(),
                                      pos=(350, 175), style=wx.BORDER_NONE)
            self.Done = wx.BitmapButton(panel, -1, wx.Image("icons/Done.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap(),
                                      pos=(350, 230), style=wx.BORDER_NONE)

            self.Bind(wx.EVT_BUTTON, Add_More_Process_EVT, self.Add)
            self.Bind(wx.EVT_BUTTON, Done_And_Return_To_Output_EVT, self.Done)

        def Processes_Init(self):
            #Change the  bind
            self.Bind(wx.EVT_BUTTON, Add_Process_EVT, self.Add)
            self.Bind(wx.EVT_BUTTON, Done_Process_EVT,self.Done)
            #Static Texts
            self.Process_Size_Static= wx.StaticText(panel,-1,"Process Size",(10,170))
            self.Process_Size_Static.SetBackgroundColour("white")
            self.Process_Size_Static.SetFont(
            wx.Font(20, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_ITALIC, wx.BOLD, False, u'Tahoma'))

            self.Process_Size = wx.TextCtrl(panel, pos=(200, 173), size=(100, 32), style=wx.BORDER_NONE)
            self.Process_Size.SetFont(
            wx.Font(20, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_ITALIC, wx.BOLD, False, u'Viner Hand ITC'))
            # Setting default Value
            self.Process_Size.Value = '0'

        def Output(self):
            self.Deallocate = wx.BitmapButton(panel, -1, wx.Image("icons/Deallocate.bmp", wx.BITMAP_TYPE_ANY).ConvertToBitmap(),
                                      pos=(0,100), style=wx.BORDER_NONE)
            self.Add_More = wx.BitmapButton(panel, -1, wx.Image("icons/Add.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap(),
                                      pos=(100,100), style=wx.BORDER_NONE)
            self.Bind(wx.EVT_BUTTON, Deallocate_EVT, self.Deallocate)
            self.Bind(wx.EVT_BUTTON, Add_More_EVT, self.Add_More)




        # Did you read the wiki?
        WikiQuestion = wx.MessageDialog(None, 'Did you read the "how to use" Wiki?', 'Title', wx.YES_NO)
        WikiQuestion_Answer = WikiQuestion.ShowModal()
        WikiQuestion.Destroy()
        Wiki_Question_Handler(WikiQuestion_Answer)

        # Main Frame
        image = 'icons/roses.png'
        self.bmp1 = wx.Image(image, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.Width = self.bmp1.GetWidth()
        self.Hight = self.bmp1.GetHeight()
        wx.Frame.__init__(self, parent, id, "Memory Holes manager", size=(self.Width, self.Hight/1.5),
                          style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)
        panel = wx.Panel(self)
        # Making the Dinosaurs picture the main panel
        self.bitmap1 = wx.StaticBitmap(self, -1, self.bmp1, (0, 0))
        panel = self.bitmap1
        #OS scheduler animated text
        OS = 'icons/0.bmp'
        OS_im = wx.Image(OS, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, OS_im, (0, 0))


        Holes_Init(self)


        """HELP ME! button """
        HELP = wx.BitmapButton(panel, -1, wx.Image("icons/help.bmp", wx.BITMAP_TYPE_ANY).ConvertToBitmap(), pos=(1200, 5),
                               style=wx.BORDER_NONE)
        self.Bind(wx.EVT_BUTTON, lambda event: self.Play_Video(event), HELP)
        self.Panel1 = panel


    #Play wiki video handler
    def Play_Video(self, event):
        Wiki_Question_Handler(wx.ID_NO)
#Main
if __name__ == '__main__':
    app = wx.App(0)
    frame = Mem(parent=None, id=-1)
    frame.Show(True)
    app.MainLoop()
