import os
import sys
import platform


class Graphical_User_Interface_Menus_Collection_And_Related_Operations:
    detected_operating_system = platform.system()
    selected_menu_screen = None


    def __init__(self, init_selected_menu_screen):
        self.selected_menu_screen = init_selected_menu_screen

    def GUI_Function_Operator(self):

        try:
            return_value = ""

            if self.selected_menu_screen == "main menu screen":
                return_value = self.__Main_Menu_Screen()

            elif self.selected_menu_screen == "transcription sub menu":
                return_value = self.__Transcription_Sub_Menu()

            elif self.selected_menu_screen == "youtube transcription sub menu":
                return_value = self.__YouTube_Transcription_Sub_Menu()

            elif self.selected_menu_screen == "audio file transcription sub menu":
                return_value = self.__Audio_File_Transcription_Sub_Menu()

            elif self.selected_menu_screen == "file location":
                return_value = self.__File_Location_Selection_Menu()

            elif self.selected_menu_screen == "file name selection sub menu":
                return_value = self.__File_Binary_Data_Assembly_File_Name_Selection_Menu()

            elif self.selected_menu_screen == "file extension selection sub menu":
                return_value = self.__File_Binary_Data_Assembly_File_Type_Selection_Menu()

            elif self.selected_menu_screen == "pytube module warning":
                self.__Pytube_Module_Warning_Message()

            elif self.selected_menu_screen == "whisper module warning":
                self.__Whisper_Module_Warning_Message()

            elif self.selected_menu_screen == "pytube module installed":
                self.__Pytube_Module_Warning_Message()

            elif self.selected_menu_screen == "whisper module installed":
                self.__Whisper_Module_Warning_Message()

            elif self.selected_menu_screen == "numpy module warning":
                self.__Numpy_Module_Update_Warning()

            elif self.selected_menu_screen == "numpy module updated":
                self.__Numpy_Module_Update_Warning_Installed()

            elif self.selected_menu_screen == "transcription error linux":
                return_value = self.__Transcription_Error_Message_Linux()

            elif self.selected_menu_screen == "transcription error windows":
                return_value = self.__Transcription_Error_Message_Windows()

            elif self.selected_menu_screen == "settings menu":
                return_value = self.__Settings_Menu()

            elif self.selected_menu_screen == "speech model processing menu":
                return_value = self.__Speech_Model_Processing_Unit_Selection()

            elif self.selected_menu_screen == "speech model menu":
                return_value = self.__Speech_Model_Selection_Sub_Menu()

            elif self.selected_menu_screen == "details page":
                return_value = self.__Details_Page()

            elif self.selected_menu_screen == "transcription warning":
                self.__Transcription_In_Progress_Warning_Message()

            return return_value

        except KeyboardInterrupt:
            sys.exit(0)

    def __clear_screen(self):
        try:
            if self.detected_operating_system == "Windows":
                os.system('cls')

            else:
                os.system('clear')

        except KeyboardInterrupt:
            sys.exit(0)

    def __Main_Menu_Screen(self):
        self.__clear_screen()

        print("                                                      7PB5~")
        print("                                                     :@@@@B")
        print("                                                      !&@#:")
        print("                      :!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!&@B!!!~")
        print("                      ?@@@@@@@@&&@@@@@@@@@@@@@@@@@@@&&@@@@@@@B")
        print("                      ?@@@@@@@@&&@@@@@@@@@@@@@@@@@@@&&@@@@@@@B")
        print("                      ?@@@@&Y!^::^?G@@@@@@@@@@@@&Y!^::^?G@@@@B")
        print("                      ?@@@G:        7@@@@@@@@@@G.        7@@@B")
        print("                      ?@@@^          P@@@@@@@@@^          P@@B")
        print("                      ?@@@?         .#@@@@@@@@@?         .#@@B")
        print("                      ?@@@@Y:     .!B@@@@@@@@@@@J:     .!B@@@B")
        print("                      ?@@@@@&B5Y5P#@@@@@@@@@@@@@@&B5Y5P#@@@@@B")
        print("                      ?@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@B")
        print("                      ?@@@@@@#GP#@@@@@@@@@@@@@@@@@&BG#@@@@@@@B")
        print("                      ?@@@@@J.   7#&&&&&&&&&&&&&&Y:  .7&@@@@@B")
        print("                      ?@@@@@~     .::::::::::::::      G@@@@@B")
        print("                      ?@@@@@~                          G@@@@@B")
        print("                      ?@@@@@~     ...............      G@@@@@B")
        print("                      ?@@@@@J.  .7###############?.   ~&@@@@@B")
        print("                      ?@@@@@@&GG&@@@@@@@@@@@@@@@@@#GPB@@@@@@@#")
        print("                      ?@@@@@@@@&&@@@@@@@@@@@@@@@@@@@&&@@@@@@@B")
        print("")
        print("")
        print("=======  ======= ======= ==   == ======= ======= ======= ==   == ======= ======= ======= =======")
        print("|||||||  ||||||| ||||||| |||  || ||||||| ||||||| |||||||  || ||  ||||||  ||||||| ||||||| |||||||")
        print("  |||    ||   || ||   || |||| || |||     |||     |||  ||   |||   |||  ||   |||   ||   || |||  ||")
        print("  |||    ||||||| ||||||| || |||| ||||||| |||     |||||||   |||   ||||||    |||   ||   || |||||||")
        print("  |||    ||  ||  ||   || ||  |||     ||| |||     ||  ||    |||   |||       |||   ||   || ||  || ")
        print("  |||    ||   || ||   || ||   || ||||||| ||||||| ||   ||   |||   |||       |||   ||||||| ||   ||\n\n")
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("[]                                       MAIN MENU                                             []")
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("[]                                                                                             []")
        print("[]                           - PRESS 'T' TO TRANSCRIBE A FILE                                  []")
        print("[]                                                                                             []")
        print("[]                           - PRESS 'E' TO EXIT                                               []")
        print("[]                                                                                             []")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| |||||||")

        selected_input = input("\n\n[ _ Input ]: ")
        return selected_input

    def __Transcription_Sub_Menu(self):
        self.__clear_screen()

        print("\n\n|||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("[]                 TRANSCRIPTION                 []")
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("[]                                               []")
        print("[] - PRESS 'Y' TO TRANSCRIBE FROM A YOUTUBE LINK []")
        print("[]                                               []")
        print("[] - PRESS 'A' TO TRANSCRIBE FROM AN AUDIO FILE  []")
        print("[]                                               []")
        print("[] - PRESS 'S' FOR TRANSCRIPTION SETTINGS        []")
        print("[]                                               []")
        print("[] - PRESS 'D' FOR DETAILS                       []")
        print("[]                                               []")
        print("[] - PRESS 'M' TO GO BACK TO THE MAIN MENU       []")
        print("[]                                               []")
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||")

        selected_input = input("\n\n[ _ Input ]: ")
        return selected_input

    def __YouTube_Transcription_Sub_Menu(self):
        self.__clear_screen()

        print("\n\n||||||||||||||||||||||||||||||||||||||||||")
        print("[] INSERT THE YOUTUBE LINK OF THE VIDEO []")
        print("[] YOU WANT TO TRANSCRIBE               []")
        print("[]                                      []")
        print("[] ENTER '_BACK' TO GO BACK             []")
        print("||||||||||||||||||||||||||||||||||||||||||")

        selected_input = input("\n\n[ _ Input ]: ")
        return selected_input

    def __Audio_File_Transcription_Sub_Menu(self):
        self.__clear_screen()

        print("\n\n||||||||||||||||||||||||||||||||||||||")
        print("[] INSERT THE FULL PATH TO THE FILE []")
        print("[] YOU WANT TO TRANSCRIBE           []")
        print("[]                                  []")
        print("[] ENTER '_BACK' TO GO BACK         []")
        print("||||||||||||||||||||||||||||||||||||||")

        selected_input = input("\n\n[ _ Input ]: ")
        return selected_input

    def __File_Location_Selection_Menu(self):
        self.__clear_screen()

        print("|||||||||||||||||||||||||||||||||||||||||")
        print("[] ENTER THE FULL PATH OF THE LOCATION []")
        print("[] WHERE THE FILE WILL BE SAVED:       []")
        print("[]                                     []")
        print("[] ENTER '_BACK' TO GO BACK            []")
        print("|||||||||||||||||||||||||||||||||||||||||")

        selected_input = input("\n\n[ _ Input ]: ")
        return selected_input

    def __File_Binary_Data_Assembly_File_Name_Selection_Menu(self):
        self.__clear_screen()

        print("||||||||||||||||||||||||||||||||||")
        print("[] INSERT THE NAME OF THE FILE  []")
        print("[]                              []")
        print("[] ENTER '_BACK' TO GO BACK     []")
        print("||||||||||||||||||||||||||||||||||")

        selected_input = input("\n\n[ _ Input ]: ")
        return selected_input

    def __File_Binary_Data_Assembly_File_Type_Selection_Menu(self):
        self.__clear_screen()

        print("|||||||||||||||||||||||||||||||||||||||||||")
        print("[] INSERT THE NAME OF THE FILE EXTENSION []")
        print("[]  (e.g: '.txt', '.docx', '.xml' . . .) []")
        print("[]                                       []")
        print("[] ENTER '_BACK' TO GO BACK              []")
        print("|||||||||||||||||||||||||||||||||||||||||||")

        selected_input = input("\n\n[ _ Input ]: ")
        return selected_input

    def __Transcription_Error_Message_Linux(self):
        print("\n\n||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("[ ! ! ! ]      FILE TRANSCRIPTION FAILED     [ ! ! ! ]")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("[]                                                  []")
        print("[] THE REASON CAN BE CAUSED BY THE FACT THAT        []")
        print("[] THE PACKAGE 'ffmpeg' IS MISSING ( LINUX )        []")
        print("[] INSTALL PACKAGE -> 'sudo apt-get install ffmpeg' []")
        print("[]                                                  []")
        print("[]                                                  []")
        print("[]   - PRESS ANY KEY TO CLEAR                       []")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||")

        selected_input = input("\n\n[ _ Input ]: ")
        return selected_input

    def __Transcription_Error_Message_Windows(self):
        print("\n\n||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("[ ! ! ! ]      FILE TRANSCRIPTION FAILED     [ ! ! ! ]")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("[]                                                  []")
        print("[]   - PRESS ANY KEY TO CLEAR                       []")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||")

        selected_input = input("\n\n[ _ Input ]: ")
        return selected_input

    def __Pytube_Module_Warning_Message(self):
        print("\n\n[ |||||||||||||||||||||||||||||||||||||||||||||| ]")
        print("[ _ _ _ ] [ CHECKING IF PYTUBE YOUTUBE ] [ _ _ _ ]")
        print("[ _ _ _ ] [ VIDEO DOWNLOAD MODULE      ] [ _ _ _ ]")
        print("[ _ _ _ ] [ IS INSTALLED               ] [ _ _ _ ]")
        print("[ |||||||||||||||||||||||||||||||||||||||||||||| ]\n\n")

        print("\n\n[ ||||||||||||||||||||||||||||||||| ]")
        print("[ ! ! ! ] [ PLEASE DO NOT ] [ ! ! ! ]")
        print("[ ! ! ! ] [ CLOSE THE     ] [ ! ! ! ]")
        print("[ ! ! ! ] [ PROGRAM       ] [ ! ! ! ]")
        print("[ ||||||||||||||||||||||||||||||||| ]\n\n")

    def __Whisper_Module_Warning_Message(self):
        print("\n\n[ |||||||||||||||||||||||||||||||||||||||||||||| ]")
        print("[ _ _ _ ] [ CHECKING IF WHISPER SPEECH ] [ _ _ _ ]")
        print("[ _ _ _ ] [ RECOGNITION ENGINE IS      ] [ _ _ _ ]")
        print("[ _ _ _ ] [ INSTALLED                  ] [ _ _ _ ]")
        print("[ |||||||||||||||||||||||||||||||||||||||||||||| ]\n\n")

        print("\n\n[ ||||||||||||||||||||||||||||||||| ]")
        print("[ ! ! ! ] [ PLEASE DO NOT ] [ ! ! ! ]")
        print("[ ! ! ! ] [ CLOSE THE     ] [ ! ! ! ]")
        print("[ ! ! ! ] [ PROGRAM       ] [ ! ! ! ]")
        print("[ ||||||||||||||||||||||||||||||||| ]\n\n")

    def __Pytube_Module_Installed_Message(self):
        print("\n\n[ |||||||||||||||||||||||||||||||||||||||||||||| ]")
        print("[ _ _ _ ] [ PYTUBE YOUTUBE VIDEO           ] [ _ _ _ ]")
        print("[ _ _ _ ] [ DOWNLOAD MODULE                ] [ _ _ _ ]")
        print("[ _ _ _ ] [ IS INSTALLED                   ] [ _ _ _ ]")
        print("[ |||||||||||||||||||||||||||||||||||||||||||||||||| ]\n\n")


    def __Whisper_Module_Warning_Installed(self):
        print("\n\n[ |||||||||||||||||||||||||||||||||||||||||||||| ]")
        print("[ _ _ _ ] [ WHISPER SPEECH RECOGNITION ] [ _ _ _ ]")
        print("[ _ _ _ ] [ ENGINE IS INSTALLED        ] [ _ _ _ ]")
        print("[ |||||||||||||||||||||||||||||||||||||||||||||| ]\n\n")


    def __Numpy_Module_Update_Warning(self):
        print("\n\n[ |||||||||||||||||||||||||||||||||| ]")
        print("[ _ _ _ ] [ UPDATING NUMPY ] [ _ _ _ ]")
        print("[ |||||||||||||||||||||||||||||||||| ]\n\n")

        print("\n\n[ ||||||||||||||||||||||||||||||||| ]")
        print("[ ! ! ! ] [ PLEASE DO NOT ] [ ! ! ! ]")
        print("[ ! ! ! ] [ CLOSE THE     ] [ ! ! ! ]")
        print("[ ! ! ! ] [ PROGRAM       ] [ ! ! ! ]")
        print("[ ||||||||||||||||||||||||||||||||| ]\n\n")

    def __Numpy_Module_Update_Warning_Installed(self):
        print("\n\n[ ||||||||||||||||||||||||||||||||| ]")
        print("[ _ _ _ ] [ NUMPY UPDATED ] [ _ _ _ ]")
        print("[ ||||||||||||||||||||||||||||||||| ]\n\n")

    def __Details_Page(self):
        self.__clear_screen()

        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("[] MODEL NAME     REQUIRED VRAM/RAM SIZE     NUMBER OF PARAMETERS []")
        print("[]                                                                []")
        print("[]   'tiny'               ~ 1 GB                  39 MILLION      []")
        print("[]                                                                []")
        print("[]   'base'               ~ 1 GB                  74 MILLION      []")
        print("[]                                                                []")
        print("[]   'small'              ~ 2 GB                 244 MILLION      []")
        print("[]                                                                []")
        print("[]   'medium'             ~ 5 GB                 769 MILLION      []")
        print("[]                                                                []")
        print("[]   'large'              ~ 10 GB               1.55 BILLION      []")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("[]                                                                []")
        print("[] NUMBER OF PARAMETERS = THE NUMBER OF PARAMETERS TOOK INTO      []")
        print("[]                        CONSIDERATION WHEN SPEECH RECOGNITION   []")
        print("[]                        RECOGNITION IS DONE. BIGGER THE         []")
        print("[]                        NUMBER, BETTER THE ACCURACY             []")
        print("[]                                                                []")
        print("[]                                                                []")
        print("[] REQUIRED VRAM/RAM = THE AMOUNT OF RAM REQUIRED TO BE AVAILABLE []")
        print("[]                     IN ORDER FOR THE MODEL TO RUN              []")
        print("[]                                                                []")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("[]                                                                []")
        print("[] ENTER '_BACK' TO GO BACK                                       []")
        print("[]                                                                []")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

        selected_input = input("\n\n[ _ Input ]: ")
        return selected_input

    def __Settings_Menu(self):
        self.__clear_screen()

        print("||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("[] SELECT 'MODEL' TO SET THE DESIRED SPEECH MODEL []")
        print("[] SIZE OR 'PROCESSING' TO SELECT THE DESIRED     []")
        print("[] PROCESSING METHOD:                             []")
        print("[]                                                []")
        print("[] ENTER '_BACK' TO GO BACK                       []")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||")

        selected_input = input("\n\n[ _ Input ]: ")
        return selected_input

    def __Speech_Model_Selection_Sub_Menu(self):
        self.__clear_screen()

        print("||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("[] SELECT THE SPEECH RECOGNITION ENGINE           []")
        print("[] MODEL SIZE:                                    []")
        print("[] ( 'tiny', 'base', 'small', 'medium', 'large' ) []")
        print("[]                                                []")
        print("[] ENTER '_BACK' TO GO BACK                       []")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||")

        selected_input = input("\n\n[ _ Input ]: ")
        return selected_input

    def __Speech_Model_Processing_Unit_Selection(self):
        self.__clear_screen()

        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("[] INSERT 'CPU' TO PROCESS THE TRANSCRIPTION USING THE []")
        print("[] CPU, OR 'GC' TO PROCESS THE TRANSCRIPTION USING THE []")
        print("[] GRAPHICS CARD.                                      []")
        print("[]                                                     []")
        print("[] ENTER '_BACK' TO GO BACK                            []")
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

        selected_input = input("\n\n[ _ Input ]: ")
        return selected_input

    def __Transcription_In_Progress_Warning_Message(self):
        self.__clear_screen()

        print("|||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("[] [ ! ! ! ] TRANSCRIPTION IN PROGRESS [ ! ! ! ] []")
        print("[] [ ! ! ! ] DO NOT CLOSE THE PROGRAM  [ ! ! ! ] []")
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||")
