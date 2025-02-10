
import random
movie_list=['avesham','pani','kill','marco','drishyam']
chosen_movie=random.choice(movie_list)
print(chosen_movie)

lives=6
a=[]
for i in range(len(chosen_movie)):
    a+='_'
print(a)
   
game_over=False
while not game_over:
    b=input('guess a letter:---')
    for position in range(len(chosen_movie)):
        letter=chosen_movie[position]
        if letter==b:
            a[position]=b
    print(a)

    if b not in chosen_movie:
        lives-=1
        if lives==0:
            game_over=True
            print('you lose')
    if '_' not in a:
        game_over=True
        print('you win')
