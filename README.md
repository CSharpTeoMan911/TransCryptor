# TransCryptor
<br>
<br>

## TransCryptor, an open-source speech-to-text transcription application.<br>

<br>
<br>

## About
____________

***TransCryptor*** is build in Python using the OpenAI's speech-to-text engine named **Whisper**. TransCryptor is open-source and free to use.
***TransCryptor*** can be used in multiple domanis and/or multiple purposes, such as data science, software engineering, machine learning,  
movie subtitle generation, or the transcription of pre-recorded meetings at work or school into text. The extracted information can 
be then saved in any file format, desired by the user. Long story short, what was previously stated means that ***TransCryptor***
can be used for data-mining, the generation of captions for movies and videos, and the transcription of recordings and other various
audio files into text (recordings from meetings, voicemails, etc.)


<br>
<br>

## Requirements
___________________________

[-] Python

<br>

To install Python go to this link: https://www.python.org/downloads/

<br>

After the installation, open your terminal and type:  **[** *python --version* **]**  **OR**  **[** *python3 --version* **]**. <br>
If the version of Python is not displayed, then you must add Python to the <br>
'Environment Variables'.



<br>
<br>

[-] PIP

To install PIP, open your terminal and type:  **[** *python -m pip install pip* **]**  **OR**  **[** *python3 -m pip install pip* **]**. <br>

<br>

After the installation, open your terminal and type:  **[** *pip --version* **]** . <br>
If the version of PIP is not displayed, then you must add PIP to the <br>
'Environment Variables'.


<br>
<br>

## Installation

In order to install *TransCryptor* open Command Prompt or PowerShell on Windows, or any other terminal
on Linux or Mac OS, and type:

<br>
<br>

#### **[ pip install git+https://github.com/CSharpTeoMan911/TransCryptor ]**

<br>
<br>
<br>
<br>

## Usage
__________________

In order to use **TransCryptor**, you must select between YouTube video transcription and audio file transcription.
These options are diplayed in the transcription menu as '**Y**' for YouTube transcription and '**A**' for audio
file transcription, respectively. 

<br>
<br>

### YouTube transcription
___________________________

If '**Y**' for YouTube transcription is selected, a menu prompting the user to enter the link of the video will appear.
Insert the link of the desired YouTube video you want to transcribe. After the transcription completed, a menu prompting
the user to insert the path where the file must be saved will appear. Insert the path to the directory where the file 
should be saved. (e.g. '**C:\Users\Your Username\Desktop**'). After this, a menu prompting the user to enter the desired
file name of the transcrition will appear. Insert the your desired file name. After this, a menu prompting the user to
enter the desired file extension will appear. Enter the file extension of the file format you want the transcription to
be saved. <br> (e.g. **PDF -> '.pdf', DOCX -> '.docx', TEXT -> '.txt', etc...**)


<br>
<br>

### Audio file transcription
_____________________________

If '**A**' for audio file transcription is selected, a menu prompting the user to enter the the full path to the file will appear.
Insert the path to the desired file, including the file itself (e.g. **'C:\Users\Your Username\Desktop\FileToBeTranscribed.mp3'**). 
After the transcription completed, a menu prompting the user to insert the path where the file must be saved will appear.
Insert the path to the directory where the file should be saved. (e.g. '**C:\Users\Your Username\Desktop**'). 
After this, a menu prompting the user to enter the desired file name of the transcrition will appear.
Insert the your desired file name. After this, a menu prompting the user to enter the desired file
extension will appear. Enter the file extension of the file format you want the transcription to
be saved. (e.g. **PDF -> '.pdf', DOCX -> '.docx', TEXT -> '.txt', etc...**)


<br>
<br>
<br>
<br>


## Settings
______________

If '**S**' for application settings is selected, a menu prompting the user to enter either '**MODEL**' OR '**PROCESSING**' will appear.

<br>
<br>

### Model settings
___________________

The default speech recognition model that the application will use each time is opened is the '**base**' model. Each model has a number of parameters
that it will take into consideration when speech recognition is performed, such number of words that it can predict, number of words that it
can recognise, background noise, etc. Bigger the number of parameters took into consideration by the speech recognition engine, greater the
accuracy. Into the speech recognition model selection menu, the user is prompted to enter one of the models displayed in the menu. The number
of parameters that each model takes into consideration increases from the left-most displayed model to the right-most displayed model.

<br>
<br>

### Processing settings
_________________________

The default processing method that the application uses each time is opened is the ***CPU*** processing method. Into the processing method selection menu,
the user is prompted to choose between '***CPU***' for cpu processing and '***GC***' graphics card processing. Because speech recognition engines are built
using machine learning, they use decision making neurons in order to decide what words to recognise. Decision making neurons use weighing, and weighing is
a value set by a certain parameter within a decision making neuron upon which the decision is took. If the result is lower than the weighing value, than 
the result is discarded. These processes use vectors and matrix manipulation (array manipulation), and a graphics card is specialised in these types of 
calculations. In order to have a better result, the graphics card processing method is recommended. ***CPU*** processing is using RAM and ***Graphics card*** processing is using VRAM, respectively.


<br>
<br>

### Model requirements
__________________________

![Opera Snapshot_2022-11-05_213814_github com](https://user-images.githubusercontent.com/87245086/200142276-ed31d031-332f-4977-87c8-64b4c7647550.png)

<br>

The amount of RAM/VRAM reuired by each model reflects not only the size of the RAM/VRAM on the device but also the amount of RAM/VRAM required
to be free at the moment in which the transcription takes place. 

<br>
<br>
<br>
<br>

## Links
_____________

### Benefits of GPU processing in A.I. 

<br>

https://www.run.ai/guides/gpu-deep-learning/best-gpu-for-deep-learning#:~:text=This%20is%20because%20GPUs%20enable,faster%20than%20non-specialized%20hardware.

<br>
<br>

### OpenAI Whisper Speech Recognition engine

<br>

https://openai.com/blog/whisper/

<br>
<br>

### OpenAI Whisper Speech Recognition engine GitHub repository

<br>

https://github.com/openai/whisper








