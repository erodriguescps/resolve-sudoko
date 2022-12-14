
# Espaços não preenchidos são representados pelo número 0
def resolve(matriz):
    mat = []

    for i in range(0, 81, 9):
        mat.append(list(map(int, matriz[i:i+9])))

    qtd_por_quadrado: list = []  # Quantidade de cada numero por quadrado
    qtd_por_horizontal: list = []  # Quantidade de cada numero por horizontal
    qtd_por_vertical: list = []  # Quantidade de cada numero por vertical
    nqfq: list = []  # Numeros que falta no quadrado
    nqfh: list = []  # Numeros que falta na Horizonta.
    nqfv: list = []  # Numeros que falta na vertical

    quadrados = [   # É só uma variavel vazia que será alterada depois.
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # quadrados = list([[0]*9]*9)  # Implementar essa linha quando achar o bug.

    ############################################## Horizontais ###########################################################

    def preenche_horizontal():
        define_os_quadrados()
        for i in range(1, 10):   # Aqui é o numero que vai testar
            cont = 0
            linha_que_não_tem = []
            for j in range(6, 9):
                if i in mat[j]:
                    cont += 1
                else:
                    linha_que_não_tem = j
            if cont == 2:
                for k in range(6, 9):
                    if i not in quadrados[k]:
                        casa_preenchida = 0
                        for l in mat[linha_que_não_tem][(k-6) * 3: ((k-6) * 3) + 3]:
                            if l > 0:
                                casa_preenchida += 1
                        if casa_preenchida < 2:
                            pata = [0, 1, 2]
                            for p in range(3):
                                for linha in range(9):

                                    if mat[linha_que_não_tem][((k-6) * 3) + p] > 0:
                                        pata.remove(p)
                                        break
                                    if i == mat[linha][((k-6) * 3) + p]:
                                        pata.remove(p)

                            if len(pata) == 1:
                                mat[linha_que_não_tem][(
                                    (k-6) * 3) + pata[0]] = i
                        if casa_preenchida == 2:
                            for m in mat[linha_que_não_tem][(k-6) * 3: ((k-6) * 3) + 3]:
                                if m == 0:
                                    posicao = (
                                        k-6) * 3 + mat[linha_que_não_tem][(k-6) * 3: ((k-6) * 3) + 3].index(0)
                                    mat[linha_que_não_tem][posicao] = i
            cont = 0
            linha_que_não_tem = []
            for j in range(3, 6):  # Aqui testa nas 3 primeiras linhas
                if i in mat[j]:  # Aqui testa nas 3 primeiras linhas
                    cont += 1   # Aqui conta quantos vezes o numero i aparece
                else:
                    linha_que_não_tem = j   # Aqui conta quantas vezes ele não aparece
            if cont == 2:        # Se ele aparecer duas vezes, ele começara o processo para completar a terceira
                for k in range(3, 6):  # Contado de quadrados
                    # Aqui verifica em qual quadrado em que ele NÃO está
                    if i not in quadrados[k]:
                        casa_preenchida = 0
                        # Aqui verifica as 3 casas do quadrado em que falta
                        for l in mat[linha_que_não_tem][(k-3) * 3: ((k-3) * 3) + 3]:
                            if l > 0:
                                casa_preenchida += 1
                        if casa_preenchida < 2:
                            pata = [0, 1, 2]
                            for p in range(3):
                                for linha in range(9):
                                    if mat[linha_que_não_tem][((k-3) * 3) + p] > 0:
                                        pata.remove(p)
                                        break
                                    elif i == mat[linha][((k-3) * 3) + p]:
                                        pata.remove(p)

                            if len(pata) == 1:
                                mat[linha_que_não_tem][(
                                    (k-3) * 3) + pata[0]] = i
                        # Se ele estiver sendo ocupado por 2 lugares, ele já vai preencher.
                        if casa_preenchida == 2:
                            for m in mat[linha_que_não_tem][(k-3) * 3: ((k-3) * 3) + 3]:
                                if m == 0:
                                    posicao = (
                                        k-3) * 3 + mat[linha_que_não_tem][(k-3) * 3: ((k-3) * 3) + 3].index(0)
                                    mat[linha_que_não_tem][posicao] = i
            cont = 0
            linha_que_não_tem = []
            for j in range(3):
                if i in mat[j]:
                    cont += 1
                else:
                    linha_que_não_tem = j
            if cont == 2:    # Verifica se tem 2 numeros na horizontal
                for quadrado in range(3):
                    if i not in quadrados[quadrado]:
                        casa_preenchida = 0
                        # casa_preenchida é a quantidade casas preenchidas
                        for l in mat[linha_que_não_tem][quadrado * 3: (quadrado+1) * 3]:
                            if l > 0:
                                casa_preenchida += 1
                        if casa_preenchida < 2:
                            pata = [0, 1, 2]
                            for p in range(3):
                                for linha in range(9):

                                    if mat[linha_que_não_tem][(quadrado * 3) + p] > 0:
                                        pata.remove(p)
                                        break
                                    elif i == mat[linha][(quadrado * 3) + p]:
                                        pata.remove(p)

                            if len(pata) == 1:
                                mat[linha_que_não_tem][(
                                    quadrado * 3) + pata[0]] = i
                        if casa_preenchida == 2:
                            for m in mat[linha_que_não_tem][quadrado * 3: (quadrado+1) * 3]:
                                if m == 0:
                                    posicao = (
                                        quadrado * 3 + mat[linha_que_não_tem][quadrado * 3: (quadrado+1) * 3].index(0))
                                    mat[linha_que_não_tem][posicao] = i

    def completa_horizontal():
        qtd_por_horizontal = quantidade_por_horizontal()
        for i in qtd_por_horizontal:
            if i == 8:
                qtd_por_horizontal = quantidade_por_horizontal()
                nqfh = numeros_que_faltam_por_horizontal()
                mat[qtd_por_horizontal.index(i)][mat[qtd_por_horizontal.index(
                    i)].index(0)] = nqfh[qtd_por_horizontal.index(i)][0]

    def numeros_que_faltam_por_horizontal():
        nqfh = [[], [], [], [], [], [], [], [], []]
        for i in mat:
            n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for j in i:
                if (j in n):
                    n.remove(j)
            nqfh[mat.index(i)] = n
        return (nqfh)

    def quantidade_por_horizontal():
        qtd_por_horizontal = []
        for i in mat:
            cont = 0
            for num in range(9):
                if i[num] > 0:
                    cont += 1
            qtd_por_horizontal.append(cont)
        return (qtd_por_horizontal)

    ############################################### Verticais ###########################################################

    def preenche_vertical():

        for num in range(1, 10):
            tem_num = 0
            ntem_num = [0, 1, 2]
            for col in range(3):
                for lin in mat:
                    if num == lin[col]:
                        tem_num += 1
                        ntem_num.remove(col)
                        break
            if tem_num == 2:
                define_os_quadrados()
                for p in quadrados[::3]:
                    if num not in p:
                        cont = 0
                        for i in range(3):
                            if mat[quadrados.index(p)+i][ntem_num[0]] > 0:
                                cont += 1
                        if cont < 2:
                            possibilidade = 0
                            for i in range(3):
                                if mat[quadrados.index(p)+i][ntem_num[0]] == 0 and num not in mat[quadrados.index(p)+i]:
                                    possibilidade += 1
                            for i in range(3):
                                if possibilidade == 1:
                                    if mat[quadrados.index(p)+i][ntem_num[0]] == 0 and num not in mat[quadrados.index(p)+i]:
                                        mat[quadrados.index(
                                            p)+i][ntem_num[0]] = num
                        if cont == 2:
                            for i in range(3):
                                if mat[quadrados.index(p)+i][ntem_num[0]] == 0:
                                    mat[quadrados.index(
                                        p)+i][ntem_num[0]] = num

            tem_num = 0
            ntem_num = [3, 4, 5]
            for col in range(3, 6):
                for lin in mat:
                    if num == lin[col]:
                        tem_num += 1
                        ntem_num.remove(col)
                        break
            if tem_num == 2:
                define_os_quadrados()
                for p in quadrados[1::3]:  # Entra dentro do quadrado
                    if num not in p:
                        cont = 0
                        for i in range(3):
                            if mat[(quadrados.index(p)+i)-1][ntem_num[0]] > 0:
                                cont += 1
                        if cont < 2:
                            possibilidade = 0
                            for i in range(3):
                                if mat[(quadrados.index(p)+i)-1][ntem_num[0]] == 0 and num not in mat[(quadrados.index(p)+i)-1]:
                                    possibilidade += 1
                            for i in range(3):
                                if possibilidade == 1:
                                    if mat[(quadrados.index(p)+i)-1][ntem_num[0]] == 0 and num not in mat[(quadrados.index(p)+i)-1]:
                                        mat[(quadrados.index(p)+i) -
                                            1][ntem_num[0]] = num
                        if cont == 2:
                            for i in range(3):
                                if mat[(quadrados.index(p)+i)-1][ntem_num[0]] == 0:
                                    mat[(quadrados.index(p)+i) -
                                        1][ntem_num[0]] = num

            tem_num = 0
            ntem_num = [6, 7, 8]
            for col in range(6, 9):
                for lin in mat:
                    if num == lin[col]:
                        tem_num += 1
                        ntem_num.remove(col)
                        break
            if tem_num == 2:
                define_os_quadrados()
                for p in quadrados[2::3]:  # Entra dentro do quadrado
                    if num not in p:
                        cont = 0
                        for i in range(3):
                            if mat[(quadrados.index(p)+i)-2][ntem_num[0]] > 0:
                                cont += 1
                        if cont < 2:
                            possibilidade = 0
                            for i in range(3):
                                if mat[(quadrados.index(p)+i)-2][ntem_num[0]] == 0 and num not in mat[(quadrados.index(p)+i)-2]:
                                    possibilidade += 1
                            for i in range(3):
                                if possibilidade == 1:
                                    if mat[(quadrados.index(p)+i)-2][ntem_num[0]] == 0 and num not in mat[(quadrados.index(p)+i)-2]:
                                        mat[(quadrados.index(p)+i) -
                                            2][ntem_num[0]] = num

                        if cont == 2:
                            for i in range(3):
                                if mat[(quadrados.index(p)+i)-2][ntem_num[0]] == 0:
                                    mat[(quadrados.index(p)+i) -
                                        2][ntem_num[0]] = num

    def completa_vertical():
        qtd_por_vertical = quantidade_por_vertical()
        for i in range(9):
            if qtd_por_vertical[i] == 8:
                for j in range(9):
                    if mat[j][i] == 0:
                        qtd_por_vertical = quantidade_por_vertical()
                        nqfv = numeros_que_faltam_por_vertical()
                        mat[j][i] = nqfv[i][0]

    def numeros_que_faltam_por_vertical():
        nqfv = [[], [], [], [], [], [], [], [], []]
        for i in range(9):
            n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for j in range(9):
                if mat[j][i] in n:
                    n.remove(mat[j][i])
            nqfv[i] = n
        return (nqfv)

    def quantidade_por_vertical():
        qtd_por_vertical = [[], [], [], [], [], [], [], [], []]
        for i in range(9):
            cont = 0
            for j in range(9):
                if mat[j][i] > 0:
                    cont += 1
            qtd_por_vertical[i] = cont
        return (qtd_por_vertical)

    ############################################## Quadraticas #########################################################

    def completa_Quadrado():
        qtd_por_quadrado = quantidade_por_Quadrado()
        nqfq = numeros_que_faltam_por_Quadrado()
        for i in range(9):
            if qtd_por_quadrado[i] == 8:
                if i == 0:
                    for k in range(3):
                        for l in range(3):
                            if mat[k][l] == 0:
                                mat[k][l] = nqfq[i][0]
                if i == 1:
                    for k in range(3):
                        for l in range(3, 6):
                            if mat[k][l] == 0:
                                mat[k][l] = nqfq[i][0]
                if i == 2:
                    for k in range(3):
                        for l in range(6, 9):
                            if mat[k][l] == 0:
                                mat[k][l] = nqfq[i][0]
                if i == 3:
                    for k in range(3, 6):
                        for l in range(3):
                            if mat[k][l] == 0:
                                mat[k][l] = nqfq[i][0]
                if i == 4:
                    for k in range(3, 6):
                        for l in range(3, 6):
                            if mat[k][l] == 0:
                                mat[k][l] = nqfq[i][0]
                if i == 5:
                    for k in range(3, 6):
                        for l in range(6, 9):
                            if mat[k][l] == 0:
                                mat[k][l] = nqfq[i][0]
                if i == 6:
                    for k in range(6, 9):
                        for l in range(3):
                            if mat[k][l] == 0:
                                mat[k][l] = nqfq[i][0]
                if i == 7:
                    for k in range(6, 9):
                        for l in range(3, 6):
                            if mat[k][l] == 0:
                                mat[k][l] = nqfq[i][0]
                if i == 8:
                    for k in range(6, 9):
                        for l in range(6, 9):
                            if mat[k][l] == 0:
                                mat[k][l] = nqfq[i][0]

    def numeros_que_faltam_por_Quadrado():
        nqfq = []
        define_os_quadrados()
        conta = 0
        for i in quadrados:
            conta += 1
            n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for j in i:
                if (j in n):
                    n.remove(j)
            nqfq.append(n)
        return (nqfq)

    def quantidade_por_Quadrado():
        qtd_por_quadrado = []
        define_os_quadrados()
        for i in quadrados:
            cont = 0
            for num in range(9):
                if i[num] > 0:
                    cont += 1
            qtd_por_quadrado.append(cont)
        return (qtd_por_quadrado)

    def define_os_quadrados():
        cont = -1
        for i in range(3):  # 1 quadrado
            for j in range(3):
                cont += 1
                quadrados[0][cont] = mat[i][j]
        cont = -1
        for i in range(3):  # 2 quadrado
            for j in range(3, 6):
                cont += 1
                quadrados[1][cont] = mat[i][j]
        cont = -1
        for i in range(3):  # 2 quadrado
            for j in range(6, 9):
                cont += 1
                quadrados[2][cont] = mat[i][j]
        cont = -1
        for i in range(3, 6):  # 4 quadrado
            for j in range(3):
                cont += 1
                quadrados[3][cont] = mat[i][j]
        cont = -1
        for i in range(3, 6):  # 5 quadrado
            for j in range(3, 6):
                cont += 1
                quadrados[4][cont] = mat[i][j]
        cont = -1
        for i in range(3, 6):  # 6 quadrado
            for j in range(6, 9):
                cont += 1
                quadrados[5][cont] = mat[i][j]
        cont = -1
        for i in range(6, 9):  # 7 quadrado
            for j in range(3):
                cont += 1
                quadrados[6][cont] = mat[i][j]
        cont = -1
        for i in range(6, 9):  # 8 quadrado
            for j in range(3, 6):
                cont += 1
                quadrados[7][cont] = mat[i][j]
        cont = -1
        for i in range(6, 9):  # 9 quadrado
            for j in range(6, 9):
                cont += 1
                quadrados[8][cont] = mat[i][j]

    # RESOLVEDOR
    while '0' in str(mat):
        last_mat = mat
        completa_horizontal()
        completa_vertical()
        completa_Quadrado()
        preenche_horizontal()
        preenche_vertical()

    # Matrix final
    return mat
