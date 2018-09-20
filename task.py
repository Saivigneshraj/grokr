import boto3
import os

s3 = boto3.resource('s3')
s3.Bucket('datagrokr-assessment').download_file('task.txt', 'task.txt')


from collections import Counter;
cnt = Counter ();
A = []
for line in open ('task.txt', 'r'):
	for word in line.split ():
		cnt [word] += 1

sorted(cnt)
print(cnt.most_common(5))
