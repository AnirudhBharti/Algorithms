def MaximumAsToPrint(N):

    if N <= 6:
        return N

    screens = [0]*N

    for i in range(1, N):
        screens[i-1] = i

    for n in range(7, N+1):
        screens[n-1] = 0
        for breakpoint in range(n-3, 0, -1):
            curr = (n-breakpoint-1)*screens[breakpoint-1]
            if curr > screens[n-1]:
                screens[n-1] = curr

    return screens[N-1]


if __name__ == "__main__":
    for N in range(1, 21):
        print("For N = ", N, " Max Print of A's gonna be", MaximumAsToPrint(N))
