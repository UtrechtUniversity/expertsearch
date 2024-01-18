# Parse logs and analyze results
import scikit_posthocs as sp#.posthoc_nemenyi_friedman
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix



import scipy.stats as stats
import matplotlib.pyplot as plt

#p0 is my testdata
p0_logs = 'time 1643305719277 task -1 window open?\ntime 1643305720531 task -1 query test numresults 22\ntime 1643305869597 starting task 0\ntime 1643305883862 task 0 window open?\ntime 1643305884404 task 0 query fietsgebruik allochtonen numresults 26\ntime 1643305899842 task 0 toggle on W.S. Doornbos rank 1 numresults 3\ntime 1643305906465 task 0 click 10f4e260-1ba4-48ae-a67d-199747afa9ce\ntime 1643305912870 task 0 click 66092949-5bfe-412d-9ffa-0d3079b4dd93\ntime 1643305927166 task 0 toggle on Freek Deuss rank 3 numresults 2\ntime 1643305936226 stopping task 0\ntime 1643305940484 starting task 1\ntime 1643305950449 task 1 window open?\ntime 1643305951430 task 1 query zorgcentrum rosendael numresults 11\ntime 1643305970957 task 1 toggle on P. Buisman rank 2 numresults 1\ntime 1643305972766 task 1 toggle on R.J. Evelein rank 0 numresults 1\ntime 1643305983610 stopping task 1\ntime 1643305986822 starting task 2\ntime 1643306002913 task 2 window open?\ntime 1643306003319 task 2 query jaarlijkse overnachtingen utrecht numresults 1030\ntime 1643306015449 task 2 window open?\ntime 1643306015715 task 2 query toeristen overnachtingen utrecht numresults 1030\ntime 1643306018980 task 2 window open?\ntime 1643306019169 task 2 query toeristen overnachtingen  numresults 29\ntime 1643306024340 task 2 toggle on V.J. Drost rank 0 numresults 3\ntime 1643306030249 task 2 toggle on A.P.M. Ruis rank 1 numresults 3\ntime 1643306049398 stopping task 2\ntime 1643306051296 starting task 3\ntime 1643306071752 task 3 window open?\ntime 1643306072187 task 3 query bedrijven vestigen numresults 327\ntime 1643306079127 task 3 toggle on Aloys Kersten rank 0 numresults 1\ntime 1643306119046 task 3 window open?\ntime 1643306119528 task 3 query bedrijven vestigen wijk numresults 671\ntime 1643306128426 task 3 toggle on G.J.W. Wanders rank 1 numresults 1\ntime 1643306131162 stopping task 3\ntime 1643306132566 task -1 window open?\ntime 1643306132615 task -1 query bedrijven vestigen wijk numresults 1691\ntime 1643306520764 starting task 4\ntime 1643306528678 task 4 window open?\ntime 1643306529032 task 4 query anti-speculatiebeding numresults 35\ntime 1643306537890 task 4 window open?\ntime 1643306537921 task 4 query antispeculatiebeding numresults 1\ntime 1643306540795 task 4 toggle on Ellen van Beckhoven rank 0 numresults 1\ntime 1643306544157 task 4 window open?\ntime 1643306544184 task 4 query speculatiebeding numresults 1\ntime 1643306548081 task 4 toggle on R. van Essen rank 0 numresults 1\ntime 1643306552702 stopping task 4\ntime 1643306556869 starting task 5\ntime 1643306562342 task 5 window open?\ntime 1643306562386 task 5 query uithoflijn numresults 94\ntime 1643306566304 task 5 toggle on J.H. Greeven rank 0 numresults 1\ntime 1643306568111 task 5 toggle on B. Coenen rank 1 numresults 1\ntime 1643306571391 stopping task 5\ntime 1643306574382 starting task 6\ntime 1643306587441 task 6 window open?\ntime 1643306587489 task 6 query jonge huishoudens overvecht numresults 757\ntime 1643306596018 task 6 window open?\ntime 1643306596073 task 6 query \'jonge huishoudens\' overvecht numresults 757\ntime 1643306603774 task 6 window open?\ntime 1643306603863 task 6 query "jonge huishoudens" overvecht numresults 550\ntime 1643306611561 task 6 toggle on N. Terpstra rank 1 numresults 1\ntime 1643306616802 task 6 window open?\ntime 1643306616857 task 6 query wonen overvecht numresults 1222\ntime 1643306625500 task 6 window open?\ntime 1643306625535 task 6 query overvecht numresults 550\ntime 1643306636698 stopping task 6\ntime 1643306639336 starting task 7\ntime 1643306648654 task 7 window open?\ntime 1643306648701 task 7 query wijkaanpak overvecht numresults 558\ntime 1643306652223 task 7 toggle on W.M. Hendrix rank 0 numresults 1\ntime 1643306655588 task 7 toggle on M. van den Berg rank 1 numresults 1\ntime 1643306662498 stopping task 7\n'
#Other log data has been removed, as we only obtained informed consent for sharing aggregated findings
p1_logs = ''
p2_logs = ''
p3_logs = ''
p4_logs = ''
p5_logs = ''
p6_logs = ''
p7_logs = ''
p8_logs = ''
p8_logs = ''
p9_logs = ''
#p10 misunderstood assignment, ignored results as described in paper
p10_logs = ''
p11_logs = ''
p12_logs = ''
p13_logs = ''
p14_logs = ''
p15_logs = ''
p16_logs = ''
p17_logs = ''
p18_logs = ''
p19_logs = ''






#i != 5 and i != 11 and i != 12 and i != 13 and i != 14 and i != 17
#p5_logs = ''
#p11_logs = ''
#p12_logs = ''
#p13_logs = ''
#p14_logs = ''
#p17_logs = ''
logs = [p0_logs, p1_logs, p2_logs, p3_logs, p4_logs, p5_logs, p6_logs, p7_logs, p8_logs, p9_logs, p10_logs, p11_logs, p12_logs, p13_logs, p14_logs, p15_logs, p16_logs, p17_logs, p18_logs, p19_logs]

#Randomly generated task orders from python shuffle
n = 25
task_order = ['07314625', '15740236', '41605273', '01325746', '30265147', '45760312', '16025734', '30167254', '54326017', '64721503', '60513427', '06324715', '32146057', '21450736', '32461057', '61534720', '02164735', '63157402', '15327460', '42675031', '20174653', '61427053', '42173650', '23701564', '63714520']

interface_order = ['can', 'doc', 'can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can']

ranking1_order = ['can', 'can', 'doc', 'doc', 'can', 'can', 'doc', 'doc', 'can', 'can', 'doc', 'doc', 'can', 'can', 'doc', 'doc', 'can', 'can', 'doc', 'doc', 'can', 'can', 'doc', 'doc', 'can']
ranking2_order = ['doc', 'doc', 'can', 'can', 'can', 'can', 'doc', 'doc', 'doc', 'doc', 'can', 'can', 'can', 'can', 'doc', 'doc', 'doc', 'doc', 'can', 'can', 'can', 'can', 'doc', 'doc', 'doc']



#metrics to keep track off for now
#time per task 
#number ticked per task
#number ticked correct per task
#document clicks per task



participants = []

for numdex, log in enumerate(logs):
    #stuff we keep track of per participant
    p = []
    for i in range(8):
        p.append({  'clicks': 0, 
                    'toggles': "",
                    'numtoggles': 0,
                    'numrelevant': 0,
                    'numrelevants':{},
                    'ranks':{},
                    'queries': 0,
                    'starttime':0,
                    'endtime':0,
                    'delays':0,         # if the windows was accidentally closed, add missed time to delays 
                    'time':0,
                    'times':[],
                    'time_to_query':0})
    
    prevline = ''
    curtask = -1
    print('Starting p ' + str(numdex))
    for line in log.split("\n"):
        lp = line.split(" ")
        print(line)

        #if the window was closed and re opened during an active task, add the difference to the 'delay'
        if 'window open' in line and 'window close' in prevline and curtask > -1:
            p[curtask]['delays'] += int(lp[1]) - int(prevline.split(" ")[1])

        if 'query' in line and curtask > -1:
            p[curtask]['queries'] += 1
            if p[curtask]['time_to_query'] == 0:
                p[curtask]['time_to_query'] = int(lp[1]) - p[curtask]['starttime']
                
            if 'query' in prevline and lp[1] != prevline.split(" ")[1]:
                print('INSPECT ME: next page?')
                
                #IF SAME QUERY BUT NEXT PAGE, DON'T COUNT AS NEW QUERY
        
        if 'starting task' in line and int(lp[-1]) < 8:
            curtask = int(lp[-1])
            p[curtask]['starttime'] = int(lp[1])
            
        if 'toggle' in line and curtask > -1:
            if lp[-5] in p[curtask]['toggles']:
                p[curtask]['numtoggles'] -= 1
                p[curtask]['toggles'] = p[curtask]['toggles'].replace((" ").join(lp[6:-4]), "")
                p[curtask]['numrelevant'] -= int(lp[-1])
                p[curtask]['numrelevants'].pop((" ").join(lp[6:-4]), None)
                p[curtask]['ranks'].pop((" ").join(lp[6:-4]), None)
            else:
                p[curtask]['numtoggles'] += 1
                p[curtask]['toggles'] += (" ").join(lp[6:-4])
                p[curtask]['numrelevant'] += int(lp[-1])
                p[curtask]['numrelevants'][(" ").join(lp[6:-4])] = int(lp[-1])
                p[curtask]['ranks'][(" ").join(lp[6:-4])] = int(lp[-3])
                
        if 'click' in line and curtask > -1:
            p[curtask]['clicks'] += 1
            
        if 'stopping task' in line and curtask > -1:
            p[curtask]['endtime'] = int(lp[1])
            p[curtask]['time'] = p[curtask]['endtime'] - p[curtask]['starttime'] - p[curtask]['delays']
            p[curtask]['times'].append(p[curtask]['endtime'] - p[curtask]['starttime'] - p[curtask]['delays'])
            curtask = -1
        
        prevline = line
        
    participants.append(p)


#manually fix some stuff due to bad logging (we didn't log 'next page' presses, and need to fix the clicked ranks to be clicked_rank + 10*numpage)
participants[4][0]['ranks']['Eelko van den Boogaard'] = 13
participants[5][4]['ranks']['R. van Alfen'] = 27
participants[7][7]['ranks']['R. Mouktadibillah'] = 10
participants[7][7]['ranks']['Monique van Kampen'] = 13
participants[7][7]['ranks']['M.E.J. van Lijden'] = 17
participants[7][7]['ranks']['D.T. Crabbendam'] = 23
participants[7][7]['ranks']['B.J. Brijder'] = 34
participants[11][0]['ranks']['A.W. Velthuis'] = 6
participants[11][1]['ranks']['div. auteurs'] = 21
participants[11][4]['ranks']['M. Kessels'] = 12
participants[15][1]['ranks']['Hans Huurman'] = 12
participants[15][1]['ranks']['V.J. Drost'] = 14
#print(participants[15][3]['ranks'])


print('Per participant')
avg_start = 0
avg_count = 0
outliers = []
outliers2 = []
outliers3 = []
outliers4 = []

alliers = []
for i, p in enumerate(participants):
#    print('Participant ' + str(i))
    person_avg = 0
    person_count = 0
    for j, t in enumerate(p):
        person_avg += t['time_to_query']
        person_count += 1
    
        avg_start += t['time_to_query']
        avg_count += 1
        alliers.append(t['time_to_query'] / 60000)
        if ((t['time_to_query'] / 60000) > 1):
            outliers.append(t['time_to_query'] / 60000)
        if ((t['time_to_query'] / 60000) > 0.5):
            outliers2.append(t['time_to_query'] / 60000)
        if ((t['time_to_query'] / 60000) > 0.75):
            outliers3.append(t['time_to_query'] / 60000)
        if ((t['time_to_query'] / 60000) > 0.85):
            outliers4.append(t['time_to_query'] / 60000)
            
            
    print('Average person time to query ' + str(person_avg / person_count / 60000))
#        print('Task ' + str(j))
#        print(t)
#        print()
#    print()

person_avg = 0
person_cnt = 0
person_times = []
for j, t in enumerate(participants[12]):
    #outliers are after 1 minute, confirmed by manual inspection of this participant
    if (t['time_to_query'] / 60000) < 1:
        person_avg += t['time_to_query']
        person_times.append(t['time_to_query'] / 60000)
        person_cnt += 1

print()
print('p12 avg ' + str(person_avg / person_cnt / 60000))
print(person_times)


#There are two obvious outliers due to their pre-emptive starting of their task / distractions. Set their time to query to their avg instead
#and adjust overall time 
participants[12][0]['time'] -= (participants[12][0]['time_to_query'] - (person_avg / person_cnt))
print('removing this many minutes from task 0 ' + str((participants[12][0]['time_to_query'] - (person_avg / person_cnt)) / 60000))
participants[12][3]['time'] -= (participants[12][3]['time_to_query'] - (person_avg / person_cnt))
print('removing this many minutes from task 3 ' + str((participants[12][3]['time_to_query'] - (person_avg / person_cnt)) / 60000))

person_avg = 0
person_cnt = 0
person_times = []
for j, t in enumerate(participants[14]):
    #outliers are after 1 minute, confirmed by manual inspection of this participant
    if (t['time_to_query'] / 60000) < 1:
        person_avg += t['time_to_query']
        person_times.append(t['time_to_query'] / 60000)
        person_cnt += 1

print()
print('p14 avg ' + str(person_avg / person_cnt / 60000))
print(person_times)
#There are four obvious outliers due to their pre-emptive starting of their task / distractions. Set their time to query to their avg instead
#and adjust overall time 
participants[14][0]['time'] -= (participants[14][0]['time_to_query'] - (person_avg / person_cnt))
print('removing this many minutes from task 0 ' + str((participants[14][0]['time_to_query'] - (person_avg / person_cnt)) / 60000))
participants[14][4]['time'] -= (participants[14][4]['time_to_query'] - (person_avg / person_cnt))
print('removing this many minutes from task 4 ' + str((participants[14][4]['time_to_query'] - (person_avg / person_cnt)) / 60000))
participants[14][5]['time'] -= (participants[14][5]['time_to_query'] - (person_avg / person_cnt))
print('removing this many minutes from task 5 ' + str((participants[14][5]['time_to_query'] - (person_avg / person_cnt)) / 60000))
participants[14][5]['time'] -= (participants[14][5]['time_to_query'] - (person_avg / person_cnt))
print('removing this many minutes from task 5 ' + str((participants[14][5]['time_to_query'] - (person_avg / person_cnt)) / 60000))


avg_start /= avg_count

#plt.plot(sorted(alliers), '.')
#plt.show()

print()

print('Average starttask to query ' + str(avg_start / 60000))
#print(len(outliers2))
#print(len(outliers3))
#print(len(outliers4))
#print(len(outliers))
#print(outliers)

tasks = []
for i in range(8):
    tasks.append({  'clicks': 0, 
                    'toggles': "",
                    'numtoggles': 0,
                    'numrelevant': 0,
                    'queries': 0,
                    'starttime':0,
                    'endtime':0,
                    'delays':0,         
                    'time':0,
                    'numtasks':0,
                    'times':[]})
                    
for p, ts in enumerate(participants):

    for t, task in enumerate(ts):
        to = int(task_order[p][t])
            
        if p == 12 and t == 2:
            pass #laptop shut down for a prolonged period during this task
        else:
            if task['time'] == 0:
                print('skipping')
                pass
            tasks[to]['clicks'] += task['clicks']
            tasks[to]['toggles'] += task['toggles']
            tasks[to]['numtoggles'] += task['numtoggles']
            tasks[to]['numrelevant'] += task['numrelevant']
            tasks[to]['queries'] += task['queries']
            tasks[to]['delays'] += task['delays']
            tasks[to]['time'] += task['time']
            tasks[to]['times'].append(task['time'])
            tasks[to]['numtasks'] += 1
            

#We compute the averages in a seperate step so we can more easily control changes that need to happen because
#we have to skip some tasks that were interrupted
for task in tasks:
    task['clicks'] /= task['numtasks']
    task['numrelevant'] /= task['numtasks']
    task['numtoggles'] /= task['numtasks']
    task['queries'] /= task['numtasks']
    task['delays'] /= task['numtasks']
    task['time'] /= task['numtasks']

print('\n\nPer task')
time_total = 0
for i, t in enumerate(tasks):
#    print('Task ' + str(i))
#    print(t)
    print('Average ' + str(t['time'] / 60000) + ' minutes')
    time_total += t['time'] / 60000
    print()
    
print('Average time experiment ' + str(time_total))
   
   
print('\n\nPer condition')

docdoc = {          'clicks': 0, 
                    'toggles': "",
                    'numtoggles': 0,
                    'numrelevant': 0,
                    'queries': 0,
                    'starttime':0,
                    'endtime':0,
                    'delays':0,         
                    'time':0,
                    'numtasks':0,
                    'times':[],
                    'tasks':[],
                    'numactions':[],
                    'fulltasks':[],
                    'ids':[],
                    'taskids':[],
                    'qs':[],
                    'cs':[],
                    'completions':[],
                    'avgcompletion': []}
candoc = {          'clicks': 0, 
                    'toggles': "",
                    'numtoggles': 0,
                    'numrelevant': 0,
                    'queries': 0,
                    'starttime':0,
                    'endtime':0,
                    'delays':0,         
                    'time':0,
                    'numtasks':0,
                    'times':[],
                    'tasks':[],
                    'numactions':[],
                    'fulltasks':[],
                    'ids':[],
                    'taskids':[],
                    'qs':[],
                    'cs':[],
                    'completions':[],
                    'avgcompletion': []}         
cancan = {          'clicks': 0, 
                    'toggles': "",
                    'numtoggles': 0,
                    'numrelevant': 0,
                    'queries': 0,
                    'starttime':0,
                    'endtime':0,
                    'delays':0,         
                    'time':0,
                    'numtasks':0,
                    'times':[],
                    'tasks':[],
                    'numactions':[],
                    'fulltasks':[],
                    'ids':[],
                    'taskids':[],
                    'qs':[],
                    'cs':[],
                    'completions':[],
                    'avgcompletion': []}         
doccan = {          'clicks': 0, 
                    'toggles': "",
                    'numtoggles': 0,
                    'numrelevant': 0,
                    'queries': 0,
                    'starttime':0,
                    'endtime':0,
                    'delays':0,         
                    'time':0,
                    'numtasks':0,
                    'times':[],
                    'tasks':[],
                    'numactions':[],
                    'fulltasks':[],
                    'ids':[],
                    'taskids':[],
                    'qs':[],
                    'cs':[],
                    'completions':[],
                    'avgcompletion': []}         
intcan = {          'clicks': 0, 
                    'toggles': "",
                    'numtoggles': 0,
                    'numrelevant': 0,
                    'queries': 0,
                    'starttime':0,
                    'endtime':0,
                    'delays':0,         
                    'time':0,
                    'numtasks':0,
                    'times':[],
                    'tasks':[],
                    'numactions':[],
                    'fulltasks':[],
                    'ids':[],
                    'taskids':[],
                    'qs':[],
                    'cs':[],
                    'completions':[],
                    'avgcompletion': []}  
intdoc = {          'clicks': 0, 
                    'toggles': "",
                    'numtoggles': 0,
                    'numrelevant': 0,
                    'queries': 0,
                    'starttime':0,
                    'endtime':0,
                    'delays':0,         
                    'time':0,
                    'numtasks':0,
                    'times':[],
                    'tasks':[],
                    'numactions':[],
                    'fulltasks':[],
                    'ids':[],
                    'taskids':[],
                    'qs':[],
                    'cs':[],
                    'completions':[],
                    'avgcompletion': []}  
rankcan = {          'clicks': 0, 
                    'toggles': "",
                    'numtoggles': 0,
                    'numrelevant': 0,
                    'queries': 0,
                    'starttime':0,
                    'endtime':0,
                    'delays':0,         
                    'time':0,
                    'numtasks':0,
                    'times':[],
                    'tasks':[],
                    'numactions':[],
                    'fulltasks':[],
                    'ids':[],
                    'taskids':[],
                    'qs':[],
                    'cs':[],
                    'completions':[],
                    'avgcompletion': []}  
rankdoc = {          'clicks': 0, 
                    'toggles': "",
                    'numtoggles': 0,
                    'numrelevant': 0,
                    'queries': 0,
                    'starttime':0,
                    'endtime':0,
                    'delays':0,         
                    'time':0,
                    'numtasks':0,
                    'times':[],
                    'tasks':[],
                    'numactions':[],
                    'fulltasks':[],
                    'ids':[],
                    'taskids':[],
                    'qs':[],
                    'cs':[],
                    'completions':[],
                    'avgcompletion': []}

def addtask_condition(task, condition, to, i):
    if task['time'] == 0:
        print('skipping2')
        pass
    else:
        condition['clicks'] += task['clicks']
        condition['toggles'] += task['toggles']
        condition['numtoggles'] += task['numtoggles']
        condition['numrelevant'] += task['numrelevant']
        condition['queries'] += task['queries']
        condition['delays'] += task['delays']
        condition['time'] += task['time']
        condition['times'].append(task['time'])
        condition['tasks'].append(to)
        condition['numtasks'] += 1
        condition['numactions'].append(task['clicks'] + task['queries'])
        condition['fulltasks'].append(task)
        condition['ids'].append(i)
        condition['taskids'].append(to)
        condition['qs'].append(task['queries'])
        condition['cs'].append(task['clicks'])

for i, p in enumerate(participants):
    for j, t in enumerate(p):
        
        to = int(task_order[i][j]) 
        if interface_order[i] == 'can':
            if j < 4:
                addtask_condition(t, intcan, to, i)
                if ranking1_order[i] == 'can':
                    addtask_condition(t, cancan, to, i)
                    addtask_condition(t, rankcan, to, i)
                else:
                    addtask_condition(t, rankdoc, to, i)
                    addtask_condition(t, candoc, to, i)
            else:
                addtask_condition(t, intdoc, to, i)
                if ranking2_order[i] == 'can':
                    addtask_condition(t, rankcan, to, i)
                    addtask_condition(t, doccan, to, i)
                else:
                    addtask_condition(t, rankdoc, to, i)
                    addtask_condition(t, docdoc, to, i)
        else:
            if j < 4:
                addtask_condition(t, intdoc, to, i)
                if ranking1_order[i] == 'can':
                    addtask_condition(t, rankcan, to, i)
                    addtask_condition(t, doccan, to, i)
                else:
                    addtask_condition(t, rankdoc, to, i)
                    addtask_condition(t, docdoc, to, i)
            else:
                addtask_condition(t, intcan, to, i)
                if ranking2_order[i] == 'can':
                    addtask_condition(t, rankcan, to, i)
                    addtask_condition(t, cancan, to, i)
                else:
                    addtask_condition(t, rankdoc, to, i)
                    addtask_condition(t, candoc, to, i)

"""
task_order = ['07314625', '15740236', '41605273', '01325746', '30265147', '45760312', '16025734', '30167254', '54326017', '64721503', '60513427', '06324715', '32146057', '21450736', '32461057', '61534720', '02164735', '63157402', '15327460', '42675031', '20174653', '61427053', '42173650', '23701564', '63714520']

interface_order = ['can', 'doc', 'can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can']

ranking1_order = ['can', 'can', 'doc', 'doc', 'can', 'can', 'doc', 'doc', 'can', 'can', 'doc', 'doc', 'can', 'can', 'doc', 'doc', 'can', 'can', 'doc', 'doc', 'can', 'can', 'doc', 'doc', 'can']
ranking2_order = ['doc', 'doc', 'can', 'can', 'can', 'can', 'doc', 'doc', 'doc', 'doc', 'can', 'can', 'can', 'can', 'doc', 'doc', 'doc', 'doc', 'can', 'can', 'can', 'can', 'doc', 'doc', 'doc']
"""

def averagetask_condition(condition):
    condition['clicks'] /= condition['numtasks']
    condition['numrelevant'] /= condition['numtasks']
    condition['numtoggles'] /= condition['numtasks']
    condition['queries'] /= condition['numtasks']
    condition['delays'] /= condition['numtasks']
    condition['time'] /= condition['numtasks']
    
averagetask_condition(docdoc)
averagetask_condition(candoc)
averagetask_condition(doccan)
averagetask_condition(cancan)

averagetask_condition(intdoc)
averagetask_condition(intcan)
averagetask_condition(rankdoc)
averagetask_condition(rankcan)

print('\n\nCondition docdoc')
print(docdoc)
print()
print('Average time ' + str(docdoc['time'] / 60000) + ' minutes')

print('\n\nCondition candoc')
print(candoc)
print()
print('Average time ' + str(candoc['time'] / 60000) + ' minutes')

print('\n\nCondition doccan')
print(doccan)
print()
print('Average time ' + str(doccan['time'] / 60000) + ' minutes')

print('\n\nCondition cancan')
print(cancan)
print()
print('Average time ' + str(cancan['time'] / 60000) + ' minutes')

print('\n\nInterface candidate')
print(cancan)
print()
print('Average time ' + str(intcan['time'] / 60000) + ' minutes')

print('\n\nInterface document')
print(cancan)
print()
print('Average time ' + str(intdoc['time'] / 60000) + ' minutes')

print('\n\nRanking candidate')
print(cancan)
print()
print('Average time ' + str(rankcan['time'] / 60000) + ' minutes')

print('\n\nRanking document')
print(cancan)
print()
print('Average time ' + str(rankdoc['time'] / 60000) + ' minutes')
print()



import statsmodels.api as sm
from statsmodels.formula.api import ols

import numpy as np
import pandas as pd
import math

dataset = []
dataset_log = []
for i, time in enumerate(docdoc['times']):
    dataset.append(['doc', 'doc', docdoc['tasks'][i], docdoc['numactions'][i], time])
    if docdoc['numactions'][i] != 0:
        dataset_log.append(['doc', 'doc', 'docdoc', docdoc['tasks'][i], math.log(docdoc['numactions'][i]), math.log(time), docdoc['ids'][i]])
    
    
for i, time in enumerate(candoc['times']):
    dataset.append(['can', 'doc', candoc['tasks'][i], candoc['numactions'][i], time])
    if candoc['numactions'][i] != 0:
        dataset_log.append(['can', 'doc', 'candoc', candoc['tasks'][i], math.log(candoc['numactions'][i]), math.log(time), candoc['ids'][i]])
    
for i, time in enumerate(doccan['times']):
    dataset.append(['doc', 'can', doccan['tasks'][i], doccan['numactions'][i], time])
    if doccan['numactions'][i] != 0:
        dataset_log.append(['doc', 'can', 'doccan', doccan['tasks'][i], math.log(doccan['numactions'][i]), math.log(time), doccan['ids'][i]])
    
for i, time in enumerate(cancan['times']):
    dataset.append(['can', 'can', cancan['tasks'][i], cancan['numactions'][i], time])
    if cancan['numactions'][i] != 0:
        dataset_log.append(['can', 'can', 'cancan', cancan['tasks'][i], math.log(cancan['numactions'][i]), math.log(time), cancan['ids'][i]])


df = pd.DataFrame(data=dataset, columns=['interface','ranking','task','numactions','time'])
df2 = pd.DataFrame(data=dataset_log, columns=['interface','ranking','condition','task','numactions','time', 'pid'])
print(df)

print()
print()
#partial eta is SS_effect / (SS_effect + SS_residuals)

#sm.stats.anova_lm



from statsmodels.stats.multicomp import pairwise_tukeyhsd
# perform Tukey's test
tukey = pairwise_tukeyhsd(endog=df2['time'],
                          groups=df2['condition'],
                          alpha=0.05)
                          
print()
print()
print()
print('tukey groups')
print(tukey)


print()
print()
print()
print('tukey ranking only')
tukey = pairwise_tukeyhsd(endog=df2['time'],
                          groups=df2['ranking'],
                          alpha=0.05)
print(tukey)

print('avg')
dt  = df2[df2['ranking'] == 'doc']['time']
ct = df2[df2['ranking'] == 'can']['time']
print(sum(dt)/len(dt))
print(sum(ct)/len(ct))
print()
print()

print('\n\nNormality assumption test on transofrmed - unsignificant p value means the assumption holds')
print(stats.shapiro(model.resid))
print()

print(len(docdoc['times']))
print(len(doccan['times']))
print(len(candoc['times']))
print(len(cancan['times']))


print('Variance assumption test - unsignificant p value means the assumption holds')
print('F(' + str(4 - 1) + ", " + str(len(docdoc['times'])+len(candoc['times'])+len(doccan['times'])+len(cancan['times']) - 4) + ')')
print(stats.levene([math.log(x) for x in docdoc['times']],
    [math.log(x) for x in candoc['times']],
    [math.log(x) for x in doccan['times']],
    [math.log(x) for x in cancan['times']]))

#print(stats.levene(model.resid))    


from statsmodels.graphics.factorplots import interaction_plot
print(df2['interface'])

fig, ax = plt.subplots(figsize=(6, 6))
fig = interaction_plot(
    x=df2['interface'],
    trace=df2['ranking'],
    response=df2['time'],
    colors=["red", "blue"],
    markers=["D", "^"],
    ms=10,
    ax=ax,
)

#plt.show()
from time import sleep

#sleep(60)

print()
print()
print()
print()
print()


print()
print()
#print('mixed factor anova')
#import pingouin as pg
#pg.mixed_anova(dv='time', between='ranking', within='interface', subject='pid', data=df2)


print('lets try durbin')
#Durbin’s test whether k groups (or treatments) in a two-way balanced incomplete block design (BIBD) have identical effects. See references for additional information
#https://scikit-posthocs.readthedocs.io/en/latest/generated/scikit_posthocs.test_durbin/?highlight=durbin




#d = [docdoc['numactions'], doccan['numactions'], candoc['numactions'], cancan['numactions']]

#print('p value, statistic, degrees of freedom')
#print(sp.test_durbin(d))
#print()
#print()
#print(sp.posthoc_durbin(d))

#In the case of an two-way balanced incomplete block design, the Durbin test can be employed. The H0 is rejected, if at least one group (treatment) is significantly different.


#Test ANOVA assumptions
#https://www.pythonfordatascience.org/anova-python/

print('\n\nNormality assumption test - unsignificant p value means the assumption holds')
print(stats.shapiro(model.resid))
print()
#we fail the shapiro test - it seems not normally distributed per condition - let's plot?


fig = plt.figure(figsize= (10, 10))
ax = fig.add_subplot(111)

normality_plot, stat = stats.probplot(model.resid, plot= plt, rvalue= True)
ax.set_title("Probability plot of model residual's", fontsize= 20)
ax.set

#plt.show()

data = [    docdoc['times'],
             candoc['times'],
             doccan['times'],
             cancan['times']]
             

print('Variance assumption test - unsignificant p value means the assumption holds')
print(stats.levene(docdoc['times'],
             candoc['times'],
             doccan['times'],
             cancan['times']))
print()
             
fig = plt.figure(figsize= (5, 2.5))
ax = fig.add_subplot(111)

import copy
#data in minutes instead of ms
datamin = copy.deepcopy(data)

for indi, i in enumerate(data):
    for indj, j in enumerate(i):
        datamin[indi][indj] = (data[indi][indj] / 1000)/60
print(data)
print(datamin)



bp = ax.violinplot(datamin, showmedians=True,showextrema=True)
plt.xticks([1,2,3,4],['doc interface' + '\n' +' doc ranking', 'can interface ' + '\n' + 'doc ranking', 'doc interface ' + '\n' + 'can ranking', 'can interface ' + '\n' + 'can ranking'])
#           showmeans= True)
ax.set_ylabel('Task completion time (min)')
#ax.legend([bp['medians'][0], bp['means'][0]], ['median', 'mean'])

#plt.show()


#Let's test number of actions instead
print('number of actions')
print('docdoc ' + str(sum(docdoc['numactions']) / len(docdoc['numactions'])))
print('candoc ' + str(sum(candoc['numactions']) / len(candoc['numactions'])))
print('doccan ' + str(sum(doccan['numactions']) / len(doccan['numactions'])))
print('cancan ' + str(sum(cancan['numactions']) / len(cancan['numactions'])))
print()
print('doc interface ' + str(sum(intdoc['numactions']) / len(intdoc['numactions'])))
print('can interface ' + str(sum(intcan['numactions']) / len(intcan['numactions'])))
print('doc ranking ' + str(sum(rankdoc['numactions']) / len(rankdoc['numactions'])))
print('can ranking ' + str(sum(rankcan['numactions']) / len(rankcan['numactions'])))


print()
print('Testing ANOVA assumptions')
print(stats.shapiro(model.resid))
print(stats.levene(docdoc['numactions'],
             candoc['numactions'],
             doccan['numactions'],
             cancan['numactions']))
             

fig = plt.figure(figsize= (10, 10))
ax = fig.add_subplot(111)

normality_plot, stat = stats.probplot(model.resid, plot= plt, rvalue= True)
ax.set_title("Probability plot of model residual's", fontsize= 20)
ax.set

#plt.show()

plt.clf()

print()
print()
#let's check   times people stopped searching
docdoc['times'].sort()
docdoc['times'] = [x / 60000 for x in docdoc['times']]
candoc['times'].sort()
candoc['times'] = [x / 60000 for x in candoc['times']]
doccan['times'].sort()
doccan['times'] = [x / 60000 for x in doccan['times']]
cancan['times'].sort()
cancan['times'] = [x / 60000 for x in cancan['times']]

#subplot test
plt.plot(docdoc['times'])
plt.plot(doccan['times'])
plt.plot(candoc['times'])
plt.plot(cancan['times'])
#fig, axs = plt.subplots(2, 2)
#axs[0,0].plot(docdoc['times'])
#axs[0,1].plot(doccan['times'])
#axs[1,0].plot(candoc['times'])
#axs[1,1].plot(cancan['times'])

#plt.show()


#alternative methods?        
#https://www.statisticssolutions.com/what-to-do-when-the-assumptions-of-your-analysis-are-violated/





#Okay now, let's play with the response data
print('\n\n\nResponse data')

responses = pd.read_csv('responses20.csv', header=0, encoding='ANSI', delimiter=';')

#for line in responses:
#    print(line)

print()

rdocdoc = { 'zekerheid':0,
            'zekerheids':[],
          'sus':[],
          'avg_sus':0,
          'numanswers':0,
          'snap':0,
          'snaps':[],
          'fijn':0,
          'feedback':'',
          'ids':[],
          }
rdoccan = { 'zekerheid':0,
            'zekerheids':[],
          'sus':[],
          'avg_sus':0,
          'numanswers':0,
          'snap':0,
          'snaps':[],
          'fijn':0,
          'feedback':''
        }
rcandoc = { 'zekerheid':0,
            'zekerheids':[],
          'sus':[],
          'avg_sus':0,
          'numanswers':0,
          'snap':0,
          'snaps':[],
          'fijn':0,
          'feedback':''
        }
rcancan = { 'zekerheid':0,
            'zekerheids':[],
          'sus':[],
          'avg_sus':0,
          'numanswers':0,
          'snap':0,
          'snaps':[],
          'fijn':0,
          'feedback':''
        }
rintcan = { 'zekerheid':0,
            'zekerheids':[],
          'sus':[],
          'avg_sus':0,
          'numanswers':0,
          'snap':0,
          'snaps':[],
          'fijn':0,
          'feedback':''
        }
rintdoc = { 'zekerheid':0,
            'zekerheids':[],
          'sus':[],
          'avg_sus':0,
          'numanswers':0,
          'snap':0,
          'snaps':[],
          'fijn':0,
          'feedback':''
        }
rrankdoc = { 'zekerheid':0,
            'zekerheids':[],
          'sus':[],
          'avg_sus':0,
          'numanswers':0,
          'snap':0,
          'snaps':[],
          'fijn':0,
          'feedback':''
        }
rrankcan = { 'zekerheid':0,
            'zekerheids':[],
          'sus':[],
          'avg_sus':0,
          'numanswers':0,
          'snap':0,
          'snaps':[],
          'fijn':0,
          'feedback':''
        }
        

def addanswer(row, condition, order):
    #if can first
    if order == 1:
        condition['zekerheid'] += int(row[3])
        condition['zekerheids'].append(int(row[3]))
        if row[4].is_integer():
            condition['snaps'].append(int(row[4]))
        condition['fijn'] += int(row[5])
        sus = 2.5*(int(row[6]) + int(row[7]) + int(row[8]) + int(row[9]) + int(row[10]) + int(row[11]) + int(row[12]) + int(row[13]) + int(row[14]) + int(row[15]))
        condition['sus'].append(sus)
        susbefore.append(sus)
    else:
        condition['zekerheid'] += int(row[17])
        condition['zekerheids'].append(int(row[17]))
        condition['fijn'] += int(row[18])
        sus = 2.5*(int(row[20]) + int(row[21]) + int(row[22]) + int(row[23]) + int(row[24]) + int(row[25]) + int(row[26]) + int(row[27]) + int(row[28]) + int(row[19]))
        condition['sus'].append(sus)
        susafter.append(sus)
        
    condition['numanswers'] += 1
        
        
        
        
sorted_preferences = {}
sorted_sus = {}
preferences = []
susbefore = []
susafter = []
for j, t in responses.iterrows():

    if j < 21:
        print('hi')
        i = j

        if i == 19:  #aligning questionnaire results w/ log results        
            i = 1
    #        print('HERE')
    #        print(t)
    #        pass;
        if i == 20:
            i = 19

        #p10 used the system incorrectly 
        if i == 10:
            pass
            
            
        if interface_order[i] == 'can':
            preferences.append(['can'+str(ranking1_order[i]), 'doc' + str(ranking2_order[i]), int(t[30]), t[31], t[32]])
        else:
            print(ranking1_order[i])
            print(ranking2_order[i])
            print(t)
            preferences.append(['doc'+str(ranking1_order[i]), 'can' + str(ranking2_order[i]), int(t[30]), t[31], t[32]])
        
        
        #in between this other stuff, lets store the system preference per participant id
        if interface_order[i] == 'can':
            if int(t[30]) < 3:
                sorted_preferences[i] = 'can'
                sorted_sus[i] = 2.5*(int(t[6]) + int(t[7]) + int(t[8]) + int(t[9]) + int(t[10]) + int(t[11]) + int(t[12]) + int(t[13]) + int(t[14]) + int(t[15]))
            elif int(t[30]) > 3:
                sorted_preferences[i] = 'doc'
                sorted_sus[i] = 2.5*(int(t[6]) + int(t[7]) + int(t[8]) + int(t[9]) + int(t[10]) + int(t[11]) + int(t[12]) + int(t[13]) + int(t[14]) + int(t[15]))
            else:
                sorted_preferences[i] = 'tie'
                sorted_sus[i] = 2.5*(int(t[6]) + int(t[7]) + int(t[8]) + int(t[9]) + int(t[10]) + int(t[11]) + int(t[12]) + int(t[13]) + int(t[14]) + int(t[15]))
        else:
            if int(t[30]) < 3:
                sorted_preferences[i] = 'doc'
                sorted_sus[i] = 2.5*(int(t[6]) + int(t[7]) + int(t[8]) + int(t[9]) + int(t[10]) + int(t[11]) + int(t[12]) + int(t[13]) + int(t[14]) + int(t[15]))
            elif int(t[30]) > 3:
                sorted_preferences[i] = 'can'
                sorted_sus[i] = 2.5*(int(t[6]) + int(t[7]) + int(t[8]) + int(t[9]) + int(t[10]) + int(t[11]) + int(t[12]) + int(t[13]) + int(t[14]) + int(t[15]))
            else:
                sorted_preferences[i] = 'tie'
                sorted_sus[i] = 2.5*(int(t[6]) + int(t[7]) + int(t[8]) + int(t[9]) + int(t[10]) + int(t[11]) + int(t[12]) + int(t[13]) + int(t[14]) + int(t[15]))
        
        
        if interface_order[i] == 'can':
                addanswer(t, rintcan, 1)
                if ranking1_order[i] == 'can':
                    addanswer(t, rcancan, 1)
                    addanswer(t, rrankcan, 1)
                else:
                    addanswer(t, rrankdoc, 1)
                    addanswer(t, rcandoc, 1)
                addanswer(t, rintdoc, 2)
                if ranking2_order[i] == 'can':
                    addanswer(t, rrankcan, 2)
                    addanswer(t, rdoccan, 2)
                else:
                    addanswer(t, rrankdoc, 2)
                    addanswer(t, rdocdoc, 2)
        else:
                addanswer(t, rintdoc, 1)
                if ranking1_order[i] == 'can':
                    addanswer(t, rrankcan, 1)
                    addanswer(t, rdoccan, 1)
                else:
                    addanswer(t, rrankdoc, 1)
                    addanswer(t, rdocdoc, 1)
                addanswer(t, rintcan, 2)
                if ranking2_order[i] == 'can':
                    addanswer(t, rrankcan, 2)
                    addanswer(t, rcancan, 2)
                else:
                    addanswer(t, rrankdoc, 2)
                    addanswer(t, rcandoc, 2)

def avganswers(condition):
    condition['zekerheid'] /= condition['numanswers']
    condition['avg_sus'] = sum(condition['sus']) / len(condition['sus'])
    condition['fijn'] /= condition['numanswers']
    condition['snap'] = sum(condition['snaps']) / len(condition['snaps'])

avganswers(rdocdoc)
avganswers(rcandoc)
avganswers(rdoccan)
avganswers(rcancan)

avganswers(rintdoc)
avganswers(rintcan)
avganswers(rrankdoc)
avganswers(rrankcan)

"""
print('doc doc')
print(rdocdoc)
print('can doc')
print(rcandoc)
print('doc can')
print(rdoccan)
print('can can')
print(rcancan)
"""



rdataset = []
for i, sus in enumerate(rdocdoc['sus']):
    rdataset.append(['doc', 'doc', rdocdoc['zekerheids'][i], sus])
    
for i, sus in enumerate(rcandoc['sus']):
    rdataset.append(['can', 'doc', rcandoc['zekerheids'][i], sus])
    
for i, sus in enumerate(rdoccan['sus']):
    rdataset.append(['doc', 'can', rdoccan['zekerheids'][i], sus])
    
for i, sus in enumerate(rcancan['sus']):
    rdataset.append(['can', 'can', rcancan['zekerheids'][i], sus])

rdf = pd.DataFrame(data=rdataset, columns=['interface','ranking','zekerheid','sus'])
print(df)

print('Average SUS, fijn and zekerheid scores for conditions')
print('doc doc')
print(rdocdoc['avg_sus'])
print(rdocdoc['fijn'])
print(rdocdoc['zekerheid'])
print()
print('doc can')
print(rdoccan['avg_sus'])
print(rdoccan['fijn'])
print(rdoccan['zekerheid'])
print()
print('can doc')
print(rcandoc['avg_sus'])
print(rcandoc['fijn'])
print(rcandoc['zekerheid'])
print()
print('can can')
print(rcancan['avg_sus'])
print(rcancan['fijn'])
print(rcancan['zekerheid'])
print()
print('doc interface')
print(rintdoc['avg_sus'])
print(rintdoc['fijn'])
print(rintdoc['zekerheid'])
print()
print('can interface')
print(rintcan['avg_sus'])
print(rintcan['fijn'])
print(rintcan['zekerheid'])
print()
print('doc ranking')
print(rrankdoc['avg_sus'])
print(rrankdoc['fijn'])
print(rrankdoc['zekerheid'])
print()
print('can ranking')
print(rrankcan['avg_sus'])
print(rrankcan['fijn'])
print(rrankcan['zekerheid'])
print()

print()
print()
print()
print()
print()
print()
print()
print()
print()



print()
print('\n\nNormality assumption test SUS - unsignificant p value means the assumption holds')
print(stats.shapiro(model.resid))

print('Variance assumption test - unsignificant p value means the assumption holds')
#print('F(' + str(4 - 1) + ", " + str(len(docdoc['sus'])+len(candoc['sus'])+len(doccan['sus'])+len(cancan['sus']) - 4) + ')')
print(stats.levene([x for x in rdocdoc['sus']],
    [x for x in rdoccan['sus']],
    [x for x in rcandoc['sus']],
    [x for x in rcancan['sus']]))
    



print('\n\nPairwise preferences')

#construct a dataset with all responses
rdataset = []
for i, row in enumerate(rdocdoc):
    rdataset.append('hi')





#Average preference interface
#Average preference ranking
#TODO look for pairwise preference stuff online
print(preferences)

def compare_binary(cond1, cond2, ps=preferences):
    count = 0
    found = 0
    if cond1 == cond2:
        return '-'
    for p in ps:
        if p[0] == cond1 and p[1] == cond2:
            found += 1
            count += 1
        if p[0] == cond2 and p[1] == cond1:
            found += 1
            count -= 1

    if found == 0:
        return 'x'
    return str(count / found)




def compare(cond1, cond2, ps=preferences):
    count = 0
    found = 0
    if cond1 == cond2:
        return '-'
    for p in ps:
        if p[0] == cond1 and p[1] == cond2:
            found += 1
            count += 1- (p[2] / 5)
    if found == 0:
        return 'x'
    return str(count / found)

def compare_avg(cond1, cond2, ps=preferences):
    count = 0
    found = 0
    if cond1 == cond2:
        return '-'
    for p in ps:
        if p[0] == cond1 and p[1] == cond2:
            found += 1
            count += 1 - (p[2] / 5)
        if p[0] == cond2 and p[1] == cond1:
            found += 1
            count += abs((p[2] / 5))

    if found == 0:
        return 'x'
    return str(count / found)

print()
print('Pairwise comparisons: row system 1, column system 2')
print(' interface ')
print('      docdoc    candoc    doccan   cancan')
print('docdoc  ' + compare('docdoc', 'docdoc') + '          ' + compare('docdoc', 'candoc') + '         ' + compare('docdoc', 'doccan') + '        ' + compare('docdoc', 'cancan'))
print('candoc  ' + compare('candoc', 'docdoc') + '          ' + compare('candoc', 'candoc') + '         ' + compare('candoc', 'doccan') + '        ' + compare('candoc', 'cancan'))
print('doccan  ' + compare('doccan', 'docdoc') + '          ' + compare('doccan', 'candoc') + '         ' + compare('doccan', 'doccan') + '        ' + compare('doccan', 'cancan'))
print('cancan  ' + compare('cancan', 'docdoc') + '          ' + compare('cancan', 'candoc') + '         ' + compare('cancan', 'doccan') + '        ' + compare('cancan', 'cancan'))

print()
print()
print('Pairwise comparisons averaged')
print('      docdoc    candoc    doccan   cancan')
print('docdoc  ' + compare_avg('docdoc', 'docdoc') + '          ' + compare_avg('docdoc', 'candoc') + '         ' + compare_avg('docdoc', 'doccan') + '        ' + compare_avg('docdoc', 'cancan'))
print('candoc  ' + compare_avg('candoc', 'docdoc') + '          ' + compare_avg('candoc', 'candoc') + '         ' + compare_avg('candoc', 'doccan') + '        ' + compare_avg('candoc', 'cancan'))
print('doccan  ' + compare_avg('doccan', 'docdoc') + '          ' + compare_avg('doccan', 'candoc') + '         ' + compare_avg('doccan', 'doccan') + '        ' + compare_avg('doccan', 'cancan'))
print('cancan  ' + compare_avg('cancan', 'docdoc') + '          ' + compare_avg('cancan', 'candoc') + '         ' + compare_avg('cancan', 'doccan') + '        ' + compare_avg('cancan', 'cancan'))

print()
print()

print('Binary pairwise comparisons averaged')
print('      docdoc    candoc    doccan   cancan')
print('docdoc  ' + compare_binary('docdoc', 'docdoc') + '          ' + compare_binary('docdoc', 'candoc') + '         ' + compare_binary('docdoc', 'doccan') + '        ' + compare_binary('docdoc', 'cancan'))
print('candoc  ' + compare_binary('candoc', 'docdoc') + '          ' + compare_binary('candoc', 'candoc') + '         ' + compare_binary('candoc', 'doccan') + '        ' + compare_binary('candoc', 'cancan'))
print('doccan  ' + compare_binary('doccan', 'docdoc') + '          ' + compare_binary('doccan', 'candoc') + '         ' + compare_binary('doccan', 'doccan') + '        ' + compare_binary('doccan', 'cancan'))
print('cancan  ' + compare_binary('cancan', 'docdoc') + '          ' + compare_binary('cancan', 'candoc') + '         ' + compare_binary('cancan', 'doccan') + '        ' + compare_binary('cancan', 'cancan'))




print('\nAverage preference for the second system')
lst = [x[2] for x in preferences]
print(sum(lst) / len(lst))
#print('thats huge!')

print(sum(susbefore) / len(susbefore))
print(sum(susafter) / len(susafter))

def avg_preference(condition):
    p = 0
    c = compare_avg(condition, 'docdoc')
    if c != 'x' and c != '-':
        p += float(c)
        
    c = compare_avg(condition, 'doccan')
    if c != 'x' and c != '-':
        p += float(c)

    c = compare_avg(condition, 'candoc')
    if c != 'x' and c != '-':
        p += float(c)

    c = compare_avg(condition, 'cancan')
    if c != 'x' and c != '-':
        p += float(c)

    return str(p / 2.0)
    
def avg_preference_count(condition):
    p = 0
    c = compare_avg(condition, 'docdoc')
    if c != 'x' and c != '-':
        if float(c) > 2.5:
            p += 1
        
    c = compare_avg(condition, 'doccan')
    if c != 'x' and c != '-':
        if float(c) > 2.5:
            p += 1

    c = compare_avg(condition, 'candoc')
    if c != 'x' and c != '-':
        if float(c) > 2.5:
            p += 1

    c = compare_avg(condition, 'cancan')
    if c != 'x' and c != '-':
        if float(c) > 2.5:
            p += 1

    return str(p / 2.0)

print()
print('Average preference score')
print('docdoc ' + avg_preference('docdoc'))
print('doccan ' + avg_preference('doccan'))
print('candoc ' + avg_preference('candoc'))
print('cancan ' + avg_preference('cancan'))
print()
print('Average preference - only choices score')
print('docdoc ' + avg_preference_count('docdoc'))
print('doccan ' + avg_preference_count('doccan'))
print('candoc ' + avg_preference_count('candoc'))
print('cancan ' + avg_preference_count('cancan'))
print()
print()



#Make the table
print('      Condition       |   Effectiveness   |                Efficiency                |     User satisfaction      |')
print('Interface    Ranking  |                   |  Time (m)   queries   clicks   #actions  |   SUS   Zekerheid   Fijn   |') 
print('   doc         doc    |                   |    ' + str(round(docdoc['time'] / 60000, 2)) + '      ' + str(round(docdoc['queries'], 2)) + "      " + str(round(docdoc['clicks'], 2)) + "      " + str(round(docdoc['queries'] + docdoc['clicks'], 2)) + '    |  ' + str(round(rdocdoc['avg_sus'], 2)) + '     ' + str(round(rdocdoc['zekerheid'], 2))  + '       ' + str(round(rdocdoc['fijn'], 2)) + '  |')
print('   doc         can    |                   |    ' + str(round(doccan['time'] / 60000, 2)) + '      ' + str(round(doccan['queries'], 2)) + "      " + str(round(doccan['clicks'], 2)) + "      " + str(round(doccan['queries'] + doccan['clicks'], 2)) + '    |  ' + str(round(rdoccan['avg_sus'], 2)) + '     ' + str(round(rdoccan['zekerheid'], 2))  + '      ' + str(round(rdoccan['fijn'], 2)) + '  |')
print('   can         doc    |                   |    ' + str(round(candoc['time'] / 60000, 2)) + '      ' + str(round(candoc['queries'], 2)) + "      " + str(round(candoc['clicks'], 2)) + "      " + str(round(candoc['queries'] + candoc['clicks'], 2)) + '    |  ' + str(round(rcandoc['avg_sus'], 2)) + '     ' + str(round(rcandoc['zekerheid'], 2))  + '       ' + str(round(rcandoc['fijn'], 2)) + ' |')
print('   can         can    |                   |    ' + str(round(cancan['time'] / 60000, 2)) + '      ' + str(round(cancan['queries'], 2)) + "      " + str(round(cancan['clicks'], 2)) + "      " + str(round(cancan['queries'] + cancan['clicks'], 2)) + '    |  ' + str(round(rcancan['avg_sus'], 2)) + '      ' + str(round(rcancan['zekerheid'], 2))  + '       ' + str(round(rcancan['fijn'], 2)) + ' |')

print()
print()


#Look in overlap of experts toggled


print('Quick test to compare numactions per interface')
print('docdoc ' + str(sum(docdoc['numactions']) / len(docdoc['numactions'])))
print('candoc ' + str(sum(candoc['numactions']) / len(candoc['numactions'])))
print('doccan ' + str(sum(doccan['numactions']) / len(doccan['numactions'])))
print('cancan ' + str(sum(cancan['numactions']) / len(cancan['numactions'])))

print(( sum(docdoc['numactions']) / len(docdoc['numactions']) + sum(doccan['numactions']) / len(doccan['numactions']) )/ 2)
print(( sum(candoc['numactions']) / len(candoc['numactions']) + sum(cancan['numactions']) / len(cancan['numactions']) )/ 2)


print()
print('clicks')
print('docdoc ' + str(docdoc['clicks']))
print('candoc ' + str(candoc['clicks']))
print('doccan ' + str(doccan['clicks']))
print('cancan ' + str(cancan['clicks']))


#['cancan', 'doccan', 2] ['cancan', 'doccan', 4]
#['doccan', 'cancan', 5] ['doccan', 'cancan', 1]


print()
print()
print()
print()
print('Lets check out user preferences per interface')
print('(commented)')


def feedback(cond1, cond2, v=3, ps=preferences):
    i = 3#detault value: system preference description
    if v == 'behaviour':
        i = 4

    count = 0
    found = 0
    if cond1 == cond2:
        return 'No comparisons available'
    for p in ps:
        if p[0] == cond1 and p[1] == cond2:
            print(str(p[0]) + " " + str(p[2]) + " " + str(p[1]) + "   " + str(p[i]))
            found += 1
            count += p[2]
    if found == 0:
        return 'No comparisons available'
#    return str(count / found)


    
# more experience searching for experts? 
# hypothesis: less secure users want longer snippets?





#print('Lets investigate candoc, because it seems to do so well')
#print(candoc['ids'])
#for t in candoc['fulltasks']:
#    print()
#    print(t)
#    print()
    
print()
print()
print()

print('Onderzoek: wat is het verschil tussen mensen die candidate preferren, mensen die doc preferren?')


rs = []
for line in responses.iterrows():
    rs.append(line)

#print(rs[1][1][2])




#lazy late night (deadline) programming: copy paste previous code and do slight adjustment




def add_fan(condition, row, order, p):
    condition['names'].append(row[2])
    if order == 1:
    
        condition['zekerheids'].append(int(row[3]))
        condition['fijns'].append(int(row[5]))
        condition['sus_loves'].append(2.5*(int(row[6]) + int(row[7]) + int(row[8]) + int(row[9]) + int(row[10]) + int(row[11]) + int(row[12]) + int(row[13]) + int(row[14]) + int(row[15])))
        
        cnt = 0
        c = 0
        q = 0
        t = 0
        if p[0]['time'] != 0:
            cnt += 1
            t += p[0]['time']
            c += p[0]['clicks']
            q += p[0]['queries']
             
        if p[1]['time'] != 0:
            cnt += 1
            t += p[1]['time']
            c += p[1]['clicks']
            q += p[1]['queries']
        if p[2]['time'] != 0:
            cnt += 1
            t += p[2]['time']
            c += p[2]['clicks']
            q += p[2]['queries']
        if p[3]['time'] != 0:
            cnt += 1
            t += p[3]['time']
            c += p[2]['clicks']
            q += p[2]['queries']
        if cnt != 0:
            condition['times'].append(t / cnt / 60000)
            condition['clicks'].append(c / cnt)
            condition['queries'].append(q / cnt)
        
#        condition['times'].append(p[0]['time']     ['times'][:3] / 3)
    else:
        
        condition['zekerheids'].append(int(row[17]))
        condition['fijns'].append(int(row[18]))
        condition['sus_loves'].append(2.5*(int(row[20]) + int(row[21]) + int(row[22]) + int(row[23]) + int(row[24]) + int(row[25]) + int(row[26]) + int(row[27]) + int(row[28]) + int(row[19])))

        cnt = 0
        c = 0
        q = 0
        t = 0
        if p[4]['time'] != 0:
            cnt += 1
            t += p[4]['time']
            c += p[4]['clicks']
            q += p[4]['queries']
             
        if p[5]['time'] != 0:
            cnt += 1
            t += p[5]['time']
            c += p[5]['clicks']
            q += p[5]['queries']
        if p[6]['time'] != 0:
            cnt += 1
            t += p[6]['time']
            c += p[6]['clicks']
            q += p[6]['queries']
        if p[7]['time'] != 0:
            cnt += 1
            t += p[7]['time']
            c += p[7]['clicks']
            q += p[7]['queries']
        if cnt != 0:
            condition['times'].append(t / cnt / 60000)
            condition['clicks'].append(c / cnt)
            condition['queries'].append(q / cnt)

cans = {'names':[],
        'times':[],
        'clicks':[],
        'queries':[],
        'sus_loves':[],
        'fijns':[],
        'zekerheids':[]
        }
docs = {'names':[],
        'times':[],
        'clicks':[],
        'queries':[],
        'sus_loves':[],
        'fijns':[],
        'zekerheids':[]
}

alldocs = {'names':[],
        'times':[],
        'clicks':[],
        'queries':[],
        'sus_loves':[],
        'fijns':[],
        'zekerheids':[]
        }

allcans = {'names':[],
        'times':[],
        'clicks':[],
        'queries':[],
        'sus_loves':[],
        'fijns':[],
        'zekerheids':[]
}

zdocdoc = {'names':[],
        'times':[],
        'clicks':[],
        'queries':[],
        'sus_loves':[],
        'fijns':[],
        'zekerheids':[]
}

zdoccan = {'names':[],
        'times':[],
        'clicks':[],
        'queries':[],
        'sus_loves':[],
        'fijns':[],
        'zekerheids':[]
}

zcandoc = {'names':[],
        'times':[],
        'clicks':[],
        'queries':[],
        'sus_loves':[],
        'fijns':[],
        'zekerheids':[]
}

zcancan = {'names':[],
        'times':[],
        'clicks':[],
        'queries':[],
        'sus_loves':[],
        'fijns':[],
        'zekerheids':[]
}

nofans = 0
allfans = 0
can_strongfans = 0
doc_strongfans = 0

for j, p in enumerate(preferences):
    if j == 19: # ignore second performance of task 1
        pass
    else:
        i = j
        if i == 20:
            i = 19
    
        allfans += 1
        
        if p[0][:3] == 'doc':
            add_fan(alldocs, rs[i][1], 1, participants[i])
        else:
            add_fan(allcans, rs[i][1], 1, participants[i])

        if p[1][:3] == 'doc':
            add_fan(alldocs, rs[i][1], 2, participants[i])
        else:
            add_fan(allcans, rs[i][1], 2, participants[i])

    
    
        if p[2] == 1 or p[2] == 2:
            if p[0][:3] == 'doc':
                add_fan(docs, rs[i][1], 1, participants[i])
                if p[2] == 1:
                    doc_strongfans += 1
            else:
                add_fan(cans, rs[i][1], 1, participants[i])
                if p[2] == 1:
                    can_strongfans +=1
                
                
            if p[0] == 'docdoc':
                add_fan(zdocdoc, rs[i][1], 1, participants[i])
            if p[0] == 'candoc':
                add_fan(zcandoc, rs[i][1], 1, participants[i])
            if p[0] == 'doccan':
                add_fan(zdoccan, rs[i][1], 1, participants[i])
            if p[0] == 'cancan':
                add_fan(zcancan, rs[i][1], 1, participants[i])

                
                
        elif p[2] == 5 or p[2] == 4:
            if p[1][:3] == 'doc':
                add_fan(docs, rs[i][1], 2, participants[i])
                if p[2] == 5:
                    doc_strongfans += 1
            else:
                add_fan(cans, rs[i][1], 2, participants[i])
                if p[2] == 5:
                    can_strongfans +=1



            if p[1] == 'docdoc':
                add_fan(zdocdoc, rs[i][1], 2, participants[i])
            if p[1] == 'candoc':
                add_fan(zcandoc, rs[i][1], 2, participants[i])
            if p[1] == 'doccan':
                add_fan(zdoccan, rs[i][1], 2, participants[i])
            if p[1] == 'cancan':
                add_fan(zcancan, rs[i][1], 2, participants[i])
                
                
        

        else:
            print(p)
            print('No fans!')
            nofans += 1
            
        
            
        
#    print(p)

print()
#print('doc lovers ' + str(docs))
#print('can kickers ' + str(cans))

print()
print('lets check some seperate factors')
print()
print()

print('times doc ' + str(sum(docs['times']) / len(docs['times'])) + ' can ' + str(sum(cans['times']) / len(cans['times'])))
print('queries doc ' + str(sum(docs['queries']) / len(docs['queries'])) + ' can ' + str(sum(cans['queries']) / len(cans['queries'])))
print('clicks doc ' + str(sum(docs['clicks']) / len(docs['clicks'])) + ' can ' + str(sum(cans['clicks']) / len(cans['clicks'])))
print('zekerheids doc ' + str(sum(docs['zekerheids']) / len(docs['zekerheids'])) + ' can ' + str(sum(cans['zekerheids']) / len(cans['zekerheids'])))
print()

#print(alldocs)
print('times doc ' + str(sum(alldocs['times']) / len(alldocs['times'])) + ' allcans ' + str(sum(allcans['times']) / len(allcans['times'])))
print('queries doc ' + str(sum(alldocs['queries']) / len(alldocs['queries'])) + ' allcans ' + str(sum(allcans['queries']) / len(allcans['queries'])))
print('clicks doc ' + str(sum(alldocs['clicks']) / len(alldocs['clicks'])) + ' allcans ' + str(sum(allcans['clicks']) / len(allcans['clicks'])))
print('zekerheids doc ' + str(sum(alldocs['zekerheids']) / len(alldocs['zekerheids'])) + ' allcans ' + str(sum(allcans['zekerheids']) / len(allcans['zekerheids'])))
print()
print()
print()

print('no votes ' + str(nofans))
print('docdoc zekerheid ' + str(sum(zdocdoc['zekerheids']) / len(zdocdoc['zekerheids'])) + ' votes' + str(len(zdocdoc['zekerheids']) / allfans))
print('doccan zekerheid ' + str(sum(zdoccan['zekerheids']) / len(zdoccan['zekerheids'])) + ' votes' + str(len(zdoccan['zekerheids']) / allfans))
print('candoc zekerheid ' + str(sum(zcandoc['zekerheids']) / len(zcandoc['zekerheids'])) + ' votes' + str(len(zcandoc['zekerheids']) / allfans))
print('cancan zekerheid ' + str(sum(zcancan['zekerheids']) / len(zcancan['zekerheids'])) + ' votes' + str(len(zcancan['zekerheids']) / allfans))
#print('zekerheids docdoc ' + str(sum(docs['zekerheids']) / len(docs['zekerheids'])) + ' can ' + str(sum(cans['zekerheids']) / len(cans['zekerheids'])))

print()
print('We find that fans feel are more confident on their chosen system')
print((4.3 + 4.0) / 2)
print((3.8421052631578947 + 3.789473684210526) / 2)


print('lets try non-parametric two-way anova alternative on time ')
print()
print()

from scipy import stats
#print(len(docdoc['times'][:32]))
#print(len(candoc['times'][:32]))
#print(len(cancan['times'][:32]))
#print(len(doccan['times'][:32]))

times = list(docdoc['times'])
times.extend(candoc['times'])
times.extend(doccan['times'])
times.extend(cancan['times'])

def prepnum(l):
    new = []
    for x in l:
        if x != 0:
            #x = 0.00001
            new.append(math.log(x))
    return new

print(docdoc['numactions'])
print(doccan['numactions'])
print(candoc['numactions'])
print(cancan['numactions'])



actions1 = list((docdoc['numactions']))
actions1.extend((doccan['numactions']))
actions1.extend((candoc['numactions']))
actions1.extend((cancan['numactions']))


actions = list(prepnum(docdoc['numactions']))
actions.extend(prepnum(doccan['numactions']))
actions.extend(prepnum(candoc['numactions']))
actions.extend(prepnum(cancan['numactions']))


f = open("rdata.txt", "a")
f.write("int rank actions pid\n")
lim = 32
for i, action in enumerate(docdoc['numactions']):
    if i < lim:
        tea = docdoc["taskids"][i]
        if tea > 3:
            tea -= 4
        f.write("doc doc " + str(action) + " " + str(docdoc['ids'][i]) + str(tea) + "\n")
for i, action in enumerate(candoc['numactions']):
    if i < lim:
        tea = candoc["taskids"][i]
        if tea > 3:
            tea -= 4
        f.write("can doc " + str(action) + " " + str(candoc['ids'][i]) + str(tea) + "\n")
for i, action in enumerate(doccan['numactions']):
    if i < lim:
        tea = doccan["taskids"][i]
        if tea > 3:
            tea -= 4
        f.write("doc can " + str(action) + " " + str(doccan['ids'][i]) + str(tea) + "\n")
for i, action in enumerate(cancan['numactions']):
    if i < lim:
        tea = cancan["taskids"][i]
        if tea > 3:
            tea -= 4
        f.write("can can " + str(action) + " " + str(cancan['ids'][i]) + str(tea) + "\n")
f.close()


import math
#print(times)
times = [math.log(x) for x in times]

#plt.clf()
#plt.hist(docdoc['times'], bins = 50)
#plt.show()

#plt.clf()
#plt.hist(cancan['times'], bins = 50)
#plt.show()

#plt.clf()
#plt.hist(candoc['times'], bins = 50)
#plt.show()

#plt.clf()
#plt.hist(doccan['times'], bins = 50)
#plt.show()

#plt.clf()
#plt.hist(times, bins = 50)
#plt.show()



#plt.clf()
#plt.hist(actions1, bins = 50)
#plt.show()
print()
print(cancan['qs'])
qs = list(docdoc['qs'])
qs.extend(doccan['qs'])
qs.extend(candoc['qs'])
qs.extend(cancan['qs'])
plt.hist(qs, bins = 50)
#plt.show()

plt.clf()
clicks = list(docdoc['cs'])
print(doccan)
clicks.extend(doccan['cs'])
clicks.extend(candoc['cs'])
clicks.extend(cancan['cs'])
plt.hist(clicks, bins = 50)
#plt.show()

plt.clf()
#plt.show()
plt.hist(actions1, bins = 50)
#plt.show()



#print(stats.friedmanchisquare(docdoc['times'][:32], doccan['times'][:32], candoc['times'][:32], cancan['times'][:32]))
#print(sp.posthoc_nemenyi_friedman(np.array([docdoc['times'][:32], candoc['times'][:32], doccan['times'][:32], cancan['times'][:32]])))
#print(sp.posthoc_nemenyi_friedman(np.array([docdoc['times'][:32], candoc['times'][:32], doccan['times'][:32], cancan['times'][:32]]).T))
#print('We see pairwise comparisons for  docdoc (0), doccan (1), candoc (2), and cancan (3)')
#print()
#print()
#stats.kruskal(x, y)

#print('kruskal')
#print(stats.kruskal(docdoc['times'][:32], doccan['times'][:32], candoc['times'][:32], cancan['times'][:32]))


print()
print()
print()
print()
print()
print('Investigating effectiveness')
















for attribute in docdoc:
    print(attribute)
    
print()
    
    
    







#keep track of all candidates toggled, which we have to evaluate later
gt_candidates = {'docdoc':[], 'candoc':[], 'doccan':[], 'cancan':[]}
for c in gt_candidates:
    for i in range(8):
        gt_candidates[c].append([])






    
def print_effectiveness(condition, name):
    print()
    print(str(name))
    task_count = 0
    task_unsuccess = 0
    task_toggles = 0
    task_numrelevant = 0
    task_1toggle = 0
    task_2toggle = 0
    task_3toggle = 0
    ranks = 0
    firstranks = 0
    firstrank_counts = 0
    
    for i, t in enumerate(condition['fulltasks']):
       
        task_count += 1
        if t['numtoggles'] == 0:
            task_unsuccess += 1
        task_toggles += t['numtoggles']
        task_numrelevant += t['numrelevant']
        
        task_candidates = []
        #for i in range(8):
        #    task_candidates.append([])
        for nr in t['numrelevants']:
            if t['numrelevants'][nr] == 1:
                task_1toggle +=1
            if t['numrelevants'][nr] == 2:
                task_2toggle +=1
            if t['numrelevants'][nr] == 3:
                task_3toggle +=1
                
                
                
            task_candidates.append(nr)
        for nr in t['ranks']:
            ranks += t['ranks'][nr]
            
        if len(t['ranks']) > 0:
            firstranks += min(t['ranks'].values())
            #print(min(t['ranks'].values()))
            firstrank_counts += 1
            
        #print(condition['taskids'][i])
        gt_candidates[name][condition['taskids'][i]].append(task_candidates)
#            print(t['numrelevants'][nr])
#        task_1toggle = 
#        if round(t['numrelevant']) == round(2* t['numtoggles']):
#            task_2toggle += 1
#        if round(t['numrelevant']) == round(3*t['numtoggles']):
#            task_3toggle += 1
    
    print(str(task_unsuccess / task_count) + ' tasks without toggles')
    print(str(task_toggles / task_count) + ' average toggles')
    print(str(task_numrelevant / task_toggles) + ' results per toggle')
    print()
    print(str(task_1toggle / task_toggles) + ' % of toggles had one documents')
    print(str(task_2toggle / task_toggles) + ' % of toggles had two documents')
    print(str(task_3toggle / task_toggles) + ' % of toggles had three documents')
    print()
    print('Average ranking is ' + str(ranks/task_toggles))
    print()
    print('First ranking is ' + str(firstranks/firstrank_counts))
    print()
    
print()
print('Metric 1: did they select an expert?    Also testing if people prefer toggling experts with more documents')
#for t in docdoc:
print_effectiveness(docdoc, 'docdoc')
print_effectiveness(doccan, 'doccan')
print_effectiveness(candoc, 'candoc')
print_effectiveness(cancan, 'cancan')

print()






print('Metric 2: did they select relevant experts')
# Create a ground truth per task
    # Per task, see what experts were toggled




print(gt_candidates['docdoc'])
print(len(gt_candidates['docdoc']))


print()
print()
gt_full = []

for i in range(8):
    gt_full.append([])

    for t in gt_candidates['docdoc'][i]:
        gt_full[i].extend(t)
    for t in gt_candidates['doccan'][i]:
        gt_full[i].extend(t)
    for t in gt_candidates['candoc'][i]:
        gt_full[i].extend(t)
    for t in gt_candidates['cancan'][i]:
        gt_full[i].extend(t)

print('gt7')
print(gt_full[7])
print(set(gt_full[7]))
print(len(gt_full))

    # Then determine if they were relevant based on their portfolio

#gt_candidates['conditionname'][task_performed][list of candidates toggled on]

print("Total set of candidates for task 0")


#expert annotation
# Mobiliteit, Openbare ruimte, Jeugd en Jeugdzorg, Verkeer en Mobiliteit, Ruimtelijke Ontwikkeling, Diversiteit, Werk en inkomen
true0 = ['C.A. Verbokkem', 'J.W. Tamboer', 'Freek Deuss', 'R. van Alfen', 'W.S. Doornbos', 'A.W. Velthuis', 'S.C.G. Hol', 'P. Stumpel-Vos', 'M. Fleer', 'M. van Teeseling', 'Trix Aarts', 'Martijn Dijkhof', 'J.C. Damoiseaux', 'M.C. Manders', 'M. Braams']
false0 = ['W.J. van Mierlo', 'Elkie van Ginneke']






#annotations
#Ruimtelijke ordening, Ruimtelijke Ontwikkeling, Economische Zaken, Vastgoed, Economie, Bestuursinformatie, Economie
true1 = ['W.F. Matser', 'G.J.W. Wanders', 'M. van der Scheer', 'J.W.R. Huurman', 'W.C.F. van Gelder', 'J.M. Offenberg', 'M. van Dijk', 'Aldert de Vries', 'Hans Huurman', 'L. Roxs', 'J. Schuilenburg', 'J. Zuidgeest', 'Klaas Beerda', 'W.J.L. Kalfsvel', 'K. Verschoor', 'R. Wierdsma', 'A.M. Eling', 'Bas Akkers', 'Natalie Horning', 'D.C.M. Fiolet']
# verkerke is openbare ruimte... note sure on this one!
false1 = ['A.A.H. Verkerke', 'G.T. Houtman', 'J. Jepsen', 'D.S.M. van de Ven', 'Aloys Kersten', 'N. Horst']


#annotations
#Ruimtelijke Ontwikkeling, Wonen, Jeugd en Jeugdzorg, Ruimtelijke Ontwikkeling, Samen voor Overvecht, wijk overvecht, Burgerzaken, Jeugd en Jeugdzorg, Onderwijs
true2 = ['M.K. Kikkert', 'J.A. van Soelen', 'J. Lekkerkerker- Rack', 'W. Brandsen', 'W.M. Hendrix', 'Angela van der Putten', 'C. Aalberts', 'K. van der Goot', 'Marina Slijkerman', 'M.J. van Leeuwen', 'S. Hamimid', 'Manon Moonen', 'J.J. van Luxemburg', 'A.E. Postma', 'J.N. Wigboldus', 'W. Westgeest', 'O. Blok', 'A.A.G. Timmerman']
# onderwijs blok, werk en inkomen
false2 = ['J. van Kruijsdijk', 'A.R. Boelens', 'L. Maats', 'E.C. Dekker', 'E.S. Quak', 'C.E. Bac', 'M.P.J. Daverschot', 'G.J. Schoonvelde', 'C. van Ommen']



#annotates
#economie, economische zaken, citymarketing/stadspromotie
true3 = ['V.J. Drost', 'Bram van Grasstek', 'Ank Hendriks', 'A.P.M. Ruis', 'Eelko van den Boogaard', 'AH. Arendsen', 'Oscar Rentinck', 'W.J.L. Kalfsvel']
false3 = ['M. van Teeseling', 'D.S.M. van de Ven', ]




# annotates
#wonen
true4 = ['M. Kessels', 'S.M. Draad', 'B.J. Brijder', 'M.E.J. van Lijden', 'R. Koene', 'Trudy Maas', 'J. Lagerweij', 'R. Mouktadibillah', 'E. de Ridder', 'Monique van Kampen', 'D.T. Crabbendam']
false4 = ['R. van Essen', 'Philippe Thijssen', 'Annette Damen', 'K. Verschoor', 'I. van de Klundert']



# annotaties
#ruimtelijke ontwikkeling, volksgezondheid, samen voor overvecht
true5 = ['J.C.D. Hofland', 'Philippe Thijssen', 'Trix Aarts', 'E.S. Hochheimer', 'M. van den Berg', 'P. van der Meer', 'W.M. Hendrix', 'M.P.D.J. van der Horst', 'M. Weber', 'G. Hengeveld', 'Tinja Verkleij', 'K. van der Goot', 'Fabian Mol']
false5 = ['E.S. Quak', 'Ben Norg', 'F. Douglas', 'M. Kik', 'C.A. Kuin', 'y in de stad Essa', 'C.A. Verbokkem']


# annotes
# mobiliteit, stationsgebied, verkeer en mobiliteit, ruimtelijke ontwikkeling
true6 = ['div. auteurs', 'R. Tiemersma', 'Marieke Zijp', 'Rogier Crusio', 'B. Coenen', 'J.H. Greeven', 'S.C. de Gier', 'R. Boot', 'R. Doedens', 'Marjon van Caspel']
false6 = ['O.A. James', 'S.M. Draad', 'F. van der Zanden', 'De heer J. van Rooijen', 'W.J. van Mierlo']



# 
#Ruimtelijke ordening, Ruimtelijke Ontwikkeling, wonen, vastgoed, openbare ruimte
true7 = ['W.F. Matser', 'S.B. Beenen', 'Esther van Bladel', 'P. Buisman', 'M.K. Kikkert', 'D.P. Reinking', 'Karin Sam Sin-Vos', 'P.H. Meijer', 'B. de Jong', 'A.A.H. Verkerke']
false7 = ['M.A. van Kooten', 'Antoniek Vermeulen', 'J.M.W. Koolenbrander', 'R.J. Evelein']





gt_manual = [true0, true1, true2, true3, true4, true5, true6, true7]

#gt_manual = [true0_final, true1_final, true2_final, true3_final, true4_final, true5, true6, true7]




print()
print()
print()

print('groundtruth test')
def gt_print(condition):
    print()
    truth = 0
    fail = 0
    cond = docdoc
    if(condition == 'candoc'):
        cond = candoc
    if(condition == 'doccan'):
        cond = doccan
    if(condition == 'cancan'):
        cond = cancan
    
    numtasks = 0
    numcorrect = 0
    for t in range(8):
        #print(gt_candidates[condition][t])
        #taskset = 
        
        #print(gt_candidates[condition][t])
        #print(len(gt_candidates[condition][t]))
        
        for person in gt_candidates[condition][t]:
            containstruth = 0
            
            #not sure what i'm checking here - toggles? 
            for c in person:
                #print(c)
                if c in gt_manual[t]:
                    truth += 1
                    containstruth += 1
                else:
                    fail += 1
            if containstruth > 0:
                numcorrect += 1
                cond['completions'].append(1)
            else:
                cond['completions'].append(0)
                
            avgc = sum(cond['completions']) / len(cond['completions'])
            if len(person) > 0:
                cond['avgcompletion'].append(avgc)

            
            numtasks += 1
                            
                    
    print(condition + '  precision  ' + str(truth / (truth + fail)))
    print('and task completion ' + str(numcorrect / numtasks))
    
    

print('EFFECTIVENESS AND PRECISION')
gt_print('docdoc')
gt_print('doccan')
gt_print('candoc')
gt_print('cancan')


import collections


print()
print()
def find_overlap(condition):
    print(condition)
    lst = []
    for t in range(8):
        print('task ' + str(t))
        lst = []
        for p in gt_candidates[condition][t]:
            lst.extend(p)
        
        print([item for item, count in collections.Counter(lst).items() if count > 3])

#find_overlap('docdoc')
#print()
#find_overlap('doccan')
#print()
#find_overlap('candoc')
#print()
#find_overlap('cancan')
print()
print()

print('so lets try a little less complicated: get a set of all items for each condition. then show intersection')
print()
print()
docdoc_set = []
doccan_set = []
candoc_set = []
cancan_set = []

for t in range(8):
    [docdoc_set.extend(x) for x in gt_candidates['docdoc'][t]]
    [doccan_set.extend(x) for x in gt_candidates['doccan'][t]]
    [candoc_set.extend(x) for x in gt_candidates['candoc'][t]]
    [cancan_set.extend(x) for x in gt_candidates['cancan'][t]]
    
#print(docdoc_set)
print()
docdoc_set = set(docdoc_set)
doccan_set = set(doccan_set)
candoc_set = set(candoc_set)
cancan_set = set(cancan_set)

print('Overlap both doc interfaces')
print(docdoc_set & doccan_set)
print(len(docdoc_set & doccan_set))

print()
print('Overlap can interfaces')
print(candoc_set & cancan_set)
print(len(candoc_set & cancan_set))
print()


print('Overlap both doc rankings')
print(docdoc_set & candoc_set)
print(len(docdoc_set & candoc_set))

print()
print('Overlap can rankings')
print(doccan_set & cancan_set)
print(len(doccan_set & cancan_set))
print()



print()
print()
print()
     
print()
#for t in docdoc[tasks]

#print(docdoc['toggles'])
#print()
#print(candoc['toggles'])

print()
#print(docdoc['fulltasks'][0])
#print(candoc['fulltasks'][0])
#print(doccan['fulltasks'][0])
#print(cancan['fulltasks'][0])



print('Metric 3: average rank of selected experts')


















print()
print()
print()


    
print('variance')

times = []
lim=16000
for i, t in enumerate(docdoc['fulltasks']):
    if i < lim:
        times.append(t['time'])

for i, t in enumerate(doccan['fulltasks']):
    if i < lim:
        times.append(t['time'])

for i, t in enumerate(candoc['fulltasks']):
    if i < lim:
        times.append(t['time'])

for i, t in enumerate(cancan['fulltasks']):
    if i < lim:
        times.append(t['time'])
    
times = [x / 60000 for x in times]

import statistics
#print(times)
print(statistics.variance(times))
print()
print(statistics.variance(docdoc['times']))
print(statistics.variance(doccan['times']))
print(statistics.variance(candoc['times']))
print(statistics.variance(cancan['times']))


print()
print()
print()


for i, p in enumerate(participants):
    print('participant ' + str(i))
    t = []
    for j in range(8):
        #print(p[j])
        t.extend([x / 60000 for x in p[j]['times']])
        #print(p[i]['times'])
    if(len(t) > 0):
        print(statistics.variance(t) )
    print()
    
    
print('lets use some representative candidates for variation')
sample = []
saample = []
saaaample = []
for i in range(0, 4):
    for j in range(8):
        sample.extend([x / 60000 for x in participants[i][j]['times']])

for i, p in enumerate(participants):
    if i != 5 and i != 11 and i != 12 and i != 13 and i != 14 and i != 17:
        for j in range(8):
            saample.extend([x / 60000 for x in participants[i][j]['times']])
    saaaample.extend([x / 60000 for x in participants[i][j]['times']])

saaample = []
for i in [0, 2, 9]:
    for j in range(8):
        saaample.extend([x / 60000 for x in participants[i][j]['times']])

print('std dev first 5 ' + str(math.sqrt(statistics.variance(sample))))
print(math.sqrt(statistics.variance(saample)))
print(math.sqrt(statistics.variance(saaample)))
print(math.sqrt(statistics.variance(saaaample)))



print()
print()
print()
print()
print('okay so due to variation - we need a looot of participants. can we use numactions as a proxy')



print(len(docdoc['numactions']))
print(len(doccan['numactions']))
print(len(candoc['numactions']))
print(len(cancan['numactions']))

print('kruskal')
print(stats.kruskal(docdoc['numactions'][:32], doccan['numactions'][:32], candoc['numactions'][:32], cancan['numactions'][:32]))

#model = ols('numactions ~ C(interface) * C(ranking)', data=df2).fit()

#from sklearn.linear_model import LogisticRegression
#clf = LogisticRegression(random_state=0).fit(X, y)

print()
print()
print()
print()
print('logistic test')
print()
print()
print()
print()
print()
import statsmodels.formula.api as smf


print(sorted_preferences)
#print('HELFKASDFJASLDF' )

dataset_log = []
dataset_log2 = []

for i, time in enumerate(docdoc['times']):
    if docdoc['numactions'][i] != 0:
        dataset_log.append(['doc', 'doc', 'docdoc', docdoc['tasks'][i], math.log(docdoc['numactions'][i]), math.log(time), docdoc['ids'][i], docdoc['completions'][i], sorted_preferences[docdoc['ids'][i]], sorted_sus[docdoc['ids'][i]]])    
    
for i, time in enumerate(candoc['times']):
    if candoc['numactions'][i] != 0:
        dataset_log.append(['can', 'doc', 'candoc', candoc['tasks'][i], math.log(candoc['numactions'][i]), math.log(time), candoc['ids'][i], candoc['completions'][i], sorted_preferences[candoc['ids'][i]], sorted_sus[docdoc['ids'][i]]])
    
for i, time in enumerate(doccan['times']):
    if doccan['numactions'][i] != 0:
        dataset_log.append(['doc', 'can', 'doccan', doccan['tasks'][i], math.log(doccan['numactions'][i]), math.log(time), doccan['ids'][i], doccan['completions'][i], sorted_preferences[doccan['ids'][i]], sorted_sus[docdoc['ids'][i]]])
    
for i, time in enumerate(cancan['times']):
    if cancan['numactions'][i] != 0:
        dataset_log.append(['can', 'can', 'cancan', cancan['tasks'][i], math.log(cancan['numactions'][i]), math.log(time), cancan['ids'][i], cancan['completions'][i], sorted_preferences[cancan['ids'][i]], sorted_sus[docdoc['ids'][i]]])



fig = plt.figure(figsize= (5, 2.5))
bx = fig.add_subplot(111)

data2 = [    docdoc['avgcompletion'],
             candoc['avgcompletion'],
             doccan['avgcompletion'],
             cancan['avgcompletion']]
             
data2 = [    docdoc['completions'],
             candoc['completions'],
             doccan['completions'],
             cancan['completions']]

data2 = [    docdoc['avgcompletion'],
             candoc['avgcompletion'],
             doccan['avgcompletion'],
             cancan['avgcompletion']]

bp2 = bx.violinplot(data2,
           showmedians=True, showextrema=True)
plt.xticks([1,2,3,4],['doc interface' + '\n' +' doc ranking', 'can interface ' + '\n' + 'doc ranking', 'doc interface ' + '\n' + 'can ranking', 'can interface ' + '\n' + 'can ranking'])
#bx.legend([bp2['medians'][0], bp2['means'][0]], ['median', 'mean'])
bx.set_ylabel('Correct tasks per participant')
#bx.set_ylabel('Average task completion rate per participant')

#bp2['cmeans'].set_color('b')
#bp2['cmedians'].set_color('g')
#bp2.legend()

print(docdoc['completions'])
print(candoc['completions'])
print(np.average(docdoc['completions']))
print(np.average(candoc['completions']))
print(np.average(doccan['completions']))
print(np.average(cancan['completions']))



#for key in docdoc:
#    print(key)
#rdf_pref = pd.DataFrame(data=rdataset, columns=['interface','ranking','zekerheid','sus', 'preferences'])


df3 = pd.DataFrame(data=dataset_log, columns=['interface','ranking','condition','task','numactions','time', 'pid', 'completion', 'preferences', 'sus'])
#df4 = pd.DataFrame(data=dataset_log, columns=['interface','ranking','condition','task','numactions','time', 'pid', 'completion', 'preference'])

df3_backup = pd.DataFrame(data=dataset_log, columns=['interface','ranking','condition','task','numactions','time', 'pid', 'completion', 'preferences', 'sus'])

print(np.array(df3).shape)

#df3 = df3[df3.pid != 10]
df3 = df3[df3.preferences != "tie"]


print('Effectiveness logistic test')
model = LogisticRegression(solver='liblinear', random_state=0)


"""
x = []
y = []
for ind, i in enumerate(df3.interface):
    ntfc = df3.interface[ind]
    if ntfc == 'doc':
        ntfc = 0
    else:
        ntfc = 1
    rnkng = df3.ranking[ind]
    if rnkng == 'doc':
        rnkng = 0
    else:
        rnkng = 1
    x.append([ntfc, rnkng])
    y.append(df3.completion[ind])

model.fit(x, y)
"""
import statsmodels.api as sm
from statsmodels.graphics.factorplots import interaction_plot

#breaking


print('strong doc fans ' + str(doc_strongfans))
print('strong can fans ' + str(can_strongfans))


print()
print()
print()

    
    
print()



print()
print('we gotta make an overview of all portfolios per task')


portfolios0 = 'Mobiliteit, Openbare ruimte, Milieu en Emissieloos Vervoer, Openbare Orde en Veiligheid, Jeugd en Jeugdzorg, Sport, Verkeer en Mobiliteit, Ruimtelijke Ontwikkeling, Diversiteit, Organisatie(vernieuwing) en personeel, Werk en inkomen, Prostitutie, Openbare Orde en Veiligheid, Inkoop en aanbestedingen, Personeel en Organisatie'



#goede portefeuilles voor buurt aantrekkelijk wil maken voor bedrijven: Ruimtelijke Ontwikkeling, economische zaken, vastgoed, ruimtelijke ordening
#schuilenburg geen port -> maar schrijft wel over vestigen van een bedrijf
#We rekenen geen portefeuille goed! denk ik?
portfolios1 = 'Milieu en Emissieloos Vervoer, Ruimtelijke ordening, Ruimtelijke Ontwikkeling, Openbare orde, veiligheid, toezicht en handhaving, Sport, Economische Zaken, Vastgoed, Jeugd en Jeugdzorg, Mobiliteit, Economie, Merwedekanaalzone, Energie, Financien, Maatschappelijke Ondersteuning, Bestuursinformatie, Bestuurlijke zaken, Diversiteit, Cultuur, Economie'


#speelplek bouwen porto's: ruimtelijke ontwikkelign, wonen, jeugd en jeugdzorg, cultuur, sport, overvecht, Jeugd en Jeugdzorg, wonen
portfolios2 = 'Ruimtelijke Ontwikkeling, Mobiliteit, Openbare Orde en Veiligheid, Verkeer en Mobiliteit, Diversiteit, Wonen, Dierenwelzijn, Economische Zaken, Cultuur,  Jeugd en Jeugdzorg, wijk west, Ruimtelijke Ontwikkeling, Samen voor Overvecht, Circulaire Economie, Sport, wijk overvecht,  Burgerzaken, Jeugd en Jeugdzorg, Onderwijs, welzijn, maatschappelijke ondersteuning, volksgezondheid, werk en inkomen, Asiel en Integratie'


#toeristen: economie, 
portfolios3 = 'economie, economische zaken, openbare ruimte, vastgoed, citymarketing/stadspromotie, ruimtelijke ontwikkeling, mobiliteit, verkeer en mobiliteit, bestuurlijke zaken'

#anti speculatiebeding
portfolios4 = 'financien, financien en belastingen, wonen, ruimelijke ontwikkeling, leidsche rijn, stationsgebied, bestuurlijke zaken, milieu en emmissieloos vervoer, economische zaken, sport, economie, energie, duurzaamheid, milieu, openbare ruimte, openbare orde en veiligheid'


#gezond gedrag
portfolios5 = 'ruimtelijke ontwikkeling, leidsche rijn, mobiliteit, volksgezondheid, samen voor overvecht, groen, openbare orde, werk en inkomen'


#tijdlijn uithoflijn
portfolios6 = 'financien, financien en belastingen, mobiliteit, personeel en organisatie, milieu en emissieloos vervoer, stationsgebied, grondzaken, verkeer en mobiliteit, ruimtelijke ontwikkeling, ruimtelijke ordening, onderwijs'


#corona rosendael
portfolios7 = 'Milieu en Emissieloos Vervoer, Ruimtelijke ordening, Ruimtelijke Ontwikkeling, Openbare orde, veiligheid, toezicht en handhaving, Sport, leidsche rijn, verkeer en mobiliteit, jeugd en jeugdzorg, wonen, mobiliteit, openbare orde en veiligheid, volksgezondheid, vastgoed, samen voor overvecht, ombudszaken/klachtafhandeling, economische zaken, merwedekanaalzone, openbare ruimte, werk en inkomen, wijkgericht werken en participatie, financien, financien en belastingen'


print()
print()
print()

portfolios = [portfolios0, portfolios1, portfolios2, portfolios3, portfolios4, portfolios5, portfolios6, portfolios7]

fulltasks = ["Stel dat je onderzoek voorbereid voor een project over fietsgedrag in Utrecht. Is er bij collega's iets bekend over het fietsgebruik van niet-Westerse allochtonen?", 
	"Stel dat je een buurt aantrekkelijk wil maken voor bedrijven. Hebben collega's data over het aantal bedrijven en het aantal arbeidsplaatsen in de verschillende wijken van Utrecht? Weten we waarom bedrijven voor deze plekken kiezen?", 
	"Stel dat je een nieuwe speelplek wil laten bouwen, en wil je controleren of er genoeg belangstelling voor is. Is er bij collega's al iets bekend over hoeveel kinderen er zijn in de wijk Overvecht, en of we meer jonge huishoudens kunnen verwachten in de toekomst?", 
	"Stel dat je Utrecht aantrekkelijk wil maken voor toeristen. Weten collega's hoeveel overnachtigen er jaarlijks in Utrecht zijn door toeristen, en waarom toeristen kiezen voor Utrecht?", 
	"Als je een woning koopt zit er een anti-speculatiebeding op om te voorkomen dat mensen huizen kopen om ze vervolgens door te verkopen. Welke collega's kunnen helpen onderzoeken in hoeverre deze maatregel helpt om huizen meer betaalbaar te maken?", 
	"Stel dat je beleid wil maken om gezondheid gedrag in Leidsche Rijn te stimuleren, en je weet dat collega's in een andere wijk hierin succesvol waren. Welke collega's kunnen je helpen onderzoeken hoe de Wijkaanpak Overvecht opgezet is?", 
	"Stel dat je de tijdlijn wil schetsen van de bouw van de Uithoflijn, vanaf de planning tot de huidige status. Wie kan je hierbij helpen?", 
	"Stel dat je wil weten of corona invloed gaat hebben een bouwproject in jouw wijk. Wie kan je vertellen of corona invloed heeft op de bouwplannen Zorgcentrum Rosendael?"]

for i, p in enumerate(fulltasks):
    print()
    print(p)
    for j in portfolios[i].split(","):
        print(j)
    print()
    
#   df3 = df3[df3.preferences != 'tie']

df4 = df3.replace('can', 1)    
df4 = df4.replace('doc', 0)     
df4.preferences = pd.to_numeric(df4.preferences)



print(df4)

print(df4.preferences)

#print('WITH PREFERENCES time after transform')
model = smf.logit("completion ~ C(interface) * C(ranking) * C(preferences)", data = df4).fit()

print(model.summary2())
print(df4)


#breaking

fig, ax = plt.subplots(figsize=(6, 6))
fig = interaction_plot(
    x=df4.interface,
    trace=df4.ranking,
    response=df4.completion,
    colors=["red", "blue"],
    markers=["D", "^"],
    ms=10,
    ax=ax,
)
#fig.show()
#plt.show()



print('TIME ~ stuff')
print()
print()
modelll = ols('time ~ C(interface) * C(ranking) * C(preferences)', data=df3).fit()
print()
print()
print()
print(sm.stats.anova_lm(modelll, typ=2))
print()



print()
print()
print()





print('SUS with preferences')
model = ols('sus ~ C(interface) * C(ranking) * C(preferences)', data=df3).fit() #rdf
print(sm.stats.anova_lm(model, typ=2))
print()


fig, ax = plt.subplots(figsize=(6, 6))
fig = interaction_plot(
    x=df3['preferences'],
    trace=df3['ranking'],
    response=df3['sus'],
    colors=["red", "blue"],
    markers=["D", "^"],
    ms=10,
    ax=ax,
)

plt.show()


print()
print('mean sus scores')
docs = 0
cans = 0
docnum = 0
cannum = 0

for key in sorted_sus:
    if sorted_preferences[key] == 'doc':
        docs += 1
        docnum += sorted_sus[key]
    if sorted_preferences[key] == 'can':
        cans += 1
        cannum += sorted_sus[key]
        
print(docnum / docs)
print(cannum / cans)
#print(np.mean(df3.preferences=='doc'))

#print('whuh')
print()
#print(modelll.summary())

