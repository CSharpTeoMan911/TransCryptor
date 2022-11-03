import sys
import os

import pytube.exceptions

from Main_Package import Graphical_User_Interface_Menus


class Audio_File_Transcription_Operation:
    model_size = None
    file_path = None
    gpu_processing = False
    operation = ""

    def __init__(self, init_model_size, init_file_path, init_gpu_processing, init_operation):
        self.model_size = init_model_size
        self.file_path = init_file_path
        self.gpu_processing = init_gpu_processing
        self.operation = init_operation

    def Audio_File_Transcription_Initiator(self):
        return self.__Audio_File_Transcription()

    def __Audio_File_Transcription(self):
        try:

            try:

                try:

                    import whisper

                    selected_model_size = None

                    gui = Graphical_User_Interface_Menus.Graphical_User_Interface_Menus_Collection_And_Related_Operations("transcription warning")
                    gui.GUI_Function_Operator()


                    if self.model_size == "tiny":
                        selected_model_size = self.model_size

                    elif self.model_size == "base":
                        selected_model_size = self.model_size

                    elif self.model_size == "small":
                        selected_model_size = self.model_size

                    elif self.model_size == "medium":
                        selected_model_size = self.model_size

                    elif self.model_size == "large":
                        selected_model_size = self.model_size

                    else:
                        return None

                    language_model = whisper.load_model(selected_model_size)


                    if self.file_path is not None:
                        transcription_result = language_model.transcribe(self.file_path, fp16=self.gpu_processing)

                        if self.operation == "youtube audio transcription":
                            os.remove(self.file_path)

                        return transcription_result["text"]

                    else:

                        if self.operation == "youtube audio transcription":
                            os.remove(self.file_path)

                        return None

                except:
                    return None

            except KeyboardInterrupt:
                sys.exit(0)

        except ModuleNotFoundError:
            return None


class YouTube_Audio_File_Binary_Extraction_Operation:
    youtube_link = None
    model_size = None
    gpu_processing = False
    operation = ""

    gui = Graphical_User_Interface_Menus.Graphical_User_Interface_Menus_Collection_And_Related_Operations(
        "transcription warning")
    gui.GUI_Function_Operator()

    def __init__(self, init_youtube_link, init_model_size, init_gpu_processing, init_operation):
        self.youtube_link = init_youtube_link
        self.model_size = init_model_size
        self.gpu_processing = init_gpu_processing
        self.operation = init_operation

    def YouTube_Audio_File_Binary_Extraction_Initiator(self):
        return self.__YouTube_Audio_File_Binary_Extraction()

    def __YouTube_Audio_File_Binary_Extraction(self):
        try:
            try:
                from pytube import YouTube, exceptions
                try:
                    try:
                        try:
                            try:
                                try:
                                    try:
                                        try:
                                            try:
                                                try:
                                                    try:
                                                        try:
                                                            try:
                                                                youtube_object = YouTube(self.youtube_link)

                                                                video_audio = youtube_object.streams.filter(
                                                                    only_audio=True).first()

                                                                path = video_audio.download(output_path=".")

                                                                audio_file_transcription = Audio_File_Transcription_Operation(
                                                                    self.model_size, path,
                                                                    self.gpu_processing, self.operation)
                                                                audio_file_transcription_result = audio_file_transcription.Audio_File_Transcription_Initiator()

                                                                return audio_file_transcription_result
                                                            except ValueError:
                                                                return None
                                                        except exceptions.AgeRestrictedError:
                                                            return None
                                                    except exceptions.HTMLParseError:
                                                        return None
                                                except exceptions.MaxRetriesExceeded:
                                                    return None
                                            except exceptions.MembersOnly:
                                                return None
                                        except exceptions.Pattern:
                                            return None
                                    except exceptions.RecordingUnavailable:
                                        return None
                                except exceptions.PytubeError:
                                    return None
                            except exceptions.LiveStreamError:
                                return None
                        except exceptions.VideoPrivate:
                            return None
                    except exceptions.ExtractError:
                        return None
                except exceptions.RegexMatchError:
                    return None
            except ModuleNotFoundError:
                return None

        except KeyboardInterrupt:
            sys.exit(0)


def Audio_Transcription_Operator(operation, youtube_link_or_file_path, model_size, gpu_processing):
    try:
        if operation == "youtube audio transcription":
            youtube_file_extraction = YouTube_Audio_File_Binary_Extraction_Operation(youtube_link_or_file_path,
                                                                                     model_size, gpu_processing,
                                                                                     operation)
            youtube_file_extraction_result = youtube_file_extraction.YouTube_Audio_File_Binary_Extraction_Initiator()
            return youtube_file_extraction_result

        else:
            audio_file_extraction = Audio_File_Transcription_Operation(model_size, youtube_link_or_file_path,
                                                                       gpu_processing, operation)
            audio_file_extraction_result = audio_file_extraction.Audio_File_Transcription_Initiator()
            return audio_file_extraction_result

    except KeyboardInterrupt:
        sys.exit(0)
