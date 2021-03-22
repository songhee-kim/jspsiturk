import json
import csv
import pandas as pd
import math
#%pprint

verbs = ['run', 'read', 'reach', 'knock', 'build', 'notice']

#queryf = pd.read_excel('/Users/songkim/Google Drive/Primary/Projects/VerbVector/query/query_v0.xlsx', index_col='Name')
queryf = pd.read_excel('/Users/songheekim/Google Drive/Primary/Projects/VerbVector/query/query_v1.xlsx', index_col='Name')
queryf_event = queryf.iloc[-7:]  ## select only the 7 newly added features 
feature_names = queryf_event.index.tolist()
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

        examples = []
        dic = {0:'h', 1:'m', 2:'l'}
        for counter, ex in enumerate([h_ex, m_ex, l_ex]):
            if ex!='none':
                examples.append(counter)
        examples_neat = [dic.get(ex) for ex in examples]

        if len(examples_neat) == 3: 
            stims['question'] = ("<h><b> %s </b></h><br><p><b> %s? </b></p><p> For comparison, <b> %s </b> would receive a high rating on " +
              'this question, because %s <br><br>In contrast, <b> %s </b> might receive a medium rating, because ' +
              "%s </p><br> <p> Finally, <b> %s </b> might receive a low rating, because %s </p><br><p>Your rating for <b>%s</b>:</p>") %(lemma, query, h_ex, h_exp, m_ex, m_exp, l_ex, l_exp, lemma)
            # print (stims['question'])
        elif len(examples_neat) == 2:
            if examples_neat == ['h', 'm']:
                stims['question'] = ("<h><b> %s </b></h><br><p><b> %s? </b></p><p> For comparison, <b> %s </b> would receive a high rating on " +
                  'this question, because %s <br><br>In contrast, <b> %s </b> might receive a medium rating, because ' +
                  "%s </p><br> <p>Your rating for <b>%s</b>:</p>") %(lemma, query, h_ex, h_exp, m_ex, m_exp, lemma)
                # print (stims['question']) 
            elif examples_neat == ['h', 'l']:
                stims['question'] = ("<h><b> %s </b></h><br><p><b> %s? </b></p><p> For comparison, <b> %s </b> would receive a high rating on " +
                  'this question, because %s <br><br>In contrast, <b> %s </b> might receive a low rating, because ' +
                  "%s </p><br> <p>Your rating for <b>%s</b>:</p>") %(lemma, query, h_ex, h_exp, l_ex, l_exp, lemma)
                # print (stims['question'])                

            else: 
                print ('examples seem wrong')

        else:
            print ('example number is neither 3 nor 2')

        stims_list.append(stims)
        grand_stims_list.append(stims)
    # print (vb)
    # print (stims_list)
    # break


    # with open("/Users/songheekim/Google Drive/Primary/Projects/VerbVector/query/%s.json" %(vb), "w") as outfile:
    #     json.dump(stims_list, outfile) ## This writes everything in ONE line. 
    with open("/Users/songheekim/Google Drive/Primary/Projects/VerbVector/query/%s.js" %(vb), "w") as outfile: 
        outfile.write('var stims=[')
        for feature in stims_list:
            outfile.write(json.dumps(feature))
            outfile.write(",\n")
        outfile.write(']')

print ('# of stims in pilot_stim:', len(grand_stims_list))
with open("/Users/songheekim/Google Drive/Primary/Projects/VerbVector/query/pilot_stim.js", "w") as outfile: 
    outfile.write('var stims=[')
    for feature in grand_stims_list:
        outfile.write(json.dumps(feature))
        outfile.write(",\n")
    outfile.write(']')










