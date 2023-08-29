#Import all the required libraries.
from pathlib import Path
from pydub import AudioSegment
import speech_recognition as sr
import yake
from rpunct import RestorePuncts

cumulative_kw_frequency = {}

def clear_file(file_name):
    '''Clear the text file.'''
    with open(file_name,'w') as file:
        pass

def audio_extraction(file_path):
    '''Loads the video from a given file path and extracts the audio into a wav file, ensuring it is in the correct format.'''
    video = AudioSegment.from_file(file_path, format = "mp4")
    audio = video.set_channels(1).set_frame_rate(16000).set_sample_width(2) 
    audio.export("audio.wav", format="wav")

def speech_recognition():
    '''Loads the audio file and extracts the speech from it, writing the transcript to a text file.'''
    r = sr.Recognizer()
    with sr.AudioFile("audio.wav") as source:
        audio_text = r.record(source)

    try:
        text = r.recognize_google(audio_text,language="en-US") #Google Speech Recognition model.

        file_name = "transcript.txt"
        with open(file_name, "w") as file:
            file.write(text)

    except sr.UnknownValueError:
        print("Could not transcribe.")

def keyword_extraction():
    '''Performs keyword extraction on the repunctuated transcript using the YAKE method. All keywords are appended to a text file.'''
    with open("transcript.txt", "r") as file:
        words = file.read().split()

    words_string = " ".join(words)

    #Restore punctuation to the transcript to improve keyword extraction accuracy.
    rpunct = RestorePuncts()
    punctuated_string = rpunct.punctuate(words_string)

    kw_extractor = yake.KeywordExtractor(lan="en",n=2,dedupLim=0.6)
    keywords = kw_extractor.extract_keywords(punctuated_string)

    for kw, _ in keywords:
        kw = kw.lower()
        cumulative_kw_frequency[kw] = cumulative_kw_frequency.get(kw, 0) + 1

def main(start_video=1, end_video=5, file_name="keywords.txt"):
    '''The output of the pipeline is a text file containing all the keywords from the entire subset of specified videos.'''
    clear_file(file_name)

    for i in range(start_video,end_video+1):
        #The file path should follow the naming convention of the saved videos.
        file = "video" + str(i)
        file_path = f"./downloads/{file}.mp4"

        audio_extraction(file_path)
        speech_recognition()
        keyword_extraction()

    with open(file_name,"a") as file:
        for kw in cumulative_kw_frequency.keys():
            file.write(f"{kw} {cumulative_kw_frequency[kw]}\n")

if __name__ == "__main__":
    main()