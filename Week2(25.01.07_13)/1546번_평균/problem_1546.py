N = int(input())

scores = list(map(int, input().split()))

max_score = max(scores)
# 리스트에 다시 저장해줘야 함. 
new_scores=[(score / max_score)* 100 for score in scores]

new_avg_score = sum(new_scores)/N
print(new_avg_score)