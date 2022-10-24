import speech_recognition as sr
from datetime import date, datetime
import pyttsx3, time

robot_ear = sr.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ''
today = date.today().strftime('%B %d, %Y')
timenow = datetime.now().strftime('%H hours %M minutes')

while True:
    with sr.Microphone() as mic:
        print("Robot: I'm listening!")
        audio = robot_ear.listen(mic)

    try:
        you = robot_ear.recognize_google(audio)

    except:
        you = ''

    print(f"You: {you}")

    if 'bye'in you:
        robot_brain = 'Bye!'
        print(f'Robot: {robot_brain}')
        robot_mouth.runAndWait()
        break

    if you == '':
        robot_brain = "I can't hear you, please try again!"

    if 'time' in you:
        robot_brain = timenow
    elif 'today' in you:
        robot_brain = today

    print('Robot: ...!')
    time.sleep(2)
    print(f'Robot: {robot_brain}')
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()