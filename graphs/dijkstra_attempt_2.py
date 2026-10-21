from math import inf

def dijkstra(grafo, s):
    """
    grafo: dict {nodo: [(vicino, costo), ...]}  (ogni nodo deve comparire come chiave)
    s: nodo sorgente
    Restituisce (L, pred): distanze minime e predecessori.
    """
    nodi = set(grafo)
    L = dict.fromkeys(nodi, inf)     # L_u <- +inf
    pred = dict.fromkeys(nodi)       # pred_u <- nil (None)
    L[s] = 0                         # L_s <- 0
    S = set()                        # S <- ∅

    while len(S) != len(nodi):
        v = min(nodi - S, key=L.get)     # v <- argmin{L_u : u ∉ S}
        S.add(v)                         # S <- S ∪ {v}

        archi = grafo[v]                 # δ+(v)
        i = 0
        while i < len(archi):
            w, c = archi[i]
            if L[w] > L[v] + c:          # L_w > L_v + c_vw
                L[w] = L[v] + c
                pred[w] = v
            i += 1

    return L, pred


# Esempio d'uso
grafo = {
    "A": [("B", -10), ("C", 1)],
    "B": [("D", 1), ("A", -1)],
    "C": [("B", 2), ("D", 5)],
    "D": [("A", -100)],
}
L, pred = dijkstra(grafo, "A")
print(L)     # {'A': 0, 'B': 3, 'C': 1, 'D': 4}  (l'ordine delle chiavi può variare)
print(pred)  # {'A': None, 'B': 'C', 'C': 'A', 'D': 'B'}