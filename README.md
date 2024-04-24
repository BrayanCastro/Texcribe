# Texcribe
Texcribe aims to streamline efficiency by automating Video/Audio summarization while bridging the gap between technical and non-technical listeners through language translation and simplification.

The following code is for texcribe, a web application used for meeting summarization and translation.

The following code uses two api's:
- assembly ai: used to transcribe any video or audio formats submitted 
- google gemini api: used to pick the summary format as well as the chosen language for translation

For the files to be run on your device: you need to run the following pip commands in the terminal:

pip install assemblyai

pip install google-generativeai

pip install googletrans==4.0.0rc1

pip install -U pip setuptools wheel

pip install spacy

pip install wordsapy

pip install rake-nltk

python -c "import nltk; nltk.download('stopwords')"

pip install nltk

pip install git+https://github.com/boudinfl/pke.git

python -m nltk.downloader stopwords
python -m nltk.downloader universal_tagset
python -m spacy download en_core_web_sm # download the english model

pip install flask flask-sqlalchemy flask-login
export FLASK_APP=project
export FLASK_DEBUG=1
flask run

after running both commands in the terminal it should work as expected
