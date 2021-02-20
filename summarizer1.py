
import en_core_web_sm
from string import punctuation
nlp = en_core_web_sm.load()
from heapq import nlargest


def summarize(rawtext):
    doc = nlp(rawtext)
    tokens = [token.text for token in doc]

    stopwords = ["a", "about", "above", "after", "again", "against", "ain", "all", "am", "an", "and", "any", "are",
                 "aren",
                 "aren't", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both",
                 "but", "by",
                 "can", "couldn", "couldn't", "d", "did", "didn", "didn't", "do", "does", "doesn", "doesn't",
                 "doing",
                 "don", "don't", "down", "during", "each", "few", "for", "from", "further", "had", "hadn", "hadn't",
                 "has",
                 "hasn", "hasn't", "have", "haven", "haven't", "having", "he", "her", "here", "hers", "herself",
                 "him",
                 "himself", "his", "how", "i", "if", "in", "into", "is", "isn", "isn't", "it", "it's", "its",
                 "itself",
                 "just", "ll", "m", "ma", "me", "mightn", "mightn't", "more", "most", "mustn", "mustn't", "my",
                 "myself",
                 "needn", "needn't", "no", "nor", "not", "now", "o", "of", "off", "on", "once", "only", "or",
                 "other",
                 "our", "ours", "ourselves", "out", "over", "own", "re", "s", "same", "shan", "shan't", "she",
                 "she's",
                 "should", "should've", "shouldn", "shouldn't", "so", "some", "such", "t", "than", "that",
                 "that'll", "the",
                 "their", "theirs", "them", "themselves", "then", "there", "these", "they", "this", "those",
                 "through",
                 "to", "too", "under", "until", "up", "ve", "very", "was", "wasn", "wasn't", "we", "were", "weren",
                 "weren't", "what", "when", "where", "which", "while", "who", "whom", "why", "will", "with", "won",
                 "won't",
                 "wouldn", "wouldn't", "y", "you", "you'd", "you'll", "you're", "you've", "your", "yours",
                 "yourself",
                 "yourselves", "could", "he'd", "he'll", "he's", "here's", "how's", "i'd", "i'll", "i'm", "i've",
                 "let's",
                 "ought", "she'd", "she'll", "that's", "there's", "they'd", "they'll", "they're", "they've", "we'd",
                 "we'll", "we're", "we've", "what's", "when's", "where's", "who's", "why's", "would", "able",
                 "abst",
                 "accordance", "according", "accordingly", "across", "act", "actually", "added", "adj", "affected",
                 "affecting", "affects", "afterwards", "ah", "almost", "alone", "along", "already", "also",
                 "although",
                 "always", "among", "amongst", "announce", "another", "anybody", "anyhow", "anymore", "anyone",
                 "anything",
                 "anyway", "anyways", "anywhere", "apparently", "approximately", "arent", "arise", "around",
                 "aside", "ask",
                 "asking", "auth", "available", "away", "awfully", "b", "back", "became", "become", "becomes",
                 "becoming",
                 "beforehand", "begin", "beginning", "beginnings", "begins", "behind", "believe", "beside",
                 "besides",
                 "beyond", "biol", "brief", "briefly", "c", "ca", "came", "cannot", "can't", "cause", "causes",
                 "certain",
                 "certainly", "co", "com", "come", "comes", "contain", "containing", "contains", "couldnt", "date",
                 "different", "done", "downwards", "due", "e", "ed", "edu", "effect", "eg", "eight", "eighty",
                 "either",
                 "else", "elsewhere", "end", "ending", "enough", "especially", "et", "etc", "even", "ever", "every",
                 "everybody", "everyone", "everything", "everywhere", "ex", "except", "f", "far", "ff", "fifth",
                 "first",
                 "five", "fix", "followed", "following", "follows", "former", "formerly", "forth", "found", "four",
                 "furthermore", "g", "gave", "get", "gets", "getting", "give", "given", "gives", "giving", "go",
                 "goes",
                 "gone", "got", "gotten", "h", "happens", "hardly", "hed", "hence", "hereafter", "hereby", "herein",
                 "heres", "hereupon", "hes", "hi", "hid", "hither", "home", "howbeit", "however", "hundred", "id",
                 "ie",
                 "im", "immediate", "immediately", "importance", "important", "inc", "indeed", "index",
                 "information",
                 "instead", "invention", "inward", "itd", "it'll", "j", "k", "keep", "keeps", "kept", "kg", "km",
                 "know",
                 "known", "knows", "l", "largely", "last", "lately", "later", "latter", "latterly", "least", "less",
                 "lest",
                 "let", "lets", "like", "liked", "likely", "line", "little", "'ll", "look", "looking", "looks",
                 "ltd",
                 "made", "mainly", "make", "makes", "many", "may", "maybe", "mean", "means", "meantime",
                 "meanwhile",
                 "merely", "mg", "might", "million", "miss", "ml", "moreover", "mostly", "mr", "mrs", "much", "mug",
                 "must",
                 "n", "na", "name", "namely", "nay", "nd", "near", "nearly", "necessarily", "necessary", "need",
                 "needs",
                 "neither", "never", "nevertheless", "new", "next", "nine", "ninety", "nobody", "non", "none",
                 "nonetheless", "noone", "normally", "nos", "noted", "nothing", "nowhere", "obtain", "obtained",
                 "obviously", "often", "oh", "ok", "okay", "old", "omitted", "one", "ones", "onto", "ord", "others",
                 "otherwise", "outside", "overall", "owing", "p", "page", "pages", "part", "particular",
                 "particularly",
                 "past", "per", "perhaps", "placed", "please", "plus", "poorly", "possible", "possibly",
                 "potentially",
                 "pp", "predominantly", "present", "previously", "primarily", "probably", "promptly", "proud",
                 "provides",
                 "put", "q", "que", "quickly", "quite", "qv", "r", "ran", "rather", "rd", "readily", "really",
                 "recent",
                 "recently", "ref", "refs", "regarding", "regardless", "regards", "related", "relatively",
                 "research",
                 "respectively", "resulted", "resulting", "results", "right", "run", "said", "saw", "say", "saying",
                 "says",
                 "sec", "section", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self", "selves",
                 "sent",
                 "seven", "several", "shall", "shed", "shes", "show", "showed", "shown", "showns", "shows",
                 "significant",
                 "significantly", "similar", "similarly", "since", "six", "slightly", "somebody", "somehow",
                 "someone",
                 "somethan", "something", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry",
                 "specifically",
                 "specified", "specify", "specifying", "still", "stop", "strongly", "sub", "substantially",
                 "successfully",
                 "sufficiently", "suggest", "sup", "sure", "take", "taken", "taking", "tell", "tends", "th",
                 "thank",
                 "thanks", "thanx", "thats", "that've", "thence", "thereafter", "thereby", "thered", "therefore",
                 "therein",
                 "there'll", "thereof", "therere", "theres", "thereto", "thereupon", "there've", "theyd", "theyre",
                 "think",
                 "thou", "though", "thoughh", "thousand", "throug", "throughout", "thru", "thus", "til", "tip",
                 "together",
                 "took", "toward", "towards", "tried", "tries", "truly", "try", "trying", "ts", "twice", "two", "u",
                 "un",
                 "unfortunately", "unless", "unlike", "unlikely", "unto", "upon", "ups", "us", "use", "used",
                 "useful",
                 "usefully", "usefulness", "uses", "using", "usually", "v", "value", "various", "'ve", "via", "viz",
                 "vol",
                 "vols", "vs", "w", "want", "wants", "wasnt", "way", "wed", "welcome", "went", "werent", "whatever",
                 "what'll", "whats", "whence", "whenever", "whereafter", "whereas", "whereby", "wherein", "wheres",
                 "whereupon", "wherever", "whether", "whim", "whither", "whod", "whoever", "whole", "who'll",
                 "whomever",
                 "whos", "whose", "widely", "willing", "wish", "within", "without", "wont", "words", "world",
                 "wouldnt",
                 "www", "x", "yes", "yet", "youd", "youre", "z", "zero", "a's", "ain't", "allow", "allows", "apart",
                 "appear", "appreciate", "appropriate", "associated", "best", "better", "c'mon", "c's", "cant",
                 "changes",
                 "clearly", "concerning", "consequently", "consider", "considering", "corresponding", "course",
                 "currently",
                 "definitely", "described", "despite", "entirely", "exactly", "example", "going", "greetings",
                 "hello",
                 "help", "hopefully", "ignored", "inasmuch", "indicate", "indicated", "indicates", "inner",
                 "insofar",
                 "it'd", "keep", "keeps", "novel", "presumably", "reasonably", "second", "secondly", "sensible",
                 "serious",
                 "seriously", "sure", "t's", "third", "thorough", "thoroughly", "three", "well", "wonder"]

    # punctuation = punctuation + '\n'

    word_frequencies = {}
    for word in doc:
        if word.text.lower() not in stopwords:
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1

    max_frequency = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word] / max_frequency

    sentence_tokens = [sent for sent in doc.sents]

    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]

    select_length = int(len(sentence_tokens) * 0.3)

    summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)

    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)
    print('nothing',summary)
    return summary


# raw_text='While we got independence from British rule on August 15, 1947, our country was still lacking a concrete constitution. Moreover, India also did not have any experts and political powers which would help in the functioning of the state affairs smoothly.  Up until then, the 1935 Government of India Act was basically modified in order to govern, however, that act was more bent towards the colonial rule. Therefore, there was a dire need to form an exclusive constitution that would reflect all that India stands for.  # Thus, Dr. B.R. Ambedkar led a constitutional drafting committee on August 28, 1947.  After drafting, it was presented to the Constituent Assembly by the same committee on November 4, 1947. This whole procedure was very elaborate and took up to 166 days to complete. Moreover, the committee organized sessions were kept open to the public.  # No matter the challenges and hardships, our constitutional committee left no stone unturned to include rights for all. It aimed to create the perfect balance so all citizens of the country could enjoy equal rights pertaining to their religions, culture, caste, sex, creed and more. At last, they presented the official Indian constitution to the country on January 26, 1950.  # Moreover, the first session of the India Parliament was also conducted on this day. In addition to that, 26th January also witnessed the swearing-in of India’s first president, Dr. Rajendra Prasad. Thus, this day is very important as it marks the end of the British rule and birth of India as a Republic State.'
# summarize(raw_text)