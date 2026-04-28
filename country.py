class india():
    def country_capital(self):
        print("capital of india is New Delhi")
class Australia():
    def country_capital(self):
        print("capital of Australia is Melbourne")
obj_ind=india()
obj_aus=Australia()
for country in(obj_ind,obj_aus):
    country.country_capital()

        