from comm.base_comm import CommTargetCallback

numeroInicial = 1
print(f"Numero inicial começão em {numeroInicial}")
volta = 0
while numeroInicial <= 10:
    volta +=1
    numeroInicial += 2
    print(f"Na volta {volta+1} o numeroInicial será =  {numeroInicial}")