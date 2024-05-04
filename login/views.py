import os
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_input(input_text):
    # Tokenize and normalize the input text
    tokens = word_tokenize(input_text.lower())
    
    # Initialize WordNet Lemmatizer
    lemmatizer = WordNetLemmatizer()
    
    # Lemmatize tokens
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    # Filter out stopwords and non-alphabetic tokens
    filtered_tokens = [word for word in lemmatized_tokens if word.isalpha() and word not in stopwords.words('english')]
    return filtered_tokens


# Create your views here.
def home(request):
    warning_message= None
    if request.method=='POST':
        username1 = request.POST['username']
        password1 = request.POST['password']

        user_model = get_user_model()
        try:
            user = user_model.objects.get(username=username1,password=password1)
            print("hi")
            
            #user = authenticate(password=password1)
        except user_model.DoesNotExist:
            user = None

        if user is not None:
            # Passwords match
            #return render(request, 'login_signup.html')
            return render(request,'main/login')
            

        else:
            warning_message="Invalid credentials"
            print("here")
            return render(request, 'login_signup.html', {'warning_message': warning_message})
        """
        user = auth.authenticate(username=username1,password=password1)
        if user is not None:
            auth.login(request, user)
            return redirect("/")"""
        
            
            
       
    else:
        return render(request,'login_signup.html')


def signup_view(request):
    warning_message=None
    # Your signup view logic here
    if request.method == 'POST':
       
        username = request.POST['new_username']
        password1 = request.POST['new_password']
        password2 = request.POST['confirm_password']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                print("username taken")
                warning_message = "Username already taken"
                return render(request, 'login_signup.html', {'warning_message': warning_message})
            else:
                user_object = User.objects.create(username=username, password=password1)
                user_object.save()
                print("created user")
                return redirect('/')
            
        else:
            print("not created")
            warning_message="Password not same"
            return render(request, 'login_signup.html', {'warning_message': warning_message})
        
    else:   
        return render(request, 'login_signup.html')
    
def player_view(request):
    # Get the song URL and image URL from the query parameters
    song_url = request.GET.get('song')
    image_url = request.GET.get('image')

    # Check if song URL and image URL are provided
    if not song_url or not image_url:
        # Handle the case where the URLs are not provided
        return HttpResponseBadRequest("Song URL and Image URL are required.")

    # Add any additional logic here

    context = {
        'image_url': image_url,
        'song_url': song_url,
    }
    return render(request, 'player.html', context)
def home_reach(request):
    return render(request,'home.html')
    

def quick_sleep(request):
    return render(request,'songs.html')

def deep_sleep(request):
    return render(request,'deep.html')

def inner_peace(request):
    return render(request,'inner.html')

def healing_music(request):
    return render(request,'healing.html')

def tales(request):
    return render(request,'tales.html')

def allmusic(request):
    return render(request,'allmusic.html')

def breathing(request):
    return render(request,'breathing.html')

def apnea(request):
    return render(request,'apnea.html')

def account(request):
    return render(request,'account.html')

def dream(request):
    return render(request,'dream.html')
def chatbot_process(request):
    # Your logic for processing chatbot input goes here
    return render(request, 'chatbot.html')











def interpretdream(user_input):
    # Dream interpretations dictionary
    dream_interpretations = {
        "falling": "Dreams about falling often represent feeling out of control or insecure in some aspect of your life.",
    "flying": "Dreams of flying may symbolize a desire for freedom or a sense of empowerment.",
    "chased": "Being chased in a dream may indicate that you are avoiding confronting a problem or fear in your waking life.",
    "teeth": "Dreams about teeth falling out can symbolize anxiety about appearance or concerns about communication.",
    "naked": "Dreams of being naked in public may suggest feelings of vulnerability or embarrassment.",
    "late": "Dreams of being late may reflect anxiety about time management or fear of missing out on opportunities.",
    "animal": "Animals in dreams may represent instincts or primal desires.",
    "love": "Dreams about love may reflect feelings of affection, romance, or connection.",
    "danger": "Dreams of danger may suggest feelings of fear or insecurity in your waking life.",
    "test": "Dreams about taking a test may symbolize feelings of pressure or evaluation in your waking life.",
    "winning": "Dreams of winning may symbolize success, achievement, or a sense of accomplishment.",
    "trapped": "Dreams of being trapped may represent feelings of being stuck or confined in your waking life.",
    "lost": "Dreams of being lost may symbolize feelings of confusion, uncertainty, or a lack of direction.",
    "celebrity": "Dreams about celebrities may indicate desires for fame, recognition, or admiration.",
    "exam": "Dreams about exams may reflect feelings of stress or anxiety about performance or evaluation.",
    "accident": "Dreams of accidents may suggest feelings of vulnerability, unpredictability, or fear of losing control.",
    "money": "Dreams about money may symbolize feelings of security, abundance, or financial concerns.",
    "run": "Dreams of running may symbolize a desire for escape, avoidance, or pursuit of goals.",
    "water": "Dreams about water may symbolize emotions, purification, or the unconscious mind.",
    "fire": "Dreams of fire may represent transformation, passion, or destruction.",
    "death": "Dreams about death may symbolize endings, transitions, or fear of the unknown.",
    "ghost": "Seeing ghosts in dreams may suggest unresolved emotions, memories, or past experiences.",
    "house": "Dreams about houses may symbolize the self, family, security, or different aspects of your life.",
    "school": "Dreams of being in school may reflect feelings of learning, growth, or past experiences.",
    "baby": "Dreams about babies may symbolize new beginnings, innocence, or vulnerability.",
    "friend": "Dreams of friends may represent social connections, support, or aspects of yourself that you associate with your friends.",
    "snake": "Seeing snakes in dreams may symbolize transformation, healing, or fear of the unknown.",
    "forest": "Dreams of forests may represent exploration, mystery, or a need to connect with nature.",
    "mountain": "Dreams of mountains may symbolize challenges, obstacles, or a desire for spiritual growth.",
    "ocean": "Dreams about the ocean may represent vastness, depth, or the unconscious mind.",
    "road": "Dreams of roads may symbolize a journey, direction, or choices in life.",
    "mirror": "Seeing mirrors in dreams may suggest self-reflection, self-awareness, or a desire to understand oneself better.",
    "monster": "Dreams of monsters may symbolize fears, insecurities, or aspects of yourself that you perceive as threatening.",
    "key": "Dreams about keys may represent opportunities, solutions, or access to new possibilities.",
    "door": "Dreams of doors may symbolize opportunities, transitions, or new beginnings.",
    "skeleton": "Seeing skeletons in dreams may symbolize mortality, the passage of time, or unresolved issues.",
    "music": "Dreams of music may represent emotions, harmony, or a desire for self-expression.",
    "flower": "Dreams about flowers may symbolize beauty, growth, or the blossoming of potential.",
    "star": "Seeing stars in dreams may symbolize guidance, inspiration, or aspirations.",
    "cloud": "Dreams of clouds may represent thoughts, emotions, or a sense of detachment from reality.",
    "book": "Dreams about books may symbolize knowledge, learning, or the search for answers.",
    "light": "Dreams of light may symbolize illumination, clarity, or insight.",
    "darkness": "Dreams about darkness may represent fear, the unknown, or hidden aspects of the self.",
    "anger": "Dreams of anger may reflect unresolved emotions, frustrations, or conflicts in waking life.",
    "peace": "Dreams about peace may symbolize inner harmony, tranquility, or a desire for serenity.",
    "rainbow": "Seeing rainbows in dreams may symbolize hope, promise, or a connection between the spiritual and physical worlds.",
    "island": "Dreams of islands may represent solitude, self-discovery, or a desire for escape from the complexities of life.",
    "space": "Dreams about outer space may symbolize exploration, boundlessness, or the search for meaning in life.",
    "alien": "Seeing aliens in dreams may suggest feelings of otherness, curiosity, or encounters with the unfamiliar.",
    "robot": "Dreams of robots may represent automation, efficiency, or a fear of losing individuality in a technological world.",
    "magic": "Dreams about magic may symbolize creativity, wonder, or a belief in possibilities beyond the ordinary.",
    "time": "Dreams of time may symbolize impermanence, change, or a sense of urgency in waking life.",
    "treasure": "Seeing treasures in dreams may represent hidden talents, opportunities, or the search for inner richness.",
    "party": "Dreams of attending a party may symbolize social interaction, celebration, or a desire for fun and enjoyment.",
    "forest": "Dreams of being in a forest may represent exploration, mystery, or a need to connect with nature.",
    "flood": "Dreams of a flood may symbolize overwhelming emotions, sudden change, or a feeling of being inundated by circumstances.",
    "rescue": "Dreams of being rescued may suggest a desire for help, support, or guidance in a challenging situation.",
    "school": "Dreams of being in school may reflect feelings of learning, growth, or past experiences.",
    "stairs": "Dreams of stairs may symbolize progress, elevation, or transitions in life.",
    "wrapping": "Dreams of wrapping may represent completion, preparation, or the need to conceal or protect something.",
    "store": "Dreams of being in a store may symbolize choices, opportunities, or desires for material possessions.",
    "medication": "Dreams of taking medication may suggest a need for healing, relief, or resolution of physical or emotional issues.",
    "asthma": "Dreams of asthma may symbolize feelings of suffocation, restriction, or difficulty expressing oneself.",
    "conflict": "Dreams of conflict may represent inner turmoil, unresolved issues, or challenges in relationships.",
    "deception": "Dreams of deception may suggest feelings of betrayal, dishonesty, or a need to uncover hidden truths.",
    "relationship": "Dreams of relationships may symbolize connection, intimacy, or the dynamics of interpersonal interactions.",
    "pool": "Dreams of a pool may represent emotions, relaxation, or a desire for leisure and recreation.",
    "basement": "Dreams of a basement may symbolize the subconscious mind, hidden aspects of the self, or the foundation of one's life.",
    "lying": "Dreams of lying may suggest feelings of guilt, deceit, or a desire to conceal the truth.",
    "loneliness": "Dreams of loneliness may symbolize feelings of isolation, abandonment, or a longing for companionship.",
    "accident": "Dreams of an accident may represent unexpected events, loss of control, or a warning to pay attention to one's actions.",
    "work": "Dreams of work may symbolize productivity, responsibility, or concerns about one's career or professional life.",
    "funeral": "Dreams of a funeral may symbolize endings, transitions, or the need to grieve and let go of the past.",
    "dreaming": "Dreams of dreaming may suggest self-awareness, reflection, or the recognition of one's inner thoughts and desires.",
    "helplessness": "Dreams of helplessness may represent feelings of vulnerability, powerlessness, or a lack of control in waking life.",
    "escape": "Dreams of escape may symbolize a desire for freedom, liberation, or avoidance of responsibilities or difficulties.",
    "reunion": "Dreams of a reunion may represent reconciliation, connection with loved ones, or a desire to revisit the past.",
    "death": "Dreams of death may symbolize endings, transitions, or fear of the unknown.",
    "afterlife": "Dreams of the afterlife may suggest spiritual beliefs, contemplation of mortality, or curiosity about what lies beyond.",
    "home": "Dreams of home may represent security, comfort, or a sense of belonging.",
    "dynamite": "Dreams of dynamite may symbolize explosive emotions, destructive tendencies, or a need for drastic change.",
    "nudity": "Dreams of nudity may represent vulnerability, exposure, or a desire to express oneself authentically.",
    "medical": "Dreams of medical procedures or conditions may suggest concerns about health, well-being, or self-care.",
    "anxiety": "Dreams of anxiety may reflect feelings of stress, worry, or unease about future events or uncertainties.",
    "nightmare": "Dreams of nightmares may signify fear, trauma, or unresolved psychological issues.",
    "journey": "Dreams of a journey may symbolize personal growth, exploration, or a quest for self-discovery.",
    "confusion": "Dreams of confusion may represent uncertainty, indecision, or a lack of clarity in one's thoughts or actions.",
    "survival": "Dreams of survival may suggest resilience, resourcefulness, or the ability to overcome obstacles in challenging situations.",
    "transition": "Dreams of transition may symbolize change, adaptation, or the process of moving from one phase of life to another.",
    "forgiveness": "Dreams of forgiveness may represent reconciliation, acceptance, or the healing of past wounds.",
    "betrayal": "Dreams of betrayal may reflect feelings of hurt, distrust, or disillusionment in relationships.",
    "hope": "Dreams of hope may symbolize optimism, resilience, or a belief in positive outcomes despite challenges.",
    "security": "Dreams of security may represent stability, protection, or a sense of safety and well-being.",
    "freedom": "Dreams of freedom may symbolize liberation, independence, or the pursuit of personal autonomy and expression.",
    "girl": "Dreams of a girl may symbolize innocence, youth, femininity, or aspects of the dreamer's inner child.",
    "boy": "Dreams of a boy may symbolize youth, masculinity, energy, or the emergence of new ideas and endeavors.",
    "meeting": "Dreams of a meeting may represent collaboration, communication, exchange of ideas, or the need to connect with others.",
    "proposal": "Dreams of a proposal may symbolize commitment, partnership, union, or a desire for romantic connection and stability.",
    "celebration": "Dreams of a celebration may represent joy, achievement, recognition, or the need to honor milestones and accomplishments.",
    "birth": "Dreams of birth may symbolize new beginnings, creativity, transformation, or the emergence of new ideas or opportunities.",
    "death": "Dreams of death may symbolize endings, transitions, transformation, or the need to let go of the past to embrace the future.",
    "wedding": "Dreams of a wedding may represent union, partnership, commitment, or the integration of different aspects of the self.",
    "journey": "Dreams of a journey may symbolize personal growth, exploration, adventure, or the pursuit of self-discovery and enlightenment.",
    "adventure": "Dreams of an adventure may represent excitement, challenge, exploration, or the pursuit of new experiences and opportunities.",
    "success": "Dreams of success may symbolize achievement, fulfillment, recognition, or the realization of one's goals and aspirations.",
    "failure": "Dreams of failure may represent disappointment, setback, frustration, or the fear of not meeting expectations or goals.",
    "escape": "Dreams of escape may symbolize avoidance, evasion, liberation, or the desire to break free from constraints or limitations.",
    "struggle": "Dreams of struggle may represent conflict, resistance, challenge, or the need to overcome obstacles and adversity.",
    "victory": "Dreams of victory may symbolize triumph, success, accomplishment, or the ability to overcome challenges and emerge victorious.",
    "defeat": "Dreams of defeat may represent failure, setback, disappointment, or the fear of losing in a competitive situation or endeavor.",
    "discovery": "Dreams of discovery may symbolize revelation, insight, awareness, or the uncovering of hidden truths or secrets.",
    "surprise": "Dreams of a surprise may represent unexpected events, revelations, or developments that catch the dreamer off guard.",
    "transformation": "Dreams of transformation may symbolize change, growth, renewal, or the evolution of the self and one's life path.",
    "miracle": "Dreams of a miracle may represent hope, faith, divine intervention, or the manifestation of extraordinary events or blessings.",
    "magic": "Dreams of magic may symbolize enchantment, wonder, mystery, or the belief in supernatural forces or abilities.",
    "friendship": "Dreams of friendship may represent companionship, support, loyalty, or the importance of social connections and relationships.",
    "romance": "Dreams of romance may symbolize love, passion, desire, or the pursuit of intimate connection and emotional fulfillment.",
    "betrayal": "Dreams of betrayal may represent deceit, disloyalty, distrust, or the fear of being let down or deceived by others.",
    "trust": "Dreams of trust may symbolize confidence, security, reliability, or the importance of having faith in oneself and others.",
    "doubt": "Dreams of doubt may represent uncertainty, skepticism, hesitation, or the need to question one's beliefs, choices, or decisions.",
    "forgiveness": "Dreams of forgiveness may symbolize reconciliation, healing, release, or the willingness to let go of resentment and move forward.",
    "regret": "Dreams of regret may represent guilt, remorse, sorrow, or the wish to undo past mistakes or missed opportunities.",
    "hope": "Dreams of hope may symbolize optimism, faith, resilience, or the belief in positive outcomes and brighter days ahead.",
    "fear": "Dreams of fear may represent anxiety, insecurity, vulnerability, or the need to confront and overcome inner demons or phobias.",
    "courage": "Dreams of courage may symbolize bravery, strength, determination, or the willingness to face challenges and overcome obstacles.",
    "inspiration": "Dreams of inspiration may represent creativity, motivation, insight, or the spark of genius that ignites new ideas and possibilities.",
    "vision": "Dreams of a vision may symbolize foresight, intuition, clarity, or the ability to see beyond the present moment and envision the future.",
    "imagination": "Dreams of imagination may represent creativity, innovation, fantasy, or the power of the mind to conjure new worlds and possibilities.",
    "revelation": "Dreams of revelation may symbolize enlightenment, revelation, epiphany, or the unveiling of hidden truths or insights.",
    "intuition": "Dreams of intuition may represent instinct, inner guidance, wisdom, or the ability to trust one's gut feelings and inner knowing.",
    "reflection": "Dreams of reflection may symbolize introspection, contemplation, self-examination, or the process of looking inward for answers and understanding.",
    "resilience": "Dreams of resilience may represent strength, adaptability, perseverance, or the ability to bounce back from adversity and challenges.",
    "surrender": "Dreams of surrender may symbolize acceptance, release, surrender, or the willingness to let go of control and trust in the flow of life.",
    "acceptance": "Dreams of acceptance may represent peace, contentment, fulfillment, or the ability to embrace oneself and others without judgment or reservation.",
    "rejection": "Dreams of rejection may symbolize feelings of abandonment, unworthiness, exclusion, or the fear of being cast aside or overlooked by others.",
    "loneliness": "Dreams of loneliness may represent isolation, alienation, solitude, or the need for connection and companionship with others.",
    "community": "Dreams of community may symbolize unity, belonging, support, or the importance of social connections and shared experiences.",
    "belonging": "Dreams of belonging may represent acceptance, inclusion, validation, or the desire to be a part of something greater than oneself.",
    "isolation": "Dreams of isolation may symbolize loneliness, separation, disconnection, or the feeling of being cut off from others or one's surroundings.",
    "connectedness": "Dreams of connectedness may represent unity, harmony, integration, or the recognition of the interconnectedness of all things.",
    "alienation": "Dreams of alienation may symbolize estrangement, detachment, otherness, or the feeling of being an outsider or outcast in one's environment.",
    "growth": "Dreams of growth may represent development, expansion, evolution, or the process of becoming more fully oneself and realizing one's potential.",
    "stagnation": "Dreams of stagnation may symbolize inertia, complacency, stagnation, or the feeling of being stuck or unable to move forward in life.",
    "change": "Dreams of change may represent transformation, evolution, renewal, or the need to adapt to new circumstances or embrace new opportunities.",
    "stability": "Dreams of stability may symbolize security, consistency, reliability, or the feeling of being grounded and anchored in one's life and surroundings.",
    "uncertainty": "Dreams of uncertainty may represent doubt, ambiguity, unpredictability, or the feeling of being adrift or lacking clear direction in life.",
    "security": "Dreams of security may symbolize safety, protection, comfort, or the feeling of being secure and well-supported in one's environment.",
    "vulnerability": "Dreams of vulnerability may represent exposure, fragility, openness, or the feeling of being susceptible to harm or emotional injury.",
    "comfort": "Dreams of comfort may symbolize reassurance, solace, peace, or the feeling of being nurtured and cared for in times of distress or difficulty.",
    "discomfort": "Dreams of discomfort may represent unease, agitation, tension, or the feeling of being out of place or ill at ease in one's environment.",
    "restlessness": "Dreams of restlessness may symbolize agitation, impatience, discontent, or the feeling of being unsettled or unable to find peace or satisfaction.",
    "relaxation": "Dreams of relaxation may represent tranquility, serenity, calmness, or the feeling of being at ease and free from stress or tension.",
    "tension": "Dreams of tension may symbolize conflict, strain, pressure, or the feeling of being stretched to one's limits or on edge in waking life.",
    "peace": "Dreams of peace may represent harmony, serenity, tranquility, or the feeling of being at peace with oneself and the world around us.",
    "chaos": "Dreams of chaos may symbolize disorder, confusion, upheaval, or the feeling of being overwhelmed by conflicting emotions or external events.",
    "order": "Dreams of order may represent structure, organization, clarity, or the need to impose control and create stability in one's life and surroundings.",
    "calmness": "Dreams of calmness may symbolize composure, equanimity, poise, or the feeling of being centered and grounded in the midst of chaos or turmoil.",
    "storm": "Dreams of a storm may symbolize turmoil, upheaval, crisis, or the need to confront and weather difficult or challenging situations in life.",
    "sunshine": "Dreams of sunshine may represent warmth, light, vitality, or the feeling of being energized, uplifted, and inspired by the beauty of life.",
    "clouds": "Dreams of clouds may symbolize uncertainty, ambiguity, or the feeling of being overshadowed by doubt, fear, or worry in waking life.",
    "rain": "Dreams of rain may represent cleansing, renewal, purification, or the need to wash away negative emotions or experiences and start afresh.",
    "rainbow": "Dreams of a rainbow may symbolize hope, promise, beauty, or the feeling of being blessed and surrounded by divine protection and guidance.",
    "thunder": "Dreams of thunder may represent power, authority, awakening, or the need to pay attention to important messages or warnings from the unconscious mind.",
    "lightning": "Dreams of lightning may symbolize sudden insight, inspiration, revelation, or the feeling of being struck by a powerful force or realization.",
    "fog": "Dreams of fog may represent confusion, obscurity, or the feeling of being lost or disoriented in one's thoughts or perceptions.",
    "mist": "Dreams of mist may symbolize mystery, illusion, or the feeling of being veiled or obscured from seeing things clearly in waking life.",
    "wind": "Dreams of wind may represent change, movement, transition, or the feeling of being carried along by the currents of life and destiny.",
    "breeze": "Dreams of a breeze may symbolize refreshment, rejuvenation, or the feeling of being gently caressed by the subtle forces of nature and spirit.",
    "hurricane": "Dreams of a hurricane may represent chaos, destruction, upheaval, or the feeling of being overwhelmed by powerful forces beyond one's control.",
    "tornado": "Dreams of a tornado may symbolize sudden change, destruction, upheaval, or the feeling of being caught up in a whirlwind of events or emotions.",
    "earthquake": "Dreams of an earthquake may represent upheaval, transformation, awakening, or the need to shake up one's life and let go of old patterns.",
    "tsunami": "Dreams of a tsunami may symbolize overwhelming emotions, crisis, destruction, or the feeling of being engulfed by a tidal wave of change or adversity.",
    "volcano": "Dreams of a volcano may represent eruption, release, transformation, or the feeling of being on the verge of a powerful breakthrough or catharsis.",
    "avalanche": "Dreams of an avalanche may symbolize overwhelm, danger, crisis, or the feeling of being buried under an avalanche of responsibilities or emotions.",
    "fire": "Dreams of fire may represent passion, desire, purification, or the feeling of being consumed by intense emotions or creative energy.",
    "ice": "Dreams of ice may symbolize coldness, rigidity, stagnation, or the feeling of being frozen or unable to express oneself freely or authentically.",
    "water": "Dreams of water may represent emotions, intuition, fluidity, or the subconscious mind, and the need to go with the flow of life and trust one's instincts.",
    "earth": "Dreams of earth may symbolize grounding, stability, fertility, or the need to connect with the physical world and honor one's roots and heritage.",
    "air": "Dreams of air may represent intellect, communication, freedom, or the realm of thought and ideas, and the need to stay open-minded and flexible.",
    "fire": "Dreams of fire may represent passion, energy, transformation, or the destructive power of anger, and the need to harness one's inner fire wisely.",
    "spirit": "Dreams of spirit may represent spirituality, connection, transcendence, or the feeling of being guided or protected by higher forces or divine beings.",
    "soul": "Dreams of the soul may symbolize essence, authenticity, integrity, or the innermost core of one's being, and the need to honor and nurture one's true self.",
    "god": "Dreams of God may represent divinity, higher power, enlightenment, or the feeling of being connected to a source of love, wisdom, and grace.",
    "goddess": "Dreams of a goddess may symbolize femininity, creativity, nurturing, or the archetypal feminine energy and the need to embrace one's feminine qualities.",
    "angel": "Dreams of an angel may represent protection, guidance, inspiration, or the feeling of being watched over and cared for by benevolent forces.",
    "demon": "Dreams of a demon may symbolize fear, temptation, negativity, or the shadow aspect of the self, and the need to confront and integrate one's dark side.",
    "monster": "Dreams of a monster may represent fear, insecurity, or the feeling of being threatened by unknown or uncontrollable forces in waking life.",
    "hero": "Dreams of a hero may symbolize courage, strength, nobility, or the feeling of being empowered to overcome obstacles and achieve greatness.",
    "villain": "Dreams of a villain may represent conflict, opposition, or the feeling of being undermined or threatened by others in waking life.",
    "wizard": "Dreams of a wizard may symbolize wisdom, knowledge, magic, or the feeling of being guided by inner intuition and psychic insight.",
    "witch": "Dreams of a witch may represent manipulation, deception, or the feeling of being controlled or influenced by negative forces or toxic people.",
    "king": "Dreams of a king may symbolize authority, power, leadership, or the feeling of being in control and taking charge of one's destiny.",
    "queen": "Dreams of a queen may represent sovereignty, majesty, femininity, or the feeling of being honored and respected for one's grace and wisdom.",
    "prince": "Dreams of a prince may symbolize youth, potential, innocence, or the emergence of new ideas and opportunities in waking life.",
    "princess": "Dreams of a princess may represent purity, innocence, beauty, or the feeling of being cherished and protected by others.",
    "knight": "Dreams of a knight may symbolize chivalry, honor, courage, or the feeling of being protected and defended by a loyal and valiant ally.",
    "dragon": "Dreams of a dragon may represent fear, danger, or the feeling of being challenged by powerful or overwhelming forces in waking life.",
    "unicorn": "Dreams of a unicorn may symbolize purity, magic, rarity, or the feeling of being blessed with special gifts or talents.",
    "phoenix": "Dreams of a phoenix may represent rebirth, renewal, transformation, or the feeling of rising from the ashes and starting anew after a period of hardship.",
    "mermaid": "Dreams of a mermaid may symbolize fantasy, allure, mystery, or the feeling of being drawn to the depths of the unconscious mind and the mysteries of the sea.",
    "centaur": "Dreams of a centaur may represent duality, balance, integration, or the feeling of being caught between two worlds or conflicting desires.",
    "sphinx": "Dreams of a sphinx may symbolize mystery, riddles, or the feeling of being challenged to solve a difficult problem or unravel a hidden truth.",
    "minotaur": "Dreams of a minotaur may represent rage, aggression, or the feeling of being trapped in a labyrinth of confusion or inner conflict.",
    "pegasus": "Dreams of a pegasus may symbolize freedom, inspiration, or the feeling of being lifted up and carried to new heights by the power of imagination and dreams."
    #went
    #add other word will same meaning
    }
    
    # Preprocess user input to extract relevant keywords
    input_keywords = preprocess_input(user_input)

    # Search for matching dream interpretation
    interpretation = "I'm sorry, I couldn't determine the type of dream, give more details"
    for keyword, meaning in dream_interpretations.items():
        # Use regular expressions to find keyword in user input
        pattern = re.compile(r'\b' + re.escape(keyword) + r'\b', re.IGNORECASE)
        if any(pattern.search(word) for word in input_keywords):
            interpretation = meaning
            break

    return interpretation


def dream_interpreter(input_text):
    return interpretdream(input_text)

def chat(a):
        interpretation = dream_interpreter(a)
        return interpretation

def interpret_dream(request):
    if request.method == 'POST':
        dream_input = request.POST.get('dream', '')  # Get the dream input from the request
        interpretations = chat(dream_input)  # Pass the dream input to the chat function
        return render(request, 'dream.html', {'interpretation': interpretations})  # Use 'interpretation' instead of 'interpretations'
    else:
        return HttpResponse('Method not allowed')
    


















from django.shortcuts import render
from django.http import HttpResponse
import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from keras.models import load_model

# Load NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

# Initialize WordNet Lemmatizer
lemmatizer = WordNetLemmatizer()

# Load intents data
intents = json.loads(open(r'C:\Users\saseedharan\aisleep\aisleep\login\intents.json').read())


# Load pickle files
directory = 'C:/Users/saseedharan/aisleep/aisleep/login/'

# Load words.pkl
with open(os.path.join(directory, 'words.pkl'), 'rb') as file:
    words = pickle.load(file)

# Load classes.pkl

with open(os.path.join(directory, 'classes.pkl'), 'rb') as file:
    classes = pickle.load(file)

# Load the pre-trained model
model = load_model(os.path.join(directory, 'chatbot_model.h5'))

# Define function to clean up sentence
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

# Define function to create bag of words
def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

# Define function to predict class
def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

# Define function to get response
def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

# Define your view function
def chatbot(request):
    if request.method == 'POST':
        # Get user input from form
        user_message = request.POST.get('user_input', '')  # Changed 'message' to 'user_input'
        
        # Add the user's message to the conversation history
        messages = [
            {'user': True, 'content': user_message},
        ]
        
        # Predict intent and get response
        ints = predict_class(user_message)
        bot_response = get_response(ints, intents)
        
        # Add the bot's response to the conversation history
        messages.append({'user': False, 'content': bot_response})
        
        # Pass the conversation history to the template
        return render(request, 'chatbot.html', {'messages': messages})
    else:
        # Render initial chatbot page without any messages
        return render(request, 'chatbot.html', {})


from django.shortcuts import render

def chatbot_process(request):
    if request.method == 'POST':
        # Assuming you have retrieved or generated new chat messages
        messages = [
            {'user': True, 'content': 'User message'},
            {'user': False, 'content': 'Bot response'}
            # Add more chat messages as needed
        ]
        return render(request, 'chatbot.html', {'messages': messages})
    else:
        # Render initial chatbot page if it's not a POST request
        return render(request, 'chatbot.html', {})
