def stream_user_ages():
    for a in data_set:
        yield age

def AVERAGE():
    a, c = 0, 0 #a is current average, c is count of the number of ages
    for x in stream_user_ages():
        c += 1
        a = (a * (c - 1)) + x) // c
    return a

print(f"Average age of users: {a}")

