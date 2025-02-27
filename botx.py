#Importing Modules
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import pyttsx3
#import pywhatkit


engine = pyttsx3.init()
engine.setProperty('rate', 150)


def intro():
    #Intro sound for Bot X
    engine.say('Welcome to the Bot X')
    #engine.runAndWait()

    #Bot Logo start Window 
    def close_window():
        root.destroy()

    root = tk.Tk()
    root.title("Bot X")
    root.geometry("400x400")

    # Load the background image
    background_image_path = "D:\\All projects\\BotX\\logo.jpg"
    background_image = Image.open(background_image_path)
    background_photo = ImageTk.PhotoImage(background_image)

    # Create a canvas to place the background image
    canvas = tk.Canvas(root, width=400, height=300)
    canvas.pack()
    canvas.create_image(0, 0, image=background_photo, anchor=tk.NW)

    click_button = tk.Button(root, text="Start", command=close_window)
    click_button.pack()

    root.mainloop()

def info():
    #print('This a Multi Functional Python Bot which is made to automate and make tasks easier for users')
    engine.say('This a Multi Functional Python Bot which is made to automate and make tasks easier for users')
    engine.runAndWait()

    #print('These are the functions of Bot X listed below')
    engine.say('These are the functions of Bot X listed below')
    engine.runAndWait()

    engine.say('click which function you want to use')
    engine.runAndWait()

def functions():

    import tkinter as tk

    def button_clicked(serial_number, option):

        if option == "Games":

            engine.say('You have selected Games')
            engine.runAndWait()
            print('You have selected Games')
            print('''
            1.Rock,Paper,Scissors
            2.Hangman
            ''')
            
            engine.say('Select one of the games from the list')
            engine.runAndWait()

            input2 = int(input('Select any one game in the list : ', ))

            if input2 == 1:
                
                import random
                import time
                print("Welcome to ROCK PAPER SCISSOR")
                print("Lets Start the game")
                time.sleep(1)
                User_Choice=int(input("Enter your Choice:\n 0.Rock \n 1.Paper \n 2.Scissor \n"))
                print("User's Choice:",User_Choice)
                time.sleep(2)
                if (User_Choice>=3 or User_Choice<0):
                    print("You lost the Game")

                    inputx = input('You want to go to main menu or Exit, enter y or n: ', )
                    if inputx == 'y':
                        functions()
                    else:
                        exit()
                    
                else:
                    Computer_Choice=random.randint(0,2)
                    print("Computer's Choice:",Computer_Choice)
                    if (User_Choice==Computer_Choice):
                        print("It's a Draw")

                        
                        inputx = input('You want to go to main menu or Exit, enter y or n: ', )

                        if inputx == 'y':
                            functions()
                        else:
                            exit()
                        
                    elif (User_Choice==2 and Computer_Choice==0):
                        print("You Lost")
                        

                        inputx = input('You want to go to main menu or Exit, enter y or n: ', )
                        
                        if inputx == 'y':
                            functions()
                        else:
                            exit()
                        
                    elif (Computer_Choice==2 and User_Choice==0):
                        print("You Win")


                        inputx = input('You want to go to main menu or Exit, enter y or n: ', )
                        
                        if inputx == 'y':
                            functions()
                        else:
                            exit()
                        
                    elif (User_Choice>Computer_Choice):
                        print("You Won")


                        inputx = input('You want to go to main menu or Exit, enter y or n: ', )
                        
                        if inputx == 'y':
                            functions()
                        else:
                            exit()
                        
                    elif (Computer_Choice>User_Choice):
                        print("You Lost")


                        inputx = input('You want to go to main menu or Exit, enter y or n: ', )
                        if inputx == 'y':
                            functions()
                        else:
                            exit()

            if input2 == 2:
                import random
                import time
                print("Welcome to HANGMAN Game")
                time.sleep(1)
                print("Instructions to play the Game:")
                time.sleep(2)

                print('''1.Player One Picks a Secret word and Draws a each line for each letter(Here line represents Underscore(_).)
                2.Player Two tries to guess the word one letter at a time.
                3. If Player One guesses a letter correctly, Player Two replaces the corresponding underscore with the correct letter. 
                In this version of the game, if a letter appears twice in a word, you have to guess it twice.
                4. Player One guesses incorrectly, Player two draws a body part of a hanged stick figure (starting with the head).
                5. If Player One completes the word before the drawing of the total hangman , they win. If not, they lose. ''')
                time.sleep(4)

                Player_1=input("Enter Player_1 name:")
                print("Player_2 is a Computer")
                print("All the best",Player_1,"Let's start the Game")
                print("The topic is Places of india")
                time.sleep(2)

                def hangman():
                    places = ['delhi','mumbai','kolkata','chennai','bengaluru','hyderabad','jaipur','agra','varanasi','goa','kochi',
                              'udaipur''jaisalmer','shimla','manali','rishikesh','amritsar','darjeeling','ooty','pondicherry','hampi',
                              "andhrapradesh","arunachalpradesh","assam","bihar","chhattisgarh", "gujarat", "haryana","himachalpradesh",
                              "jammuandkashmir", "jharkhand","karnataka","kerala","madhyapradesh","maharashtra","manipur", "meghalaya",
                              "mizoram", "nagaland","odisha","punjab", "rajasthan", "sikkim", "tamil nadu", "telangana", "tripura", 
                              "uttarpradesh", "uttarakhand","west bengal"]
                    word = random.choice(places)
                    guessmade = ''
                    turns = 10
                    valid_entry = set('abcdefghijklmnopqrstuvwxyz')
                    
                    while (len(word)>0):
                        main_word=''
                        
                        for letter in word:
                            if letter in guessmade:
                                main_word=main_word+letter
                            else:
                                main_word=main_word+'_ '
                                
                        if (main_word==word):
                            print(main_word)
                            print("You won")
                            break
                            
                        print("Guess the letter",main_word)
                        guess = input()
                        
                        if guess in valid_entry:
                            guessmade = guessmade+guess
                        else:
                            print("Please enter valid entry")
                            
                        if guess not in word:
                            turns = turns-1
                            if turns==9:
                                print("9 Turns left")
                                print("-------------")
                            elif turns==8:
                                print("8 Turns left")
                                print("-------------")
                                print('     o     ')
                            elif turns==7:
                                print("7 Turns left")
                                print("-------------")
                                print('     o     ')
                                print('     |     ')
                            elif turns==6:
                                print("6 Turns left")
                                print("-------------")
                                print('     o     ')
                                print('     |     ')
                                print('    /      ')
                            elif turns==5:
                                print("5 Turns left")
                                print("-------------")
                                print('     o     ')
                                print('     |     ')
                                print('    / \    ')
                            elif turns==4:
                                print("4 Turns left")
                                print("-------------")
                                print('    \o     ')
                                print('     |     ')
                                print('    / \    ')
                            elif turns==3:
                                print("3 Turns left")
                                print("-------------")
                                print('    \o/    ')
                                print('     |     ')
                                print('    / \    ')
                            elif turns==2:
                                print("2 Turns left")
                                print("-------------")
                                print('    \o/ |   ')
                                print('     |     ')
                                print('    / \    ')
                            elif turns==1:
                                print("1 Turn left")
                                print("-------------")
                                print('    \o/_|  ')
                                print('     |     ')
                                print('    / \    ')
                            elif turns==0:
                                print("The word is",word)
                                print("No more Turns left")
                                print("You Lost")
                                print("Hangman is dead")
                                break
                hangman()

        if option == "Language Translator":
        
            engine.say('You have selected Language Translator')
            engine.runAndWait()
            print('You have selected Language Translator')
            from tkinter import Tk, Label, Entry, Text, Button
            from tkinter import ttk
            from googletrans import Translator, LANGUAGES
            root = Tk()
            root.geometry("1100x320")
            root.resizable(0,0)
            root["bg"] = "blue"

            root.title("Language translator")
            label = Label(root,text = "Language translator" ,font = " Arial 20 bold")
            label.pack()

            label1 = Label(root,text = " Enter text" , font = "Arial 13 bold")
            label1.place(x = 163, y = 90)
             
            Input_text = Entry(root,width = 60)
            Input_text.place(x = 150, y= 130)
            Input_text.get()

            label2 = Label(root , text ="Output" , font = "Arial 13 bold")
            label2.place(x = 680, y = 90)
            Output_text = Text(root, font ="Arail 10", height  = 5, wrap = WORD , padx= 5 ,pady=5,width =50)
            Output_text.place( x = 700, y= 130)

            language = list(LANGUAGES.values())

            dest_lang = ttk.Combobox(root , values = language , width =22)
            dest_lang.place(x = 130,y = 180)
            dest_lang.set("Choose language")

            def Translate():
                translator = Translator()
                translated =  translator.translate(text = Input_text.get() ,dest =  dest_lang.get())
                Output_text.delete(1.0 ,END)
                Output_text.insert(END,translated.text )

            trans_button = Button(root , text = "Translate" , font ="Arial 13 bold" , command = Translate, bg = "orange")
            trans_button.place(x = 445, y = 180)   

            root.mainloop()

            inputx = input('You want to go to main menu or Exit, enter y or n: ', )
                        
            if inputx == 'y':
                functions()
            else:
                exit()
            

        if option == "Email Automation":
            
            engine.say('You Selected Email Automation, by this you can send mails to anyone from your mail')
            engine.runAndWait()
            print('You have selected Email Automation')

            import smtplib
            import threading
            import email.message
            import tkinter as tk
            from tkinter import messagebox

            def send_email():
                # Get user input from the GUI
                receiver_email = receiver_email_entry.get()
                subject = subject_entry.get()
                content = content_text.get("1.0", tk.END)

                # Your Gmail account credentials
                gmail_username = "aarti081004@gmail.com"  # Replace with your Gmail email
                gmail_password = "ntgdizilpjnmicsp"   # Replace with your Gmail password or app password

                # Create an email message
                msg = email.message.Message()
                msg['Subject'] = subject
                msg['From'] = gmail_username
                msg['To'] = receiver_email
                msg.add_header('Content-Type', 'text/plain')
                msg.set_payload(content)

                try:
                    # Establish a connection to the Gmail SMTP server
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()

                    # Login to your Gmail account
                    server.login(gmail_username, gmail_password)

                    # Send the email
                    server.sendmail(gmail_username, [receiver_email], msg.as_string())

                    # Close the connection
                    server.quit()

                    # Show success message
                    messagebox.showinfo("Success", "Email sent successfully!")

                except Exception as e:
                    # Show error message if something goes wrong
                    messagebox.showerror("Error", f"Failed to send email:\n{str(e)}")

            def on_send_button_click():
                # Start a new thread to send the email (avoid freezing the GUI)
                threading.Thread(target=send_email).start()

            # Create the main application window
            root = tk.Tk()
            root.title("Gmail Bot")
            root.geometry("400x400")  # Set the window size

            # Define contrasting colors
            bg_color = "#263D42"      # Dark blue-green
            fg_color = "#FFFFFF"      # White
            button_bg = "#FF8C00"     # Dark orange
            button_fg = "#FFFFFF"     # White

            # Set the background color for the entire window
            root.config(bg=bg_color)

            # Create and place the GUI elements with the contrasting colors
            receiver_email_label = tk.Label(root, text="Receiver Email:", bg=bg_color, fg=fg_color)
            receiver_email_label.pack()
            receiver_email_entry = tk.Entry(root)
            receiver_email_entry.pack()

            subject_label = tk.Label(root, text="Subject:", bg=bg_color, fg=fg_color)
            subject_label.pack()
            subject_entry = tk.Entry(root)
            subject_entry.pack()

            content_label = tk.Label(root, text="Content:", bg=bg_color, fg=fg_color)
            content_label.pack()
            content_text = tk.Text(root, height=10, width=50)
            content_text.pack()

            send_button = tk.Button(root, text="Send Email", bg=button_bg, fg=button_fg, command=on_send_button_click)
            send_button.pack()

            # Start the GUI main loop
            root.mainloop()

            inputx = input('You want to go to main menu or Exit, enter y or n: ', )
                        
            if inputx == 'y':
                functions()
            else:
                exit()            
        

        if option == "Wikipedia Scraping":
        
            engine.say('You Selected Wikipedia Scraping, by this you can get any information from wikipedia')
            engine.runAndWait()
            print('You have selected Wikipedia Scraping')

            import wikipedia as w
            import tkinter as tk
            from tkinter import scrolledtext

            def get_wikipedia_summary(search_term):
                try:
                    wiki_summary = w.summary(search_term)
                    return wiki_summary
                except w.exceptions.DisambiguationError as e:
                    options = e.options
                    print(f"'{search_term}' may refer to:")
                    for idx, option in enumerate(options, start=1):
                        print(f"{idx}. {option}")
                    while True:
                        try:
                            choice = int(input("Enter the number of the specific topic you want: "))
                            if 1 <= choice <= len(options):
                                return w.summary(options[choice - 1])
                            else:
                                print("Invalid choice. Please enter a valid number.")
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
                except w.exceptions.PageError as e:
                    raise ValueError(f"PageError: {e}")
                except Exception as e:
                    raise ValueError(f"An error occurred while fetching the Wikipedia summary: {e}")

            def fetch_and_display_summary():
                global entry, text
                user_input = entry.get()
                try:
                    wiki_summary = get_wikipedia_summary(user_input)
                    text.delete("1.0", tk.END)
                    text.insert(tk.INSERT, wiki_summary)
                except ValueError as e:
                    text.delete("1.0", tk.END)
                    text.insert(tk.INSERT, f"An error occurred: {e}")
                except Exception as e:
                    text.delete("1.0", tk.END)
                    text.insert(tk.INSERT, f"An unexpected error occurred: {e}")

            def search_again():
                global entry, text
                entry.delete(0, tk.END)
                text.delete("1.0", tk.END)

            def main():
                global entry, text
                root = tk.Tk()
                root.title("Wikipedia Summary Bot")

                frame = tk.Frame(root)
                frame.pack(padx=10, pady=10)

                label = tk.Label(frame, text="Enter anything:")
                label.pack()

                entry = tk.Entry(frame, width=50)
                entry.pack()

                button_search = tk.Button(frame, text="Search", command=fetch_and_display_summary)
                button_search.pack()

                button_again = tk.Button(frame, text="Clear Text", command=search_again)
                button_again.pack()

                text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20)
                text.pack(padx=10, pady=10)

                root.mainloop()

            if __name__ == "__main__":
                main()

                def main():
                    speaker = pyttsx3.init()
                    user_input = input("Enter anything: ")

                    try:
                        wiki_summary = get_wikipedia_summary(user_input)
                        print("\nSummary:")
                        print(wiki_summary)

                        speaker.say(wiki_summary)
                        speaker.runAndWait()
                    except ValueError as e:
                        print(f"An error occurred: {e}")
                    except KeyboardInterrupt:
                        print("\nProcess interrupted by the user.")
                    except Exception as e:
                        print(f"An unexpected error occurred: {e}")


                if __name__ == "__main__":
                    main()

                inputx = input('You want to go to main menu or Exit, enter y or n: ', )
                        
                if inputx == 'y':
                    functions()
                else:
                    exit()

        if option == "Social Media Automation":
        
            engine.say('Social Media Automation')
            engine.runAndWait()
            print('Social Media Automation')

            engine.say('These are the available Bots in Social Media')
            engine.runAndWait()
            print('''
                   1.Instagram
                   2.Whatsapp
                   ''')
            input7 = int(input('Enter any number: ', ))

            if input7 == 1:
                from instabot import Bot

                import os
                import glob
                cookie_del = glob.glob("config/*cookie.json")
                if len(cookie_del) > 0:
                    os.remove(cookie_del[0])

                bot = Bot()

                engine.say('Welcome to the Instagram Bot')
                print('Welcome to the Instagram Bot')

                username = str(input('Enter username of your Instagram ID: ', ))
                password = str(input('Enter Password of your Instagram ID: ', ))

                try:
                    bot.login(username = username, password = password, use_cookie=True)
                    print("Login successful!")
                except Exception as e:
                    print(f"Error: {str(e)}")

                engine.say('The Functions of this Instagram Bot are listed Below')

                print('''1.Upload Photo
                         2.Follow People
                         3.Send Message
                         4.Get Follwers List
                         5.Unfollow Everyone
                         ''')

                input1 = int(input('Enter Number to select the Function: ', ))

                if input1 == 1:
                    path1 = str(input('Enter path for Uploading photo: ', ))
                    path = rpath
                    bot.upload_photo(path , caption = caption1)

                if input1 == 2:
                    follow = str(input('Enter the Instagram ID for follwing them: ', ))
                    bot.follow(follow)

                if input1 == 3:
                    message = str(input('Enter Message to send : ', ))
                    user = str(input('Enter ID to send message: ', ))
                    bot.send_message(message ,[user])

                if input1 == 4:
                    followers = bot.get_user_followers(username)
                    for follower in followers:
                        print(bot.get_user_info(follower))

                if input1 == 5:
                    bot.unfollow_everyone()

                else:
                    print('Enter valid number')
            import pywhatkit

            if input7 == 2:
                message = input('enter message: ', )
                number = input('enter phone number (+91-number): ', )
                time1 = int(input('enter time(hour): ',))
                time2 = int(input('enter time(minute): ',))
                
                pywhatkit.sendwhatmsg(number,message,time1,time2)

            inputx = input('You want to go to main menu or Exit, enter y or n: ', )
                        
            if inputx == 'y':
                functions()
            else:
                exit()
        
        
        if option == "Desktop (Files Organizer, Reminders)":
        
            engine.say('You Selected Desktop')
            engine.runAndWait()
            print('You have selected Desktop')

            engine.say('In desktop automation you an choose reminders and files organiser')
            engine.runAndWait()
            print('''1.Reminders
                     2.files organiser
                  ''')
            input3 = int(input('choose reminders and files organiser : ', ))

            if input3 == 1:
                from win10toast import ToastNotifier
                import time

                toaster = ToastNotifier()
                Toasttitle = input("\nTitle of Remainder:")
                msg = input("Message: ")
                minutes = float(input("How many minutes: "))

                seconds = minutes * 60
                print("\nRemainder Set Successfully!\n")
                time.sleep(seconds)
                toaster.show_toast(Toasttitle,msg,duration = 10,threaded=True)

                while toaster.notification_active:
                    time.sleep(0.1)

                inputx = input('You want to go to main menu or Exit, enter y or n: ', )
                        
                if inputx == 'y':
                    functions()
                else:
                    exit()

            if input3 == 2:
                import os
                import shutil

                path = input("Enter Path: ")
                files = os.listdir(path)

                for file in files:
                    filename,extension = os.path.splitext(file)
                    extension = extension[1:]

                    if os.path.exists(path+'/'+extension):
                        shutil.move(path+'/'+file,path+'/'+extension+'/'+file)
                    else:
                        os.makedirs(path+'/'+extension)
                        shutil.move(path+'/'+file,path+'/'+extension+'/'+file)

                inputx = input('You want to go to main menu or Exit, enter y or n: ', )
                        
                if inputx == 'y':
                    functions()
                else:
                    exit()
                        
        
        
        if option == "Weather Info":
        
            engine.say('You Selected Weather Info')
            engine.runAndWait()
            print('This Program shows you weather info')
            import datetime as dt
            import requests
            import PySimpleGUI as sg

            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            api_key = "8e4ffda65c3bdaae37d6d201ec1e7ec5"


            def ktocf(kelvin):
                celsius = kelvin - 273.15
                fahrenheit = celsius * (9 / 5) + 32
                return celsius, fahrenheit


            def get_weather_info(city):
                url = base_url + "appid=" + api_key + "&q=" + city
                response = requests.get(url).json()

                if response['cod'] == '404':
                    return f"Sorry, I couldn't find weather information for '{city}'. Please check the spelling and try again."

                temp_kelvin = response['main']['temp']
                temp_celsius, temp_fahrenheit = ktocf(temp_kelvin)
                feels_like_kelvin = response['main']['feels_like']
                feels_like_celsius, feels_like_fahrenheit = ktocf(feels_like_kelvin)
                wind_speed = response['wind']['speed']
                humidity = response['main']['humidity']
                description = response['weather'][0]['description']
                sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
                sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

                weather_info = (
                    f"Temperature in {city}: {temp_celsius:.2f}C or {temp_fahrenheit}F\n"
                    f"Temperature in {city} feels like: {feels_like_celsius:.2f}C or {feels_like_fahrenheit:.2f}F\n"
                    f"Humidity in {city}: {humidity}%\n"
                    f"Wind Speed in {city}: {wind_speed}m/s\n"
                    f"General Weather in {city}: {description}\n"
                    f"Sun rises in {city}: {sunrise_time} local time.\n"
                    f"Sun sets in {city}: {sunset_time} local time."
                )
                return weather_info


            def main():
                sg.theme('DarkBlue')


                layout = [
                    [sg.Text("Weather Chatbot", font=("Helvetica", 20), text_color="white")],
                    [sg.InputText(default_text="Enter a city name", key='-CITY-', font=("Helvetica", 14))],
                    [sg.Button("Search", key='-SEARCH-', font=("Helvetica", 14))],
                    [sg.Multiline(size=(40, 10), key='-OUTPUT-', font=("Helvetica", 14), disabled=True, background_color="black", text_color="white")],
                ]

                window = sg.Window("Weather Chatbot", layout, finalize=True)

                while True:
                    event, values = window.read()
                    if event == sg.WIN_CLOSED:
                        break
                    elif event == '-SEARCH-':
                        city = values['-CITY-'].strip().upper()
                        if city == "EXIT":
                            window['-OUTPUT-'].update("Goodbye! Have a great day!")
                        else:
                            weather_info = get_weather_info(city)
                            window['-OUTPUT-'].update(weather_info)

                window.close()


            if __name__ == "__main__":
                main()


            inputx = input('You want to go to main menu or Exit, enter y or n: ', )
                        
            if inputx == 'y':
                functions()
            else:
                exit()

        if option == "News Aggregator":

            engine.say('You Selected News Aggregator')
            engine.runAndWait()
            print('This Program shows you News')
            
            import tkinter as tk
            import nltk
            from textblob import TextBlob
            from newspaper import Article
            nltk.download('punkt')

            def summarise():
                url = utext.get('1.0',"end").strip()
                article = Article(url)
                article.download()
                article.parse()

                article.nlp()

                title.config(state="normal")
                author.config(state="normal")
                publication.config(state="normal")
                summary.config(state="normal")
                sentiment.config(state="normal")

                title.delete('1.0','end')
                title.insert('1.0',article.title)

                author.delete('1.0', 'end')
                author.insert('1.0', article.authors)

                publication.delete('1.0', 'end')
                publication.insert('1.0', str(article.publish_date))

                summary.delete('1.0', 'end')
                summary.insert('1.0', article.summary)

                analysis = TextBlob(article.text)
                sentiment.delete('1.0','end')
                sentiment.insert('1.0',f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

                title.config(state="disabled")
                author.config(state="disabled")
                publication.config(state="disabled")
                summary.config(state="disabled")
                sentiment.config(state="disabled")

            root = tk.Tk()
            root.title("News Summarizer")
            root.geometry('1200x600')

            tlabel = tk.Label(root, text="Title")
            tlabel.pack()

            title = tk.Text(root, height=1, width=140)
            title.config(state='disabled', bg="#E6E6E6")
            title.pack()

            alabel= tk.Label(root, text="Author")
            alabel.pack()

            author = tk.Text(root, height=1, width=140)
            author.config(state='disabled', bg="#E6E6E6")
            author.pack()

            plabel= tk.Label(root, text="Publishing Date")
            plabel.pack()

            publication = tk.Text(root, height=1, width=140)
            publication.config(state='disabled', bg="#E6E6E6")
            publication.pack()

            slabel= tk.Label(root, text="Summary")
            slabel.pack()

            summary = tk.Text(root, height=20, width=140)
            summary.config(state='disabled', bg="#E6E6E6")
            summary.pack()

            selabel = tk.Label(root, text="Sentiment Analysis")
            selabel.pack()

            sentiment = tk.Text(root, height=1, width=140)
            sentiment.config(state='disabled', bg="#E6E6E6")
            sentiment.pack()

            ulabel= tk.Label(root, text="URL")
            ulabel.pack()

            utext = tk.Text(root, height=1, width=140)
            utext.pack()

            btn = tk.Button(root, text="Summarise", command=summarise)
            btn.pack()

            root.mainloop()

            inputx = input('You want to go to main menu or Exit, enter y or n: ', )
                        
            if inputx == 'y':
                functions()
            else:
                exit()
            
        
        else:
            print("Selected Option {}: {}".format(serial_number, option))


    # Create the main window
    root = tk.Tk()
    root.title("Options Canvas")

    # Create the canvas
    canvas = tk.Canvas(root, width=500, height=500, bg="white")
    canvas.pack()

    # Function to create a button at given coordinates with a label
    def create_button(x, y, serial_number, label):
        button = tk.Button(canvas, text="{}. {}".format(serial_number, label), command=lambda: button_clicked(serial_number, label), width=40)
        button.place(x=x, y=y)

    # Create nine buttons with labels and serial numbers
    options = [
        "Games",
        "Language Translator",
        "Email Automation",
        "Wikipedia Scraping",
        "Social Media Automation",
        "Desktop (Files Organizer, Reminders)",
        "Weather Info",
        "News Aggregator",
    ]

    x_position = 50
    y_position = 50

    for serial_number, option in enumerate(options, start=1):
        create_button(x_position, y_position, serial_number, option)
        y_position += 50

    # Run the Tkinter event loop
    root.mainloop()

'''
print(
      1.Games
      2.Language Translator
      3.Email Automation
      4.Wikipedia Scraping
      5.Social Media Automation
      6.Desktop (Files Organizer , Reminders)
      7.Weather Info
      8.News Aggregator
      )
'''

intro()
info()
functions()
