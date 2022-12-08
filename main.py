from diaries.DiarySample import DiarySample
from diaries.MitsuzawaDiary import MitsuzawaDiary

# ↓のリストには、メンバーの各⽇記が格納されます。
diaries = [
      DiarySample(), 
      MitsuzawaDiary(),
]
for d in diaries:
      print("---------------------------------")
      print(d.get_date())
      print(d.get_summary())
      print(d.get_author())
      print()