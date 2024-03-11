'''*********************** first method to import ******************'''

# import shiftingitem_jenny.books
# shiftingitem_jenny.books.display()
# b=shiftingitem_jenny.books.myclass()
# b.booktype()
'''hi my name is anand kumar
hi from books module
this module/carton contain all my books
it has all my non-friction books'''

# import shiftingitem_jenny.clothes.jeans
# shiftingitem_jenny.clothes.jeans.display()
'''hi from jeans module
this module/carton contain all my jeans'''

'''******************* second method to import ***********************'''

# from shiftingitem_jenny import books
# books.display()
'''hi my name is anand kumar
hi from books module
this module/carton contain all my books'''

# from shiftingitem_jenny.footwear import shoes,heel
# shoes.display()
'''hi from shoes module
hi from heel module
this module/carton contain all my shoes'''

# from shiftingitem_jenny.footwear.shoes import display,shoes_color
# display()
# shoes_color()
'''hi from shoes module
this module/carton contain all my shoes
red, pink, blue, white'''

# from shiftingitem_jenny.footwear.shoes import *
# display()
# shoes_types()
'''hi from shoes module
this module/carton contain all my shoes
kolhapuri'''

# from shiftingitem_jenny.footwear import *
# shoes.display()
'''error'''

'''go to footwear __init__ file'''
from shiftingitem_jenny.footwear import *
shoes.display()
'''hi from shoes module
hi from heel module
this module/carton contain all my shoes'''