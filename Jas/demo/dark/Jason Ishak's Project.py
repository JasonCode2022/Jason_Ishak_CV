choices = {
            "fruits" : ['Apple', 'apricot', 'avocado', 'banana', 'berry', 'blackberry', 'blood orange', 'blueberry', 'boysenberry', 'breadfruit', 'cantaloupe', 'cherry', 'citron', 'citrus', 'coconut', 'crabapple', 'cranberry', 'current', 'date', 'dragon fruit', 'durian', 'elderberry', 'fig', 'grape', 'grapefruit', 'guava', 'honeydew', 'jackfruit', 'kiwi', 'kumquat', 'lemon', 'lime', 'lingonberry', 'loquat', 'lychee', 'mandarin orange', 'mango', 'marionberry', 'melon', 'mulberry', 'nectarine', 'orange', 'papaya', 'passion fruit', 'peach', 'pear', 'persimmon', 'pineapple', 'plantain', 'plum', 'pluot', 'pomegranate', 'pomelo', 'prune', 'quince', 'raisin', 'raspberry', 'star fruit', 'strawberry', 'tangelo', 'tangerine', 'ugli fruit', 'watermelon'],
            "vegetables" : ['alfalfa sprouts', 'azuki beans ', 'bean sprouts', 'black beans', 'black-eyed peas', 'borlotti bean', 'broad beans', 'chickpeas', 'green beans', 'kidney beans', 'lentils', 'lima beans ', 'mung beans', 'navy beans', 'peanuts', 'pinto beans', 'runner beans', 'split peas', 'soy beans', 'peas mange tout  ', 'broccoflower', 'broccoli ', 'brussels sprouts', 'cabbage', 'kohlrabi', 'Savoy cabbage', 'red cabbage', 'cauliflower', 'celery', 'endive', 'fiddleheads', 'frisee', 'fennel', 'greens bok choy', 'chard ', 'collard greens', 'kale', 'mustard greens', 'herbs', 'anise', 'basil', 'caraway', 'coriander', 'chamomile', 'daikon', 'dill', 'fennel', 'lavender', 'cymbopogon', 'marjoram', 'oregano', 'parsley', 'rosemary', 'thyme', 'lettuce', 'arugula', 'mushroomsnettles', 'New Zealand spinach', 'okra', 'onions', 'chives', 'garlic', 'leek', 'onion', 'shallot', 'scallion ', 'peppers', 'bell pepper', 'chili pepper', 'jalapeño', 'habanero', 'paprika', 'tabasco pepper', 'cayenne pepper', 'radicchio', 'rhubarb', 'root vegetables', 'beetroot ', 'mangel-wurzel', 'carrot', 'celeriac', 'corms', 'eddoe', 'konjac', 'taro', 'water', 'hestnut', 'ginger', 'parsnip', 'rutabaga', 'radish', 'wasabi', 'horseradish', 'daikon  ', 'tubers', 'jicama', 'jerusalem artichoke', 'potato', 'sweet potato', 'yam', 'turnip', 'salsify', 'skirret', 'sweetcorn', 'topinambur', 'acorn squash', 'bitter melonbutternut squash', 'banana squash', 'courgette ', 'cucumber ', 'delicata', 'gem squash', 'hubbard squash', 'marrow ', 'spaghetti squash', 'zucchini'],
            "countries" : ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua&Deps', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia', 'Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Rep', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Congo Democratic Rep', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland Republic', 'Israel', 'Italy', 'Ivory Coast', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea North', 'Korea South', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', ' Burma', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russian Federation', 'Rwanda', 'St Kitts & Nevis', 'St Lucia', 'Saint Vincent & the Grenadines', 'Samoa', 'San Marino', 'Sao Tome & Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia','South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad & Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'],
           }

pool = ["fruits","vegetables","countries"]
import random
r = random.choice(pool).lower()
rr = random.choice(choices[r]).lower()



# print(r)
# print(rr)


print("The game is about guessing an unknown number of letters that forms a <<< Noun >>> N.B.:(could be composed of one or more words).")
a = input("If you wish to proceed type 'Yes' else press 'No'>>>>>: ")
g2=0

while len(rr)>0:
    if a.lower() == "yes":
        for i in range(7, 0, -1):
            print("  " * (7 - i), end="")
            print("* " * (2 * i - 1))
        print("The <<< Noun >>> you need to guess is composed of", len(rr), "letters.")

        c = 1
        while c <= 2:
            print(f"Guess the category of the <<< Noun >>> between Countries, Fruits and Vegetables. You have {3-c} trial(s) .")
            g1 = input(f"Enter guess: ")
            if g1 != r and c == 1 :
                print( f"Wrong guess ,you have {2 - c} trial: ")

            if g1 != r and c == 2 :
                print(f"You lost, the categorie was: ",r)
                break

            if g1 == r:
                print("Right guess")

                for j in range(5, 0, -1):
                    print("  " * (5 - j), end="")
                    print("* " * (2 * j - 1))

                def count_words(s):
                    return len(s.split())
                w = str(rr)
                count_words(w)

                if int(count_words(w)) < 2:
                     print("The <<< Noun >>> contains 1 word")
                     print("You have trials equal to rounded down half the length of the <<< Noun >>>, so you have",
                           {(len(rr) // 2)},  "trials")
                     f = 0
                     while f in range(0,(len(rr)//2)):
                         g2 = input("Enter the your guess about the <<< Noun >>>: ").lower()

                         if g2 != rr:
                             for j in range(3, 0, -1):
                                 print("  " * (4 - j), end="")
                                 print("* " * (2 * j - 1))
                             print(f"Wrong guess you have {(len(rr) // 2) - (f + 1)} trial(s)")
                         f += 1
                         if g2 != rr and ((len(rr) // 2) - (f)) == 0:
                            print("You lost the <<< Noun >>> was: ",rr)
                            break

                         if g2 == rr:
                             print("!!!### Congratulations ###!!!")
                             print(" "*9," You Won ")
                             break

                else :
                    print("The <<< Noun >>> contains 2 words")
                    print("You have trials equal to rounded down half the length of the <<< Noun >>>, so you have",
                          {(len(rr) // 2)}, "trials")
                    f = 0
                    while f in range(0, (len(rr) // 2)):
                        g2 = input("Enter the your guess about the <<< Noun >>>: ").lower()

                        if g2 != rr:
                            for j in range(3, 0, -1):
                                print("  " * (4 - j), end="")
                                print("* " * (2 * j - 1))
                            print(f"Wrong guess you have {(len(rr) // 2) - (f + 1)} trial(s)")
                        f += 1
                        if g2 != rr and ((len(rr) // 2) - (f)) == 0:
                            print("You lost the <<< Noun >>> was: ", rr)
                            break

                        if g2 == rr:
                            print("!!!### Congratulations ###!!!")
                            print(" " * 9, " You Won ")
                            break

                break
            c += 1

        break

    if a.lower() == "no":
        print("Well I know it's not Dota 2 but at least try my project ;)")
        break

    if g2 == rr or a.lower() != "yes" or "no":
        print("Don't play that game with me, haha I thought you might do that..")
        break










