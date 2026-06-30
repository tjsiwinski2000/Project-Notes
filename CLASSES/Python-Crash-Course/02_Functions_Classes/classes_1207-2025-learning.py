#1207-2025 p179 
# ✅exercise 9-10
from restaurant import Restaurant
my_restaurant = Restaurant("MH","asian")
my_restaurant.describe_restaurant()

# ✅exercise 9-11
import user_administration as user_admin
my_admin = user_admin.Admin('t','siwinski','0001','male','7')
my_admin.privileges.update_privileges("add / delete users")
my_admin.privileges.show_privileges()

# exercise 9-12

import admin_privileges
my_number2_admin = admin_privileges.Admin('t','siwinski','0002','male','7')
my_number2_admin.privileges.update_privileges('eat peanut butter')
my_number2_admin.privileges.show_privileges()
