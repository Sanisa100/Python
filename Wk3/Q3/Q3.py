#Q3
class Car:
  website = 'https://www.fictitiouscarsales.com.au'

  def __str__(carObj):
    return 'Vehicle details:\n{} {} {} {}\nSale id: {}'.format(carObj.make, carObj.model, carObj.body_type, carObj.year,
                                                               carObj.sale_id)

  def __init__(carObj, make, model, body_type, year, sale_id):
    carObj.make = make
    carObj.model = model
    carObj.body_type = body_type
    carObj.year = year
    carObj.sale_id = sale_id

  def sale_page(self):
    return 'https://www.fictitiouscarsales.com.au' + '/' + str(carObj.sale_id)

  def __repr__(carObj):
    return "Car('{}', '{}', '{}', {}, {})".format(carObj.make, carObj.model, carObj.body_type, carObj.year,
                                                  carObj.sale_id)


print(Car.website)
carObj = Car("Mazda", "CX-5", "SUV", 2022, 220)
print(carObj.make)
print(carObj.model)
print(carObj.body_type)
print(carObj.year)
print(carObj.sale_id)
print(str(carObj))
print(repr(carObj))
print(carObj.sale_page())
