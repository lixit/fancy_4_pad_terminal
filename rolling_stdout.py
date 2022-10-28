import time

def clear_line(n=10):
    LINE_UP = '\033[1A'
    LINE_CLEAR = '\x1b[2K'
    for i in range(n):
        print(LINE_UP, end=LINE_CLEAR)


def rolling(max_line: int):
    l = [None] * max_line
    b = e = 0

    isEmpty = True

    for i in range(100):
        
        actual_b = b % max_line
        actual_e = e % max_line
        # begin not reach end
        if actual_b != actual_e:
            l[actual_e] = str(i)
            e = actual_e + 1
        else:
            if isEmpty:
                # put at end.
                l[actual_e] = str(i)
                e = actual_e + 1
                isEmpty = False
            else:
                l[actual_e] = str(i)
                e = actual_e + 1
                b = actual_b + 1
                isEmpty = False
        

        # print one screen
        actual_e = e % max_line
        actual_b = b % max_line

        if actual_b == actual_e:
            for i in range(max_line):
                index = b + i
                actual_i = index % max_line
                print(l[actual_i], flush=True)
            clear_line(max_line)
        else:
            b_tmp = actual_b
            while b_tmp != actual_e:
                print(l[b_tmp])
                b_tmp += 1
            clear_line(actual_e - actual_b)
        time.sleep(0.1)


rolling(20)