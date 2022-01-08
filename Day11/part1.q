
m:"I"$'(string') read0 `:part1inputs.txt;
n:count m;

checknine:{[m]  / check if any value is greater than 9; if so, set them to 0
    r:where {$[not x~`long$();1b;0b]}each c:{where x}each  9<m;   /  retrieve indice of value greater than 9;r:row indice ; c:column indice
    c:c except enlist `long$();           / remove empty element from c
    ind:raze {x cross y}'[r;c];
    {.[x;y;:;0]}/[m;ind]      / set all values greater than 9 to 0 by iterating ind;return matrix
    }

findzero:{[m]        
    r:where {$[not x~`long$();1b;0b]}each c:{where x}each  0=m; 
    c:c except enlist `long$();
    ind0:raze {x cross y}'[r;c]  / indice of 0s
    }

run:{[m]
    m+:1;
    m:checknine[m];
    ind0:findzero[m];
    adjind:raze {r:i,(-1+i),1+i:first x;c:j,(-1+j),1+j:last x;r cross c}each ind0;   /  find all neighbor indice around 0s
    adjind:adjind where (min') (adjind >=0) & adjind < n;  / remove neighbor indice that are less than 0 and greater than or equals to 10
    index:adjind except ind0;  / remove neighbor indice already in 0s indice (ind)
    {$[not .[x;y]=0;[p:.[x;y;+;1];$[.[p;y]>9;.[p;y;:;0];p]];x]}/[m;index]   /  update all neighbor values and return a final matrix
    }
run[100;m]


