# import theater_module
#
# theater_module.price(3) #3명 영화보러 갔을때의 가격
# theater_module.price_morning(3) #3명이 조조영화 보러 갔을때의 가격
# theater_module.price_soldier(5) #5명의 군인이 영화 보러 갔을때의 가격
#
# #모듈에 별명 붙이기
# import theater_module as mv #theater_module에 별명을 붙인다. mv로!
# mv.price(3)
# mv.price_morning(3)
# mv.price_soldier(5)
#
#
# from theater_module import *
# price(3)
# price_morning(3)
# price_soldier(5)
#
# from theater_module import price,price_morning #price_soldier는 필요없을때
# price(3)
# price_morning(3)
# #price_soldier(3)  >> 쓸 수 없다.
#
# from theater_module import price_soldier as price
# #price_soldier만 가져다 쓰는데 별명을 price로!
# price(5)  #이떄의 price는 price_soldier이다.
