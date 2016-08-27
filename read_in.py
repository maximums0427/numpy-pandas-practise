'''
Written by Max on 27/08/2016
'''
import csv
import pandas as pd
import numpy as np

def read_csv(filename):
	with open(filename, 'rb') as f:
		reader = csv.DictReader(f)
		return list(reader)

enrollments = pd.read_csv('enrollments.csv')
daily_engagement = pd.read_csv('daily_engagement.csv')
project_submissions = pd.read_csv('project_submissions.csv')

daily_engagement.columns = [u'account_key', u'utc_date', u'num_courses_visited', u'total_minutes_visited', u'lessons_completed', u'projects_completed']


enrollments = enrollments[enrollments.join_date != enrollments.cancel_date]

engaged_student = np.unique(daily_engagement['account_key'])
enrolled_student = enrollments['account_key']
#enrollments_refined = pd.DataFrame(np.nan, index = [0], columns=['account_key', 'status', 'join_date', 'cancel_date', 'days_to_cancel', 'is_udacity', 'is_cancel'])
#print enrollments_refined
for i,id in enumerate(enrolled_student):
	if id not in engaged_student:
		enrollments = enrollments[enrollments.account_key!=id]

print enrollments.shape
#create a student dictionary: paid_student
paid_student = {}
for index, row in enrollments.iterrows():
	if np.isnan(row['days_to_cancel']) or row['days_to_cancel']>7:
		if row['account_key'] not in paid_student or row['join_date']>paid_student[row['account_key']]:
			paid_student[row['account_key']] = row['join_date']
print len(paid_student)




#print enrollments.shape
#print daily_engagement.head()

#print enrollments.describe()
'''
print enrollments.shape[0]
print 'enrollments:'
print np.unique(enrollments['account_key']).shape[0]
print daily_engagement.shape[0]
print 'daily_engagement:'
print np.unique(daily_engagement['acct']).shape[0]
print project_submissions.shape[0]
print 'project_submissions:'
print np.unique(project_submissions['account_key']).shape[0]
#enrollments = pd.read_csv('enrollments.csv')
#print type(enrollments['days_to_cancel'][1])
'''
