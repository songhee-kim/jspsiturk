import json
import csv
import pandas as pd
import math
#%pprint

#verbs = ['run', 'read', 'reach', 'knock', 'build', 'notice']
verbs = ['flourish', 'exist', 'run', 'read', 'build', 'arrive', 'depart', \
         'begin', 'knock', 'contain', 'restrict', 'throw', 'find', 'hesitate']

#queryf = pd.read_excel('/Users/songkim/Google Drive/Primary/Projects/VerbVector/query/query_v0.xlsx', index_col='Name')

queryf = pd.read_excel('/Users/songkim/Google Drive/Primary/Projects/VerbVector/query/query_v2.xlsx', index_col='Name')

queryf_caused = queryf.loc[queryf.index=='Caused']
queryf_event = queryf.iloc[-5:]  ## select only the 7 newly added features 
queryf_event = pd.concat([queryf_caused, queryf_event]) 
feature_names = queryf_event.index.tolist()
print (feature_names)
query_dict = queryf_event.to_dict(orient='index')
grand_stims_list = []
#print (queryf.head())
#print (query_dict['State of Being'])

## let's build a dict that will be converted into a json object
for vb in verbs: 
    stims_list = []
    for k, v in query_dict.items():
        lemma = vb.upper().strip()
        print ('lemma:', lemma)
        stims = dict()
        print ('attribute:' , k)
        query = v['Query'].strip()
        h_ex = v['High Example'].strip()
        h_exp = v['High Explanation'].strip()
        m_ex = v['Med Example'].strip()
        m_exp = v['Medium Explanation'].strip()
        l_ex = v['Low Example'].strip()
        l_exp = v['Low Explanation'].strip()
        stims['attribute'] = k.strip() ## 'Boundedness'
        stims['verb'] = vb

        examples = []
        dic = {0:'h', 1:'m', 2:'l'}
        for counter, ex in enumerate([h_ex, m_ex, l_ex]):
            if ex!='none':
                examples.append(counter)
        examples_neat = [dic.get(ex) for ex in examples]

        if len(examples_neat) == 3: 
            stims['question'] = ('<h><b>%s</b></h><br><br><p class="qn"><b> %s </b></p><br><ul class="a"><li><b>%s</b> might receive a high rating on ' +
              'this question, because %s </li><br><br><li><b> %s </b> might receive a medium rating, because ' +
              '%s </li><br><br><li><b> %s </b> might receive a low rating, because %s </li></ul><br><p class="prompt">Your rating for <b>%s</b>:</p>') %(lemma, query, h_ex, h_exp, m_ex, m_exp, l_ex, l_exp, lemma)
            # print (stims['question'])
        elif len(examples_neat) == 2:
            if examples_neat == ['h', 'm']:
                stims['question'] = ('<h><b>%s</b></h><br><br><p class="qn"><b> %s </b></p><br><ul class="a"><li><b> %s </b> might receive a high rating on ' +
                  'this question, because %s </li><br><br><li><b> %s </b> might receive a medium rating, because ' +
                  '%s </li></ul><br><p class="prompt">Your rating for <b>%s</b>:</p>') %(lemma, query, h_ex, h_exp, m_ex, m_exp, lemma)
                # print (stims['question']) 
            elif examples_neat == ['h', 'l']:
                stims['question'] = ('<h><b> %s </b></h><br><br><p class="qn"><b> %s </b></p><br><ul class="a"><li><b> %s </b> might receive a high rating on ' +
                  'this question, because %s </li><br><br><li><b> %s </b> might receive a low rating, because ' +
                  '%s </li></ul><br><p class="prompt">Your rating for <b>%s</b>:</p>') %(lemma, query, h_ex, h_exp, l_ex, l_exp, lemma)
                # print (stims['question'])                

            else: 
                print ('examples seem wrong')

        else:
            print ('example number is neither 3 nor 2')


        stims_list.append(stims)
        grand_stims_list.append(stims)       
    # with open("/Users/songheekim/Google Drive/Primary/Projects/VerbVector/query/%s.json" %(vb), "w") as outfile:
    #     json.dump(stims_list, outfile) ## This writes everything in ONE line. 
    with open("/Users/songkim/Google Drive/Primary/jsp/jspsych-crea/pilot/queries/%s.js" %(vb), "w") as outfile: 
        outfile.write('var %s=[' %(vb))
        for feature in stims_list:
            outfile.write(json.dumps(feature))
            outfile.write(",\n")
        outfile.write(']')


# print ('# of stims in pilot_stim:', len(grand_stims_list))
# with open("/Users/songheekim/Google Drive/Primary/Projects/VerbVector/query/pilot_stim.js", "w") as outfile: 
#     outfile.write('var stims=[')
#     for feature in grand_stims_list:
#         outfile.write(json.dumps(feature))
#         outfile.write(",\n")
#     outfile.write(']')










