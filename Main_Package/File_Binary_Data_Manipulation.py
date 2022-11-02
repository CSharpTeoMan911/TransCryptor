import sys


class Binary_File_Assembly_Operation:

    transcribed_data = None
    file_name = None

    def __init__(self, init_transcribed_data, init_file_name):
        self.transcribed_data = init_transcribed_data
        self.file_name = init_file_name


    def Binary_File_Assembly_Initiator(self):
        self.__Binary_File_Assembly()


    def __Binary_File_Assembly(self):

        try:
            try:
                with open(self.file_name, "wb") as wb:
                    transcribed_data_binary_data = str(self.transcribed_data).encode("utf-8")
                    wb.write(transcribed_data_binary_data)
            except FileNotFoundError:
                print("! ! FILE NOT FOUND ! !")
        except KeyboardInterrupt:
            sys.exit(0)

