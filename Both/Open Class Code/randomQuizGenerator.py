import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 
   'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate the 35 quizes
for quizNum in range(35):
    # TODO: Create a quiz and answer key files
    quizFile = open(f"capitalsquiz{quizNum+1}.txt","w")
    answerKeyFile = open(f"capitalsquiz_answers{quizNum+1}.txt", "w")
    quizFile.write("Name:\n\nDate:\n\nPeriod:\n\n")
    quizFile.write((' ' * 20) + f"State Capitals Quiz (Form {quizNum + 1})")
    quizFile.write("\n\n")
    
    # TODO: Shuffle states order
    states = list(capitals.keys())
    random.shuffle(states)

    # TODO: Make a question for each state
    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3) # Get me 3 random samples
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        quizFile.write(f"{questionNum + 1} What is the capital of {states[questionNum]}?\n")
        for i in range(4):
            quizFile.write(f"   {'ABCD'[i]}. { answerOptions[i]}\n")
        quizFile.write("\n")

        answerKeyFile.write(f"{questionNum + 1}. {'ABCD'[answerOptions.index(correctAnswer)]}\n")
    quizFile.close()
    answerKeyFile.close()
        