import sys


from Main_Package import Audio_Transcription, File_Binary_Data_Manipulation, Graphical_User_Interface_Menus, \
    Os_Detection_And_Dependency_Installation, Trans_Cryptor

model_size = "base"
gpu_processing = False


def Details_Page_Sub_Menu(detected_operating_system, returned_dependency_download_result):
    gui = Graphical_User_Interface_Menus.Graphical_User_Interface_Menus_Collection_And_Related_Operations(
        "details page")
    selected_input = gui.GUI_Function_Operator()

    if selected_input == "_BACK":
        Transcription_Operation(detected_operating_system, returned_dependency_download_result, False)
    else:
        Details_Page_Sub_Menu(detected_operating_system, returned_dependency_download_result)


def Settings_Sub_Menu(detected_operating_system, returned_dependency_download_result):
    gui = Graphical_User_Interface_Menus.Graphical_User_Interface_Menus_Collection_And_Related_Operations(
        "settings menu")
    selected_option = gui.GUI_Function_Operator()

    if selected_option == "PROCESSING":
        Processing_Unit_Selection_Sub_Menu(detected_operating_system, returned_dependency_download_result)

    elif selected_option == "MODEL":
        Model_Selection_Sub_Menu(detected_operating_system, returned_dependency_download_result)

    elif selected_option == "_BACK":
        Transcription_Operation(detected_operating_system, returned_dependency_download_result, False)

    else:
        Settings_Sub_Menu(detected_operating_system, returned_dependency_download_result)


def Processing_Unit_Selection_Sub_Menu(detected_operating_system, returned_dependency_download_result):
    gui = Graphical_User_Interface_Menus.Graphical_User_Interface_Menus_Collection_And_Related_Operations(
        "speech model processing menu")
    selected_option = gui.GUI_Function_Operator()

    if selected_option == "CPU":
        Trans_Cryptor.gpu_processing = False
        Settings_Sub_Menu(detected_operating_system, returned_dependency_download_result)

    elif selected_option == "GC":
        Trans_Cryptor.gpu_processing = True
        Settings_Sub_Menu(detected_operating_system, returned_dependency_download_result)

    elif selected_option == "_BACK":
        Settings_Sub_Menu(detected_operating_system, returned_dependency_download_result)

    else:
        Processing_Unit_Selection_Sub_Menu(detected_operating_system, returned_dependency_download_result)


def Model_Selection_Sub_Menu(detected_operating_system, returned_dependency_download_result):
    gui = Graphical_User_Interface_Menus.Graphical_User_Interface_Menus_Collection_And_Related_Operations(
        "speech model menu")
    selected_model_size = gui.GUI_Function_Operator()

    if selected_model_size == "tiny":
        Trans_Cryptor.model_size = selected_model_size

    elif selected_model_size == "base":
        Trans_Cryptor.model_size = selected_model_size
        Settings_Sub_Menu(detected_operating_system, returned_dependency_download_result)

    elif selected_model_size == "small":
        Trans_Cryptor.model_size = selected_model_size
        Settings_Sub_Menu(detected_operating_system, returned_dependency_download_result)

    elif selected_model_size == "medium":
        Trans_Cryptor.model_size = selected_model_size
        Settings_Sub_Menu(detected_operating_system, returned_dependency_download_result)

    elif selected_model_size == "large":
        Trans_Cryptor.model_size = selected_model_size
        Settings_Sub_Menu(detected_operating_system, returned_dependency_download_result)

    elif selected_model_size == "_BACK":
        Settings_Sub_Menu(detected_operating_system, returned_dependency_download_result)

    else:
        Model_Selection_Sub_Menu(detected_operating_system, returned_dependency_download_result)


def Transcription_Operation(detected_operating_system, returned_dependency_download_result, error_occurred):
    try:
        gui = Graphical_User_Interface_Menus.Graphical_User_Interface_Menus_Collection_And_Related_Operations(
            "transcription sub menu")
        selected_input = gui.GUI_Function_Operator()

        if error_occurred is True:

            if detected_operating_system == "Windows":
                gui = Graphical_User_Interface_Menus.Graphical_User_Interface_Menus_Collection_And_Related_Operations(
                    "transcription error windows")
                selected_input = gui.GUI_Function_Operator()

                if selected_input is not None:
                    Transcription_Operation(detected_operating_system, returned_dependency_download_result, False)

            else:
                gui = Graphical_User_Interface_Menus.Graphical_User_Interface_Menus_Collection_And_Related_Operations(
                    "transcription error linux")
                selected_input = gui.GUI_Function_Operator()

                if selected_input is not None:
                    Transcription_Operation(detected_operating_system, returned_dependency_download_result, False)

        else:
            if selected_input == "Y":
                gui = Graphical_User_Interface_Menus.Graphical_User_Interface_Menus_Collection_And_Related_Operations(
                    "youtube transcription sub menu")
                youtube_link = gui.GUI_Function_Operator()

                if youtube_link == "_BACK":
                    Transcription_Operation(detected_operating_system, returned_dependency_download_result, False)

                youtube_transcription_result = Audio_Transcription.Audio_Transcription_Operator(
                    "youtube audio transcription", youtube_link, Trans_Cryptor.model_size, Trans_Cryptor.gpu_processing)

                if youtube_transcription_result is not None:
                    gui = Graphical_User_Interface_Menus.Graphical_User_Interface_Menus_Collection_And_Related_Operations(
                        "file name selection sub menu")
                    selected_input_file_name = gui.GUI_Function_Operator()

                    if selected_input_file_name == "_BACK":
                        Transcription_Operation(detected_operating_system, returned_dependency_download_result, False)

                    gui = Graphical_User_Interface_Menus.Graphical_User_Interface_Menus_Collection_And_Related_Operations(
                        "file extension selection sub menu")
                    selected_input_file_extension = gui.GUI_Function_Operator()
                    complete_file_name = selected_input_file_name + selected_input_file_extension

                    if selected_input_file_name == "_BACK":
                        Transcription_Operation(detected_operating_system, returned_dependency_download_result, False)

                    binary_file_assembly_operation = File_Binary_Data_Manipulation.Binary_File_Assembly_Operation(
                        youtube_transcription_result, complete_file_name)
                    binary_file_assembly_operation.Binary_File_Assembly_Initiator()

                    Transcription_Operation(detected_operating_system, returned_dependency_download_result, False)

                else:
                    Transcription_Operation(detected_operating_system, returned_dependency_download_result, True)

            elif selected_input == "A":
                gui = Graphical_User_Interface_Menus.Graphical_User_Interface_Menus_Collection_And_Related_Operations(
                    "audio file transcription sub menu")
                audio_file_path = gui.GUI_Function_Operator()

                if audio_file_path == "_BACK":
                    Transcription_Operation(detected_operating_system, returned_dependency_download_result, False)

                audio_file_transcription_result = Audio_Transcription.Audio_Transcription_Operator(
                    "audio file transcription", audio_file_path, Trans_Cryptor.model_size, Trans_Cryptor.gpu_processing)

                if audio_file_transcription_result is not None:
                    gui = Graphical_User_Interface_Menus.Graphical_User_Interface_Menus_Collection_And_Related_Operations(
                        "file name selection sub menu")
                    selected_input_file_name = gui.GUI_Function_Operator()

                    if selected_input_file_name == "_BACK":
                        Transcription_Operation(detected_operating_system, returned_dependency_download_result, False)

                    gui = Graphical_User_Interface_Menus.Graphical_User_Interface_Menus_Collection_And_Related_Operations(
                        "file extension selection sub menu")
                    selected_input_file_extension = gui.GUI_Function_Operator()
                    complete_file_name = selected_input_file_name + selected_input_file_extension

                    if selected_input_file_name == "_BACK":
                        Transcription_Operation(detected_operating_system, returned_dependency_download_result, False)

                    binary_file_assembly_operation = File_Binary_Data_Manipulation.Binary_File_Assembly_Operation(
                        audio_file_transcription_result, complete_file_name)
                    binary_file_assembly_operation.Binary_File_Assembly_Initiator()

                    Transcription_Operation(detected_operating_system, returned_dependency_download_result, False)

                else:
                    Transcription_Operation(detected_operating_system, returned_dependency_download_result, True)

            elif selected_input == "S":
                Settings_Sub_Menu(detected_operating_system, returned_dependency_download_result)

            elif selected_input == "D":
                Details_Page_Sub_Menu(detected_operating_system, returned_dependency_download_result)

            elif selected_input == "M":
                main_control_menu(detected_operating_system, returned_dependency_download_result)

            else:
                Transcription_Operation(detected_operating_system, returned_dependency_download_result, False)




    except KeyboardInterrupt:
        sys.exit(0)


def main_control_menu(detected_operating_system, returned_dependency_download_result):
    try:

        if returned_dependency_download_result is True:
            gui = Graphical_User_Interface_Menus.Graphical_User_Interface_Menus_Collection_And_Related_Operations(
                "main menu screen")
            selected_input = gui.GUI_Function_Operator()

            if selected_input == "T":
                Transcription_Operation(detected_operating_system, returned_dependency_download_result, False)

            elif selected_input == "E":
                sys.exit(0)

            else:
                main_control_menu(detected_operating_system, returned_dependency_download_result)

        else:
            sys.exit(0)


    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == "__main__":
    try:
        operating_system = Os_Detection_And_Dependency_Installation.main_operational_controller("os detection", None)
        dependency_download_result = Os_Detection_And_Dependency_Installation.main_operational_controller(
            "dependency download", operating_system)
        main_control_menu(operating_system, dependency_download_result)
    except KeyboardInterrupt:
        sys.exit(0)
