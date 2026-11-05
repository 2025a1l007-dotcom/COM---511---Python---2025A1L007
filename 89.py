#sort orders by delivery time
orders ={
    ("order-A",45),
    ("0rder-B",20),
    ("order-C",35),
    ("order-D",15)
}
def get_delivery_time(order):
    return order[1]
sorted_orders = sorted(orders, key=get_delivery_time)
print("Orders sorted by delivery time:")
for order_name,minutes in sorted_orders:
    print(order_name, ":", minutes, "minutes")