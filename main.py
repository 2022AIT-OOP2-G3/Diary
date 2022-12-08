from diaries.DiarySample import DiarySample
from diaries.IwadoDiary import IwadoDiary
# ↓のリストには、メンバーの各⽇記が格納されます。
diaries = [
      DiarySample(), 
      IwadoDiary(),
]
for d in diaries:
      print("---------------------------------")
      print(d.get_date())
      print(d.get_summary())
      print(d.get_author())
      print()