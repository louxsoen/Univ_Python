# 세트 자료구조를 사용한다.
clubA={'kim', 'park', 'hwang'}
clubB={'park', 'lee', 'choi'}

# 동아리에 가입한 학생들의 모든 명단을 ClubC에 저장한 후에 출력한다.
clubC = clubA.union(clubB)
print(clubC)
# A, B 동아리에 둘 다 가입한 학생의 명단을 출력하시오.
print(clubA.intersection(clubB))
# A동아리에서 B동아리에 가입한 학생들의 명단을 제외하시오.
print(clubA.difference(clubB))
# B동아리에서 A동아리에 가입한 학생들의 명단을 제외하시오.
print(clubB.difference(clubA))
# A동아리에 'yang' 회원이 새로 가입했다.
clubA.add('yang')
print(clubA)
# B동아리에 'lee' 회원이 탈퇴했다.
clubB.remove('lee')
print(clubB)
# A, B 동아리의 회원들을 각각 출력하시오.
print('A 동아리 : ', clubA)
print('B 동아리 : ', clubB)
