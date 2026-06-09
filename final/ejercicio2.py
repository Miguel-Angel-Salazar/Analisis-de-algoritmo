def e2(S, k):

    resultado = []

    def backtrack(pos, subsecuencia):

        if len(subsecuencia) == k:
            resultado.append(subsecuencia)
            return

        for i in range(pos, len(S)):

            c = S[i]

            if subsecuencia:

                ultimo = subsecuencia[-1]

                # Alternancia
                if ultimo.isupper() == c.isupper():
                    continue

                # Orden alfabético ignorando may/min
                if ultimo.lower() > c.lower():
                    continue

                # No repetir letras
                if c.lower() in [x.lower() for x in subsecuencia]:
                    continue

            backtrack(i + 1, subsecuencia + c)

    backtrack(0, "")

    return resultado

S = "aYMuchaChOOoooooos"
k = 3

print(e2(S, k))