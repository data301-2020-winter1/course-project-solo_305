import pandas as pd
def load_process(path_to_csv_file):
    df = (pd.read_csv(path_to_csv_file)
          .drop(columns={'BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6'})
          .drop(columns={"PAY_AMT1",'PAY_AMT2','PAY_AMT3','PAY_AMT4','PAY_AMT5','PAY_AMT6'})
          .rename(columns={"PAY_0": "PAY_1"})
          .rename(columns={"default.payment.next.month":'Default'})
         )
    return df
load_process('/Users/jo-elle/Desktop/Data301/project/course-project-solo_305/data/raw.data/UCI_Credit_Card.csv')


def correlation(Col1, Col2):
    a = df.groupby([Col1, Col2]).size().unstack()
    a['percentage'] = (a[a.columns[1]]/(a[a.columns[0]] + a[a.columns[1]]))
    return a

def boxplot1(feature1, feature2, feature3, width=16):
    fig, ax1 = plt.subplots(ncols=1, figsize=(width,6))
    s = sns.boxplot(ax = ax1, x=feature1, y=feature2, hue=feature3,
                data=df,showfliers=False)