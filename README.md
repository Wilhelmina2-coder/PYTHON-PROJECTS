# AI VOICE ASSISTANT- sulwe

### Getting Started

**mina** is an assistive AI written from simple python libraries and has the following feature:

* Tell time and date
* Play videos from youtube
* Tell a joke
* Answer web fetched questions
* Customized text

### Installation
Using the terminal, install the following

- For speech recognition   

   [`pip install speech recognition`]()  


- To convert text to speech.

    [`pip install pyttsx3`]() 

- To play vidoes from the web eg youtube.

   [`pywhatkit`]()

-  To tell the date and time.

    [`datetime`]()

- To fetch infomation from wikipedia

    [`wikipedia']()

-  To tell random tech jokes

    [`pyjokes`]()

 2. ### Methods  And Functions

 `listener = sr.Recognizer()`

 This is to allow the program listen and understand spoken words.

 `engine = pyttsx3.init()`

This line of code allow  the prgram to give verbal output.

`voices = engine.getProperty('voices') `

This line of code fetches a list of voices that can be 
used by the program.

`engine.setProperty('voice', voices[1].id)`

This line of code is used to customize the voice. 

3.  This function is a support for the above method so the program can give a verbal output of the user command.
>
    def talk(text)
    engine.say(text)
    engine.runAndWait()
   
4.
 
> def take_command():

    defines a function named take_command with no arguments.

> try:

    starts a try-except block, which is used for error handling. It allows you to capture and handle any errors that might occur during the execution of the code within the try block.

> with sr.Microphone() as source:

    initiates the use of the microphone as the audio source for speech recognition. It opens the microphone in a way that ensures it is properly closed after use.

> print('Lets roll...')

    prints a message to indicate that the program is ready to listen for a command. This is just a user-friendly message.
    
> voice = listener.listen(source)

    captures audio input from the microphone and stores it in the voice variable using the listener object you defined earlier. This line effectively listens for spoken words.

> command = listener.recognize_google(voice)

     recognizes the spoken words in the captured audio using Google's speech recognition service. It converts the spoken words into text and stores the result in the command variable.

> command = command.lower()

    converts the recognized text command to lowercase to make it easier to process. This ensures that the program can handle commands regardless of whether they are spoken in uppercase or lowercase.

> if 'sulwe' in command:

    checks if the word "sulwe" is present in the recognized command. If it is found, it proceeds to the next line.

> command = command.replace('sulwe','')

    removes the word "sulwe" from the recognized command. This is done to clean up the command, removing any unwanted or triggering words.

> print(command)

    prints the cleaned-up command for debugging purposes. It shows the command after removing "sulwe."

>except:

    starts the exception-handling block. If any errors occurred within the try block, this block will handle them.


> pass

    This is used as a placeholder in the except block, indicating that no specific action is taken if an error occurs during the audio capture or speech recognition process.

> return command

    return command returns the recognized and cleaned-up command as a result of the function. The calling    code can then use this command to perform specific actions based on the spoken input.


> def run_sulwe()

    This line defines a function called run_sulwe. Inside this function, commands will be processed based on what the user says.
>command = take_command():

    This line calls the take_command function (which captures voice commands) and stores the recognized command in the command variable.
>print(command):

    This line prints the recognized command to the console for debugging purposes. It shows what the user said.

*The code then uses a series of if, elif (else if), and else statements to check the recognized command and perform specific actions based on the content of the command.* 

>
 - If the command contains "play," it assumes the user wants to play something, extracts the song name, and plays it on YouTube.

 - If the command contains "time," it retrieves the current time and speaks it.

 - If the command contains "who is," it looks up information about a person (the name provided after "who is") on Wikipedia and speaks a summary.

 - If the command is "papa," it expresses gratitude for tomorrow's lunch.

 - If the command is "good night," it delivers a comforting goodnight message.

 - If the command is "joke," it tells a random joke.

 - If none of the above conditions are met, it requests the 
 - user to repeat the command.
The while True: loop:

        This loop ensures that the run_mina function runs continuously, allowing the assistant to listen for and respond to commands indefinitely.




