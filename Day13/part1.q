i:"I"$"," vs' read0 `:part1inputs.txt;
ax:1+max i[;0];
ay:1+max i[1;];
m:(ay,ax)#0            / zero matrix
m:{.[x;reverse y;:;1]}/[m;i]      / replace 0 with 1

fold:{[m;yorx;n]          / m: original matrix; yorx: is it along `y fold or `x fold; n:fold cutting line. n=7 along y in the example
 $[yorx=`y;[upfold:n#m;
            downfold:reverse m[(n+1)+til n]];
   yorx=`x;[upfold:m[;til n];
            downfold:flip reverse flip m[;(1+n)+til n];]];
   c:{where x}each  2=comb r:where  (max')2=comb:upfold+downfold;
   idx:raze {x cross y}'[r;c];
   :{.[x;y;:;1]}/[comb;idx]
 }

/ a:`y`x;
/ b:7 5
/ show sum sum {fold[x;y;z]}/[m;a;b];
/ 1 1 1 1 1
/ 1 0 0 0 1
/ 1 0 0 0 1
/ 1 0 0 0 1
/ 1 1 1 1 1
/ 0 0 0 0 0
/ 0 0 0 0 0
show sum sum fold[m;`x;655]  / final answer :695
