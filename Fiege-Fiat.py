import sympy as sp
from random import randint

vec_len = 3

def trusted_third_party():    
    p = sp.randprime(2^10, 2^20)
    q = p = sp.randprime(2^10, 2^20)
    n = p*q
    return n


print("Trusted 3rd party generating n...")
n = trusted_third_party()
print(f"Generated n: {n}")


def Alice():
    
    print("Alice generates her public & private key")
    s, v = [], []
    
    for i in range(vec_len):
        st, vt = Alice_key_gen(n)
        s.append(st)
        v.append(vt)

    print(f"Alice's public key 'v': {v}")
    print(f"Alice's private key 's': {s}")
    
    r,x = Alice_witness()

    print(f"Alice generates random 'r': {r}")
    print(f"Alice sends witness 'x': {x} to Bob")

    y = Alice_transaction(r, s)

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

    y = []
    for i, j in zip(c, s):
        y.append( r*(j**i)%n )
    return y
    
def Bob_send_challenge():    
    return randint(0,1)

c = []
for i in range(vec_len):
    c.append(Bob_send_challenge())

def Bob(opt, params=[]):
    
    if opt == 0:
        print(f"Bob sends Alice the challenge: {c}")
        return c
    elif opt==1:
        print("Bob verifies Alice...")
        Bob_verify(params, c)


def Bob_verify(params, c: int):
    y, x, v = params
    print(f"c: {c}, y: {y}, x: {x}, v: {v}")
    

    for yt, vt, ct in zip(y, v, c):

        if (yt*yt)%n == ( x*(vt**ct) )%n:
            print("--> Probable")
        else:
            print("--> Improbable")
    

print("Alice starts...")
Alice()
