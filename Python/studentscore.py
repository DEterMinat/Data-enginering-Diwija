try:
#     fw = open("score.txt", "w", encoding="utf-8")
#     while True:
#         studentId = input("Student id:")
#         if studentId =="exit":
#             break
#         score = input("Score :")
#         fw.writelines(studentId+"\t"+score+"\n")
#     fw.close()
    fr = open("score.txt", "r", encoding="utf-8")
    fw = open("score.txt", "w", encoding="utf-8")
    grade =None
    for line in fr.readlines():
        score=line[-4:].strip()
        studentId=line[-4:].strip()
        score=int(score)
        if score>=80:
            grade="A"
        elif score>=70 and score<=80 :
            grade="B"
        elif score>=60 and score<=70 :
            grade="C"
        else:
            grade="F"
        fw.writelines(studentId+"\t"+str(score)+"\t"+grade+"\n")
    fw.close()
    fr.close()
        
except Exception as e:
    print(e)