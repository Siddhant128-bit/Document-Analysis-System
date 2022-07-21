import table_extractor as t_e
import initial_analysis as i_a
import final_extractor as f_e
import os
import art

def main_function():
    my_art = art.text2art("Result Analysis Tool") 
    print(my_art)
    choice=int(input('Enter 1 to insert data\nEnter 2 to obtain result\nEnter 3 to exit: '))
    if choice==1:
        extr=t_e.extractor()
        anlzr=i_a.analyzer_int(extr.text_content,extr.table_content)
        return True
    elif choice==2:
        f_extr=f_e.extractor()
        print('Here lies analysis')
        return True
    elif choice==3:
        return False
    

if __name__=='__main__':
    os.system('color fa')
    os.system('cls')
    run=True
    while run:
        os.system('color fa')
        try: 
            run=main_function()
            os.system('color fa')
            os.system('cls')
        except:
            import traceback
            print(traceback.format_exc())
            os.system('color ca')
            msg=input('**ERROR**: Failure in system \nPress Enter to Restart: ')