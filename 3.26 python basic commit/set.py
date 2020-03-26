#집합 (세트)
#중복 안됨, 순서 없음
my_set = {1,2,3,4,5}
print(my_set)

java = {"유재석","김태호","양세형"}
python = set(["유재석","박명수"])

#교집합 (java와 python을 모두 할수있는 개발자)
print(java & python)
print(java.intersection(python))

#합집합 (java또는 python중 하나라도 할 수 있는 개발자)
print(java | python)
print(java.union(python))

#차집합 (java는 하는데 python을 못 하는 개발자)
print(java - python)
print(java.difference(python))

#python을 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

#java를 잊어먹음
java.remove("김태호")
print(java)