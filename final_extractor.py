import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

class extractor:
    def __init__(self):
        
        faculty_in=input('Enter Faculty Name: ')
        year_in=input('Enter Year Name: ')
        print(year_in+'\\'+faculty_in)
        try: 
            df=pd.read_csv(year_in+'\\'+faculty_in+'\\Analysis_data.csv')
            print(df)
            mean_percentage=df['Percentage'].mean()
            Std_Percentage=df['Percentage'].std(ddof=0)
            Variance=Std_Percentage**2
            total_pass=df['Status'].loc[~df['Status'].str.contains('Fail')].count()
            total_fail=df['Status'].loc[df['Status'].str.contains('Fail')].count()
            
            with open(year_in+'\\'+faculty_in+'\\summary_analysis.txt','w') as f: 
                f.writelines('Summary_Report\n\tMean: '+str(mean_percentage)+'\n\tStandard Deviation: '+str(Std_Percentage)+'\n\tVarance: '+str(Variance)+'\n\ttotal_pass: '+str(total_pass)+'\n\ttotal_failed: '+str(total_fail))
            
            #plotting pie chart here
            plt.subplot(221)
            plt.title("Pie Chart")
            slices=[df['Status'].loc[df['Status'].str.contains('Distinction')].count(),df['Status'].loc[df['Status'].str.contains('First')].count(),df['Status'].loc[df['Status'].str.contains('Second')].count(),df['Status'].loc[df['Status'].str.contains('Fail')].count()]
            plt.pie(slices,
                labels=['Distinction','1st Div','2nd Div','Fail'],
                colors=['r','g','b','k']
            )
            plt.legend(loc="upper left",fontsize='5',bbox_to_anchor=(1,0.5))
            
            #plotting bar graph from down here 
            plt.subplot(222)
            plt.title('Bar Graph')
            X=np.array(df['Roll'])
            Y=np.array(df['Percentage'])
            plt.xlabel('Roll Number')
            plt.ylabel('Percentage')
            plt.bar(X,Y,color='b')

            #Plotting histogram
            plt.subplot(223)
            plt.title('Histogram')
            X=np.array(df['Percentage'])
            bins=[4,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
            plt.hist(X,bins,edgecolor='black')

            #plotting scaterplot
            plt.subplot(224)
            plt.title('ScatterPlot',y=-0.25)
            X=np.array(df['Roll'])
            Y=np.array(df['Percentage'])
            plt.scatter(X,Y,label='Marks-graph',color='r')
            plt.axhline(y=mean_percentage,color='k')
            plt.legend()
            plt.show()
            plt.savefig(year_in+'\\'+faculty_in+'\\'+'Ouput_Image.png')
            os.system(year_in+'\\'+faculty_in+'\\summary_analysis.txt')
        except:
            print('Invalid File Requested')
