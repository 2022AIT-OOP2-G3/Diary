from diaries.DiarySample import DiarySample
from diaries.DiarySample import ShikaDiary
from diaries.DiarySample import ShimaPacaDiary
from diaries.MizutaniDiary import DiaryMizutani
from diaries.MitsuzawaDiary import MitsuzawaDiary

# ↓のリストには、メンバーの各⽇記が格納されます。
from diaries.ShikaDiary import ShikaDiary
# ↓のリストには、メンバーの各⽇記が格納されます。
diaries = [
      DiarySample(), 
      ShikaDiary(),
      ShimaPacaDiary(),
      DiaryMizutani(),
      MitsuzawaDiary(),
]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
