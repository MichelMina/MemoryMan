import wx
import pygame

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


    def __init__(self, parent, id):

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
        wx.Frame.__init__(self, parent, id, "Memory Holes manager", size=(self.Width, self.Hight),
                          style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)
        panel = wx.Panel(self)
        # Making the Dinosaurs picture the main panel
        self.bitmap1 = wx.StaticBitmap(self, -1, self.bmp1, (0, 0))
        panel = self.bitmap1
        '''# OS scheduler animated text
        OS = 'icons/0.bmp'
        OS_im = wx.Image(OS, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, OS_im, (0, 0))'''
        def Holes_Init(self):
            # BMP Buttons
            self.Add_Hole = wx.BitmapButton(panel, -1, wx.Image("icons/Add.bmp", wx.BITMAP_TYPE_ANY).ConvertToBitmap(),
                                      pos=(350, 175), style=wx.BORDER_NONE)
            self.Done_Holes = wx.BitmapButton(panel, -1, wx.Image("icons/Done.bmp", wx.BITMAP_TYPE_ANY).ConvertToBitmap(),
                                      pos=(500, 180), style=wx.BORDER_NONE)
            #Static Texts
            self.Starting_Address= wx.StaticText(panel,-1,"Starting Address",(10,170))
            self.Starting_Address.SetFont(
            wx.Font(20, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_ITALIC, wx.BOLD, False, u'Viner Hand ITC'))
            self.Hole_Size= wx.StaticText(panel,-1,"Hole Size",(10,230))
            self.Hole_Size.SetFont(
            wx.Font(20, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_ITALIC, wx.BOLD, False, u'Viner Hand ITC'))

            # Starting Address Input
            Starting_Address_Text = wx.TextCtrl(panel, pos=(250, 173), size=(100, 32), style=wx.BORDER_NONE)
            # Changing Starting Address Input font
            Starting_Address_Text.SetFont(
            wx.Font(20, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_ITALIC, wx.BOLD, False, u'Viner Hand ITC'))
            # Setting default Value
            Starting_Address_Text.Value = '0'
            # Hole Size text input
            Hole_Size = wx.TextCtrl(panel, pos=(250, 233), size=(100, 32), style=wx.BORDER_NONE)
            # Changing Hole Size font
            Hole_Size.SetFont(
            wx.Font(20, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_ITALIC, wx.BOLD, False, u'Viner Hand ITC'))
            # Setting default Value
            Hole_Size.Value = '0'




        Holes_Init(self)

        '''
        """ Arrival time objects """
        # Arrival Time static text
        wx.StaticBitmap(self, -1, wx.Image('icons/1.bmp', wx.BITMAP_TYPE_ANY).ConvertToBitmap(), (0, 120))
        # Arrival Time text
        Arrival_Time_Text = wx.TextCtrl(panel, pos=(250, 137), size=(100, 32), style=wx.BORDER_NONE)
        # Changing arrival time font
        Arrival_Time_Text.SetFont(
            wx.Font(20, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_ITALIC, wx.BOLD, False, u'Viner Hand ITC'))
        # Setting default Value
        Arrival_Time_Text.Value = '0'
        # Arrival_Time_Static = wx.StaticText(panel, -1, 'Arrival time', pos=(10, 10), size=(-1, -1), style=0)

        """ Burst Time objs """
        # Burst time static text
        wx.StaticBitmap(self, -1, wx.Image('icons/2.bmp', wx.BITMAP_TYPE_ANY).ConvertToBitmap(), (5, 188))
        # Burst time Text
        Burst_Time_Text = wx.TextCtrl(panel, pos=(250, 187), size=(100, 32), style=wx.BORDER_NONE)
        Burst_Time_Text.Value = '0'
        # Changing font
        Burst_Time_Text.SetFont(
            wx.Font(20, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_ITALIC, wx.BOLD, False, u'Viner Hand ITC'))
        # Burst_Time_Static = wx.StaticText(panel, -1, 'Burst time', pos=(10, 30), size=(-1, -1), style=0)




        """Finish Button"""
        # Finish process addition button
        self.Finish = wx.BitmapButton(panel, -1, wx.Image("icons/Schedule.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap(),
                                      pos=(480, 125), style=wx.BORDER_NONE)
        self.Bind(wx.EVT_BUTTON, lambda event: self.Finish_EVT(event, Scheduler_Mode_Answer), self.Finish)

        """HELP ME! button """
        HELP = wx.BitmapButton(panel, -1, wx.Image("icons/help.bmp", wx.BITMAP_TYPE_ANY).ConvertToBitmap(), pos=(1200, 5),
                               style=wx.BORDER_NONE)
        self.Bind(wx.EVT_BUTTON, lambda event: self.Play_Video(event), HELP)
        self.Panel1 = panel

        # Add button action event handlers
        if Scheduler_Mode_Answer == 'FCFS' or Scheduler_Mode_Answer == 'SJF Preemptive' or Scheduler_Mode_Answer == 'SJF non-Preemptive':
            self.Bind(wx.EVT_BUTTON, lambda event: self.Add_Process_EVT(event, Burst_Time_Text, Arrival_Time_Text),
                      Add_Process)

        elif Scheduler_Mode_Answer == 'Priority preepmtive' or Scheduler_Mode_Answer == 'Priority non-Preemptive':
            self.Bind(wx.EVT_BUTTON,
                      lambda event: self.Add_Process_EVT_P(event, Burst_Time_Text, Arrival_Time_Text, Priority_Text),
                      Add_Process)

        elif Scheduler_Mode_Answer == 'Round Robin':
            self.Bind(wx.EVT_BUTTON, lambda event: self.Add_Process_EVT_T(event, Burst_Time_Text, Arrival_Time_Text,
                                                                          Time_Slice_Spinner, panel), Add_Process)'''


    #Play wiki video handler
    def Play_Video(self, event):
        Wiki_Question_Handler(wx.ID_NO)

#Main
if __name__ == '__main__':
    app = wx.App(0)
    frame = Mem(parent=None, id=-1)
    frame.Show(True)
    app.MainLoop()
