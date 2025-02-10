import random,time

questions=[{"q": "what is the capital city of the japan?", "answer" : "c"},
           {"q":"in which year did the titanic sink?","answer" : "a"},
           {"q":"which gas makes up the majority of earth's atmosphere?", "answer": "b"},
           {"q":"who won the 2018 fifa world cup?", "answer": "c"},
           {"q":"which player has won the most ballon d'Or awaards?", "answer": "b"}]

options=[["a. nagasaki", "b. hiroshima", "c. tokyo", "d. osaka"],
         ["a. 1912", "b. 1866", "c. 1914", "d. 1915"],
         ["a. oxygen", "b. nitrogen", "c. hydrogen", "d. carbon"],
         ["a. brazil", "b. argentina", "c. france", "d. portugal"],
         ["a. cristiano_ronaldo", "b. lionel_messi", "c. luka_modric", "d. neymar"]]
# answers=["c","a","b","c","b"]

score=0
time_limit=10

def check_answer(user_guess,correct_answer):
      if user_guess==correct_answer:
            return True
      else:
            return False

for question_num in range(len(questions)): 
    print(questions[question_num]["q"])
    for i in options[question_num]:
        print(i)

    b=input({"enter your answer!!..."}).lower()
    c=check_answer(b,questions[question_num]["answer"])
    st_time=time.time()
    time_che=time.time()-st_time
    if time_che > time_limit:
         print("time is up")
         continue
    if c:
          print("correct answer")
          score+=1
    else:
          print("incorrect answer")
print(f"total score is: {score}/5 questions")
