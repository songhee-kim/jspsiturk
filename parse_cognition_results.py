import pandas as pd
import csv

raw = pd.read_csv('/Users/songkim/Google Drive/Primary/jsp/jspsych-crea/pilot/results/event-concept-pilot-survey_21.csv')  
#print (raw)

sub_id = raw.loc[1, "responses"].replace('"', '')
sub_id = sub_id.replace('{', '').replace('}', '').split(':')[1]    
raw_dict = raw.to_dict(orient='index')
#print(raw_dict)


out = list() 
for k, row in raw_dict.items():
    #print (len(row['responses']))
    if (len(row['responses']) > 1) and (sub_id not in row['responses']): 
        #print ("I am in")
        ind_tuple = []
        lem = row['lemma']
        feat1 = row['responses'].replace('"', '').replace('{', '').replace('}', '').split(':')[0] 
        resp = row['responses'].replace('"', '').replace('{', '').replace('}', '').split(':')[1] 
        feature = row['feature'] 
        if feat1 != feature :
            print (k, ' row is wrong') 
            print (row)
        rt = row['rt'] 
        ind_tuple.append(sub_id) 
        ind_tuple.append(lem) 
        ind_tuple.append(feature) 
        ind_tuple.append(resp) 
        ind_tuple.append(rt) 
        #print (ind_tuple)
        # break
        ind_tuple = tuple(ind_tuple) 
        out.append(ind_tuple)
        # break
    # break


df = pd.DataFrame(out, columns=['sub_id', 'word', 'feature', 'response', 'RT'])
df.to_csv('/Users/songkim/Google Drive/Primary/jsp/jspsych-crea/pilot/results/eventconcept_pilot_%s.csv' %sub_id)
#print(df)
print ('df is created')

#print (df)