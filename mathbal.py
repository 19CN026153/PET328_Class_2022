nx=int(input('Enter number of rows  '))
ny=int(input('Enter number of columns  '))
nz=int(input('Enter number of layers  '))
N=float(input('Enter value of initial oil in place  '))
pb=int(input('Enter value of borehole pressure  '))
bob=float(input('Enter value of final oil formation volume  '))
ce=co=float(input('Enter value of effective compressibility'))

total_np=0
for k in range(1,nz+1):
    for j in range (1,ny+1):
        for i in range (1,nx+1):
            block_n_order=((k-1)*nx*ny)+(nx*(j-1))+i
            pnow=float(input('Enter value of current pressure for Block{0}?'.format(block_n_order)))
            boi=float(input('Enter value of initial volume factor for Block{0}?'.format(block_n_order)))
            pi=float(input('Enter value of initial reservoir prerssure for Block{0}?'.format(block_n_order)))
            bo=(bob*(1-(co*(pnow-pb)))
            block_np=(N*boi*ce*(pi-pnow))/bo
            total_np= total_np + block_np
            print('The cummulative oil produced from block {0} is {1:2f} STB'.format(block_n_order,block_np))
            print('The total cummulative oil produced from the entire reservoir is {0:2f} STB'.format(total_np))
