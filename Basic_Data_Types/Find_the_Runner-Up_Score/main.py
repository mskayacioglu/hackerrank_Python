if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    max_val = max(arr)
    
    runner_ups = [i for i in arr if i != max_val]
    runner_up = max(runner_ups)
    
    print(runner_up)
