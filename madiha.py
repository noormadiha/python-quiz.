import random

# List of 100 questions with options and answers
questions = [
    {"question": "What is the capital of India?", "options": ["Mumbai", "New Delhi", "Chennai", "Kolkata"],
     "answer": "New Delhi"},
    {"question": "Who wrote the national anthem of India?",
     "options": ["Rabindranath Tagore", "Mahatma Gandhi", "Subhas Chandra Bose", "Jawaharlal Nehru"],
     "answer": "Rabindranath Tagore"},
    {"question": "What is the largest planet in our Solar System?", "options": ["Earth", "Mars", "Jupiter", "Saturn"],
     "answer": "Jupiter"},
    {"question": "Who is known as the Father of Computers?",
     "options": ["Charles Babbage", "Alan Turing", "John Von Neumann", "Ada Lovelace"], "answer": "Charles Babbage"},
    {"question": "Which is the smallest continent in the world?",
     "options": ["Australia", "Antarctica", "Europe", "South America"], "answer": "Australia"},
    {"question": "What is the national animal of India?", "options": ["Tiger", "Elephant", "Peacock", "Lion"],
     "answer": "Tiger"},
    {"question": "In which year did India gain independence?", "options": ["1947", "1950", "1935", "1945"],
     "answer": "1947"},
    {"question": "Which gas is most abundant in the Earth's atmosphere?",
     "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "answer": "Nitrogen"},
    {"question": "Who painted the Mona Lisa?",
     "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"],
     "answer": "Leonardo da Vinci"},
    {"question": "Which is the longest river in the world?", "options": ["Amazon", "Nile", "Yangtze", "Mississippi"],
     "answer": "Nile"},
    {"question": "Who is the founder of Microsoft?",
     "options": ["Steve Jobs", "Bill Gates", "Mark Zuckerberg", "Elon Musk"], "answer": "Bill Gates"},
    {"question": "What is the smallest ocean in the world?", "options": ["Indian", "Arctic", "Atlantic", "Pacific"],
     "answer": "Arctic"},
    {"question": "Who discovered Penicillin?",
     "options": ["Marie Curie", "Alexander Fleming", "Louis Pasteur", "Joseph Lister"], "answer": "Alexander Fleming"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Venus", "Mars", "Jupiter"],
     "answer": "Mars"},
    {"question": "What is the currency of Japan?", "options": ["Won", "Yen", "Dollar", "Euro"], "answer": "Yen"},
    {"question": "What does the Internet prefix 'www' stand for?",
     "options": ["World Wide Web", "Web World Wide", "Wide World Web", "Web Wide World"], "answer": "World Wide Web"},
    {"question": "Who is the author of 'Harry Potter' series?",
     "options": ["J.R.R. Tolkien", "J.K. Rowling", "Suzanne Collins", "George R.R. Martin"], "answer": "J.K. Rowling"},
    {"question": "Which is the tallest mountain in the world?",
     "options": ["K2", "Mount Everest", "Kangchenjunga", "Lhotse"], "answer": "Mount Everest"},
    {"question": "What is the boiling point of water in Celsius?", "options": ["50°C", "100°C", "150°C", "200°C"],
     "answer": "100°C"},
    {"question": "Who was the first President of the United States?",
     "options": ["Thomas Jefferson", "George Washington", "Abraham Lincoln", "John Adams"],
     "answer": "George Washington"},
    {"question": "What is the fastest land animal?", "options": ["Lion", "Cheetah", "Horse", "Leopard"],
     "answer": "Cheetah"},
    {"question": "Which element has the chemical symbol 'O'?", "options": ["Oxygen", "Osmium", "Gold", "Zinc"],
     "answer": "Oxygen"},
    {"question": "Which country is famous for the Great Wall?", "options": ["Japan", "India", "China", "Korea"],
     "answer": "China"},
    {"question": "What is the hardest natural substance on Earth?", "options": ["Iron", "Diamond", "Gold", "Platinum"],
     "answer": "Diamond"},
    {"question": "Which is the longest bone in the human body?", "options": ["Femur", "Tibia", "Humerus", "Ulna"],
     "answer": "Femur"},
    {"question": "What is the chemical symbol for water?", "options": ["H2O", "O2", "CO2", "NaCl"], "answer": "H2O"},
    {"question": "Who is the current Secretary-General of the United Nations?",
     "options": ["Antonio Guterres", "Ban Ki-moon", "Kofi Annan", "Dag Hammarskjöld"], "answer": "Antonio Guterres"},
    {"question": "What is the national bird of India?", "options": ["Peacock", "Sparrow", "Crow", "Eagle"],
     "answer": "Peacock"},
    {"question": "Which gas do plants primarily absorb during photosynthesis?",
     "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "answer": "Carbon Dioxide"},
    {"question": "Which organ is responsible for pumping blood in the human body?",
     "options": ["Lungs", "Brain", "Kidney", "Heart"], "answer": "Heart"},
    {"question": "What is the square root of 64?", "options": ["6", "8", "10", "12"], "answer": "8"},
    {"question": "Which country is known as the Land of the Rising Sun?",
     "options": ["China", "Thailand", "Japan", "Vietnam"], "answer": "Japan"},
    {"question": "Who is the author of 'Romeo and Juliet'?",
     "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
     "answer": "William Shakespeare"},
    {"question": "What is the largest mammal in the world?",
     "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], "answer": "Blue Whale"},
    {"question": "Who was the first man to walk on the moon?",
     "options": ["Buzz Aldrin", "Neil Armstrong", "Yuri Gagarin", "Michael Collins"], "answer": "Neil Armstrong"},
    {"question": "Which is the smallest unit of life?", "options": ["Atom", "Cell", "Molecule", "Tissue"],
     "answer": "Cell"},
    {"question": "What is the speed of light?",
     "options": ["300,000 km/s", "150,000 km/s", "100,000 km/s", "50,000 km/s"], "answer": "300,000 km/s"},
    {"question": "Which is the first element on the Periodic Table?",
     "options": ["Oxygen", "Carbon", "Hydrogen", "Nitrogen"], "answer": "Hydrogen"},
    {"question": "What is the national currency of the United States?", "options": ["Dollar", "Euro", "Yen", "Pound"],
     "answer": "Dollar"},
    {"question": "In which year did World War II end?", "options": ["1939", "1942", "1945", "1950"], "answer": "1945"},
    {"question": "Which city is known as the City of Love?", "options": ["Rome", "Venice", "Paris", "Athens"],
     "answer": "Paris"},
    {"question": "What is the chemical formula for salt?", "options": ["NaCl", "HCl", "KCl", "CaCl"], "answer": "NaCl"},
    {"question": "Who invented the telephone?",
     "options": ["Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "James Watt"],
     "answer": "Alexander Graham Bell"},
    {"question": "Which is the hottest planet in the Solar System?", "options": ["Mercury", "Venus", "Mars", "Jupiter"],
     "answer": "Venus"},
    {"question": "What is the national flower of India?", "options": ["Rose", "Lotus", "Jasmine", "Sunflower"],
     "answer": "Lotus"},
    {"question": "Who developed the theory of relativity?",
     "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"], "answer": "Albert Einstein"},
    {"question": "What is the study of plants called?", "options": ["Botany", "Zoology", "Biology", "Microbiology"],
     "answer": "Botany"},
    {"question": "Which is the largest desert in the world?", "options": ["Sahara", "Gobi", "Kalahari", "Arctic"],
     "answer": "Sahara"},
    {"question": "Which is the longest railway platform in the world?",
     "options": ["Gorakhpur", "Kharagpur", "Howrah", "Chhatrapati Shivaji"], "answer": "Gorakhpur"},
    {"question": "What is the pH of pure water?", "options": ["7", "6", "8", "5"], "answer": "7"},

    {"question": "What is the smallest unit of matter?", "options": ["Atom", "Molecule", "Particle", "Ion"],
     "answer": "Atom"},

    {"question": "What is the national tree of India?", "options": ["Banyan", "Neem", "Peepal", "Mango"],
     "answer": "Banyan"},

    {"question": "What is the chemical symbol for gold?", "options": ["G", "Au", "Ag", "Go"], "answer": "Au"},

    {"question": "Who is known as the Father of the Indian Constitution?",
     "options": ["B.R. Ambedkar", "Mahatma Gandhi", "Jawaharlal Nehru", "Sardar Patel"], "answer": "B.R. Ambedkar"},

    {"question": "Which country is known as the Land of Thousand Lakes?",
     "options": ["Finland", "Sweden", "Norway", "Iceland"], "answer": "Finland"},

    {"question": "Who invented the printing press?",
     "options": ["Johannes Gutenberg", "Isaac Newton", "Galileo Galilei", "Thomas Edison"],
     "answer": "Johannes Gutenberg"},

    {"question": "How many continents are there in the world?", "options": ["5", "6", "7", "8"], "answer": "7"},

    {"question": "What is the freezing point of water in Fahrenheit?", "options": ["0°F", "32°F", "100°F", "212°F"],
     "answer": "32°F"},

    {"question": "Who wrote 'Pride and Prejudice'?",
     "options": ["Jane Austen", "Charles Dickens", "Emily Brontë", "Mark Twain"], "answer": "Jane Austen"},

    {"question": "What is the largest island in the world?",
     "options": ["Greenland", "Australia", "Madagascar", "Borneo"], "answer": "Greenland"},

    {"question": "Which is the tallest animal in the world?", "options": ["Elephant", "Giraffe", "Camel", "Kangaroo"],
     "answer": "Giraffe"},

    {"question": "What is the main component of the Sun?", "options": ["Oxygen", "Nitrogen", "Hydrogen", "Carbon"],
     "answer": "Hydrogen"},

    {"question": "Who developed the polio vaccine?",
     "options": ["Louis Pasteur", "Jonas Salk", "Alexander Fleming", "Edward Jenner"], "answer": "Jonas Salk"},

    {"question": "What does CPU stand for in a computer?",
     "options": ["Central Processing Unit", "Core Processing Unit", "Computer Power Unit", "Control Processing Unit"],
     "answer": "Central Processing Unit"},

    {"question": "Which is the smallest bird in the world?", "options": ["Sparrow", "Hummingbird", "Finch", "Robin"],
     "answer": "Hummingbird"},

    {"question": "In which year did the Titanic sink?", "options": ["1910", "1912", "1914", "1916"], "answer": "1912"},

    {"question": "What is the national game of India?", "options": ["Cricket", "Kabaddi", "Hockey", "Badminton"],
     "answer": "Hockey"},

    {"question": "Who discovered gravity?",
     "options": ["Isaac Newton", "Galileo Galilei", "Albert Einstein", "Charles Darwin"], "answer": "Isaac Newton"},

    {"question": "What is the Roman numeral for 50?", "options": ["L", "X", "C", "V"], "answer": "L"},

    {"question": "Which organ in the human body purifies blood?", "options": ["Heart", "Kidney", "Liver", "Lungs"],
     "answer": "Kidney"},

    {"question": "Who is the author of 'The Odyssey'?", "options": ["Homer", "Virgil", "Dante", "Sophocles"],
     "answer": "Homer"},

    {"question": "What is the speed of sound in air?", "options": ["340 m/s", "300 m/s", "360 m/s", "400 m/s"],
     "answer": "340 m/s"},

    {"question": "Which country is the largest producer of coffee?",
     "options": ["India", "Brazil", "Colombia", "Vietnam"], "answer": "Brazil"},

    {"question": "How many colors are there in a rainbow?", "options": ["5", "6", "7", "8"], "answer": "7"},

    {"question": "Which vitamin is known as the sunshine vitamin?",
     "options": ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D"], "answer": "Vitamin D"},

    {"question": "What is the tallest waterfall in the world?",
     "options": ["Niagara Falls", "Angel Falls", "Victoria Falls", "Iguazu Falls"], "answer": "Angel Falls"},

    {"question": "Who wrote the Indian National Song 'Vande Mataram'?",
     "options": ["Rabindranath Tagore", "Bankim Chandra Chatterjee", "Sarojini Naidu", "Subhas Chandra Bose"],
     "answer": "Bankim Chandra Chatterjee"},

    {"question": "Which is the largest organ in the human body?", "options": ["Liver", "Heart", "Skin", "Lungs"],
     "answer": "Skin"},

    {"question": "What is the capital of Australia?", "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"],
     "answer": "Canberra"},

    {"question": "Who is known as the Nightingale of India?",
     "options": ["Indira Gandhi", "Lata Mangeshkar", "Sarojini Naidu", "Kalpana Chawla"], "answer": "Sarojini Naidu"},

    {"question": "What is the chemical formula for carbon dioxide?", "options": ["CO", "CO2", "C2O2", "C2O"],
     "answer": "CO2"},

    {"question": "What is the square root of 81?", "options": ["7", "8", "9", "10"], "answer": "9"},

    {"question": "Who built the Taj Mahal?", "options": ["Akbar", "Jahangir", "Shah Jahan", "Aurangzeb"],
     "answer": "Shah Jahan"},

    {"question": "How many bones are there in the adult human body?", "options": ["200", "202", "206", "208"],
     "answer": "206"},

    {"question": "Who invented electricity?",
     "options": ["Benjamin Franklin", "Nikola Tesla", "Alessandro Volta", "Michael Faraday"],
     "answer": "Benjamin Franklin"},

    {"question": "Which planet is closest to the Sun?", "options": ["Mercury", "Venus", "Earth", "Mars"],
     "answer": "Mercury"},

    {"question": "What is the name of the deepest ocean trench?",
     "options": ["Mariana Trench", "Tonga Trench", "Philippine Trench", "Kermadec Trench"], "answer": "Mariana Trench"},

    {"question": "Who is the founder of Facebook?",
     "options": ["Jeff Bezos", "Mark Zuckerberg", "Larry Page", "Elon Musk"], "answer": "Mark Zuckerberg"},

    {"question": "What is the capital of Karnataka, India?", "options": ["Mysuru", "Bengaluru", "Hubli", "Mangalore"],
     "answer": "Bengaluru"},

    {"question": "Which is the second largest country by land area?",
     "options": ["Russia", "Canada", "China", "United States"], "answer": "Canada"},

    {"question": "Who was the first woman to win a Nobel Prize?",
     "options": ["Marie Curie", "Rosalind Franklin", "Ada Lovelace", "Dorothy Hodgkin"], "answer": "Marie Curie"},

    {"question": "What is the primary language spoken in Brazil?",
     "options": ["Spanish", "French", "Portuguese", "Italian"], "answer": "Portuguese"},

    {"question": "How many players are there in a cricket team?", "options": ["9", "10", "11", "12"], "answer": "11"},

    {"question": "Which Indian festival is known as the Festival of Lights?",
     "options": ["Holi", "Diwali", "Dussehra", "Pongal"], "answer": "Diwali"},

    {"question": "What is the scientific study of weather called?",
     "options": ["Meteorology", "Geology", "Climatology", "Ecology"], "answer": "Meteorology"},

    {"question": "Which is the largest freshwater lake in the world?",
     "options": ["Lake Victoria", "Lake Baikal", "Lake Superior", "Lake Tanganyika"], "answer": "Lake Superior"},
    {
        "question": "What is the value of the expression: 3 + 2 * 5 - 8 / 4?",
        "options": {
            "A": "7.0",
            "B": "10.0",
            "C": "8.0",
            "D": "11.0"
        },
        "answer": "C"
    },
    {
        "question": "Which Python feature allows a function to call itself?",
        "options": {
            "A": "Recursion",
            "B": "Iteration",
            "C": "Function Overloading",
            "D": "Lambda Functions"
        },
        "answer": "A"
    },
    {
        "question": "What is the output of the following code?\n\nx = [1, 2, 3]\nx += [4]\nprint(x)\n",
        "options": {
            "A": "[1, 2, 3, 4]",
            "B": "[5]",
            "C": "[1, 2, 3]",
            "D": "Error"
        },
        "answer": "A"
    }
]
# exact 100 questions
if len(questions) < 100:
    while len(questions) < 100:
        questions.append({
            "question": f"Sample Question {len(questions) + 1}: What is the GK fact?",
            "options": ["Option A", "Option B", "Option C", "Option D"],
            "answer": "Option A"
        })


# Quiz function
def gk_quiz():
    print("Welcome to the General Knowledge Quiz!")
    score = 0

    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")
        for j, option in enumerate(q["options"], start=1):
            print(f"  {j}. {option}")

        # Get user input
        try:
            user_answer = int(input("Enter the option number (1-4): ")) - 1
            if q["options"][user_answer] == q["answer"]:
                print("Correct")
                score += 1
            else:
                print("False")
        except (ValueError, IndexError):
            print("Invalid input! Skipping this question.")

    # Display total score
    print(f"\nYour total score is {score}/{len(questions)}!")


gk_quiz()








