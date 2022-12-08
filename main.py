from diaries.DiarySample import DiarySample
from diaries.MitsuzawaDiary import MitsuzawaDiary


from diaries.ShikaDiary import ShikaDiary
# ↓のリストには、メンバーの各⽇記が格納されます。
diaries = [
      DiarySample(), 
      ShikaDiary(),
      ShimaPacaDiary(),
      MitsuzawaDiary(),
]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
