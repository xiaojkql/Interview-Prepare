# coding=utf-8
if __name__ == '__main__':
    x,y,n = list(map(int,input().split()))
    ls = []
    for i in range(n):
        ls.append(list(map(int,input().split())))
    row_min = min(list(zip(ls))[0])
    row_max = max(list(zip(ls))[0])
    col_min = min(list(zip(ls))[1])
    col_max = max(list(zip(ls))[1])
    print()
    next_ = [[-1,-1],[1,1],[-1,1],[1,-1]]
    min_res = 100000
    def recurse(row,col,min_):
        if row==x and col==y:
            min_res = min(min_res,min_)
        for (n_r,n_c) in next_:
            row += n_r
            col += n_c
            if row >max(0,x,row_max)+1 or row <min(0,x,row_min)-1 or col>max(0,x,col_max)+1 or col<min(0,x,col_min)-1:
                row -= n_r
                col -= n_c
                continue
            elif [row,col] in ls:
                row -= n_r
                col -= n_c
                continue
            else:
                recurse(row,col,min_+1)
    recurse(0,0,0)
    print(min_res)
