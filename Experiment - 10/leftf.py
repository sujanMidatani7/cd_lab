def lfactoring(prod, nt):
    words = [w for w in prod.split('|') if w != '']
    if len(words) > 1:
        counts = {}
        for w in words:
            prefix = ''
            for i in range(len(w)):
                prefix += w[i]
                counts[prefix] = counts.get(prefix, 0) + 1
        try:
            alpha = max((key for key, value in counts.items() if value > len(words) / 2), key=len)

            nt_prime = ''
            gamma = []
            for w in words:
                if alpha in w:
                    nt_prime += w.replace(alpha, '') + '|'
                else:
                    gamma.append(w)
            print(f"{nt} --> {alpha}{nt}'{'|' + '|'.join(gamma) if gamma else ''}")
            print(f"{nt}' --> {nt_prime[:-1]}#")
            nt = nt + "'"
            lfactoring(nt_prime, nt)
        except:
            print('...................')

nt = 'S'
prod = 'iEtS|iEtSeS|a|iES'
print(f"The given grammar is: {nt} --> {prod}")
print("After Left Factoring:")
lfactoring(prod, nt=nt)
