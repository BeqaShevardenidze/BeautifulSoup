import os
import sys

sys.path.append('code 1')
sys.path.append('code 2 zoomer')
sys.path.append('code 3 jobs.ge')
sys.path.append('code 4 mymarket')
import learn
import zoomer
import jobs_ge
import mymarket

def Exit():
    sys.exit()
def Cls():
    os.system("cls")

Cls()
# Exit()

print("=" * 30, "Scraping", "=" * 30)
print("""{1} - learn
{2} - Zoommer.ge
{3} - jobs.ge
{4} - mymarket.ge
""")

x = input("input >>>> ")
match x:
    case '1':
        learn.f_learn()
    case '2':
        zoomer.f_zoomer()
    case '3':
        jobs_ge.f_jobs_ge()
    case '4':
        mymarket.f_mymarket()
    case _:
        print("ERROR")




# code_1_dir = os.path.abspath("code 1")
# sys.path.append(code_1_dir)
# from learn import f_learn
# f_learn()