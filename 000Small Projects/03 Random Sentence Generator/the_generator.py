import random


class Generator:

    def __init__(self, data_dict: dict):
        self.data_dict = data_dict

    def generate_random_name(self):
        random_name = random.choice(self.data_dict['names'])
        return random_name

    def generate_random_place(self):
        random_place = random.choice(self.data_dict['places'])
        return random_place

    def generate_random_verb(self):
        random_verb = random.choice(self.data_dict['verbs'])
        return random_verb

    def generate_random_noun(self):
        random_noun = random.choice(self.data_dict['nouns'])
        return random_noun

    def generate_random_adverb(self):
        random_adverb = random.choice(self.data_dict['adverbs'])
        return random_adverb

    def generate_random_detail(self):
        random_detail = random.choice(self.data_dict['details'])
        return random_detail

    def __repr__(self):
        name = self.generate_random_name()
        place = self.generate_random_place()
        adverb = self.generate_random_adverb()
        verb = self.generate_random_verb()
        noun = self.generate_random_noun()
        detail = self.generate_random_detail()
        generated_sentence = f'{name} from {place} {adverb} {verb} {noun} {detail}!'
        return generated_sentence


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
    generator = Generator(data)
    print(generator)
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
