from address import Mailing
from address import Address


address1 = Address("11111", "Москва", "Журавлева", "11A", "1")

mail1 = Mailing(address1.info(), address1.info(), 100, "fg555")

mail1.info_mailing()

