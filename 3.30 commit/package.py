# import travel.thailand #클래스나 함수는 이 자리에 import 할수 없다.
# #import travel.thailand.ThailandPackage > 불가능!
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()
#
# #from~ import~~구문에서는 윗 사용 가능함!
# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()
#
# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

from travel import *
#trip_to = vietnam.VietnamPackage()
#trip_to = thailand.ThailandPackage()
#trip_to.detail()

import inspect
import random
print(inspect.getfile(random)) #random이라는 모듈이 어떤 위치에 있는지?
print(inspect.getfile(thailand))


