# list_1=[1,2,3]
# new_list=[n+1 for n in list_1]
# print(new_list)
# name="angela"
# new_list=[letter for letter in name]
# print(new_list)
# new_list=[n*2 for n in range(1,5)]
# print(new_list)
# new_list=[n for n in range(1,5) if n>2]
# print(new_list)
# names=['Alex','Beth','Caroline','Dave','Eleanor','Freddie']
# # short_names=[name for name in names if len(name)<5]
# # print(short_names)
# # long_names=[name.upper() for name in names if len(name)>4]
# # print(long_names)
# import random
# student_scores={student:random.randint(1,100) for student in names}
# passed_students={student:value for (student,value) in student_scores.items() if value>40}
# print(passed_students)
import pandas
student_scores={
    'Student':['angelina','james','lilly'],
    'Score':[56,72,98]
}
st_df=pandas.DataFrame(student_scores)
for (index,row) in st_df.iterrows():
    print(row.Student)
