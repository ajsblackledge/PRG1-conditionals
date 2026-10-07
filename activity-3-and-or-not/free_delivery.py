FREE_DELIVERY_THRESHOLD = 40.00


def qualifies_for_free_delivery(order_total, is_member, is_bulky, is_staff=False):
    if is_member and not is_bulky:
        return True
    if is_staff:
        return True
    if order_total >= FREE_DELIVERY_THRESHOLD and not is_bulky:
        return True
    return False


print(qualifies_for_free_delivery(20.00, True, False))
print(qualifies_for_free_delivery(20.00, True, True))
print(qualifies_for_free_delivery(45.00, False, False))
print(qualifies_for_free_delivery(45.00, False, True))
print(qualifies_for_free_delivery(30.00, False, True, True))
