import platform
import subprocess
import sys
import os as operating_system

from Main_Package import Graphical_User_Interface_Menus


class Os_Detection_And_Dependencies_Installation_Processes:
    detected_operating_system = None

    def __init__(self, init_detected_operating_system):
        self.detected_operating_system = init_detected_operating_system

    def Whisper_Speech_To_Text_Package_Module_Dependency(self):

        gui = Graphical_User_Interface_Menus.Graphical_User_Interface_Menus_Collection_And_Related_Operations("whisper module warning")
        gui.GUI_Function_Operator()

        try:
            if self.detected_operating_system == "Windows":

                operating_system.system("python -m pip install git+https://github.com/openai/whisper.git")

                return True


            elif self.detected_operating_system == "Linux" or self.detected_operating_system == "Linux2" or "Darwin":

                input_bytes = "Y".encode("utf-8")

                command_output_linux = subprocess.run("python -m pip install git+https://github.com/openai/whisper.git",
                                                      stdout=subprocess.PIPE, input=input_bytes, stderr=subprocess.PIPE,
                                                      shell=True)

                command_output_linux_output = None
                command_output_linux_error = None

                if command_output_linux.stdout is not None:
                    command_output_linux_output = command_output_linux.stdout.decode("utf-8")

                if command_output_linux.stderr is not None:
                    command_output_linux_error = command_output_linux.stderr.decode("utf-8")

                print(command_output_linux_output)

                if command_output_linux_error is None:
                    print("\n\n" + command_output_linux_output + "\n\n")
                    gui = Graphical_User_Interface_Menus.Graphical_User_Interface_Menus_Collection_And_Related_Operations("whisper module installed")
                    gui.GUI_Function_Operator()
                    return True


                else:
                    if "python: not found" in command_output_linux_error or "'python' not found" in command_output_linux_error:

                        command_output_linux = subprocess.run(
                            "python3 -m pip install git+https://github.com/openai/whisper.git",
                            stdout=subprocess.PIPE, input=input_bytes, shell=True)

                        command_output_linux_output = None
                        command_output_linux_error = None

                        if command_output_linux.stdout is not None:
                            command_output_linux_output = command_output_linux.stdout.decode("utf-8")

                        if command_output_linux.stderr is not None:
                            command_output_linux_error = command_output_linux.stderr.decode("utf-8")

                        if command_output_linux_error is None:
                            print("\n\n" + command_output_linux_output + "\n\n")
                            gui = Graphical_User_Interface_Menus.Graphical_User_Interface_Menus_Collection_And_Related_Operations(
                                "whisper module installed")
                            gui.GUI_Function_Operator()
                            return True
                        else:
                            if "No module named pip" in command_output_linux_error:
                                print(
                                    "[ ! ! ! ] [ PIP not installed ] [ ! ! ! ]\n=> Run command [ sudo apt install sudo apt install python3-pip ]")
                                return False
                            else:
                                print("\n\n" + command_output_linux_error + "\n\n")
                                return False


                    elif "No module named pip" in command_output_linux_error:
                        print(
                            "[ ! ! ! ] [ PIP not installed ] [ ! ! ! ]\n=> Run command [ sudo apt install sudo apt install python-pip ]")
                        return False
                    else:
                        print("\n\n" + command_output_linux_error + "\n\n")
                        return False

        except KeyboardInterrupt:
            sys.exit(0)

    def PyTube_YouTube_Video_Download_Dependency(self):

        gui = Graphical_User_Interface_Menus.Graphical_User_Interface_Menus_Collection_And_Related_Operations("pytube module warning")
        gui.GUI_Function_Operator()

        try:
            if self.detected_operating_system == "Windows":

                operating_system.system("python -m pip install pytube")

                return True

            elif self.detected_operating_system == "Linux" or self.detected_operating_system == "Linux2" or "Darwin":

                input_bytes = "Y".encode("utf-8")

                command_output_linux = subprocess.run("python -m pip install git+https://github.com/openai/whisper.git",
                                                      stdout=subprocess.PIPE, input=input_bytes, stderr=subprocess.PIPE,
                                                      shell=True)

                command_output_linux_output = None
                command_output_linux_error = None

                if command_output_linux.stdout is not None:
                    command_output_linux_output = command_output_linux.stdout.decode("utf-8")

                if command_output_linux.stderr is not None:
                    command_output_linux_error = command_output_linux.stderr.decode("utf-8")

                if command_output_linux_error is None:
                    print("\n\n" + command_output_linux_output + "\n\n")
                    print("\n\n[ |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| ]")
                    print("[ _ _ _ ] [ CHECKING IF PYTUBE YOUTUBE VIDEO DOWNLOAD MODULE IS INSTALLED  ] [ _ _ _ ]")
                    print("[ |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| ]\n\n")

                    return True

                else:

                    if "python: not found" in command_output_linux_error or "'python' not found" in command_output_linux_error:

                        command_output_linux = subprocess.run("python3 -m pip install pytube", stdout=subprocess.PIPE,
                                                              input=input_bytes, shell=True)

                        command_output_linux_output = None
                        command_output_linux_error = None

                        if command_output_linux.stdout is not None:
                            command_output_linux_output = command_output_linux.stdout.decode("utf-8")

                        if command_output_linux.stderr is not None:
                            command_output_linux_error = command_output_linux.stderr.decode("utf-8")

                        if command_output_linux_error is None:
                            gui = Graphical_User_Interface_Menus.Graphical_User_Interface_Menus_Collection_And_Related_Operations(
                                "pytube module installed")
                            gui.GUI_Function_Operator()
                            return True
                        else:
                            if "No module named pip" in command_output_linux_error:
                                print(
                                    "[ ! ! ! ] [ PIP not installed ] [ ! ! ! ]\n=> Run command [ sudo apt install sudo apt install python3-pip ]")
                                return False
                            else:
                                print("\n\n" + command_output_linux_error + "\n\n")
                                return False



                    elif "No module named pip" in command_output_linux_error:
                        print(
                            "[ ! ! ! ] [ PIP not installed ] [ ! ! ! ]\n=> Run command [ sudo apt install sudo apt install python-pip ]")
                        return False
                    else:
                        print("\n\n" + command_output_linux_error + "\n\n")
                        return False


        except KeyboardInterrupt:
            sys.exit(0)


    def Dependencies_Update(self):
        try:
            gui = Graphical_User_Interface_Menus.Graphical_User_Interface_Menus_Collection_And_Related_Operations(
                "numpy module warning")
            gui.GUI_Function_Operator()

            if self.detected_operating_system == "Windows":
                operating_system.system("python -m pip install numpy --upgrade")
                return True

            else:

                input_bytes = "Y".encode("utf-8")

                command_output_linux = subprocess.run("python -m pip install numpy --upgrade", stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)

                command_output_linux_output = None
                command_output_linux_error = None

                if command_output_linux.stdout is not None:
                    command_output_linux_output = command_output_linux.stdout.decode("utf-8")

                if command_output_linux.stderr is not None:
                    command_output_linux_error = command_output_linux.stderr.decode("utf-8")


                if command_output_linux_error is None:
                    return True
                else:
                    if "python: not found" in command_output_linux_error or "'python' not found" in command_output_linux_error:

                        command_output_linux = subprocess.run("python3 -m pip install numpy --upgrade", stdout=subprocess.PIPE,
                                                              input=input_bytes, shell=True)

                        command_output_linux_output = None
                        command_output_linux_error = None

                        if command_output_linux.stdout is not None:
                            command_output_linux_output = command_output_linux.stdout.decode("utf-8")

                        if command_output_linux.stderr is not None:
                            command_output_linux_error = command_output_linux.stderr.decode("utf-8")

                        if command_output_linux_error is None:
                            print("\n\n" + command_output_linux_output + "\n\n")
                            gui = Graphical_User_Interface_Menus.Graphical_User_Interface_Menus_Collection_And_Related_Operations(
                                "numpy module updated")
                            gui.GUI_Function_Operator()
                            return True
                        else:
                            if "No module named pip" in command_output_linux_error:
                                print(
                                    "[ ! ! ! ] [ PIP not installed ] [ ! ! ! ]\n=> Run command [ sudo apt install sudo apt install python3-pip ]")
                                return False
                            else:
                                print("\n\n" + command_output_linux_error + "\n\n")
                                return False

                    elif "No module named pip" in command_output_linux_error:
                        print(
                            "[ ! ! ! ] [ PIP not installed ] [ ! ! ! ]\n=> Run command [ sudo apt install sudo apt install python-pip ]")
                        return False

                    else:
                        print("\n\n" + command_output_linux_error + "\n\n")
                        return False


        except KeyboardInterrupt:
            pass


class Os_Detection_And_Dependencies_Installation_Handler:
    operation = None
    optional_parameter = None

    def __init__(self, init_operation, init_optional_parameter):
        self.operation = init_operation
        self.optional_parameter = init_optional_parameter

    def Operation_Operator(self):
        if self.operation == "os detection":
            os = self.__Os_Detection()
            return os

        else:
            dependency_download_result = self.__Dependencies_Installation()
            return dependency_download_result

    def __Dependencies_Installation(self):
        try:
            whisper_dependency_download = Os_Detection_And_Dependencies_Installation_Processes(self.optional_parameter)
            whisper_dependency_download_result = whisper_dependency_download.Whisper_Speech_To_Text_Package_Module_Dependency()

            pytube_dependency_download = Os_Detection_And_Dependencies_Installation_Processes(self.optional_parameter)
            pytube_dependency_download_result = pytube_dependency_download.PyTube_YouTube_Video_Download_Dependency()

            numpy_dependency_update = Os_Detection_And_Dependencies_Installation_Processes(self.optional_parameter)
            numpy_dependency_update_result = numpy_dependency_update.Dependencies_Update()

            if whisper_dependency_download_result is True and pytube_dependency_download_result is True and numpy_dependency_update_result is True:
                return True
            else:
                return False

        except KeyboardInterrupt:
            sys.exit(0)

    def __Os_Detection(self):
        try:
            detected_os = platform.system()
            return detected_os
        except KeyboardInterrupt:
            sys.exit(0)


def main_operational_controller(operation, optional_parameter):

    try:
        if operation == "os detection":
            os_detection = Os_Detection_And_Dependencies_Installation_Handler(operation, optional_parameter)
            os = os_detection.Operation_Operator()
            return os

        else:
            dependency_download = Os_Detection_And_Dependencies_Installation_Handler(operation, optional_parameter)
            dependency_download_result = dependency_download.Operation_Operator()
            return dependency_download_result

    except KeyboardInterrupt:
        sys.exit(0)
