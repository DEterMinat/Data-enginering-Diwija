myList = ['Apple',20]
myDF1 = sc.parallelize(myList)
myDF1.collect()