import json
import csv
import pandas as pd
#%pprint

verbs = ['run', 'read', 'reach', 'knock', 'build', 'notice']

queryf = pd.read_excel('/Users/songkim/Google Drive/Primary/Projects/VerbVector/query/query_v0.xlsx', index_col='Name')
queryf_event = queryf.iloc[-7:]  ## select only the 7 newly added features 
feature_names = queryf_event.index.tolist()
query_dict = queryf_event.to_dict(orient='index')
#print (queryf.head())
#print (query_dict['State of Being'])


## let's build a dict that will be converted into a json object
for v in verbs: 
    stims_list = []
    for q in query_dict.items():
        stims = dict()
        attribute = q[0]
        print (attribute)
        relation = q[1]['Relation']
        query = q[1]['Query']
        h_ex = q[1]['High Example']
        h_exp = q[1]['High Explanation']
        m_ex = q[1]['Med Example']
        m_exp = q[1]['Medium Explanation']
        l_ex = q[1]['Low Example']
        l_exp = q[1]['Low Explanation']
        #stims['verb'] = v
        stims['attribute'] = attribute ## 'Boundedness'
        stims['question'] = ("<h><b> %s </b></h><br><p><b>To what extent do you think this event described " +
          "by this verb refer to %s? </b></p><p> For comparison, <b> %s  </b> would receive a high rating on " +
          'this question, because %s <br><br>In contrast, <b> %s </b> might receive a medium rating, because ' +
          "%s </p><br><p>Your rating for <b>%s</b>:</p>") %(v, query, h_ex, h_exp, m_ex, m_exp, v)
        stims_list.append(stims)
    # with open("%s.json" %(v), "w") as outfile:
    #     json.dump(stims_list, outfile)
    with open("%s.json" %(v), "w") as outfile: 
        for feature in stims_list:
            outfile.write(json.dump(feature))
            outfile.write("\n")
    break


