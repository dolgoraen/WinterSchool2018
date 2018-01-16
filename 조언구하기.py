#MyMagic8Ball

import random

#답변을 입력해 봅시다.
ans1="주저하지말고 해보세요!!!"
ans2="됐거든요. 한 번 더 그런 거 생각하면 화낼거예요!!"
ans4="뭐라고요? 생각 좀 하고 말하세요!!"
ans5="모르니까 두려운 거에요. 한 번 도전해봐요!!"
ans6="미쳤어요?? 제정신이 아니군요?!"
ans7="해도 그만, 안 해도 그만, 아니겠어요??"
ans8="맞아요. 그렇게 하면 되요!! 꼭 그렇게 해보세요!!^^"

print("MyMagic8Ball에 오신 것을 환영합니다!!")

question=input("조언을 얻고 싶다면 엔터를 눌러주세요!!!")

print("\n고민중...ㅠㅠ\n"*4)
      
choice=random.randint(1,8)
if choice==1:
    answer=ans1
elif choice==2:
    answer==ans2
elif choice==3:
    answer==ans3
elif choice==4:
    answer==ans4
elif choice==5:
    answer==ans5
elif choice==6:
    answer==ans6
elif choice==7:
    answer==ans7
else:
    answer=ans8
    
print(answer)

input("\n\n마치려면 엔터 키를 누르세요!!")

    
