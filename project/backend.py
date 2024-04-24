import assemblyai as aai
import google.generativeai as genai
from googletrans import Translator
import spacy
import pke
from wordsapy import Dictionary


translator = Translator()
genai.configure(api_key="AIzaSyA6Zp92hhfFnuDLFKPUaBKXKdv0ZWKfhMA")
dictionary = Dictionary(api_key='c510078e52msh5707b0ccdfc7a58p1d56aajsn560c2eed03dc')
aai.settings.api_key = "2a872e1d793947e8ae9b4db41a91f35b"

def summary():
    """
    This function prompts the user for summary style and length (if paragraph style)
    and returns a dictionary with the chosen options.
    """
    style = input("Choose summary style (paragraph/list elements): ").lower()
    if style == "paragraph":
        length = int(input("Enter paragraph length (50, 100, or 150 words): "))
        if length not in (50, 100, 150):
            print("Invalid length. Choosing default (100 words).")
            length = 100
    else:
        length = 100
    return {"style": style, "length": length}

def translate():
    """
    This function prompts the user for the desired translation language
    and returns the chosen language code.
    """
    languages = {
        "afrikaans": "af",
        "albanian": "sq",
        "amharic": "am",
        "arabic": "ar",
        "armenian": "hy",
        "azerbaijani": "az",
        "basque": "eu",
        "belarusian": "be",
        "bengali": "bn",
        "bosnian": "bs",
        "bulgarian": "bg",
        "catalan": "ca",
        "cebuano": "ceb",
        "chichewa": "ny",
        "chinese (simplified)": "zh-cn",
        "chinese (traditional)": "zh-tw",
        "corsican": "co",
        "croatian": "hr",
        "czech": "cs",
        "danish": "da",
        "dutch": "nl",
        "english": "en",
        "esperanto": "eo",
        "estonian": "et",
        "filipino": "tl",
        "finnish": "fi",
        "french": "fr",
        "frisian": "fy",
        "galician": "gl",
        "georgian": "ka",
        "german": "de",
        "greek": "el",
        "gujarati": "gu",
        "haitian creole": "ht",
        "hausa": "ha",
        "hawaiian": "haw",
        "hebrew": "he",
        "hindi": "hi",
        "hmong": "hmn",
        "hungarian": "hu",
        "icelandic": "is",
        "igbo": "ig",
        "indonesian": "id",
        "irish": "ga",
        "italian": "it",
        "japanese": "ja",
        "javanese": "jw",
        "kannada": "kn",
        "kazakh": "kk",
        "khmer": "km",
        "korean": "ko",
        "kurdish (kurmanji)": "ku",
        "kyrgyz": "ky",
        "lao": "lo",
        "latin": "la",
        "latvian": "lv",
        "lithuanian": "lt",
        "luxembourgish": "lb",
        "macedonian": "mk",
        "malagasy": "mg",
        "malay": "ms",
        "malayalam": "ml",
        "maltese": "mt",
        "maori": "mi",
        "marathi": "mr",
        "mongolian": "mn",
        "myanmar (burmese)": "my",
        "nepali": "ne",
        "norwegian": "no",
        "odia": "or",
        "pashto": "ps",
        "persian": "fa",
        "polish": "pl",
        "portuguese": "pt",
        "punjabi": "pa",
        "romanian": "ro",
        "russian": "ru",
        "samoan": "sm",
        "scots gaelic": "gd",
        "serbian": "sr",
        "sesotho": "st",
        "shona": "sn",
        "sindhi": "sd",
        "sinhala": "si",
        "slovak": "sk",
        "slovenian": "sl",
        "somali": "so",
        "spanish": "es",
        "sundanese": "su",
        "swahili": "sw",
        "swedish": "sv",
        "tajik": "tg",
        "tamil": "ta",
        "telugu": "te",
        "thai": "th",
        "turkish": "tr",
        "ukrainian": "uk",
        "urdu": "ur",
        "uyghur": "ug",
        "uzbek": "uz",
        "vietnamese": "vi",
        "welsh": "cy",
        "xhosa": "xh",
        "yiddish": "yi",
        "yoruba": "yo",
        "zulu": "zu"
    }

    print("Available languages:")
    for language in languages:
        print(language)
    print()
    choice = input("Choose language to translate to: ").lower()
    if choice not in languages:
        print("Invalid language. Choosing English (en) as default.")
        choice = "en"
    return str(languages[choice])

# Example usage
summary_options = summary()
length = summary_options['length']

if length == 0:
    length = None

translate_language = translate()

transcriber = aai.Transcriber()

audio_url = (
    "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"
)


config = aai.TranscriptionConfig(speaker_labels=True)

transcript = transcriber.transcribe(audio_url, config)

val = transcript.text
print()
print()
print("Transcript of the audio")
print("------------------------------------------------------------------------------------------------")
print()
print(val)
print()
print()

# for utterance in transcript.utterances:
# print(f"Speaker {utterance.speaker}: {utterance.text}")


# Set up the model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 256,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

prompt_parts = [
    "input: ",
    "output: ",
]

def check_space_in_string(my_string):
    """Checks if a string contains a space using the 'in' operator."""
    return " " in my_string

convo = model.start_chat(history = [])
convo.send_message("Give me a summary of the following text " + val + ". Make the summary in the following format "+ summary_options['style'] + "and make it length " + str(length))
print("Summary of the audio")
print("------------------------------------------------------------------------------------------------")
print()
print(convo.last.text)
print()
print()



out = translator.translate(str(convo.last.text), dest=str(translate_language))

print("Translation of the summary")
print("------------------------------------------------------------------------------------------------")
print()
print(out.text)
print()
print()
#convo.send_message("return the key technical words in the summary as a python list: " + convo.last.text)
print()
print("Technical words in the summary")
print("------------------------------------------------------------------------------------------------")
print()

# initialize keyphrase extraction model, here TopicRank
extractor = pke.unsupervised.TopicRank()

# load the content of the document, here document is expected to be in raw
# format (i.e. a simple text file) and preprocessing is carried out using spacy
extractor.load_document(input=val, language='en')

# keyphrase candidate selection, in the case of TopicRank: sequences of nouns
# and adjectives (i.e. `(Noun|Adj)*`)
extractor.candidate_selection()

# candidate weighting, in the case of TopicRank: using a random walk algorithm
extractor.candidate_weighting()

# N-best selection, keyphrases contains the 10 highest scored candidates as
# (keyphrase, score) tuples
keyphrases = extractor.get_n_best(n=10)
words = []
for b in keyphrases:
    c = b[0]
    vali = check_space_in_string(c)
    if vali:
        continue
    else:
        words.append(c)
## test for class to show it handles complex words not in dictionary
##
##updated technical jargon portion that catches edge cases and uses gemini for defintions
##

file = open("defintions.txt",'a')
for b in words:
    convo.send_message("Return the definition of the  followiing word" + b + "print the definition between two curly braces. Only print out one definition of the word")
    meaning = convo.last.text
    new_meaning = ""
    for i in range(len(meaning)):
        if meaning[i] == "{" or meaning[i] == "}":
            continue
        new_meaning += (meaning[i])
    print(b+ ": " + new_meaning)
    file.write(b+ ": " + new_meaning + "\n")

file.close()
print()


#
# Handles the number of times a technical word appears in the transcription
#

technical_words = {}
transcription  = val.lower()
transcription = val.split()

for i in words:
    cnt = 0
    if i not in technical_words:
        technical_words[i] = 1

        for j in range(len(transcription)):
            if transcription[j] == i:
                cnt += 1
        technical_words[i] = cnt
