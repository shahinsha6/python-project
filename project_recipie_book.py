
class Recepie_book:

    def __init__(self,name,no_ingredients,no_instructions):
        self.name=name
        self.no_ingredients=no_ingredients
        self.no_instructions=no_instructions

    def name_recepie(self):
        f=open(f'{self.name}.txt','w')
        f.write(f'\t\t{self.name}')
        f.close()

    def ingredients(self):
        f=open(f'{self.name}.txt','a')
        f.write('\nIngredients')
        f.close()
        with open(f'{self.name}.txt','a') as f:
            for i in range(1,int(self.no_ingredients)+1):
                f.write(f'\n{i}.{input(f'Incredient{i}:')}')

    def instuction(self):
        f=open(f'{self.name}.txt','a')
        f.write('\nInstructions')
        f.close()
        with open(f'{self.name}.txt','a') as f:
            for i in range(1,int(self.no_instructions)+1):
                f.write(f'\n{i}.{input(f'Instruction{i}:')}')

try:
    number_recepie=int(input('No of Recepies:'))
except ValueError:
    print('Inalid input')
    number_recepie=int(input('No of Recepies:'))

for i in range(number_recepie):
    try:
        recepie_name=input('What is the name of your Recepie:')
        ingredients_no=int(input('Number of Ingredients:'))
        instruction_no=int(input('Number of Instructions:'))
        recepie=Recepie_book(f'{recepie_name}',f'{ingredients_no}',f'{instruction_no}')
    except ValueError:
        print('Invalid Input')
        recepie_name=input('What is the name of your Recepie:')
        ingredients_no=int(input('Number of Ingredients:'))
        instruction_no=int(input('Number of Instructions:'))
        recepie=Recepie_book(f'{recepie_name}',f'{ingredients_no}',f'{instruction_no}')
        
    recepie.name_recepie()
    recepie.ingredients()
    recepie.instuction()




