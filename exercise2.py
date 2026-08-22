# create program like kbc
question=["1.What is the capital of Australia?",
          "2. Who is known as the Father of the Indian Constitution?",
          "3. Which is the largest planet in our Solar System?",
          "4. Who was the first President of India?",
          "5. Which is the longest river in the world?",
          "6. In which year did India gain independence?",
          "7. Which country is known as the Land of the Rising Sun?",
          "8.Who invented the telephone?",
          "9. What is the national animal of India?",
          "10. Which is the largest ocean in the world?"]

option=[
    ["A) Sydney ","B) Melbourne ","C) Canberra ","D) Perth"],
    ["A) Mahatma Gandhi", "B) Dr. B. R. Ambedkar", "C) Jawaharlal Nehru", "D) Sardar Patel"],
    ["A) Earth ","B) Saturn", "C) Jupiter", "D) Neptune"],
    ["A) Dr. Rajendra Prasad", "B) Dr. S. Radhakrishnan", "C) Jawaharlal Nehru", "D) Zakir Husain"],
    ["A) Amazon", "B) Nile" ,"C) Ganga", "D) Yangtze"],
    ["A) 1945" ,"B) 1946"," C) 1947"," D) 1950"],
    ["A) China" ,"B) South Korea ","C) Thailand", "D) Japan"],
    ["A) Thomas Edison" ," B) Alexander Graham Bell"," C) Nikola Tesla"," D) James Watt"],
    ["A) Lion"," B) Elephant", "C) BengalTiger" ,"D) Leopard"],
    ["A) Atlantic Ocean", "B) Indian Ocean"," C) Arctic Ocean"," D) Pacific Ocean"]
]

answer=["C", "B", "C", "A", "B", "C", "D", "B", "C", "D"]

prize=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]

total=0
for i in range(len(question)):
    print("\n Question: ",i+1)
    print(question[i])
        
    
    for j in option[i]:
        print(j)
    
    answers=input("Enter your answer(A/B/C/D): ").upper()
    if answers==answer[i]:
        print("Correct answer!")
        print("You won: ",prize[i])
        total=prize[i]
        
    else:
        print("Wrong answer!")
        print("Correct answer was: ",answer[i])
        break
    

print("Game over!")
print("Total amount won: ",total)
    