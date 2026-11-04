# 1. In: 4 permissions for an expense system in a company: VIEW, CREATE, APPROVE, PAY
# 2. Process: give a junior accountant VIEW and CREATE, check if he can APPROVE,
#    add APPROVE when he becomes manager, then remove CREATE
# 3. Out: his permissions in binary after each step, and True or False for each check
# 4. What are my permissions about?
#    VIEW (1): see the expenses
#    CREATE (2): enter a new expense
#    APPROVE (4): accept an expense
#    PAY (8): send the money
#    In finance the same person should not create AND approve an expense, it is a
#    fraud risk. That is why I remove CREATE when I add APPROVE.

# Your code below
# One bit per permission
VIEW = 1
CREATE = 2
APPROVE = 4
PAY = 8


# Show one step: its name, the value in binary, and the normal number
def show(step, value):
    print(f"{step:<36} {format(value, '04b')}  ({value})")


# A junior accountant can see and create expenses
user = VIEW | CREATE
show("Junior accountant: VIEW + CREATE", user)

# Check if he can approve: & keeps only the APPROVE bit
show("Has APPROVE?", user & APPROVE)
print("Can approve:", user & APPROVE != 0)

# He becomes manager: add APPROVE
user = user | APPROVE
show("After adding APPROVE", user)

# Remove CREATE so he cannot approve his own expenses
user = user & ~CREATE
show("After removing CREATE", user)
print("Can approve:", user & APPROVE != 0)
print("Can create:", user & CREATE != 0)

# CHECK IT YOURSELF (reading the bits from right to left: VIEW, CREATE, APPROVE, PAY)
# 0011: VIEW and CREATE are on. Correct.
# 0000: the APPROVE bit is off, so he cannot approve. Correct.
# 0111: VIEW, CREATE and APPROVE are on. Correct.
# 0101: VIEW and APPROVE are on, CREATE is off. Correct.
# PAY was never given, the 4th bit stays 0 every time.