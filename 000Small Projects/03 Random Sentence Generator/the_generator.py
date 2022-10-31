import random


class Random:
    def __init__(self, some_list: list):
        self.some_list = some_list

    def random_choise(self):
        the_choosen_one = random.choice(self.some_list)
        return the_choosen_one

    def __repr__(self):
        random_word = self.random_choise()
        return random_word


class WordsGenerator:

    def __init__(self, data_dict):
        self.data_dict = data_dict

    def generate_random_name(self):
        names_list = self.data_dict['names']
        random_name = Random(names_list)
        return random_name

    def generate_random_place(self):
        places_list = self.data_dict['places']
        random_place = Random(places_list)
        return random_place

    def generate_random_verb(self):
        verbs_list = self.data_dict['verbs']
        random_verb = Random(verbs_list)
        return random_verb

    def generate_random_noun(self):
        nouns_list = self.data_dict['nouns']
        random_noun = Random(nouns_list)
        return random_noun

    def generate_random_adverb(self):
        adverbs_ist = self.data_dict['adverbs']
        random_adverb = Random(adverbs_ist)
        return f'{random_adverb}'

    def generate_random_detail(self):
        details_list = self.data_dict['details']
        random_detail = Random(details_list)
        return random_detail


class Concatenator:

    def __init__(self, some_dict):
        self.some_dict = some_dict

    def who_from_where(self):
        generator = WordsGenerator(self.some_dict)
        name = generator.generate_random_name()
        place = generator.generate_random_place()
        return f"{name} from {place}"

    def action(self):
        generator = WordsGenerator(self.some_dict)
        adverb = generator.generate_random_adverb()
        verb = generator.generate_random_verb()
        noun = generator.generate_random_noun()
        return f'{adverb} {verb} {noun}'

    def detail(self):
        generator = WordsGenerator(self.some_dict)
        detail = generator.generate_random_detail()
        return f'{detail}'

    def __repr__(self):
        first_part = self.who_from_where()
        second_part = self.action()
        third_part = self.detail()
        return first_part + " " + second_part + " " + third_part + "."


data = {'names': ['Felis', 'Vicky', 'Jeil', 'Ronda', 'Marsha',
                  'Su', 'Sheril', 'Janis', 'Wanda', 'Glenda',
                  'Jian', 'Marcia', 'Lesly', 'Dolores', 'Lynda',
                  'Roberta', 'Moriin', 'Jill', 'Debra', 'Key',
                  'Bill', 'Cheryl', 'Jaky', 'Katy', 'Marin'],
        'places': ['Sofia', 'Plovdiv', 'Varna', 'Burgas', 'Ruse',
                   'Stara Zagora', 'Pleven', 'Sliven', 'Dobrich', 'Shumen',
                   'Pernik', 'Yambol', 'Haskovo', 'Pazardjik', 'Blagoevgrad',
                   'Vratca', 'Gabrovo', 'Veliko Tarnovo', 'Vidin', 'Kazanlak',
                   'Asenovgrad', 'Kiustendil', 'Montana', 'Dimitrovgrad', 'Kardjali'],
        'verbs': ['ask', 'believe', 'call', 'change', 'continue',
                  'create', 'follow', 'happen', 'help', 'live',
                  'look', 'move', 'need', 'sing', 'play',
                  'remember', 'seem', 'stop', 'try', 'use',
                  'walk', 'want', 'watch', 'work', 'study'],
        'nouns': ['bike', 'car', 'bus', 'plane', 'popcorn',
                  'cake', 'bread', 'sausage', 'apple', 'banana',
                  'pineapple', 'butter', 'screwdriver', 'phone', 'knife',
                  'bubblegum', 'chocolate', 'steak', 'dish', 'pan',
                  'ashtray', 'tank', 'bed', 'sofa', 'chair'],
        'adverbs': ['extremely', 'fatally', 'fast', 'softly', 'slowly',
                    'carefully', 'suddenly', 'powerfully', 'happily', 'truly',
                    'deeply', 'madly', 'loyalty', 'often', 'usually',
                    'easily', 'only', 'kindly', 'rarely', 'gently',
                    'wisely', 'lazily', 'quickly', 'suddenly', 'hourly'],
        'details': ['near home', 'near river', 'in park', 'in pool', 'in home',
                    'at restaurant', 'under shower', 'in kitchen', 'on the street', 'in bar',
                    'in school', 'in taxi', 'near to airport', 'around the mall', 'in the cinema',
                    'in the park', 'on the beach', 'in the sea', 'in stairs', 'outside the house',
                    'in disco club', 'on concert', 'to the theater', 'in sauna', 'on roof']}

print('Hello this is random sentence generator!')

close = False
while True:
    random_sentence = Concatenator(data)
    print(random_sentence)
    print('Press [Enter] to generate new sentence, or type "Exit" for closing program.')
    command = input()
    if command == 'Exit':
        close = True
        break
    elif command != 'Exit' and command:
        valid = False
        while valid == False:
            if command != 'Exit' and command:
                print('Wrong input!')
                print('Please press [Enter] to continue or type "Exit" to close program!')
            elif command != 'Exit' and not command:
                valid = True
                break
            command = input()
        continue
    else:
        continue

if close:
    print('Successfully closed program.')
    print('GOOD BYE!')
