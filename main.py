from diaries.DiarySample import DiarySample
from diaries.ShikaDiary import ShikaDiary
from diaries.IwadoDiary import IwadoDiary
from diaries.ShimaPacaDiary import ShimaPacaDiary
from diaries.MitsuzawaDiary import MitsuzawaDiary
from diaries.MizutaniDiary import MizutaniDiary
from diaries.YamadaDiary import YamadaDiary
# ↓のリストには、メンバーの各⽇記が格納されます。
diaries = [
      DiarySample(), 
      ShikaDiary(),
      IwadoDiary(),
      ShimaPacaDiary(),
      MitsuzawaDiary(),
      MizutaniDiary(),
      YamadaDiary(),
]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
