import json
import csv
import pandas as pd
#%pprint

verbs = ['run', 'read', 'reach', 'knock', 'build', 'notice']

#queryf = pd.read_excel('/Users/songkim/Google Drive/Primary/Projects/VerbVector/query/query_v0.xlsx', index_col='Name')
queryf = pd.read_excel('/Users/songheekim/Google Drive/Primary/Projects/VerbVector/query/query_v0.xlsx', index_col='Name')
queryf_event = queryf.iloc[-7:]  ## select only the 7 newly added features 
feature_names = queryf_event.index.tolist()
query_dict = queryf_event.to_dict(orient='index')
#print (queryf.head())
#print (query_dict['State of Being'])


## let's build a dict that will be converted into a json object
for vb in verbs: 
    stims_list = []
    for k, v in query_dict.items():
        lemma = vb.capitalize()
        stims = dict()
        attribute = k
        print (attribute)
        #relation = q[1]['Relation']
        query = v['Query']
        h_ex = v['High Example']
        h_exp = v['High Explanation']
        m_ex = v['Med Example']
        m_exp = v['Medium Explanation']
        l_ex = v['Low Example']
        l_exp = v['Low Explanation']
        stims['attribute'] = attribute ## 'Boundedness'
        if 
        stims['question'] = ("<h><b> %s </b></h><br><p><b> "%s?" </b></p><p> For comparison, <b> %s  </b> would receive a high rating on " +
          'this question, because %s <br><br>In contrast, <b> %s </b> might receive a medium rating, because ' +
          "%s </p><br><p>Your rating for <b>%s</b>:</p>") %(lemma, query, h_ex, h_exp, m_ex, m_exp, v)
        stims_list.append(stims)
    # with open("%s.json" %(v), "w") as outfile:
    #     json.dump(stims_list, outfile)
    with open("%s.json" %(v), "w") as outfile: 
        for feature in stims_list:
            outfile.write(json.dump(feature))
            outfile.write("\n")
    break


