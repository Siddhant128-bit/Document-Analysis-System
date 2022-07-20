import fitz
import camelot.io as camelot
#import camelot 
import pandas as pd
import os

class extractor:
    def get_content(self,file):
        doc=fitz.open(file)
        content_of_page=doc[0].get_text()
        content_of_page=content_of_page.split('\n')
        extraction_topics=['Name','Faculty','Roll','Year']
        extraction_solutions=[]
        for i in extraction_topics:
            for text in content_of_page:
                if i in text:                            
                    extraction_solutions.append(text.split(':')[-1])
                    
        return extraction_solutions
    
    def table_content(self,file):
        table=camelot.read_pdf(file,flavor='stream')
        df=table[0].df
        start_index=df.loc[df[0].str.contains('Subjects')].index 
        end_index=df.loc[df[1].str.contains('someone finds this')].index
        start_index=int(start_index[0])
        end_index=int(end_index[0])
        return df.iloc[start_index:end_index]
    

    def __init__(self):
        self.file=input('Enter the path of file: ')
        try: 
            self.file=raw_s = r'{}'.format(self.file)
            self.text_content=self.get_content(self.file)
            self.table_content=self.table_content(self.file)
            try: 
                self.text_content[-1]=self.text_content[-1].replace(" ",'')
                self.text_content[1]=self.text_content[1].replace(" ",'')
                os.mkdir(self.text_content[-1])
                os.mkdir(self.text_content[-1]+'\\'+self.text_content[1])
            except:
                pass
            os.system('color fa')
            print('=='*30)
            self.exit_msg=input('Extraction Successful\nPress Enter to continue:')
        except :
            import traceback
            print(traceback.format_exc())
            print('=='*30)
            os.system('color ca')
            self.exit_msg=input('Extraction UnSuccessful\nPress Enter to continue:')
