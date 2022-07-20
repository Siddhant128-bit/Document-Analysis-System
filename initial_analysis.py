import pandas as pd
import os

class analyzer_int:
    def convert_to_float(self,x):
        return float(x)

    def create_standard_table(self,doc_content,df):
        final_df=pd.DataFrame()
        final_df['Name']=[doc_content[0]]
        final_df['Roll']=[doc_content[2]]
        print(df)
        df.columns=['Subjects','FM','TM','PM','Total']
        df=df.iloc[1:]
        df['FM']=df['FM'].apply(self.convert_to_float)
        df['TM']=df['TM'].apply(self.convert_to_float)
        df['PM']=df['PM'].apply(self.convert_to_float)
        df['Total']=df['Total'].apply(self.convert_to_float)
        df['Status']='Pass'
        df.loc[df['TM']<30,['Status']]='Fail'
        
        pass_or_fail=df['Status'].loc[df['Status'].str.contains('Fail')].count()
        secured_marks=df['Total'].sum()
        total_marks=df['FM'].sum()
        final_df['Status']='Fail'
        percentage=(secured_marks/total_marks)*100
        final_df['Percentage']=percentage
        if pass_or_fail==0:
            final_df.loc[final_df['Percentage']>=80,['Status']]='Distinction'
            final_df.loc[(final_df['Percentage']>=60) & (final_df['Percentage']<80) ,['Status']]='First Div'
            final_df.loc[(final_df['Percentage']>=40) & (final_df['Percentage']<60),['Status']]='Second Div'
            final_df.loc[(final_df['Percentage']>0) & (final_df['Percentage']<40),['Status']]='Third Div'
        final_df.to_csv(doc_content[-1]+'\\'+doc_content[1]+'\\'+'Analysis_data.csv',mode='a',index=False)
        final_df=pd.read_csv(doc_content[-1]+'\\'+doc_content[1]+'\\'+'Analysis_data.csv')
        os.remove(doc_content[-1]+'\\'+doc_content[1]+'\\'+'Analysis_data.csv')
        final_df=final_df.drop_duplicates(keep="first")
        final_df=final_df.loc[final_df['Name']!='Name']
        final_df.to_csv(doc_content[-1]+'\\'+doc_content[1]+'\\'+'Analysis_data.csv',mode='a',index=False)
        return df 
    def __init__(self,doc_content,table_content):
        df=self.create_standard_table(doc_content,table_content)
