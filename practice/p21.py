def decomp(n):
    
    # 12! -> 12, 11, 10, 9, ..., 0
    factors = list(range(2, n+1))
    
    # {prime: power}
    primes_dict = {2:0}
    
    # for every number in factorial
    for f in factors:

        while f != 1:
            
            nums_l = list(primes_dict.keys())
            # for each prime number recorded until now
            for x in nums_l:

                # check if this is devisable
                while f % x == 0:
                    primes_dict[x] += 1
                    f /= x

                if f == 1: break
                
                # if we reached the end and didn't get to f == 1
                elif x == nums_l[-1] and f != 1:
                    primes_dict[f] = 1
                    f = 1
                
    return ' * '.join([str(f) + '^' + str(p) if p!=1 else str(f) for f, p in primes_dict.items()])

decomp(n = 12)
