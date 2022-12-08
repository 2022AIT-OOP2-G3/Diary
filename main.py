from diaries.DiarySample import DiarySample
from diaries.ShimaPacaDiary import ShimaPacaDiary
# ↓のリストには、メンバーの各⽇記が格納されます。
diaries = [
    DiarySample(),
    ShimaPacaDiary(),
]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
