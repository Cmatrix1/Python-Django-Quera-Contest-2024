

def calculate_perimeter(n, rows):
    total_perimeter = 0
    prev_l, prev_r = None, None
    
    for l, r in rows:
        total_perimeter += 2 * (r - l)
        total_perimeter += 2
        
        if prev_l is not None:
            overlap_l = max(prev_l, l)
            overlap_r = min(prev_r, r)
            if overlap_l < overlap_r:
                total_perimeter -= 2 * (overlap_r - overlap_l)
        
        prev_l, prev_r = l, r
    return total_perimeter

n = int(input(""))
rows = []

for _ in range(n):
    l, r = map(int, input("").split(' '))
    rows.append((l, r))

print(calculate_perimeter(n, rows))