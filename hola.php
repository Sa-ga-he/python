<?php


$perro = [3, 4, 6, 27, 18, 9, 6, 31,1, 12,];

$perro[0] = 50;

$nuevo=[];

for ($i=0; $i < count($perro); $i++) { 
    if ($perro[$i]<10) {
        array_push($nuevo,$perro[$i]);
    }

}

for ($a=0; $a < count($nuevo); $a++) {
    echo $nuevo[$a]."<br>";
}

echo "<br><br>";

$variable = 0;
for ($variable;$variable<count($perro); $variable++) {
    echo $perro[$variable]+10;
    echo "<br>";
}


echo "<br><br>";


$arra = [
    [14, 5, 7],
    [18, 4, 1],
    [19, 5, 2]
];


for ($i=0; $i < count($arra) ; $i++) { 
    for ($a=0; $a < count($arra) ; $a++) {
        if ($arra[$i][$a]>10) {
            echo $arra[$i][$a]."<br>";
        }
        //echo $arra[$i][$a]."<br>";
    }
}
