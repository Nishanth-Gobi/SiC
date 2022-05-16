import sympy as sp
from random import randint

def trusted_third_party():    

    p = sp.randprime(2^10, 2^20)
    q = p = sp.randprime(2^10, 2^20)
    n = p*q
    # return n
    return 361


print("Trusted 3rd party generating n...")
n = trusted_third_party()
print(f"Generated n: {n}")


def Alice():
    
    print("Alice generates her public & private key")
    s, v = Alice_key_gen(n)
    # s, v = 272, 340
    print(f"Alice's public key 'v': {v}")
    print(f"Alice's private key 's': {s}")
    
    r,x = Alice_witness()
    # r,x = 318, 44
    print(f"Alice generates random 'r': {r}")
    print(f"Alice sends witness 'x': {x} to Bob")

    y = Alice_transaction(r, s)
    # y = 217

    print(f"Alice sends Bob 'y': {y}")
    Bob(1, [y, x, v])


def Alice_key_gen(n):
    
    # private key
    s = randint(2, n-2)
    # public key
    v = (s*s)%n
    return s, v


def Alice_witness():
    r = randint(0, n-1)
    # witness
    x = (r*r)%n
    return r, x


def Alice_transaction(r, s):
    c = Bob(0)
    y = r*(s**c)%n
    return y
    
def Bob_send_challenge():    
    return randint(0,1)
    
c: int = Bob_send_challenge()
def Bob(opt, params=[]):
    
    if opt == 0:
        print(f"Bob sends Alice the challenge: {c}")
        return c
    elif opt==1:
        print("Bob verifies Alice...")
        Bob_verify(params, c)


def Bob_verify(params, c: int):
    y, x, v = params
    
    print(f"c: {c}")

    print(f"{(y*y)%n} == {(x*(v**c))%n}")

    if (y*y)%n == ( x*(v**c) )%n:
        print("--> Probable")
    else:
        print("--> Improbable")
    

print("Alice starts...")
Alice()
